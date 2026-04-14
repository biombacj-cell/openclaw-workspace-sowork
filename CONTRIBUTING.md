# Contributing to openclaw-workspace-sowork

Thank you for your interest in contributing! This is an open workspace template for the OpenClaw agent ecosystem.

---

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion, please open a GitHub Issue with:
- A clear title and description
- Steps to reproduce (if it is a bug)
- Your OpenClaw version and OS

### Submitting Changes

1. Fork this repository
2. Create a new branch: git checkout -b feature/your-feature-name
3. Make your changes
4. Commit with a clear message: git commit -m "Add: description of change"
5. Push and open a Pull Request

---

## What We Welcome

- New example skill configs in skills/
- Useful automation scripts in scripts/
- Improvements to README or documentation
- .gitignore additions for common sensitive file types
- Translations of README into other languages (e.g., README.zh-TW.md, README.ja.md)

---

## What to Avoid

- Do NOT commit any real credentials, API keys, or tokens
- Do NOT commit personal memory files or conversation history
- Do NOT commit generated output files
- Keep the workspace structure general — avoid SoWork-specific business logic

---

## Commit Message Convention

Use the following prefixes to keep the history readable:

- Add: add a new file or feature
- Fix: fix a bug or issue
- Update: update existing content
- Remove: remove a file or feature
- Docs: documentation only changes

Example: Add: example Slack notification skill config

---

## Code Style

This repository is mostly config files and shell scripts. Please:
- Use 2-space indentation for YAML/JSON
- Add comments to shell scripts explaining what they do
- Keep scripts POSIX-compatible where possible (avoid bash-only features)

---

## Questions?

Open an Issue or reach out via the SoWork community channels.
