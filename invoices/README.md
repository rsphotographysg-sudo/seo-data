# Daily invoice generator

Tooling for the 08:30 (Singapore time) daily invoice routine: every morning an
invoice PDF is produced for each paid job that took place the day before.

* `make_invoice.py` – turns a JSON job file into `Invoice - <number>.pdf`
  (plus an `.xlsx` copy in the same layout as the hand-made invoices in
  Google Drive). Run `python3 invoices/make_invoice.py --help` for the schema.
* `assets/` – company logos used in the header.
* `examples/` – sample job files (sanitised copies only; real invoices are
  **not** committed to this public repository).

## Daily routine (what the scheduled session does)

1. Read the primary Google Calendar (`rsphotographysg@gmail.com`) for
   *yesterday* (Asia/Singapore). Each job is a calendar event whose description
   has `POC/Name`, `Event`, `Date`, `Time`, `Venue`, and a `Remarks` block with the
   amount (`S$440 - pending`), `PO No.` and `Billing Info`.
2. Keep only events that have an amount in the remarks. Skip recces, leave,
   reminders, and anything already marked paid / invoiced.
3. A multi-day job (Day 1 … Day N in one event) is invoiced the morning after
   its **last** day, listing every day; before that it is only reported as
   "in progress".
4. Entity: RS Photography (`RSP`) unless the remarks or the client's previous
   invoices say RS Media (`RSM`).
   Payment terms: `30 Days` when there is a PO number or the client is a
   government agency / statutory board / school; otherwise `Immediate`.
5. House style for the table, taken from the hand-made sheets:
   * Overtime is its own line item, `<Service> Extended till <end time>`
     (e.g. `Photography Service Extended till 9.15pm`). The `Time` line keeps
     the booked hours.
   * Durations are decimal — `(3.5 Hours)`, not `(3 Hours 30 Minutes)`.
   * Item descriptions stay plain (`Photography Service`); the hours and the
     day belong in the event block above, not in the description.
   * A job with several services on different clocks gets one `Time` line per
     service (`"time": ["Photography and Videography - 10am to 4pm (6 Hours)",
     "Live Feed: 10am to 12pm (2 Hours)"]`).
   * A multi-day job bills each day right under that day's event block: put the
     item inside the event (`"items"`), not in the invoice-level list.
   * `Attn` is the Billing Info verbatim; a PA CC/CCC/RN with no address given
     is just its name. A blank row sits between Attn and PIC unless the address
     already runs five lines.
   * Where the remarks say not to print the PO (NLB), leave `po_no` out.
6. Invoice number = `<RSM?><event date YYYYMMDD>-<n>1`, `n` = 1, 2, 3… for
   different clients on the same date. Check the Drive invoices folder first so
   numbers are never reused.
7. Write the JSON, run `make_invoice.py`, and deliver the PDFs:
   * upload to Google Drive → `Invoices` parent folder → the month's
     `NN. Invoices <Mon YYYY>` sub-folder (create it if missing), and
   * email them to rsphotographysg@gmail.com with a one-line summary per
     invoice and the list of jobs that were skipped and why.
8. Never send an invoice to a client. The PDFs are drafts for Ricky to review.

The Drive upload is what reaches the desktop: keep the Drive folder synced with
Google Drive for desktop (or drag the attachment from the 08:30 email).
