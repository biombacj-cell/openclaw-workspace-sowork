#!/usr/bin/env python3
"""
ATLAS Skills Auto-Importer

Automatically imports official agent skills from GitHub repositories
into the ATLAS skills library with proper directory structure.

Usage:
    python scripts/import_skills.py                    # Import all configured skills
        python scripts/import_skills.py --org anthropic    # Import specific org
            python scripts/import_skills.py --category official-anthropic  # Import category
                python scripts/import_skills.py --dry-run          # Preview without changes
                """

import os
import json
import shutil
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin
from dataclasses import dataclass, asdict

try:
      import requests
except ImportError:
      print("Error: requests library not found. Install with: pip install requests")
      exit(1)

# Configure logging
logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ATLAS project root
PROJECT_ROOT = Path(__file__).parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"


@dataclass
class SkillMetadata:
      """Metadata for a skill being imported"""
      name: str
      category: str
      source_org: str
      source_repo: str
      source_path: str
      imported_at: str
      github_url: str


class SkillsImporter:
      """Manages automatic importing of skills from official repositories"""

    # Configuration: Map of organizations to skills to import
      # Format: "category": [("repo", "skill_path"), ...]
      SKILLS_CONFIG = {
          "official-anthropic": [
              ("anthropics/anthropic-sdk-python", ""),  # Placeholder - actual paths vary
              ("anthropics/anthropic-sdk-js", ""),
              ("anthropics/anthropic-cookbook", ""),
          ],
          "official-google": [
              ("google/generative-ai-python", ""),
              ("google-gemini/cookbook", ""),
              ("googleapis/google-api-python-client", ""),
          ],
          "official-microsoft": [
              ("Azure/azure-sdk-for-python", ""),
              ("Azure/azure-sdk-for-js", ""),
              ("microsoft/semantic-kernel", ""),
          ],
          "official-openai": [
              ("openai/openai-python", ""),
              ("openai/openai-node", ""),
              ("openai/cookbook", ""),
          ],
          "official-vercel": [
              ("vercel/next.js", "examples"),
              ("vercel/ai", "examples"),
          ],
          "official-cloudflare": [
              ("cloudflare/workers-sdk", "templates"),
              ("cloudflare/workers-ai", "examples"),
          ],
          "official-netlify": [
              ("netlify/netlify-cli", ""),
              ("netlify/next-runtime", ""),
          ],
          "official-firebase": [
              ("firebase/firebase-tools", ""),
              ("firebase/firebase-admin-python", ""),
          ],
      }

    def __init__(self, dry_run: bool = False, github_token: Optional[str] = None):
              """
                      Initialize the importer.

                                      Args:
                                                  dry_run: If True, don't actually create files
                                                              github_token: GitHub API token for higher rate limits (optional)
                                                                      """
              self.dry_run = dry_run
              self.github_token = github_token or os.getenv("GITHUB_TOKEN")
              self.session = requests.Session()

        if self.github_token:
                      self.session.headers.update({"Authorization": f"token {self.github_token}"})

        self.imported_skills: List[SkillMetadata] = []
        self.failed_skills: List[Tuple[str, str, str]] = []

    def _fetch_github_file(self, owner_repo: str, path: str) -> Optional[str]:
              """
                      Fetch a file from GitHub via raw.githubusercontent.com.

                                      Args:
                                                  owner_repo: "owner/repo" format
                                                              path: Path to file in repo

                                                                                  Returns:
                                                                                              File content or None if not found
                                                                                                      """
              url = f"https://raw.githubusercontent.com/{owner_repo}/main/{path}"
              try:
                            resp = self.session.get(url, timeout=10)
                            if resp.status_code == 200:
                                              return resp.text
elif resp.status_code == 404:
                # Try 'master' branch instead
                url = url.replace("/main/", "/master/")
                resp = self.session.get(url, timeout=10)
                return resp.text if resp.status_code == 200 else None
except requests.exceptions.RequestException as e:
            logger.warning(f"Failed to fetch {url}: {e}")
            return None

    def _fetch_github_tree(self, owner_repo: str, path: str = "") -> Optional[Dict]:
              """
                      Fetch repository tree structure via GitHub API.

                                      Args:
                                                  owner_repo: "owner/repo" format
                                                              path: Path within repo

                                                                                  Returns:
                                                                                              Tree structure or None
                                                                                                      """
              url = f"https://api.github.com/repos/{owner_repo}/git/trees/main?recursive=1"
              try:
                            resp = self.session.get(url, timeout=10)
                            if resp.status_code == 200:
                                              return resp.json()
              else:
                                # Try master branch
                                url = url.replace("main", "master")
                                resp = self.session.get(url, timeout=10)
                                return resp.json() if resp.status_code == 200 else None
