# brain/ — the shared brain for RS Photography's AI team

Three AI agents run RS Photography's back office together: **Claude**, **Codex** and
**Gemini**. None of them remembers anything between sessions, and they cannot message
each other directly. This folder is how they share memory and plan together.

## Two layers

| Layer | Where | What goes there |
|---|---|---|
| **Public** | this folder (`seo-data/brain/`, public GitHub repo) | How we work, who does what, the task board, the automation map, the growth plan in public-safe form |
| **Private** | private GitHub repo **`rsphotographysg-sudo/rs-brain`** (agents' working copy) and the **RS Master Index** in Notion (Ricky's dashboard, mirrored weekly) | Clients, quotes, prices, pipeline, finances, contacts, risks, dated to-dos |

Rule of thumb: if a competitor or a journalist reading it would hurt RS, it goes in Notion.

## Files

| File | Purpose | Who edits |
|---|---|---|
| `team.md` | Each agent's strengths, what it owns, what it must hand off | Claude, on Ricky's say-so |
| `protocol.md` | How the three plan, claim work, hand off and review | Claude, on Ricky's say-so |
| `board.md` | The task board: every open task, its owner and status | All agents |
| `log.md` | Append-only session log — the running memory | All agents (append only) |
| `decisions.md` | Decisions Ricky made, so nobody re-litigates them | All agents (record only) |
| `automation.md` | Every business function: automated today, next step, human gate | All agents |
| `growth-plan.md` | The revenue ladder and the maths behind it | Claude, on Ricky's say-so |

## How each agent loads this

- **Claude Code** reads `CLAUDE.md` → imports `AGENTS.md`.
- **Codex** reads `AGENTS.md` automatically.
- **Gemini CLI** reads `GEMINI.md` → imports `AGENTS.md`.

For the private layer each agent needs the Notion connector (MCP) signed in to Ricky's
workspace. Without it, work from this folder only and say so in `log.md`.
