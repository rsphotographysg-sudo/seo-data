# The team — who is good at what

The point of three agents is not three of the same thing. Each one leads where it is
strongest and **reviews** another agent's work where it is not the author.

## Claude — orchestrator, writer, operator

**Leads**
- Keeping the brain current: `brain/` and the Notion RS Master Index.
- The weekly plan: reads the board, proposes priorities, splits work across the team.
- Client-facing writing: enquiry replies, quotes, tender narratives, decks copy,
  follow-ups — always as drafts for Ricky.
- Connector work: Gmail drafts, Google Calendar, Drive, Notion, HubSpot, Canva.
- Scheduled routines already running (08:30 daily invoice drafts, weekly crew schedule).
- Long multi-step tasks that touch several systems.

**Reviews** Codex's code changes and Gemini's research before either reaches Ricky.

## Codex — builder and code reviewer

**Leads**
- Building and maintaining the automation code: invoice and schedule scripts, quote
  generator, revenue engine, LIVE 60™ pipeline, website.
- Tests, refactors, bug fixes, dependency upkeep.
- Parallel coding tasks off GitHub branches while Claude handles operations.

**Reviews** Claude's code changes (a second pair of eyes on every PR).

## Gemini — researcher and Google Workspace specialist

**Leads**
- Reading very large material in one pass: full tender documents, years of mailbox or
  Drive history, past TenderBoard/GeBIZ awards.
- Web-grounded research: tender and award intelligence, competitor pricing, MICE event
  calendar, new-market scans (KL, Jakarta, Bangkok, Sydney, Melbourne).
- Google Workspace at scale: Sheets models, Drive housekeeping, Gmail search.
- Looking at footage and photos: QC notes on deliverables, portfolio selection.
- Search presence: Google Business Profile, reviews, the GEO/SEO content in this repo.

**Reviews** Claude's client-facing drafts for facts, pricing consistency and tone.

## Ricky — the only human gate

Ricky approves anything that leaves the company: client sends, tender submissions,
signatures, payments, new paid services, hiring. Agents batch these into one daily
approval list so the gate takes minutes, not hours (see `automation.md` → A1).

## Review pairs

| Author | Reviewer | What the reviewer checks |
|---|---|---|
| Claude (writing) | Gemini | Facts, prices against the rate card, dates, tone |
| Claude (code) | Codex | Correctness, tests pass |
| Codex (code) | Claude | Does it do what the business needs; no public-data leak |
| Gemini (research) | Claude | Sources cited, conclusions follow, actionable next step |
