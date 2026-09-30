# Protocol — how the three agents plan and work together

## 1. Weekly planning (Monday, Singapore time)

1. **Claude** reads `board.md`, `log.md` (last week), `decisions.md`, the Notion Master
   Index and the calendar, then writes a plan entry in `log.md` headed
   `PLAN week of <date>`: top 3 outcomes, and which agent owns each task.
2. **Gemini** adds a research brief to the same entry: new tenders closing in the next
   14 days, market or competitor changes worth acting on.
3. **Codex** adds a build note: what automation is being shipped this week and what it
   needs from Ricky (keys, files, approvals).
4. Ricky reads one page, changes what he wants, and says GO. His changes go into
   `decisions.md`.

If an agent is not run that week, the others carry on and note the gap in `log.md`.

## 2. Claiming work

- Every task lives on `board.md` with an ID (`T-###`).
- To start a task, set its owner to yourself and status to `doing`, and commit that
  change **before** doing the work. If another agent already shows `doing`, pick
  something else.
- Work on a branch named `<agent>/<T-id>-<short-name>`, e.g. `codex/T-004-quote-generator`.
- When done, status → `review` and name the reviewer from `team.md` → Review pairs.

## 3. Handoffs

When you stop mid-task or pass work on, append to `log.md`:

```
## 2026-09-30 14:10 SGT — Claude — T-001
Did: …
State: … (branch, files, anything half-finished)
Next: … (exact next step, and who)
Needs Ricky: … (or "nothing")
```

`log.md` is append-only. Never rewrite another agent's entry.

## 4. Disagreements

If two agents disagree, both write their case in `log.md` in three lines each, and the
item goes on Ricky's daily approval list. Ricky decides, the decision goes in
`decisions.md`, and nobody reopens it without new facts.

## 5. What never changes

- Drafts only; Ricky's GO for anything external.
- Nothing private in this public repo.
- Every claim in client-facing material must be provable.
- Ask before spending money.
