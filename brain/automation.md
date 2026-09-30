# Automation map — every function, what runs today, what is next

"Fully automated" at RS means: **agents do all the work up to the human gate, and the
gate is one tap.** Legal, money and client-facing sends stay behind Ricky's GO.

Status: 🟢 running · 🟡 built, not live / partial · ⚪ not started

| ID | Function | Today | Next step | Owner | Human gate |
|---|---|---|---|---|---|
| A1 | **Daily approval list** | ⚪ drafts scattered across two mailboxes | One message each morning listing every draft waiting, with a one-word reply per item (GO / EDIT / KILL) | Claude | Ricky's reply |
| A2 | Enquiry intake | 🟡 WhatsApp AI in shadow mode; email manual | Every enquiry (email, WhatsApp, web form) logged to CRM within 5 min with a draft reply | Claude | Send |
| A3 | Quote generation | ⚪ manual | Script like `make_invoice.py` that builds a quote PDF from the rate card | Codex (build), Claude (drafts) | Send |
| A4 | Tender engine | 🟡 tender library + manual reads | Daily GeBIZ/TenderBoard scan → read full docs → price vs past winners → draft | Gemini (find/read/price), Claude (write) | Submit, sign |
| A5 | Lead generation | 🟢 LinkedIn drip, association outreach (drafts) | Tie every campaign to CRM stage; stop what does not convert | Claude | Send |
| A6 | Crew scheduling | 🟢 weekly schedule + master sheet scripts | Auto-propose crew by skill, area and leave; flag clashes 14 days out | Codex | Confirm roster |
| A7 | Shoot-day delivery | 🟡 LIVE 60™ built and tested | Pilot on 3 real jobs | Codex | Style approval |
| A8 | Post-production & QC | ⚪ manual | Automated cull + preset + QC notes; editors finish | Gemini (QC), Codex (pipeline) | Final delivery |
| A9 | Delivery, reviews, repeat | ⚪ manual | Auto-draft gallery handover + Google review ask + 6/12-month rebooking nudge | Claude | Send |
| A10 | Invoicing | 🟢 08:30 daily invoice drafts to Drive + email | Match payments; chase overdue at 7/14/30 days (drafts) | Claude | Send chaser |
| A11 | Finance reporting | 🟡 War Room daily report (local) | Weekly scoreboard (growth-plan.md) written to Notion | Gemini | — |
| A12 | Search presence (SEO/GEO) | 🟢 daily GEO content in this repo | Only publish verifiable facts; track AI-answer mentions | Gemini | — |
| A13 | Brain upkeep | 🟡 Notion index, updated by hand | Weekly plan + log every session (protocol.md) | Claude | — |

Code for A6 and A10 currently lives on branch `claude/h-tktsqn` (`invoices/`, `schedule/`),
not on `main`. The revenue engine and LIVE 60™ run on Ricky's machine, outside this repo.
