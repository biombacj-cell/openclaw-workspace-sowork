# HEARTBEAT.md — Periodic Agent Tasks

> Instructions for periodic heartbeat turns. Loaded on heartbeat turns only (not every turn).
> Every task MUST have a clear stop condition — no open-ended loops.

---

## Daily Tasks

```
1. Write daily log to memory/YYYY-MM-DD.md:
   - What was accomplished or observed
   - Any notable results or anomalies
   - Items to follow up on
   Stop after writing the entry.

2. Check if files in outputs/ are older than 7 days
   Notify user if yes. Stop after notifying.

3. Verify gateway is still running (pm2 status)
   If down, notify user immediately. Stop after notifying.
```

## Marketing Team Heartbeat Tasks

### CMO Agent — Strategy
```
Weekly: Review outputs/campaigns/ for unreviewed briefs, notify user. Stop.
Weekly: Check if SOUL.md brand positioning needs updating, suggest edits. Stop.
```

### Content Agent — Writer
```
Daily: Check outputs/content/ for items not reviewed in 48h, remind user. Stop.
```

### Intel Agent — Research
```
Weekly: Scan top 3 competitor sites for changes
        Write brief to outputs/intel/YYYY-MM-DD-weekly.md
        Notify user: "Weekly intel brief is ready"
        Stop after brief is written.
```

## Alert Conditions

```
- Gateway running > 7 days: remind user to restart
- outputs/ folder > 50MB: notify user to clean up
- No memory log created today by 6pm: auto-create it
```

## Anti-Patterns

- Never send a message on every heartbeat (creates noise)
- Never monitor without a stop condition (causes loops)
- Pattern to follow: "Check X, write result to Y, notify if Z, then stop"

---

*Part of [openclaw-workspace-sowork](https://github.com/cj-wang-sowork/openclaw-workspace-sowork)*
