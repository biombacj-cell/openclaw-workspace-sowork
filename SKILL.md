---
name: openclaw-workspace-sowork
description: >
  Production-ready OpenClaw workspace template for marketing teams.
  Includes brand positioning, web research, and content writing skills,
  plus a full AGENTS/SOUL/TOOLS/USER/IDENTITY/HEARTBEAT/MEMORY workspace system.
  Battle-tested across 13 markets by SoWork. DeepEval score: 0.940.
version: "1.0.0"
author: cj-wang-sowork
license: MIT
tags:
  - marketing
  - openclaw
  - workspace
  - agent-template
  - brand-positioning
  - content-writing
  - web-research
  - memory
  - multi-agent
requirements:
  - OpenClaw (any version)
  - A Linux/macOS VM or VPS ($6/mo minimum)
---

# openclaw-workspace-sowork

A production-ready OpenClaw workspace template for marketing teams — clone it, fill in your brand context, and run.

## What This Skill Does

When you install this workspace, your OpenClaw agent gains:

1. **Brand Positioning** — Analyze brand USPs, map competitors, generate campaign strategy.
2. **Web Research** — Structured market research and trend monitoring across any market.
3. **Content Writing** — Brand-aligned content (social, blog, campaigns) for any platform.

Beyond skills, you get a **complete workspace file system**:

| File | Purpose |
|------|---------|
| AGENTS.md | Boot sequence, routing rules, checklist table |
| SOUL.md | Persona, tone, brand-in-SOUL methodology |
| TOOLS.md | Environment: SSH hosts, API config, TTS voices |
| USER.md | Team context, preferences (main sessions only) |
| IDENTITY.md | Name, emoji, avatar |
| HEARTBEAT.md | Periodic health tasks and content pipeline checks |
| MEMORY.md | Iron-law rules, key learnings (security-gated) |

## Installation

```bash
# Install via npx skills CLI
npx skills add cj-wang-sowork/openclaw-workspace-sowork

# Or clone directly to your OpenClaw workspace
git clone https://github.com/cj-wang-sowork/openclaw-workspace-sowork.git ~/.openclaw/workspace
```

## Quick Usage

After installation, trigger skills with:

```
@assistant Run brand positioning for [Your Brand]
@assistant Research [topic or market]
@assistant Write [content type] for [platform]
```

## Production Validation

Extracted from real SoWork operations:
- **13 markets** on 1 VM simultaneously
- **~$50/month** total infrastructure cost
- **3 agents** running in parallel (brand, research, content)
- **DeepEval score: 0.940** on brand consistency
- **Token efficiency**: Full bootstrap under 150k chars

## Multi-Agent Example

See `examples/marketing-team/` for a complete 3-agent setup with cost breakdown.

## Security

MEMORY.md is security-gated — loaded in main sessions only, never in group chats or sub-agents.

## Related

- [SoWork.ai](https://sowork.ai) — AI marketing platform this workspace powers
- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) — skills registry
- [win4r/openclaw-workspace](https://github.com/win4r/openclaw-workspace) — workspace maintenance skill