except requests.exceptions.RequestException as e:
            logger.warning(f"Failed to fetch tree for {owner_repo}: {e}")
            return None

    def _create_skill_directory(self, category: str, skill_name: str, files_dict: Dict[str, str]) -> bool:
              """
                      Create a skill directory with files.

                                      Args:
                                                  category: Category directory name
                                                              skill_name: Skill directory name
                                                                          files_dict: Dict of {filename: content}

                                                                                              Returns:
                                                                                                          True if successful
                                                                                                                  """
              category_dir = SKILLS_DIR / category
              skill_dir = category_dir / skill_name

        if not self.dry_run:
                      try:
                                        skill_dir.mkdir(parents=True, exist_ok=True)
                                        for filename, content in files_dict.items():
                                                              file_path = skill_dir / filename
                                                              file_path.write_text(content, encoding='utf-8')
                                                          logger.info(f"Created skill: {category}/{skill_name}")
                                        return True
except Exception as e:
                logger.error(f"Failed to create {skill_dir}: {e}")
                return False
else:
            logger.info(f"[DRY RUN] Would create skill: {category}/{skill_name}")
              return True

    def _create_skill_template(self, skill_name: str, source_org: str, source_repo: str, github_url: str) -> Dict[str, str]:
              """
                      Create template files for a new skill.

                                      Args:
                                                  skill_name: Name of the skill
                                                              source_org: Organization providing the skill
                                                                          source_repo: Source repository
                                                                                      github_url: URL to source repository

                                                                                                          Returns:
                                                                                                                      Dict of {filename: content}
                                                                                                                              """
              readable_name = skill_name.replace("-", " ").title()

        readme_content = f"""# {readable_name}

        **Category**: [Determine from context]
        **Keywords**: [skill-related keywords]
        **Compatibility**: Claude Code, Codex, Cursor, Gemini CLI
        **Source**: [{source_org}/{source_repo}]({github_url})

        ## Purpose
        [Add skill purpose and when to use it]

        ## Installation
        \`\`\`bash
        cp -r {skill_name} ~/.claude/skills/
        \`\`\`

        ## Usage
        \`\`\`python
        # Add usage examples here
        \`\`\`

        ## Requirements
        - [Python 3.x]
        - [Any external dependencies]

        ## Examples
        See `examples/` directory for usage patterns.

        ## Testing
        \`\`\`bash
        pytest tests/
        \`\`\`

        ## Attribution
        Imported from: {source_org}/{source_repo}
        License: [Check source repository]
        """

        manifest_content = json.dumps({
                      "name": skill_name,
                      "version": "1.0.0",
                      "description": f"[Description of {skill_name}]",
                      "keywords": ["skill", "atlas"],
                      "compatibility": ["claude-code", "codex", "cursor"],
                      "author": source_org,
                      "license": "MIT",
                      "source": {
                                        "org": source_org,
                                        "repo": source_repo,
                                        "url": github_url
                      },
                      "dependencies": [],
                      "categories": ["[category]"]
        }, indent=2)

        return {
                      "README.md": readme_content,
                      "manifest.json": manifest_content,
        }

    def import_skill(self, category: str, skill_name: str, source_org: str, source_repo: str, source_path: str = "") -> bool:
              """
                      Import a single skill.

                                      Args:
                                                  category: Category to import into
                                                              skill_name: Name of skill directory
                                                                          source_org: Source organization (for attribution)
                                                                                      source_repo: Source repository (owner/repo format)
                                                                                                  source_path: Path within source repo
                                                                                                              
                                                                                                                      Returns:
                                                                                                                                  True if successful
                                                                                                                                          """
              github_url = f"https://github.com/{source_repo}"

        logger.info(f"Importing {category}/{skill_name} from {source_org}...")

        # Create template files
        files = self._create_skill_template(skill_name, source_org, source_repo, github_url)

        # Try to fetch actual files from source
        if source_path:
                      content = self._fetch_github_file(source_repo, source_path)
                      if content:
                                        files[Path(source_path).name] = content

                  # Create the skill directory
                  success = self._create_skill_directory(category, skill_name, files)

        if success:
                      metadata = SkillMetadata(
                                        name=skill_name,
                                        category=category,
                                        source_org=source_org,
                                        source_repo=source_repo,
                                        source_path=source_path or "main",
                                        imported_at=__import__('datetime').datetime.now().isoformat(),
                                        github_url=github_url
                      )
                      self.imported_skills.append(metadata)
