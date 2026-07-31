#!/usr/bin/env python3
"""Apply content portfolio decision rules to a URL inventory.

Reads a CSV inventory and writes a decision per URL, following the ordered rules in
references/decision-rules.md. Protective rules fire first, missing data escalates rather
than defaulting to zero, and nothing here deletes or changes anything.

Expected columns (case-insensitive, extras ignored, missing columns treated as unknown):

  url                  required
  clicks               clicks in the current window
  clicks_prev          clicks in the prior window
  impressions          impressions in the current window
  avg_position         average position in the current window
  ranking_keywords     count of ranking keywords
  referring_domains    count of referring domains
  conversions          conversions or assisted conversions
  last_updated         ISO date of last meaningful update
  indexable            true/false/yes/no/1/0
  strategic            true/false flag from the business rules
  overlap_url          a stronger URL on the same domain serving the same intent
  citations            count of AI or external citations

Blank cells mean unknown, which is different from 0. Write an explicit 0 when the value is
genuinely zero, otherwise the row escalates to Investigate on purpose.

Usage:
  python portfolio_score.py inventory.csv --out decisions.csv
  python portfolio_score.py inventory.csv --appetite aggressive --clicks-floor 50
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

APPETITES = {
    # appetite: (clicks_floor, decline_pct, stale_days)
    "conservative": (25, 0.50, 1095),
    "balanced": (100, 0.30, 730),
    "aggressive": (250, 0.20, 545),
}

DECISIONS = ("Keep", "Update", "Consolidate", "Redirect", "Remove", "Investigate")


@dataclass
class Row:
    url: str
    raw: dict
    clicks: Optional[float] = None
    clicks_prev: Optional[float] = None
    impressions: Optional[float] = None
    avg_position: Optional[float] = None
    ranking_keywords: Optional[float] = None
    referring_domains: Optional[float] = None
    conversions: Optional[float] = None
    citations: Optional[float] = None
    last_updated: Optional[date] = None
    indexable: Optional[bool] = None
    strategic: Optional[bool] = None
    overlap_url: str = ""
    supporting: list = field(default_factory=list)
    conflicting: list = field(default_factory=list)


def parse_number(value: str) -> Optional[float]:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if text == "" or text.lower() in {"na", "n/a", "none", "null", "unknown", "-"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_bool(value: str) -> Optional[bool]:
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in {"true", "yes", "y", "1"}:
        return True
    if text in {"false", "no", "n", "0"}:
        return False
    return None


def parse_date(value: str) -> Optional[date]:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(text[:10], fmt).date()
        except ValueError:
            continue
    return None


def normalise(raw: dict) -> Row:
    lower = {(k or "").strip().lower(): v for k, v in raw.items()}
    return Row(
        url=(lower.get("url") or "").strip(),
        raw=raw,
        clicks=parse_number(lower.get("clicks")),
        clicks_prev=parse_number(lower.get("clicks_prev")),
        impressions=parse_number(lower.get("impressions")),
        avg_position=parse_number(lower.get("avg_position")),
        ranking_keywords=parse_number(lower.get("ranking_keywords")),
        referring_domains=parse_number(lower.get("referring_domains")),
        conversions=parse_number(lower.get("conversions")),
        citations=parse_number(lower.get("citations")),
        last_updated=parse_date(lower.get("last_updated")),
        indexable=parse_bool(lower.get("indexable")),
        strategic=parse_bool(lower.get("strategic")),
        overlap_url=(lower.get("overlap_url") or "").strip(),
    )


def decline_ratio(row: Row) -> Optional[float]:
    if row.clicks is None or row.clicks_prev is None or row.clicks_prev <= 0:
        return None
    return (row.clicks_prev - row.clicks) / row.clicks_prev


def days_stale(row: Row, today: date) -> Optional[int]:
    if row.last_updated is None:
        return None
    return (today - row.last_updated).days


def decide(row: Row, clicks_floor: float, decline_pct: float, stale_days: int,
           today: date) -> tuple:
    """Return (decision, confidence, destination, note). Rules are ordered."""

    zero_ish = lambda v: v is not None and v <= 0
    has = lambda v, n: v is not None and v >= n

    # Data-quality check that runs before everything else.
    if row.indexable is False and has(row.clicks, 1):
        row.conflicting.append("noindexed but receiving clicks")
        return ("Investigate", "Low", "",
                "Indexability and performance data disagree. Reconcile before deciding.")

    # R1 protected
    protections = []
    if row.strategic:
        protections.append("strategic flag set")
    if has(row.referring_domains, 5):
        protections.append(f"{int(row.referring_domains)} referring domains")
    if has(row.conversions, 1):
        protections.append(f"{row.conversions:g} conversions")
    if has(row.citations, 1):
        protections.append(f"{row.citations:g} citations")
    if protections and not has(row.clicks, clicks_floor):
        row.supporting.extend(protections)
        if has(row.clicks, 1) or has(row.impressions, 100):
            return ("Update", "Medium", "",
                    "Protected by " + "; ".join(protections) + ". Worth rebuilding, not removing.")
        return ("Investigate", "Medium", "",
                "Protected by " + "; ".join(protections) + ". Human decides between redirect and rewrite.")

    # R2 missing critical data on an otherwise weak page
    weak = not has(row.clicks, clicks_floor)
    missing = [name for name, value in (
        ("conversions", row.conversions),
        ("referring_domains", row.referring_domains),
    ) if value is None]
    if weak and missing:
        return ("Investigate", "Low", "",
                "Missing " + " and ".join(missing) + ". Missing is not zero.")

    # R3 performing
    if has(row.clicks, clicks_floor):
        ratio = decline_ratio(row)
        if ratio is not None and ratio >= decline_pct:
            row.supporting.append(f"still earns {row.clicks:g} clicks")
            row.conflicting.append(f"down {ratio:.0%} year over year")
            return ("Update", "Medium", "",
                    "Meaningful traffic but declining. Diagnose the cause before scoping the rewrite.")
        row.supporting.append(f"{row.clicks:g} clicks, stable or growing")
        stale = days_stale(row, today)
        if stale is not None and stale > stale_days:
            row.conflicting.append(f"not updated in {stale} days but performing")
        return ("Keep", "High", "", "Performing. No action.")

    # R4 declining with a foundation
    ratio = decline_ratio(row)
    foundation = has(row.ranking_keywords, 5) or has(row.referring_domains, 3) or has(row.impressions, 1000)
    if ratio is not None and ratio >= decline_pct and foundation:
        row.supporting.append("retains rankings, links, or impressions")
        row.conflicting.append(f"down {ratio:.0%} year over year")
        return ("Update", "Medium", "", "Declining but recoverable.")

    # R5 overlapping (checked before potential: overlap is often why the page underperforms)
    if row.overlap_url:
        row.supporting.append(f"overlaps {row.overlap_url}")
        return ("Consolidate", "Medium", row.overlap_url,
                "Merge the useful content into the stronger URL, then redirect.")

    # R6 unrealised potential
    if has(row.impressions, 1000) and row.avg_position is not None and 8 <= row.avg_position <= 20:
        row.supporting.append(
            f"{row.impressions:g} impressions at position {row.avg_position:.1f}")
        return ("Update", "Medium", "", "Ranking just off the click range.")

    # R7 dead but inherited value
    if has(row.referring_domains, 3) and zero_ish(row.clicks):
        row.supporting.append(f"{int(row.referring_domains)} referring domains, no traffic")
        return ("Investigate", "Medium", "",
                "Has inherited link value but no destination identified. A person picks the target.")

    # R8 genuinely dead
    stale = days_stale(row, today)
    dead = (
        zero_ish(row.clicks)
        and (row.impressions is None or row.impressions < 100)
        and (row.ranking_keywords is None or row.ranking_keywords < 1)
        and zero_ish(row.referring_domains)
        and zero_ish(row.conversions)
        and not row.strategic
    )
    if dead and (stale is None or stale > stale_days):
        row.supporting.append("no traffic, rankings, links, or conversions")
        return ("Remove", "Medium", "",
                "No value and no redirect target identified. Confirm with a human before acting.")

    # R9 fallthrough
    return ("Investigate", "Low", "", "Signals are ambiguous. Needs a look.")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Apply content portfolio decision rules to a URL inventory.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("inventory", help="Path to the inventory CSV")
    parser.add_argument("--out", default="decisions.csv", help="Output CSV path")
    parser.add_argument("--appetite", choices=sorted(APPETITES), default="balanced",
                        help="Preset thresholds. Default: balanced")
    parser.add_argument("--clicks-floor", type=float, default=None,
                        help="Override the meaningful-traffic floor")
    parser.add_argument("--decline-pct", type=float, default=None,
                        help="Override the decline threshold, as a decimal e.g. 0.3")
    parser.add_argument("--stale-days", type=int, default=None,
                        help="Override the staleness threshold in days")
    args = parser.parse_args(argv)

    clicks_floor, decline_pct, stale_days = APPETITES[args.appetite]
    if args.clicks_floor is not None:
        clicks_floor = args.clicks_floor
    if args.decline_pct is not None:
        decline_pct = args.decline_pct
    if args.stale_days is not None:
        stale_days = args.stale_days

    today = date.today()

    try:
        with open(args.inventory, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                print("Inventory has no header row.", file=sys.stderr)
                return 1
            headers = {(h or "").strip().lower() for h in reader.fieldnames}
            if "url" not in headers:
                print(f"Inventory needs a 'url' column. Found: {sorted(headers)}",
                      file=sys.stderr)
                return 1
            rows = [normalise(r) for r in reader]
    except FileNotFoundError:
        print(f"No such file: {args.inventory}", file=sys.stderr)
        return 1

    rows = [r for r in rows if r.url]
    if not rows:
        print("No rows with a url value.", file=sys.stderr)
        return 1

    results = []
    counts = {d: 0 for d in DECISIONS}
    for row in rows:
        decision, confidence, destination, note = decide(
            row, clicks_floor, decline_pct, stale_days, today)
        counts[decision] += 1
        results.append({
            "url": row.url,
            "decision": decision,
            "supporting_signals": "; ".join(row.supporting) or "none recorded",
            "conflicting_signals": "; ".join(row.conflicting) or "none",
            "destination_url": destination,
            "confidence": confidence,
            "reviewer": "",
            "note": note,
        })

    with open(args.out, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print(f"Scored {len(results)} URLs using the '{args.appetite}' preset "
          f"(clicks floor {clicks_floor:g}, decline {decline_pct:.0%}, stale {stale_days}d)")
    for decision in DECISIONS:
        print(f"  {decision:<13} {counts[decision]}")
    print(f"Written to {args.out}")
    print("\nNothing has been changed. Every redirect, consolidation, and removal "
          "still needs human approval.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
