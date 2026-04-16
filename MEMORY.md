# MEMORY.md — Long-Term Memory Template

> Curated memory for direct sessions only. Never load this file in shared chats or sub-agent runs.

---

## What Belongs Here

Store information that should survive across sessions:

- Owner preferences that change how the agent should respond
- Persistent project context and current priorities
- Reusable rules, constraints, and lessons learned
- Stable facts about infrastructure, devices, channels, or workflows

Keep it curated. This is not a raw log.

---

## What Does NOT Belong Here

Do not store:

- API keys, passwords, or private tokens
- Full chat transcripts
- Temporary TODO lists
- Sensitive information that should not reach the agent in future sessions

Use `memory/YYYY-MM-DD.md` for raw daily notes and only promote important items here.

---

## Suggested Structure

```md
# MEMORY

## Owner Preferences
- Prefers concise updates with a clear recommendation
- Wants replies in Traditional Chinese unless the task is English-first

## Current Priorities
- Launching the new website by the end of Q2
- Building a repeatable content pipeline

## Infrastructure
- Main gateway runs on Ubuntu 24.04 VM
- Telegram is the primary notification channel

## Hard-Won Lessons
- Do not deploy on Fridays without a rollback plan
- Weekly summaries perform better than daily digests for this team
```

---

## Security Rules

- Main session only
- Never quote this file into public or group outputs without explicit approval
- Review quarterly and remove stale or risky entries

---

*Part of [openclaw-workspace-sowork](https://github.com/cj-wang-sowork/openclaw-workspace-sowork)*