else:
            self.failed_skills.append((category, skill_name, source_org))

        return success

    def import_all(self) -> None:
              """Import all configured skills."""
              logger.info(f"Starting ATLAS skills import (dry_run={self.dry_run})")

        for category, skills in self.SKILLS_CONFIG.items():
                      for source_repo, source_path in skills:
                                        org = source_repo.split("/")[0]
                                        skill_name = source_repo.split("/")[1].replace("-sdk", "").replace("-", "_")

                self.import_skill(category, skill_name, org, source_repo, source_path)

        self._print_summary()

    def import_category(self, category: str) -> None:
              """Import all skills in a category."""
              if category not in self.SKILLS_CONFIG:
                            logger.error(f"Category not found: {category}")
                            logger.info(f"Available: {', '.join(self.SKILLS_CONFIG.keys())}")
                            return

              logger.info(f"Importing category: {category}")
              skills = self.SKILLS_CONFIG[category]

        for source_repo, source_path in skills:
                      org = source_repo.split("/")[0]
                      skill_name = source_repo.split("/")[1].replace("-sdk", "").replace("-", "_")
                      self.import_skill(category, skill_name, org, source_repo, source_path)

        self._print_summary()

    def import_org(self, org: str) -> None:
              """Import all skills from an organization."""
              logger.info(f"Importing organization: {org}")
              imported_orgs = set()

        for category, skills in self.SKILLS_CONFIG.items():
                      for source_repo, source_path in skills:
                                        repo_org = source_repo.split("/")[0]
                                        if repo_org.lower() == org.lower():
                                                              imported_orgs.add(category)
                                                              skill_name = source_repo.split("/")[1].replace("-sdk", "").replace("-", "_")
                                                              self.import_skill(category, skill_name, repo_org, source_repo, source_path)

                                if not imported_orgs:
                                              logger.warning(f"No skills found for organization: {org}")

        self._print_summary()

    def _print_summary(self) -> None:
              """Print import summary."""
        logger.info("=" * 60)
        logger.info(f"Import Complete: {len(self.imported_skills)} successful, {len(self.failed_skills)} failed")

        if self.imported_skills:
                      logger.info("\nImported Skills:")
            for skill in self.imported_skills:
                              logger.info(f"  ✓ {skill.category}/{skill.name}")

        if self.failed_skills:
                      logger.warning("\nFailed Skills:")
            for category, name, org in self.failed_skills:
                              logger.warning(f"  ✗ {category}/{name} ({org})")

        # Save metadata
        if not self.dry_run and self.imported_skills:
                      metadata_file = SKILLS_DIR / "IMPORT_METADATA.json"
            metadata_list = [asdict(s) for s in self.imported_skills]

            try:
                              with open(metadata_file, 'w') as f:
                                                    json.dump(metadata_list, f, indent=2)
                                                logger.info(f"\nMetadata saved to: {metadata_file}")
except Exception as e:
                logger.error(f"Failed to save metadata: {e}")


def main():
      """Main entry point."""
    parser = argparse.ArgumentParser(
              description="ATLAS Skills Auto-Importer - Import agent skills from GitHub",
              epilog="Examples:\n"
                     "  %(prog)s --all                  # Import all skills\n"
                     "  %(prog)s --category official-anthropic  # Import category\n"
                     "  %(prog)s --org anthropic        # Import organization\n"
                     "  %(prog)s --dry-run              # Preview without changes",
              formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
              "--all",
              action="store_true",
              help="Import all configured skills (default)"
    )
    parser.add_argument(
              "--category",
              help="Import specific category"
    )
    parser.add_argument(
              "--org",
              help="Import specific organization"
    )
    parser.add_argument(
              "--dry-run",
              action="store_true",
              help="Preview import without making changes"
    )
    parser.add_argument(
              "--github-token",
              help="GitHub API token (or use GITHUB_TOKEN env var)"
    )

    args = parser.parse_args()

    importer = SkillsImporter(dry_run=args.dry_run, github_token=args.github_token)

    if args.category:
              importer.import_category(args.category)
elif args.org:
        importer.import_org(args.org)
else:
        importer.import_all()


if __name__ == "__main__":
      main()
