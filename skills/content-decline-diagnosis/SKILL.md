---
name: content-decline-diagnosis
description: Diagnoses organic traffic decline on specific URLs by joining Search Console performance with ranking, backlink, SERP, and cannibalization data, then classifying the most likely cause and returning a prioritized update queue. Use this whenever the user asks why traffic or rankings dropped, mentions declining pages, a traffic loss, a content refresh or update queue, or wants to know which pages to fix next, even if they only describe the symptom and never use the word diagnosis.
---

# Content Decline Diagnosis

Find the pages losing meaningful organic traffic, work out the most likely cause of each decline,
and hand back a queue a person can act on.

The point of this skill is not to report that traffic fell. Anyone can see that in a chart. The
point is to separate the handful of causes that behave completely differently: a page that lost
rankings needs a rewrite, a page that lost demand needs nothing at all, and a page that lost its
canonical needs a five minute fix. Recommending "refresh the content" for all three is the
default failure mode this skill exists to prevent.

## Before you start

Confirm three things with the user, and propose defaults rather than asking open questions:

1. **Scope** — a domain, a folder, or a specific URL list.
2. **Comparison windows** — default is last 90 days vs the same 90 days a year earlier.
   Year over year absorbs seasonality; period over period catches recent breakage. If the user
   suspects a specific event, anchor the windows either side of it instead.
3. **Materiality floor** — default is decline of at least 30% AND at least 100 clicks lost.

Do not skip the absolute floor. Percentage-only filters fill the report with pages that went from
four clicks to one.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Actual clicks, impressions, CTR, position | GSC MCP `analytics_compare`, `analytics_query` | GSC UI export |
| Indexation and canonical state | GSC MCP `inspection_inspect` | Live crawl plus site: check |
| Ranking keywords per URL | Semrush `organic_research` / `resource_organic` | Any rank tracking export |
| Competitor movement on the same queries | Semrush `organic_research` | SERP capture |
| Keyword demand trend | Semrush `keyword_research` | Google Trends |
| Referring domains per URL | Semrush `backlinks_research` | Ahrefs or Majestic export |
| Current SERP shape and AI Overview presence | SerpAPI | Manual SERP check |
| Live page content and internal links | Firecrawl `firecrawl_scrape` | `web_fetch` |

Optional but useful: GA4 engagement and conversions, CMS publish and update dates, AI citation data.

Cap Semrush reports at `display_limit: 20` unless the user asks for more.

## Workflow

Post this checklist in the response, with items ticked off as they complete, immediately before
the output table — every run, no matter how confident an early finding feels. An output table
with no posted, ticked checklist above it is an incomplete run: go back and post one before
treating the diagnosis as done.

Red flags — stop and go back if you catch yourself thinking:
- "The top few URLs already have a strong answer, so this is basically done" — the queue isn't
  done until every surviving URL past the materiality floor has been through steps 4-8, not just
  the ones you looked at first.
- "I'll mark this one `Insufficient evidence` instead of re-running the check" — insufficient
  evidence is a conclusion reached *after* running steps 5-8 and staying ambiguous, not a
  substitute for running them. If the tool was never called, the evidence isn't insufficient —
  it's absent.

- [ ] 1. Pull period-over-period performance for the scope and rank URLs by absolute clicks lost.
- [ ] 2. Apply the materiality floor. Drop everything below it.
- [ ] 3. For each surviving URL, pull clicks, impressions, CTR, and average position for both windows.
- [ ] 4. Check indexation state first. A deindexed or canonicalised page ends the investigation.
- [ ] 5. Compare ranking keyword count and demand trend for the URL's top queries.
- [ ] 6. Check referring domains and internal links for losses.
- [ ] 7. Check the live SERP for new competitors and new SERP features.
- [ ] 8. Check whether another URL on the same domain now serves the same queries.
- [ ] 9. Classify using `references/decline-taxonomy.md`.
- [ ] 10. Assign one primary action and one fallback action per URL.

Step 4 comes early on purpose. Technical causes are cheap to confirm, produce the highest
confidence answers, and make the rest of the investigation unnecessary — but only for that one
URL. Every other surviving URL still needs steps 5-8. Confirming a redirect or noindex on your
first URL is not evidence about the second, third, or fortieth.

Work in batches. Inspecting 50 URLs one at a time wastes the run; use `inspection_inspect` with a list of URLs and
batched analytics queries, then drill into the outliers.

## Classification

Read `references/decline-taxonomy.md` for the diagnostic signature of each cause, the checks that
confirm it, and the checks that rule it out. The categories are:

Search demand declined · Rankings declined · CTR declined while rankings held · Competitor
replaced the page · Cannibalization · Technical or indexation issue · Lost links or internal
authority · Content is outdated · SERP or AI answer reduced click opportunity · Insufficient
evidence

Two rules matter more than the taxonomy itself:

- **Prefer `Insufficient evidence` over a guess — after running the checks, not instead of
  running them.** Reach this label only once steps 5-8 have actually been attempted for that URL
  and the result is still ambiguous. A row that says which check would resolve the ambiguity is
  more useful than a confident label that sends a writer down the wrong path — but "insufficient
  evidence" because a tool was never called is a skipped step wearing an honest label.
- **Check for multiple causes.** Declines often stack. Report the dominant cause, and note the
  secondary one in the evidence column rather than forcing a single label.

## Output

Produce this table first, then a short summary. Save as Markdown or CSV rather than pasting
50 rows into chat.

| Priority | URL | Clicks Lost | Click Decline | Impression Change | Position Change | Likely Cause | Supporting Evidence | Primary Action | Fallback Action | Confidence |
|---|---|---:|---:|---:|---:|---|---|---|---|---|

Priority is absolute clicks lost weighted by how fixable the cause is. A page that lost 400
clicks to a broken canonical outranks a page that lost 600 clicks to a demand collapse, because
one is recoverable and the other is not.

Evidence names the metric and window, for example "position 4.1 to 11.8, YoY, 22 of 31 ranking
keywords lost". If a check could not be run, say so in the row.

Confidence uses the scale in `../../docs/conventions.md`: High needs two independent sources plus
an observed mechanism.

## Human checkpoint

A person decides whether to update, consolidate, redirect, or leave each page alone. Do not
execute any of those. Do not edit CMS content, change redirects, or alter canonicals as part of
this workflow.

## Known limitations

- Decline causes are probabilistic. Only technical causes support a direct mechanism claim.
- GSC aggregates and drops low-volume queries, so query-level analysis on small pages is unreliable.
- Third-party ranking data is sampled and lags. Use it for direction, not for exact positions.
- A decline that started before the earliest available data cannot be attributed to an event.
- Position averages hide distribution. A page can hold average position 8 while losing every
  first-page ranking on its highest-volume terms.
