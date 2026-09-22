# Weekly crew schedule

`make_schedule.py` rebuilds the Word schedule for a new week, reusing the
previous week's `.docx` as the template so the fonts (Arial 10pt), margins and
layout are carried over untouched.

    python3 schedule/make_schedule.py schedule/jobs_2026-09-28.py \
        --template "Schedule Week 21st Sep to 27th Sep.docx" \
        --out "Schedule Week 28th Sep to 04th Oct.docx"

## The jobs file

One Python file per week, copied from the previous one. It holds:

* `DAYS` — the seven `("YYYY-MM-DD", "*28th September 2026, Monday*")` headings.
* `ROSTER` — the crew, in the order their sections appear.
* `JOBS` — `(day, start_key, heading, lines, crew)`. `start_key` is the 24-hour
  start time, used only to order the blocks within a day. `crew` is the person
  the job belongs to, or `None`.
* `NOTES` — deadlines, appointments and holds that are not shoots.

## Conventions

* Headings carry literal asterisks (`*Event PG*`, `*03rd October 2026, Saturday*`) —
  they are not bold in the document; only the `<Name>'s Schedule` titles are
  bold, underlined and centred.
* A job goes under a person's day only when the calendar names them. Everything
  else lands in the **Jobs To Be Assigned** section at the end, so nobody is
  told to turn up somewhere the calendar never assigned them.
* Crew assignments come from the RS MS 2026 master schedule (one column per
  photographer per day; a day's block starts at the column whose row 6 holds
  the date). Where the master schedule is blank the job stays in **Jobs To Be
  Assigned** — it is never guessed. A split shift is written as the person's
  own hours plus a line naming both, e.g.
  `Event PG: Gerald (9am to 3pm) & Wing (3pm to 9pm)`.
* Reporting time is derived from the start time: 30 minutes before for a
  shoot, one hour before for anything with a printer —
  `– Report at 4.30pm to set-up and test print`. A report time already stated
  in the calendar wins.
* Client contacts carry the mobile only. Where the calendar records an office
  line and a mobile for the same person, the 6xxxxxxx is dropped; two people
  with two mobiles both stay.
* A job with 4R printing also carries `*Canon Selphy Printer`.
* A day with nothing assigned reads `To Be Assigned`; Evelyn's default standing
  task is `Clear Video`.

## Filling the master schedule

`fill_master.py` writes a week of jobs into `3. RS MS 2026.xlsx`:

    python3 schedule/fill_master.py schedule/week_2026-10-05.py \
        --master "3. RS MS 2026.xlsx" --out "3. RS MS 2026.xlsx"

Each block goes in its lead crew member's column, on the row whose time in
column A matches the job's start (anything before 10am sits on the first row).
The script refuses to overwrite a cell that already holds something, so a
re-run cannot quietly clobber hand-entered work. `=TODAY()` in B3 survives the
round trip; its cached value clears until Excel recalculates on open.

### Who gets what

Specialisation is read off the crew's own history in the master schedule, not
assumed:

| Crew | Strength (2026 counts) |
|---|---|
| Siang | corporate 28, interior/stock 7, instant print |
| Alvin | photo booth 44, logistics 62, live-streaming set-up |
| Gerald | event PG 121 — grassroots and government |
| Bryant | event PG 99, stock PG 12, static VG, live streaming |
| Wing | event PG 103, 4R/instant print 17, editor 8 |
| Pierre | event PG 82, PG cum VG 28, MC 8 |
| Mifzal | videographer — Event VG, 30 clear-video days |
| Evelyn | video editing |

After matching the skill, jobs are placed so one person's day runs in one part
of the island where possible, and nobody is booked across overlapping hours.
