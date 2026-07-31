#!/usr/bin/env python3
"""Diff two crawl exports and report SEO regressions.

Compares a pre-release crawl against a post-release crawl on the dimensions in
references/diff-checks.md, and writes one row per regression. Reports only; changes nothing.

Expected columns (case-insensitive, extras ignored, missing columns skip that check):

  url                required, the join key
  status_code        200, 301, 404, 500
  indexability       or meta_robots, e.g. "index,follow" / "noindex"
  canonical          canonical URL
  redirect_url       redirect target
  title              title tag
  h1                 first H1
  meta_description   meta description
  word_count         rendered word count
  inlinks            count of inbound internal links
  schema_types       comma-separated schema.org types
  in_sitemap         true/false

Column names from Screaming Frog, Sitebulb, and Semrush exports are mapped automatically
where they differ. Anything unrecognised is ignored rather than guessed at.

Severity is assigned on the regression type only. Join the output with Search Console clicks
to get real severity, because the same broken canonical is P0 on a page with traffic and P2
on a page without.

Usage:
  python crawl_diff.py before.csv after.csv --out regressions.csv
  python crawl_diff.py before.csv after.csv --clicks clicks.csv --out regressions.csv
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from typing import Optional

# Common export headers mapped to canonical field names.
ALIASES = {
    "url": "url",
    "address": "url",
    "page": "url",
    "status code": "status_code",
    "status_code": "status_code",
    "http status": "status_code",
    "statuscode": "status_code",
    "indexability": "indexability",
    "meta robots 1": "indexability",
    "meta_robots": "indexability",
    "meta robots": "indexability",
    "robots": "indexability",
    "canonical link element 1": "canonical",
    "canonical": "canonical",
    "canonical url": "canonical",
    "redirect url": "redirect_url",
    "redirect_url": "redirect_url",
    "redirect uri": "redirect_url",
    "title 1": "title",
    "title": "title",
    "page title": "title",
    "h1-1": "h1",
    "h1": "h1",
    "meta description 1": "meta_description",
    "meta description": "meta_description",
    "meta_description": "meta_description",
    "word count": "word_count",
    "word_count": "word_count",
    "unique inlinks": "inlinks",
    "inlinks": "inlinks",
    "internal inlinks": "inlinks",
    "schema types": "schema_types",
    "schema_types": "schema_types",
    "in sitemap": "in_sitemap",
    "in_sitemap": "in_sitemap",
}

SEVERITY = {
    "url_disappeared": "P0",
    "now_error": "P0",
    "now_noindex": "P0",
    "canonical_now_external": "P0",
    "dropped_from_sitemap": "P0",
    "now_redirect": "P1",
    "redirect_type_changed": "P1",
    "redirect_target_changed": "P1",
    "canonical_removed": "P1",
    "canonical_changed": "P1",
    "title_removed": "P1",
    "h1_removed": "P1",
    "schema_removed": "P1",
    "content_collapsed": "P1",
    "inlinks_collapsed": "P1",
    "now_orphaned": "P1",
    "title_changed": "P2",
    "h1_changed": "P2",
    "meta_description_removed": "P2",
    "content_reduced": "P2",
    "inlinks_reduced": "P2",
}


def norm_key(header: str) -> Optional[str]:
    return ALIASES.get((header or "").strip().lower())


def load(path: str) -> dict:
    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames:
                sys.exit(f"{path}: no header row")
            mapping = {h: norm_key(h) for h in reader.fieldnames}
            if "url" not in mapping.values():
                sys.exit(f"{path}: no url column found. Headers: {reader.fieldnames}")
            rows = {}
            for raw in reader:
                record = {}
                for header, key in mapping.items():
                    if key:
                        record[key] = (raw.get(header) or "").strip()
                url = record.get("url", "").strip()
                if url:
                    rows[url.rstrip("/") or "/"] = record
            return rows
    except FileNotFoundError:
        sys.exit(f"No such file: {path}")


def num(value: str) -> Optional[float]:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def truthy(value: str) -> Optional[bool]:
    if value is None or str(value).strip() == "":
        return None
    return str(value).strip().lower() in {"true", "yes", "y", "1"}


def is_error(status: Optional[float]) -> bool:
    return status is not None and status >= 400


def is_redirect(status: Optional[float]) -> bool:
    return status is not None and 300 <= status < 400


def noindexed(value: str) -> Optional[bool]:
    if not value:
        return None
    return "noindex" in value.lower() or value.strip().lower() == "non-indexable"


def compare(url: str, before: dict, after: Optional[dict]) -> list:
    found = []

    def add(kind, before_val, after_val, detail=""):
        found.append({
            "url": url,
            "regression": kind,
            "severity": SEVERITY.get(kind, "P2"),
            "before": before_val,
            "after": after_val,
            "detail": detail,
        })

    if after is None:
        add("url_disappeared", "present", "absent",
            "Missing from the post-release crawl. Confirm it was deleted rather than "
            "falling outside the crawl scope.")
        return found

    b_status, a_status = num(before.get("status_code")), num(after.get("status_code"))
    # A URL that now errors or redirects will also appear to have lost its title, canonical,
    # content, and links. Reporting all of that separately buries the one finding that matters,
    # so the status change suppresses the downstream checks.
    terminal = False
    if b_status is not None and a_status is not None:
        if not is_error(b_status) and is_error(a_status):
            add("now_error", f"{b_status:.0f}", f"{a_status:.0f}",
                "Downstream checks suppressed: the status code explains them.")
            terminal = True
        elif not is_redirect(b_status) and is_redirect(a_status):
            add("now_redirect", f"{b_status:.0f}", f"{a_status:.0f}",
                f"now points to {after.get('redirect_url') or 'unknown'}. "
                "Downstream checks suppressed.")
            terminal = True
        elif is_redirect(b_status) and is_redirect(a_status) and b_status != a_status:
            add("redirect_type_changed", f"{b_status:.0f}", f"{a_status:.0f}")

    if terminal:
        b_sitemap, a_sitemap = truthy(before.get("in_sitemap", "")), truthy(after.get("in_sitemap", ""))
        if b_sitemap is True and a_sitemap is False:
            add("dropped_from_sitemap", "in sitemap", "not in sitemap")
        return found

    b_redir, a_redir = before.get("redirect_url", ""), after.get("redirect_url", "")
    if b_redir and a_redir and b_redir != a_redir:
        add("redirect_target_changed", b_redir, a_redir)

    b_noindex, a_noindex = noindexed(before.get("indexability", "")), noindexed(after.get("indexability", ""))
    if b_noindex is False and a_noindex is True:
        add("now_noindex", before.get("indexability", ""), after.get("indexability", ""))

    b_canon, a_canon = before.get("canonical", ""), after.get("canonical", "")
    if b_canon and not a_canon:
        add("canonical_removed", b_canon, "none")
    elif b_canon and a_canon and b_canon.rstrip("/") != a_canon.rstrip("/"):
        self_before = b_canon.rstrip("/") == url
        self_after = a_canon.rstrip("/") == url
        if self_before and not self_after:
            add("canonical_now_external", b_canon, a_canon,
                "Was self-referencing, now points elsewhere.")
        else:
            add("canonical_changed", b_canon, a_canon)

    b_sitemap, a_sitemap = truthy(before.get("in_sitemap", "")), truthy(after.get("in_sitemap", ""))
    if b_sitemap is True and a_sitemap is False:
        add("dropped_from_sitemap", "in sitemap", "not in sitemap")

    for field, removed_kind, changed_kind in (
        ("title", "title_removed", "title_changed"),
        ("h1", "h1_removed", "h1_changed"),
        ("meta_description", "meta_description_removed", None),
    ):
        b_val, a_val = before.get(field, ""), after.get(field, "")
        if b_val and not a_val:
            add(removed_kind, b_val[:80], "empty")
        elif changed_kind and b_val and a_val and b_val != a_val:
            add(changed_kind, b_val[:60], a_val[:60])

    b_schema, a_schema = before.get("schema_types", ""), after.get("schema_types", "")
    if b_schema and not a_schema:
        add("schema_removed", b_schema[:60], "none")

    b_words, a_words = num(before.get("word_count")), num(after.get("word_count"))
    if b_words and a_words is not None and b_words >= 200:
        ratio = a_words / b_words
        if ratio <= 0.2:
            add("content_collapsed", f"{b_words:.0f}", f"{a_words:.0f}",
                "Verify against a rendered fetch before escalating. Crawler rendering "
                "differences look identical to real content loss.")
        elif ratio <= 0.6:
            add("content_reduced", f"{b_words:.0f}", f"{a_words:.0f}")

    b_links, a_links = num(before.get("inlinks")), num(after.get("inlinks"))
    if b_links and a_links is not None and b_links >= 3:
        if a_links == 0:
            add("now_orphaned", f"{b_links:.0f}", "0")
        elif a_links / b_links <= 0.5:
            add("inlinks_collapsed", f"{b_links:.0f}", f"{a_links:.0f}")
        elif a_links / b_links <= 0.8:
            add("inlinks_reduced", f"{b_links:.0f}", f"{a_links:.0f}")

    return found


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Diff two crawl exports and report SEO regressions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("before", help="Pre-release crawl CSV")
    parser.add_argument("after", help="Post-release crawl CSV")
    parser.add_argument("--out", default="regressions.csv", help="Output CSV path")
    parser.add_argument("--clicks", help="Optional CSV with url and clicks columns, "
                                         "used to attach traffic at risk")
    args = parser.parse_args(argv)

    before, after = load(args.before), load(args.after)

    clicks = {}
    if args.clicks:
        with open(args.clicks, newline="", encoding="utf-8-sig") as handle:
            for raw in csv.DictReader(handle):
                lower = {(k or "").strip().lower(): v for k, v in raw.items()}
                url = (lower.get("url") or lower.get("page") or "").strip().rstrip("/")
                value = num(lower.get("clicks"))
                if url and value is not None:
                    clicks[url or "/"] = value

    findings = []
    for url, row in before.items():
        findings.extend(compare(url, row, after.get(url)))

    new_urls = [u for u in after if u not in before]

    for finding in findings:
        finding["clicks_at_risk"] = clicks.get(finding["url"], "")

    order = {"P0": 0, "P1": 1, "P2": 2}
    findings.sort(key=lambda f: (
        order.get(f["severity"], 3),
        -(f["clicks_at_risk"] if isinstance(f["clicks_at_risk"], float) else 0),
    ))

    fields = ["severity", "url", "regression", "before", "after", "clicks_at_risk", "detail"]
    with open(args.out, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(findings)

    by_severity = Counter(f["severity"] for f in findings)
    by_kind = Counter(f["regression"] for f in findings)

    print(f"Compared {len(before)} pre-release URLs against {len(after)} post-release URLs")
    print(f"Found {len(findings)} regressions across {len({f['url'] for f in findings})} URLs")
    for level in ("P0", "P1", "P2"):
        if by_severity[level]:
            print(f"  {level}: {by_severity[level]}")
    if by_kind:
        print("\nMost common:")
        for kind, count in by_kind.most_common(6):
            print(f"  {kind:<26} {count}")
    if new_urls:
        print(f"\n{len(new_urls)} URLs appear only in the post-release crawl. "
              "Check whether that was intended.")
    if len(before) != len(after):
        print("\nCrawl sizes differ. Confirm both crawls used the same scope and settings "
              "before treating missing URLs as deletions.")
    print(f"\nWritten to {args.out}. Join with Search Console clicks for real severity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
