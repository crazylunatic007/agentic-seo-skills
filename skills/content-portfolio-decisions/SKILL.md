---
name: content-portfolio-decisions
description: Classifies every URL in a content library as keep, update, consolidate, redirect, remove, or investigate by building a unified inventory from performance, ranking, link, freshness, and business signals, then applying explicit decision rules and escalating conflicting cases instead of forcing an answer. Use this whenever the user mentions a content audit, content pruning, deleting or consolidating old posts, a bloated blog, deciding what to refresh, or asks which pages are worth keeping.
---

# Content Portfolio Decisions

Turn a content library into a decision list, with the reasoning attached and the genuinely
ambiguous cases separated out rather than resolved by a threshold.

Content audits fail in a predictable way. Someone builds a scoring formula, sorts by score, and
deletes the bottom quartile. Six months later the team discovers they redirected the page that
held forty referring domains, removed the page the support team linked from every ticket, and kept
nine near-duplicate posts because each one cleared the traffic floor. The rules in this skill are
built to catch those cases, and the escalation path exists because some pages should never be
decided by a formula.

## Before you start

Establish, and write these down in the output so the decisions can be re-read later:

1. **Scope** — the full site, a folder, or a defined URL list.
2. **Evaluation window** — default is the last 12 months versus the prior 12 months.
3. **Business rules** — what makes a page strategically important regardless of traffic. Ask
   directly: legal or compliance pages, support documentation, sales enablement, category-defining
   pieces, pages linked from the product. Without this the audit will recommend deleting them.
4. **Appetite** — is the user pruning aggressively, or looking for an update queue? The same data
   supports both, and the answer changes the thresholds.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Full URL inventory | CMS export, sitemap, Firecrawl `firecrawl_map` | Semrush `siteaudit_research` crawl |
| Clicks, impressions, position, both windows | GSC MCP `analytics_query`, `analytics_compare_periods` | GSC UI export |
| Indexability | GSC MCP `inspection_batch` | Crawl data |
| Ranking keyword coverage | Semrush `url_research` | Rank tracker |
| Referring domains per URL | Semrush `backlink_research` | Ahrefs or Majestic |
| Engagement and conversions | GA4 via Supermetrics `data_query` | GA4 export |
| Publish and update dates | CMS export | Firecrawl `firecrawl_scrape` metadata |
| Topic overlap | GSC MCP `seo_cannibalization` plus content similarity | Manual review of title clusters |
| AI citations or brand visibility | Whatever export the user has | Omit, and say it was omitted |

Conversions are the signal most often missing and most often decisive. Ask for it explicitly rather
than proceeding without it and discovering later that the audit ignored revenue.

## Workflow

- [ ] 1. Build one unified inventory keyed on URL. Reconcile trailing slashes, protocols, and
      parameters before joining, or the join will silently drop rows.
- [ ] 2. Record which signals are missing for which URLs. Missing data is not zero.
- [ ] 3. Evaluate each URL against the signals listed in `references/decision-rules.md`.
- [ ] 4. Apply the decision rules in order. The rules are ordered so that protective rules fire first.
- [ ] 5. Flag conflicting signals rather than letting the higher-weighted one win silently.
- [ ] 6. Escalate anything matching the mandatory review list to `Investigate`.
- [ ] 7. For consolidation and redirect recommendations, identify and validate the destination URL.
- [ ] 8. Produce the decision table plus a summary of what was escalated and why.

For inventories above a few hundred URLs, use `scripts/portfolio_score.py` to apply the rules
deterministically rather than reasoning row by row. Reasoning over 2,000 rows in context produces
inconsistent decisions and burns the run. Use judgement on the escalated set, which is where
judgement is actually needed.

```bash
python scripts/portfolio_score.py inventory.csv --out decisions.csv --appetite balanced
```

Run `python scripts/portfolio_score.py --help` for the expected columns and thresholds.

## Decisions

| Decision | Meaning |
|---|---|
| Keep | Performing or strategically necessary. No action. |
| Update | Has a foundation worth building on: rankings, links, or relevance, with declining or unrealised performance. |
| Consolidate | Overlaps another page. Merge the useful content into the stronger URL. |
| Redirect | No standalone value, but has links or history worth preserving, and a genuine equivalent exists. |
| Remove | No value, no links, no strategic role, and no sensible redirect target. |
| Investigate | Signals conflict, data is missing, or the page matches the mandatory review list. |

`Investigate` is a real answer, not a failure. A audit that escalates 15% of the library and gets
the other 85% right is far more useful than one that decides everything and is wrong about the
pages that mattered.

## Guardrails

Never automatically redirect, delete, noindex, or unpublish a page. This workflow produces
recommendations only.

Route to `Investigate` for mandatory human review when a page has any of:

- Valuable referring domains
- Historical conversions, even if current traffic is low
- Significant citations, including AI citations and academic or press references
- Legal, compliance, or regulatory importance
- Strategic relevance the performance data does not capture
- No clear replacement destination for a proposed redirect

These override every other rule. A page with forty referring domains and no traffic is not a
removal candidate; it is a redirect or a rewrite candidate, and a person decides which.

## Output

| URL | Recommended Decision | Supporting Signals | Conflicting Signals | Destination URL | Confidence | Reviewer | Notes |
|---|---|---|---|---|---|---|---|

Then a summary containing: counts per decision, the escalated set with the reason for each, which
signals were missing for how many URLs, and the estimated traffic and conversion volume affected
by the proposed removals and redirects. That last figure is what makes the recommendation
approvable or not.

## Human checkpoint

Every redirect, consolidation, removal, and noindex decision requires explicit human approval, one
batch at a time. Approving the update queue is not approval of the removal queue.

Recommend implementing in stages, with the removals last and monitored, so a mistaken call is
recoverable.

## Known limitations

- Performance data does not capture strategic, legal, support, or lifecycle value. The inventory
  needs business context, and without it the audit is systematically biased toward deletion.
- GSC retains 16 months. Pages that declined earlier look uniformly dead.
- Conversion attribution to a single URL is unreliable for assisted and multi-touch paths, so
  content that influences without converting looks worthless.
- Topic overlap detected by query similarity misses pages that overlap in substance but rank for
  different terms.
- Removing content rarely improves the rest of the site by itself. Treat the case for pruning as a
  case about maintenance cost and user experience rather than an expected ranking lift.
