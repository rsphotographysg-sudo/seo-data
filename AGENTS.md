# AGENTS.md — shared instructions for every AI agent working for RS Photography

Claude (Claude Code), Codex (OpenAI) and Gemini (Gemini CLI / Gemini in Workspace) all
read this file. `CLAUDE.md` and `GEMINI.md` point here, so this is the one set of rules.

## Start of every session

1. Read `brain/README.md`, then `brain/board.md` and the last 20 entries of `brain/log.md`.
2. Read the private layer, the **RS Master Index** in Notion, if you have Notion access.
   It holds everything that must not be public (clients, prices, pipeline, finances).
3. Claim one task on `brain/board.md` before you start it (see `brain/protocol.md`).

## This repository is PUBLIC

`seo-data` is public and is deliberately indexed by search engines and AI systems.
Never commit: client names or contacts, quotes, price floors, pipeline or revenue
figures, bank details, staff personal data, invoices, credentials, or internal risk
items. Put those in the Notion Master Index and link to it by name.
`invoices/examples/` style sanitised samples are the only exception.

## Standing rules (from Ricky, apply to every agent)

- **Drafts only.** Nothing goes to a client, a tender portal, a bank, or social media
  without Ricky's explicit per-item GO. Automation does everything up to the gate.
- **Dedup before any new contact.** Run the full-history contact check (`rs-guard`)
  before drafting outreach to a new address.
- **Never claim** a certification, licence, award, client or result we cannot prove.
  No fabricated testimonials or AI-manipulated work shown as real.
- RS Photography is **not GST-registered**; all prices are nett.
- **Ask Ricky before adding any paid service**, subscription or API cost.
- Government procurement work (GeBIZ, MDDI) is prepared by agents but submitted by Ricky.

## Who does what

See `brain/team.md`. In short: Claude orchestrates and writes client-facing material,
Codex builds and tests code, Gemini researches and works across Google Workspace.
Every output that reaches Ricky is checked by a second agent first.

## End of every session

Append one entry to `brain/log.md`, update your row on `brain/board.md`, and record any
decision Ricky made in `brain/decisions.md`.
