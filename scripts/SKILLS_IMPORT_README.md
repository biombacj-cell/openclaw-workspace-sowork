# ATLAS Skills Auto-Importer Guide

Complete guide to using the automated skills importer script.

## Installation

### Prerequisites
```bash
python3 --version  # 3.8+
pip install requests
```

### Setup
```bash
cd atlas
chmod +x scripts/import_skills.py
```

## Usage

### Quick Start - Import All Skills
```bash
python scripts/import_skills.py
```

### Import by Category
```bash
# Import Anthropic skills
python scripts/import_skills.py --category official-anthropic

# Import Google skills
python scripts/import_skills.py --category official-google

# Import Microsoft skills
python scripts/import_skills.py --category official-microsoft

# Import OpenAI skills
python scripts/import_skills.py --category official-openai

# List all available categories
python scripts/import_skills.py --help
```

### Import by Organization
```bash
# Import all Anthropic skills
python scripts/import_skills.py --org anthropic

# Import all Google skills
python scripts/import_skills.py --org google

# Import all Microsoft skills
python scripts/import_skills.py --org microsoft

# Import all OpenAI skills
python scripts/import_skills.py --org openai
```

### Dry-Run (Preview Without Changes)
```bash
# See what would be imported without actually creating files
python scripts/import_skills.py --dry-run

python scripts/import_skills.py --category official-anthropic --dry-run

python scripts/import_skills.py --org google --dry-run
```

### With GitHub API Token (For Higher Rate Limits)
```bash
# Using environment variable
export GITHUB_TOKEN=your_token_here
python scripts/import_skills.py

# Or pass as argument
python scripts/import_skills.py --github-token your_token_here
```

## Examples

### Example 1: Preview Anthropic Skills Import
```bash
python scripts/import_skills.py --category official-anthropic --dry-run
```

Output:
```
[INFO] Importing category: official-anthropic
[INFO] [DRY RUN] Would create skill: official-anthropic/anthropic_sdk_python
[INFO] [DRY RUN] Would create skill: official-anthropic/anthropic_sdk_js
...
[INFO] Import Complete: 3 successful, 0 failed
```

### Example 2: Actually Import Anthropic Skills
```bash
python scripts/import_skills.py --category official-anthropic
```

Output:
```
[INFO] Starting ATLAS skills import (dry_run=False)
[INFO] Importing official-anthropic/anthropic_sdk_python from anthropic...
[INFO] Created skill: official-anthropic/anthropic_sdk_python
[INFO] Importing official-anthropic/anthropic_sdk_js from anthropic...
[INFO] Created skill: official-anthropic/anthropic_sdk_js
...
[INFO] ============================================================
[INFO] Import Complete: 3 successful, 0 failed

[INFO] Imported Skills:
[INFO]   ✓ official-anthropic/anthropic_sdk_python
[INFO]   ✓ official-anthropic/anthropic_sdk_js
...
[INFO] Metadata saved to: skills/IMPORT_METADATA.json
```

### Example 3: Import All Official Google Skills
```bash
python scripts/import_skills.py --org google
```

### Example 4: Scheduled Sync (Cron Job)
```bash
# Add to crontab for daily updates
0 2 * * * cd /path/to/atlas && python scripts/import_skills.py --dry-run >> logs/skills_sync.log 2>&1
```

## Output Structure

After importing, your skills directory will look like:
```
skills/
├── official-anthropic/
│   ├── anthropic_sdk_python/
│   │   ├── README.md
│   │   └── manifest.json
│   ├── anthropic_sdk_js/
│   │   ├── README.md
│   │   └── manifest.json
│   └── ...
├── official-google/
│   ├── generative_ai_python/
│   │   ├── README.md
│   │   └── manifest.json
│   └── ...
├── official-microsoft/
│   └── ...
├── IMPORT_METADATA.json  ← Tracks all imports
└── README.md
```

