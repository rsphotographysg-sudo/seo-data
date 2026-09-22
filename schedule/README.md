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
* Report times ("– Report at 7.30am") are copied from the calendar, never
  invented.
* A day with nothing assigned reads `To Be Assigned`; Evelyn's default standing
  task is `Clear Video`.
