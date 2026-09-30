# Task board

Claim a task by setting **Owner** and **Status → doing** and committing before you start
(`protocol.md` §2). Status: `todo` · `doing` · `review` · `blocked` · `done`.
Private detail (client names, amounts) stays in Notion; reference it by name here.

| ID | Task | Automation | Owner | Status | Reviewer | Notes |
|---|---|---|---|---|---|---|
| T-001 | Daily approval list: one morning message listing every draft waiting on Ricky, GO/EDIT/KILL per item | A1 | Claude | doing | Gemini | Biggest lever — the Master Index shows money stuck in unsent drafts |
| T-002 | Refresh the Notion send queue and tender board against real mailbox state (sent / won / lost / expired / pending) | A1 | Gemini | todo | Claude | August figures are stale; verify before acting |
| T-003 | Tender price intelligence: collect past award results, model the price gap to winners | A4 | Gemini | todo | Claude | Master Index records RS pricing well above winners |
| T-004 | Quote generator from the rate card (PDF + xlsx, same house style as invoices) | A3 | Codex | todo | Claude | Reuse `invoices/make_invoice.py` patterns |
| T-005 | Merge `invoices/` and `schedule/` tooling from `claude/h-tktsqn` onto `main` without real client data | A6, A10 | Codex | todo | Claude | Public repo — sanitised examples only |
| T-006 | Crew auto-assign: propose crew by skill table, area and leave; flag clashes 14 days out | A6 | Codex | todo | Claude | Skill table in `schedule/README.md` |
| T-007 | Enquiry intake: every email/WhatsApp/web enquiry logged to CRM with a draft reply in 5 min | A2 | Claude | todo | Gemini | WhatsApp AI is in shadow mode today |
| T-008 | Delivery follow-up: gallery handover + Google review ask + rebooking nudge drafts | A9 | Claude | todo | Gemini | |
| T-009 | Overdue receivables: daily list + chaser drafts at 7/14/30 days | A10 | Claude | todo | Gemini | |
| T-010 | Weekly scoreboard (growth-plan.md metrics) written to Notion every Monday | A11 | Gemini | todo | Claude | |
| T-011 | LIVE 60™ pilot on 3 confirmed jobs | A7 | Codex | blocked | Claude | Waiting on Ricky: storage switch-on + Lightroom preset & sample frames |
| T-012 | Private brain lives in private GitHub repo `rs-brain` | A13 | Claude | doing | — | D-008 GO; repo creation needs Ricky (GitHub app cannot create repos) |
| T-013 | Set up Codex and Gemini with this repo + Notion access | A13 | Ricky | todo | — | Steps in log.md 2026-09-30 entry |
