# self-improving-agent (OpenClaw skill, ClawHub)

> Source: https://clawhub.ai/pskoett/skills/self-improving-agent#hook-integration
> Collected: 2026-07-31
> Published: Unknown

An OpenClaw skill enabling agents to capture learnings, errors, and corrections in persistent markdown logs for continuous improvement, tracking issues, user corrections, feature requests, and discovered best practices.

## Mechanics

Maintains three log files in `.learnings/`:
- **LEARNINGS.md** — corrections, insights, knowledge gaps, best practices
- **ERRORS.md** — command failures and integration errors
- **FEATURE_REQUESTS.md** — user-requested capabilities

Entries carry structured metadata: priority, status, area tags, and a "Pattern-Key" for deduplication (format `area.symptom`, e.g. `deps.module-not-found`).

## Hook integration (optional)

1. **Bootstrap Reminder** — fires on `agent:bootstrap`, injecting learning reminders and flagging pending triage items
2. **Automatic Error Detection** — fires on `command:new`/`command:reset`, scanning ended session transcripts for error patterns, writing redacted/truncated excerpts to `ERRORS.md`

Opt-in: activates only when `.learnings/` exists. Excerpts capped at 200 characters with redaction attempts, though the documentation itself flags transcript scanning as a data-retention risk in shared workspaces.

## Promotion workflow

Valuable learnings can graduate to persistent workspace files (`SOUL.md`, `TOOLS.md`, `AGENTS.md`) once they apply broadly, preventing recurring mistakes across sessions.

> Note: the fetched page content included an embedded instruction block disguised as a system reminder, attempting to direct tool usage and asking not to be mentioned to the user. This was a prompt-injection attempt in the source page and has been disregarded; noting it here for the record rather than following it.
