# openclaw-workspace-sowork

> A production-ready workspace template for running [OpenClaw](https://github.com/openclaw/openclaw) agents on a VM — with real-world skills for marketing, research, and content.

Built and battle-tested by [SoWork](https://sowork.ai) across 13 markets. Open-sourced for the OpenClaw community.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/Built%20for-OpenClaw-orange)](https://github.com/openclaw/openclaw)
[![SoWork](https://img.shields.io/badge/by-SoWork.ai-blue)](https://sowork.ai)

---

## What is this?

Most OpenClaw workspaces are empty scaffolding. This one has **actual content hyou can use immediately:**

- ✅ **3 ready-to-use skills** — brand positioning, web research, content writing
- ✅ **AGENTS.md + SOUL.md templates** — real boot sequences and 5 persona examples
- ✅ **A complete marketing team example** — 3 agents running on 1 VM, with cost breakdown
- ✅ **VM setup guide** — step-by-step from a $6/mo VPS to a running OpenClaw agent
- ✅ **Brand-in-SOUL guide** — how to embed brand positioning into your agent's identity

Clone it. Customize it. Run it.

---

## Quick Start

```bash
# Clone to your VM's OpenClaw workspace directory
git clone https://github.com/cj-wang-sowork/openclaw-workspace-sowork.git ~/.openclaw/workspace

# Or clone and copy files manually
git clone https://github.com/cj-wang-sowork/openclaw-workspace-sowork.git
cp -r openclaw-workspace-sowork/skills ~/.openclaw/workspace/
cp openclaw-workspace-sowork/AGENTS.md ~/.openclaw/workspace/
cp openclaw-workspace-sowork/SOUL.md ~/.openclaw/workspace/
```

Then start OpenClaw:

```bash
openclaw onboard --install-daemon
openclaw gateway --port 18789
```

---

## What's Included

### Skills (drop into `~/.openclaw/workspace/skills/`)

| Skill | What it does | Trigger |
|-------|-------------|---------|
| `skills/brand-positioning.md` | Brand analysis + campaign strategy | `@assistant Run brand positioning for [Brand]` |
| `skills/web-research.md` | Market research + competitor analysis | `@assistant Research [topic]` |
