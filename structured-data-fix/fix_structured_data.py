#!/usr/bin/env python3
"""Check (and partly fix) the structured-data errors Google Search Console
reported for rsphotographysg.com in July 2026.

  1. Unparsable structured data - "Duplicate unique property"   (critical)
  2. Events  - missing organizer.url, endDate, offers           (non-critical)
  3. Videos  - uploadDate missing a timezone / invalid datetime (non-critical)

Usage:
  python3 fix_structured_data.py <site-folder>          # report only
  python3 fix_structured_data.py <site-folder> --fix    # also fix uploadDate

--fix only changes uploadDate values (adds the Singapore timezone +08:00).
Duplicate properties and Event fields need a human decision, so they are
reported with the file and the property name, never changed automatically.
"""
import json
import re
import sys
from pathlib import Path

TZ = "+08:00"
LDJSON = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.S | re.I,
)
SOURCE_EXT = {".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".astro", ".vue",
              ".svelte", ".json", ".md", ".mdx", ".njk", ".liquid", ".hbs"}
SKIP_DIRS = {"node_modules", ".git", ".next", ".cache", ".wrangler"}
ISO_TZ = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:\d{2})$")
UPLOAD = re.compile(r'("uploadDate"\s*:\s*")([^"]*)(")')


def iter_files(root):
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in SOURCE_EXT and not (SKIP_DIRS & set(p.parts)):
            yield p


def parse_dupes(text):
    dupes = []

    def hook(pairs):
        seen = set()
        for k, _ in pairs:
            if k in seen:
                dupes.append(k)
            seen.add(k)
        return dict(pairs)

    return json.loads(text, object_pairs_hook=hook), dupes


def types_of(node):
    t = node.get("@type", [])
    return set(t if isinstance(t, list) else [t])


def walk(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)


def fixed_upload_date(value):
    v = value.strip()
    if ISO_TZ.match(v):
        return None
    m = re.match(r"^(\d{4}-\d{2}-\d{2})$", v)
    if m:
        return f"{m.group(1)}T00:00:00{TZ}"
    m = re.match(r"^(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2}(:\d{2})?)$", v)
    if m:
        t = m.group(2) if m.group(3) else m.group(2) + ":00"
        return f"{m.group(1)}T{t}{TZ}"
    return "UNFIXABLE"


def check_block(data, dupes):
    problems = []
    for k in dupes:
        problems.append(("CRITICAL", f'duplicate property "{k}" in one object - keep one, delete the other'))
    for node in walk(data):
        ts = types_of(node)
        if ts & {"Event", "BusinessEvent", "EducationEvent", "SocialEvent", "ExhibitionEvent"}:
            name = node.get("name", "(no name)")
            org = node.get("organizer")
            orgs = org if isinstance(org, list) else [org] if org else []
            if not orgs:
                problems.append(("EVENT", f'"{name}": no organizer'))
            elif any(isinstance(o, dict) and not o.get("url") for o in orgs):
                problems.append(("EVENT", f'"{name}": organizer has no "url"'))
            for f in ("startDate", "endDate", "location", "offers"):
                if not node.get(f):
                    problems.append(("EVENT", f'"{name}": missing "{f}"'))
        if "VideoObject" in ts:
            name = node.get("name", "(no name)")
            ud = node.get("uploadDate")
            if not ud:
                problems.append(("VIDEO", f'"{name}": missing "uploadDate"'))
            elif not ISO_TZ.match(str(ud)):
                problems.append(("VIDEO", f'"{name}": uploadDate "{ud}" needs ISO 8601 with timezone, e.g. 2026-05-07T09:00:00{TZ}'))
            for f in ("thumbnailUrl", "description"):
                if not node.get(f):
                    problems.append(("VIDEO", f'"{name}": missing "{f}"'))
    return problems


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    root = Path(sys.argv[1])
    do_fix = "--fix" in sys.argv[2:]
    total = {"CRITICAL": 0, "EVENT": 0, "VIDEO": 0}
    fixed = 0
    for path in iter_files(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(root)
        blocks = [m.group(1) for m in LDJSON.finditer(text)] if path.suffix.lower() in {".html", ".htm"} else []
        if path.suffix.lower() == ".json" and '"@context"' in text:
            blocks = [text]
        for b in blocks:
            try:
                data, dupes = parse_dupes(b.strip())
            except json.JSONDecodeError as e:
                print(f"[CRITICAL] {rel}: JSON-LD does not parse ({e.msg}, line {e.lineno})")
                total["CRITICAL"] += 1
                continue
            for kind, msg in check_block(data, dupes):
                print(f"[{kind}] {rel}: {msg}")
                total[kind] += 1
        if do_fix and "uploadDate" in text:
            def repl(m):
                nonlocal fixed
                new = fixed_upload_date(m.group(2))
                if new is None or new == "UNFIXABLE":
                    if new == "UNFIXABLE":
                        print(f"[MANUAL] {rel}: uploadDate \"{m.group(2)}\" - write it as YYYY-MM-DDTHH:MM:SS{TZ}")
                    return m.group(0)
                fixed += 1
                print(f"[FIXED] {rel}: uploadDate \"{m.group(2)}\" -> \"{new}\"")
                return m.group(1) + new + m.group(3)
            new_text = UPLOAD.sub(repl, text)
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")
    print()
    print(f"Critical (duplicate / unparsable): {total['CRITICAL']}")
    print(f"Event fields missing:              {total['EVENT']}")
    print(f"Video date problems:               {total['VIDEO']}")
    if do_fix:
        print(f"uploadDate values fixed:           {fixed}  (re-run without --fix to confirm)")
    sys.exit(1 if total["CRITICAL"] else 0)


if __name__ == "__main__":
    main()
