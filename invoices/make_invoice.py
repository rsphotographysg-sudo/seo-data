#!/usr/bin/env python3
"""
RS Photography / RS Media invoice generator.

Reads a JSON job file and writes, for every invoice in it, a PDF (and an XLSX
copy in the same layout as the hand-made invoices kept in Google Drive).

Usage:
    python3 invoices/make_invoice.py jobs.json --out out_dir

Dependencies (installed automatically if missing): reportlab, openpyxl, pillow.

JSON schema (see examples/ for a real one):
{
  "issue_date": "2026-09-17",              # optional, defaults to today (Asia/Singapore)
  "invoices": [
    {
      "entity": "RSP" | "RSM",             # RS Photography (default) or RS Media Pte. Ltd.
      "number": "20260916-11",             # optional; auto = <prefix><event_date>-<n>1
      "event_date": "2026-09-16",          # date of the (first) job, used for numbering
      "attn": ["Company", "Address line", "Singapore 123456."],
      "pic": "Name, 91234567",             # optional
      "payment_terms": "30 Days" | "Immediate",
      "po_no": "POD26000057",              # optional
      "qtn_ref": "RSM20260812-02 dated 12th August 2026",   # optional
      "events": [
        {"event": "...", "date": "2026-09-16" | "16th September 2026, Wednesday",
         "day_label": "Day 1",             # optional, replaces the "Date" label
         "time": "12pm to 2pm (2 Hours)", "venue": ["line 1", "line 2"]}
      ],
      "items": [{"desc": "Photography Service", "amount": 440}],
      "payments_received": [{"date": "2026-09-01", "amount": 600}]   # optional
    }
  ]
}
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _ensure(pkg, mod=None):
    try:
        __import__(mod or pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", pkg])


_ensure("reportlab")
_ensure("openpyxl")
_ensure("pillow", "PIL")

from reportlab.lib.pagesizes import A4  # noqa: E402
from reportlab.pdfbase import pdfmetrics  # noqa: E402
from reportlab.pdfbase.ttfonts import TTFont  # noqa: E402
from reportlab.pdfgen import canvas  # noqa: E402

# ----------------------------------------------------------------------------
# Company entities
# ----------------------------------------------------------------------------
ENTITIES = {
    "RSP": {
        "name": "RS Photography",
        "reg": "53232305W",
        "email": "rsphotographysg@gmail.com",
        "prefix": "",
        "logo": os.path.join(HERE, "assets", "rsp_logo.jpeg"),
        # (no_col, description, amount) rows for the payment block
        "payment_info": [
            ("-", "This is an electronic invoice. No hardcopy invoice would be provided."),
            ("-", [("Payment can be made in the following forms. ", 0),
                   ("Please quote invoice number as reference", 1), (".", 0)]),
            ("", [("Cheque            : Payable to ", 0), ("RS Photography", 1)]),
            ("", [("Bank Transfer : DBS Current Account: ", 0), ("163-900020-1", 1)]),
            ("", [("PayNow           : ", 0), ("UEN 53232305W", 1)]),
            ("-", "A monthly late payment fee of 10% of the total balance due will be charged if payment has not been"),
            ("", "received by the due date."),
        ],
    },
    "RSM": {
        "name": "RS Media Pte. Ltd.",
        "reg": "202447665H",
        "email": "rsmediasg@gmail.com",
        "prefix": "RSM",
        "logo": os.path.join(HERE, "assets", "rsm_logo.png"),
        "payment_info": [
            ("1", "This is an electronic invoice. No hardcopy invoice will be provided."),
            ("2", [("Payment can be made in the following forms. ", 0),
                   ("Please quote invoice number as reference", 1), (".", 0)]),
            ("-", [("Cheque                                  : Payable to ", 0), ("RS Media Pte. Ltd.", 1)]),
            ("-", [("PayNow                                  : UEN ", 0), ("202447665H", 1)]),
            ("-", "Electronic Funds Transfer      :-"),
            ("", "Bank Name                            : DBS Bank Ltd"),
            ("", "Address                                  : 12 Marina Boulevard, DBS Asia Central,"),
            ("", "                                                  Marina Bay Financial Centre Tower 3,"),
            ("", "                                                  Singapore 018982."),
            ("", "Country                                  : Singapore"),
            ("", "Swift Code                             : DBSSSGSG"),
            ("", "Bank Code                             : 7171"),
            ("", "Branch Code                          : 072"),
            ("", [("Company Name                     : ", 0), ("RS Media Pte. Ltd.", 1)]),
            ("", [("Current Account Number      : ", 0), ("0721336944", 1)]),
            ("3", "A monthly late payment fee of 10% of the total balance due will be charged if payment has not been"),
            ("", "received by the due date."),
        ],
    },
}
ADDRESS = "22 Sin Ming Lane #06-82 Singapore 573969."
MOBILE = "Mobile: (+65) 8488 2645"
WEBSITE = "Website: www.rsphotographysg.com"


# ----------------------------------------------------------------------------
# Date helpers  ("07th September 2026, Monday" is the house style)
# ----------------------------------------------------------------------------
def _ordinal(d):
    if 11 <= d % 100 <= 13:
        suf = "th"
    else:
        suf = {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")
    return f"{d:02d}{suf}"


def fmt_date(d):
    return f"{_ordinal(d.day)} {d.strftime('%B %Y')}"


def fmt_event_date(d):
    return f"{fmt_date(d)}, {d.strftime('%A')}"


def parse_date(s):
    return dt.date.fromisoformat(s)


def today_sg():
    return (dt.datetime.utcnow() + dt.timedelta(hours=8)).date()


def money(v):
    """Return ("S$" or "-S$", "1,234.00")."""
    sign = "-" if v < 0 else ""
    return f"{sign}S$", f"{abs(v):,.2f}"


# ----------------------------------------------------------------------------
# Row model — one list of rows shared by the PDF and XLSX writers.
# Each row is a dict: kind + fields. Column letters follow the Excel template.
# ----------------------------------------------------------------------------
def _item(body, it, no):
    body.append({"kind": "item", "no": no, "desc": it.get("desc", ""),
                 "amount": float(it.get("amount", 0))})
    for line in it.get("extra_lines") or []:
        body.append({"kind": "item", "no": "", "desc": line, "amount": None})


def build_rows(inv, entity, issue_date):
    rows = []
    events = inv.get("events", [])
    multi = len(events) > 1
    po = inv.get("po_no")
    qtn = inv.get("qtn_ref")

    # -- table body --------------------------------------------------------
    body = [{"kind": "blank"}]
    if po:
        body.append({"kind": "detail", "no": "", "label": "PO No.", "value": po})
    if qtn:
        body.append({"kind": "detail", "no": "", "label": "Qtn Ref", "value": qtn})
    if po or qtn:
        if not multi:
            pass  # event details follow directly, as in the template
        else:
            body.append({"kind": "blank"})

    for i, ev in enumerate(events, 1):
        first = True
        no = str(i) if multi else ""
        if multi and i > 1:
            body.append({"kind": "blank"})
        d = ev.get("date", inv.get("event_date"))
        try:
            d = fmt_event_date(parse_date(d))
        except (ValueError, TypeError):
            pass
        lines = [("Event", ev.get("event", "")), (ev.get("day_label") or "Date", d)]
        times = ev.get("time") or []
        if isinstance(times, str):
            times = [times]
        for k, t in enumerate(times):
            lines.append(("Time" if k == 0 else "", t))
        venue = ev.get("venue") or []
        if isinstance(venue, str):
            venue = [venue]
        for k, v in enumerate(venue):
            lines.append(("Venue" if k == 0 else "", v))
        for label, value in lines:
            body.append({"kind": "detail", "no": no if first else "", "label": label, "value": value})
            first = False
        # An event's own items are billed straight under it, as in the template.
        for it in ev.get("items", []) or []:
            body.append({"kind": "blank"})
            _item(body, it, "-")

    body.append({"kind": "blank"})
    items = inv.get("items", [])
    multi = multi or any(ev.get("items") for ev in events)
    for i, it in enumerate(items, 1):
        _item(body, it, "-" if multi else str(i))
        body.append({"kind": "blank"})
    for p in inv.get("payments_received", []) or []:
        d = p.get("date")
        try:
            d = fmt_event_date(parse_date(d))
        except (ValueError, TypeError):
            pass
        body.append({"kind": "item", "no": "-", "desc": f"(-) Payment Received on {d}", "amount": -abs(float(p["amount"]))})
        body.append({"kind": "blank"})

    total = sum(r["amount"] for r in body if r["kind"] == "item" and r["amount"] is not None)

    # -- assemble ---------------------------------------------------------------
    rows.append({"kind": "logo"})            # row 1-2 (logo spans two rows)
    rows.append({"kind": "spacer", "h": 1.0})
    rows.append({"kind": "text", "text": entity["name"], "bold": True, "size": 12.5})
    for t in (ADDRESS, MOBILE, f"Registration No.: {entity['reg']}", f"Email: {entity['email']}", WEBSITE):
        rows.append({"kind": "text", "text": t})
    rows.append({"kind": "spacer", "h": 0.25})
    rows.append({"kind": "title", "text": "INVOICE"})
    rows.append({"kind": "spacer", "h": 0.25})

    attn = inv.get("attn") or []
    if isinstance(attn, str):
        attn = [attn]
    left = [("Attn", attn[0] if attn else "")] + [("", a) for a in attn[1:]]
    if inv.get("pic"):
        # A blank row separates Attn from PIC, but PIC never drops below the last
        # meta row on the right (Number of Page(s)), so a 5-line address loses it.
        while len(left) < 2 or (len(left) < 5 and left[-1] != ("", "")):
            left.append(("", ""))
        left.append(("PIC", inv["pic"]))
    terms = inv.get("payment_terms", "30 Days")
    right = [("Date of Issue", fmt_date(issue_date)), ("Invoice Number", inv["number"]), ("Payment Terms", terms)]
    if terms.lower().endswith("days"):
        try:
            n = int(terms.split()[0])
            right.append(("Payment Due Date", fmt_date(issue_date + dt.timedelta(days=n))))
        except ValueError:
            pass
    right.append(("Number of Page(s)", "Page 1 of 1"))
    for i in range(max(len(left), len(right))):
        l = left[i] if i < len(left) else ("", "")
        r = right[i] if i < len(right) else ("", "")
        rows.append({"kind": "meta", "llabel": l[0], "lvalue": l[1], "rlabel": r[0], "rvalue": r[1]})
    rows.append({"kind": "blank"})
    rows.append({"kind": "thead"})
    rows.extend(body)
    rows.append({"kind": "total", "amount": total})
    rows.append({"kind": "blank"})
    rows.append({"kind": "text", "text": "Payment Information:", "bold": True})
    for no, text in entity["payment_info"]:
        rows.append({"kind": "pay", "no": no, "text": text})
    rows.append({"kind": "blank"})
    rows.append({"kind": "text", "text": "Thank you."})
    return rows, total


# ----------------------------------------------------------------------------
# PDF writer
# ----------------------------------------------------------------------------
def _register_fonts():
    if os.environ.get("INVOICE_EMBED_FONT", "0") != "1":
        return "Helvetica", "Helvetica-Bold"
    cands = [
        ("/usr/share/fonts/truetype/msttcorefonts/Arial.ttf", "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf"),
        ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ]
    for reg, bold in cands:
        if os.path.exists(reg) and os.path.exists(bold):
            pdfmetrics.registerFont(TTFont("Inv", reg))
            pdfmetrics.registerFont(TTFont("Inv-Bold", bold))
            return "Inv", "Inv-Bold"
    return "Helvetica", "Helvetica-Bold"


# Excel column widths (characters) from the template; used to place columns.
COL_W = {"A": 4.0, "B": 1.16, "C": 7.83, "D": 1.16, "E": 12.33, "F": 12.33, "G": 9.83, "H": 11.16, "I": 11.16, "J": 1.16, "K": 20.33}
COLS = "ABCDEFGHIJK"


def write_pdf(rows, path):
    font, bold = _register_fonts()
    W, H = A4
    margin_x = 0.7 * 72
    margin_top = 0.75 * 72
    width = W - 2 * margin_x
    total_chars = sum(COL_W.values())
    x = {}
    cur = margin_x
    for c in COLS:
        x[c] = cur
        cur += width * COL_W[c] / total_chars
    x["END"] = margin_x + width
    LINE = 13.2         # row pitch (14pt Excel rows at 92% print scale)
    FS = 10.1           # 11pt Arial at 92%
    PAD = 2.5

    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("Invoice")
    c.setLineWidth(0.6)
    y = H - margin_top

    def text(xx, yy, s, f=font, size=FS, align="left"):
        c.setFont(f, size)
        if align == "right":
            c.drawRightString(xx, yy, s)
        elif align == "center":
            c.drawCentredString(xx, yy, s)
        else:
            c.drawString(xx, yy, s)

    def baseline(top, size=FS):
        return top - LINE + (LINE - size) / 2 + 1.2

    # table vertical guides: NO. col = A..B, AMOUNT col = J..K
    tbl_left, no_right, amt_left, tbl_right = x["A"], x["C"], x["J"], x["END"]
    in_table = False
    rlabels = [r["rlabel"] for r in rows if r["kind"] == "meta" and r["rlabel"]]
    colon_x = x["J"] + 0.5
    llabels = [r["llabel"] for r in rows if r["kind"] == "meta" and r["llabel"]]
    lcolon_x = max(x["B"] + 0.5, x["A"] + max(pdfmetrics.stringWidth(t, font, FS) for t in llabels) + 4)

    for r in rows:
        k = r["kind"]
        if k == "logo":
            logo = r.get("path")
            if logo and os.path.exists(logo):
                lw, lh = 4.08 * 72 * 0.92, 0.386 * 72 * 0.92   # anchor size in the Excel template
                c.drawImage(logo, x["A"] + 3, y - lh - 1, width=lw, height=lh, mask="auto")
            y -= 2 * LINE
            continue
        if k == "spacer":
            y -= LINE * r["h"]
            continue
        if k == "text":
            size = r.get("size", 11) * 0.92
            text(x["A"], baseline(y, size), r["text"], bold if r.get("bold") else font, size)
            y -= LINE if size <= FS + 0.5 else LINE * 1.2
            continue
        if k == "title":
            size = 14 * 0.92
            text((x["A"] + x["END"]) / 2, baseline(y, size), r["text"], bold, size, "center")
            y -= LINE * 1.25
            continue
        if k == "meta":
            b = baseline(y)
            if r["llabel"]:
                text(x["A"], b, r["llabel"])
                text(lcolon_x, b, ":")
            if r["lvalue"]:
                text(max(x["C"], lcolon_x + 6), b, r["lvalue"])
            if r["rlabel"]:
                text(colon_x - 3, b, r["rlabel"], font, FS, "right")
                text(colon_x, b, ":")
                text(colon_x + 6, b, r["rvalue"])
            y -= LINE
            continue
        if k == "thead":
            c.rect(tbl_left, y - LINE, tbl_right - tbl_left, LINE)
            c.line(no_right, y, no_right, y - LINE)
            c.line(amt_left, y, amt_left, y - LINE)
            b = baseline(y)
            text((tbl_left + no_right) / 2, b, "NO.", bold, FS, "center")
            text((no_right + amt_left) / 2, b, "DESCRIPTION", bold, FS, "center")
            text((amt_left + tbl_right) / 2, b, "AMOUNT", bold, FS, "center")
            y -= LINE
            in_table = True
            table_top = y
            continue
        if k == "total":
            c.rect(tbl_left, y - LINE, tbl_right - tbl_left, LINE)
            c.line(amt_left, y, amt_left, y - LINE)
            b = baseline(y)
            text(amt_left - PAD, b, "BALANCE DUE", bold, FS, "right")
            cur, num = money(r["amount"])
            text(amt_left + PAD, b, cur, bold)
            text(tbl_right - PAD, b, num, bold, FS, "right")
            # close the body borders
            c.line(tbl_left, table_top, tbl_left, y)
            c.line(no_right, table_top, no_right, y)
            c.line(amt_left, table_top, amt_left, y)
            c.line(tbl_right, table_top, tbl_right, y)
            y -= LINE
            in_table = False
            continue
        if k == "blank":
            y -= LINE
            continue
        b = baseline(y)
        if k == "detail":
            if r["no"]:
                text((tbl_left + no_right) / 2, b, r["no"], font, FS, "center")
            if r["label"]:
                text(x["C"], b, r["label"])
                text(x["D"] + 0.5, b, ":")
            text(x["E"], b, r["value"])
        elif k == "item":
            if r["no"]:
                text((tbl_left + no_right) / 2, b, r["no"], font, FS, "center")
            text(x["C"], b, r["desc"])
            if r["amount"] is not None:
                cur, num = money(r["amount"])
                text(amt_left + PAD, b, cur)
                text(tbl_right - PAD, b, num, font, FS, "right")
        elif k == "pay":
            if r["no"]:
                text((tbl_left + no_right) / 2, b, r["no"], font, FS, "center")
            runs = r["text"] if isinstance(r["text"], list) else [(r["text"], 0)]
            xx = x["C"]
            for seg, strong in runs:
                f = bold if strong else font
                text(xx, b, seg, f, FS)
                xx += pdfmetrics.stringWidth(seg, f, FS)
        y -= LINE
        if y < 40:
            raise SystemExit("Invoice is too long for one page; split the items.")

    c.showPage()
    c.save()


# ----------------------------------------------------------------------------
# XLSX writer (same layout as the hand-made template, one sheet per invoice)
# ----------------------------------------------------------------------------
def _rich(runs):
    """[(text, bold)] -> an Excel rich-text cell value matching the template."""
    from openpyxl.cell.rich_text import CellRichText, TextBlock
    from openpyxl.cell.text import InlineFont
    out = CellRichText()
    for seg, strong in runs:
        out.append(TextBlock(InlineFont(rFont="Arial", sz=11, b=bool(strong)), seg))
    return out


def write_xlsx(all_rows, path, append_to=None):
    import openpyxl
    from openpyxl.drawing.image import Image as XLImage
    from openpyxl.styles import Alignment, Border, Font, Side
    from openpyxl.utils import get_column_letter

    if append_to:                     # continue the day's existing workbook
        wb = openpyxl.load_workbook(append_to)
    else:
        wb = openpyxl.Workbook()
        wb.remove(wb.active)
    thin = Side(style="thin")
    ACC = '_-[$S$]\\ * #,##0.00_-;\\-[$S$]\\ * #,##0.00_-;_-[$S$]\\ * "-"??_-;_-@_-'

    for title, rows, logo in all_rows:
        ws = wb.create_sheet(title[:31])
        for col, w in COL_W.items():
            ws.column_dimensions[col].width = w
        ws.sheet_format.defaultRowHeight = 13
        base = Font(name="Arial", size=11)
        boldf = Font(name="Arial", size=11, bold=True)
        rn = 0
        table_top = None

        def put(cell, v, f=base, align=None, fmt=None):
            c = ws[cell]
            c.value = v
            c.font = f
            if align:
                c.alignment = align
            if fmt:
                c.number_format = fmt
            return c

        for r in rows:
            k = r["kind"]
            if k == "logo":
                rn += 2
                ws.row_dimensions[rn - 1].height = 17
                ws.row_dimensions[rn].height = 17
                if logo and os.path.exists(logo):
                    img = XLImage(logo)
                    ratio = img.width / img.height
                    img.height = 37
                    img.width = int(37 * ratio)
                    ws.add_image(img, "A1")
                continue
            if k == "spacer":
                if r["h"] < 1:
                    rn += 1
                    ws.row_dimensions[rn].height = 3
                continue
            rn += 1
            ws.row_dimensions[rn].height = 14
            if k == "text":
                f = Font(name="Arial", size=r.get("size", 11), bold=r.get("bold", False))
                put(f"A{rn}", r["text"], f, Alignment(horizontal="left"))
                if r.get("size", 11) > 11:
                    ws.row_dimensions[rn].height = 17
            elif k == "title":
                put(f"A{rn}", r["text"], Font(name="Arial", size=14, bold=True), Alignment(horizontal="center", vertical="center"))
                ws.merge_cells(f"A{rn}:K{rn}")
                ws.row_dimensions[rn].height = 18
            elif k == "meta":
                if r["llabel"]:
                    put(f"A{rn}", r["llabel"]); put(f"B{rn}", ":")
                if r["lvalue"]:
                    put(f"C{rn}", r["lvalue"])
                if r["rlabel"]:
                    put(f"I{rn}", r["rlabel"], align=Alignment(horizontal="right", vertical="center"))
                    put(f"J{rn}", ":", align=Alignment(vertical="center"))
                    put(f"K{rn}", r["rvalue"], align=Alignment(horizontal="left", vertical="center"))
            elif k == "thead":
                put(f"A{rn}", "NO.", boldf, Alignment(horizontal="center", vertical="center"))
                put(f"C{rn}", "DESCRIPTION", boldf, Alignment(horizontal="center", vertical="center"))
                put(f"J{rn}", "AMOUNT", boldf, Alignment(horizontal="center", vertical="center"))
                ws.merge_cells(f"A{rn}:B{rn}"); ws.merge_cells(f"C{rn}:I{rn}"); ws.merge_cells(f"J{rn}:K{rn}")
                for col in COLS:
                    ws[f"{col}{rn}"].border = Border(top=thin, bottom=thin,
                                                     left=thin if col in "ACJ" else None,
                                                     right=thin if col in "BIK" else None)
                table_top = rn + 1
            elif k in ("blank", "detail", "item"):
                if table_top is not None:
                    ws.merge_cells(f"A{rn}:B{rn}"); ws.merge_cells(f"J{rn}:K{rn}")
                    for col in COLS:
                        ws[f"{col}{rn}"].border = Border(left=thin if col in "ACJ" else None,
                                                         right=thin if col in "BK" else None)
                    ws[f"A{rn}"].alignment = Alignment(horizontal="center", vertical="center")
                    ws[f"J{rn}"].number_format = ACC
                    ws[f"J{rn}"].alignment = Alignment(horizontal="center", vertical="center")
                if k == "detail":
                    if r["no"]:
                        put(f"A{rn}", int(r["no"]) if r["no"].isdigit() else r["no"], align=Alignment(horizontal="center", vertical="center"))
                    if r["label"]:
                        put(f"C{rn}", r["label"]); put(f"D{rn}", ":")
                    put(f"E{rn}", r["value"])
                elif k == "item":
                    if r["no"]:
                        put(f"A{rn}", int(r["no"]) if r["no"].isdigit() else r["no"], align=Alignment(horizontal="center", vertical="center"))
                    put(f"C{rn}", r["desc"])
                    if r["amount"] is not None:
                        put(f"J{rn}", r["amount"], fmt=ACC, align=Alignment(horizontal="center", vertical="center"))
            elif k == "total":
                put(f"A{rn}", "BALANCE DUE", boldf, Alignment(horizontal="right", vertical="center"))
                put(f"J{rn}", f"=SUM(J{table_top}:K{rn - 1})", boldf, Alignment(horizontal="center", vertical="center"), ACC)
                ws.merge_cells(f"A{rn}:I{rn}"); ws.merge_cells(f"J{rn}:K{rn}")
                for col in COLS:
                    ws[f"{col}{rn}"].border = Border(top=thin, bottom=thin,
                                                     left=thin if col in "AJ" else None,
                                                     right=thin if col in "IK" else None)
                table_top = None
            elif k == "pay":
                if r["no"]:
                    put(f"A{rn}", int(r["no"]) if r["no"].isdigit() else r["no"], align=Alignment(horizontal="center"))
                if isinstance(r["text"], list):
                    put(f"C{rn}", _rich(r["text"]))
                else:
                    put(f"C{rn}", r["text"])
        ws.print_area = f"A1:K{rn}"
        ws.page_setup.orientation = "portrait"
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 1
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_margins.left = ws.page_margins.right = 0.7
        ws.page_margins.top = ws.page_margins.bottom = 0.75
    wb.save(path)


def _b64(path):
    """Write <path>.b64 (base64, 76-column lines) for uploading via connectors."""
    import base64
    with open(path, "rb") as f, open(path + ".b64", "w") as o:
        data = base64.b64encode(f.read()).decode()
        o.write("\n".join(data[i:i + 76] for i in range(0, len(data), 76)) + "\n")


# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("jobs", help="JSON file describing the invoices")
    ap.add_argument("--out", default=".", help="output directory")
    ap.add_argument("--no-xlsx", action="store_true", help="skip the XLSX copy")
    ap.add_argument("--append-to", help="existing workbook to add the sheets to")
    args = ap.parse_args()

    with open(args.jobs) as f:
        spec = json.load(f)
    os.makedirs(args.out, exist_ok=True)
    issue_date = parse_date(spec["issue_date"]) if spec.get("issue_date") else today_sg()

    # auto-number: <prefix><YYYYMMDD>-<n>1, n = running count per entity+date
    counters = {}
    outputs = []
    sheets = {}
    for inv in spec["invoices"]:
        ent_key = (inv.get("entity") or "RSP").upper()
        entity = ENTITIES[ent_key]
        ev_date = parse_date(inv["event_date"])
        key = (ent_key, ev_date)
        counters[key] = counters.get(key, 0) + 1
        if not inv.get("number"):
            inv["number"] = f"{entity['prefix']}{ev_date:%Y%m%d}-{counters[key]}1"
        rows, total = build_rows(inv, entity, issue_date)
        rows[0]["path"] = entity["logo"]
        pdf = os.path.join(args.out, f"Invoice - {inv['number']}.pdf")
        write_pdf(rows, pdf)
        outputs.append((inv["number"], total, pdf))
        book = f"Invoice - {entity['prefix']}{ev_date:%Y%m%d}.xlsx"
        sheets.setdefault(book, []).append((f"Invoice {inv['number']}", rows, entity["logo"]))
        print(f"{inv['number']}\tS$ {total:,.2f}\t{pdf}")
        _b64(pdf)

    if not args.no_xlsx:
        for book, all_rows in sheets.items():
            p = os.path.join(args.out, book)
            write_xlsx(all_rows, p, append_to=args.append_to)
            print(f"xlsx\t{p}")
            _b64(p)
    return outputs


if __name__ == "__main__":
    main()