## Import Metadata

Each import run creates/updates `skills/IMPORT_METADATA.json`:

```json
[
  {
    "name": "anthropic_sdk_python",
    "category": "official-anthropic",
    "source_org": "anthropic",
    "source_repo": "anthropics/anthropic-sdk-python",
    "source_path": "main",
    "imported_at": "2026-04-17T12:00:00.000000",
    "github_url": "https://github.com/anthropics/anthropic-sdk-python"
  },
  ...
]
```

This helps you track:
- When each skill was imported
- - Which source repository it came from
  - - Whether future updates are available
   
    - ## Configurable Skills
   
    - Edit `SKILLS_CONFIG` in `import_skills.py` to customize what gets imported:
   
    - ```python
      SKILLS_CONFIG = {
          "official-anthropic": [
              ("anthropics/anthropic-sdk-python", ""),
              ("anthropics/anthropic-sdk-js", ""),
              ("anthropics/anthropic-cookbook", ""),
          ],
          "official-google": [
              ("google/generative-ai-python", ""),
              # Add more Google repos here
          ],
          # ... customize as needed
      }
      ```

      ## Troubleshooting

      ### Issue: "requests library not found"
      ```bash
      pip install requests
      ```

      ### Issue: GitHub API Rate Limit (60 requests/hour without token)
      ```bash
      export GITHUB_TOKEN=your_personal_access_token
      python scripts/import_skills.py
      ```

      Get a token: https://github.com/settings/tokens (no special permissions needed)

      ### Issue: Network Timeout
      ```bash
      # Script has 10-second timeout, usually sufficient
      # If repos are slow, increase timeout in _fetch_github_file method
      ```

      ### Issue: Some Skills Fail to Import
      - Check the FAILED SKILLS section in output
      - - This usually means the source repository structure changed
        - - Create an issue to update the configuration
         
          - ## Integration with CI/CD
         
          - ### GitHub Actions Example
          - ```yaml
            name: Sync Skills

            on:
              schedule:
                - cron: '0 2 * * *'  # Daily at 2 AM UTC
              workflow_dispatch:      # Manual trigger

            jobs:
              sync:
                runs-on: ubuntu-latest
                steps:
                  - uses: actions/checkout@v3
                  - uses: actions/setup-python@v4
                    with:
                      python-version: '3.x'

                  - name: Install dependencies
                    run: pip install requests

                  - name: Import skills
                    run: python scripts/import_skills.py

                  - name: Commit changes
                    run: |
                      git config user.name "Skills Bot"
                      git config user.email "skills@atlas.dev"
                      git add skills/
                      git commit -m "chore: auto-sync agent skills" || true
                      git push
            ```

            ## Advanced: Custom Import Logic

            Extend the importer for your own skills:

            ```python
            from scripts.import_skills import SkillsImporter

            importer = SkillsImporter()

            # Import custom skills
            importer.import_skill(
                category="custom-skills",
                skill_name="my_awesome_skill",
                source_org="myorg",
                source_repo="myorg/my-repo",
                source_path="src/skill.py"
            )

            importer._print_summary()
            ```

            ## Performance Notes

            - **First Import**: 2-5 minutes for 100+ skills (depends on internet)
            - - **Subsequent Runs**: Overwrites existing skills (idempotent)
              - - **Memory**: Minimal - streams content from GitHub
                - - **Rate Limiting**: Respects GitHub API limits (60/hour without token, 5000/hour with token)
                 
                  - ## Support
                 
                  - For issues, questions, or suggestions:
                  - 1. Check `skills/IMPORT_METADATA.json` for import history
                    2. 2. Review logs for error messages
                       3. 3. Open an issue on GitHub: https://github.com/cj-wang-sowork/atlas/issues
                         
                          4. ---
                         
                          5. **Last Updated**: April 17, 2026
                          6. **Compatible With**: Python 3.8+
                          7. **License**: MIT
