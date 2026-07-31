---
name: seo-release-regression-guard
description: Compares a site before and after a deployment, migration, redesign, or CMS change to catch SEO regressions early, diffing status codes, redirects, canonicals, robots directives, sitemap membership, internal links, titles, headings, structured data, and rendered content, then ranking each regression by the historical value of the URLs affected and re-verifying after fixes ship. Use this whenever the user mentions a release, deploy, migration, replatform, redesign, staging comparison, or asks whether a change broke anything in search.
---

# SEO Release Regression Guard

Catch what a deployment broke before it turns into a traffic loss, and prove it was fixed
afterwards.

The thing that makes this workflow useful is not the diff. It is the loop: identify the regression,
route it to an owner with evidence and a verification step, then re-run the same checks after the
fix deploys and confirm the acceptance criteria were actually met. Most regression reports stop at
the first step, which is why the same issues reappear two releases later.

## Before you start

**A baseline must exist before the release.** This is the failure mode of the whole workflow. If
the deployment already happened and no pre-release crawl was captured, say so immediately and
switch to the recovery approach below rather than pretending a comparison is possible.

Establish:

1. **Scope** — the URL set to compare. It must be identical on both sides. Comparing 5,000 URLs
   before and 4,200 after does not tell you 800 pages disappeared; it may just mean the crawl
   stopped early.
2. **Crawl settings** — same depth, same rendering mode, same user agent, same robots handling.
   Differences here produce false regressions that waste a team's day.
3. **What was intended to change.** Without this, every deliberate change gets reported as a
   regression and the report loses credibility on first read.

**Recovery when no baseline exists** — reconstruct a partial one from the XML sitemap, GSC
performance and indexation data, and archived copies of key templates. Say clearly that it is a
partial reconstruction and that absence of evidence is not evidence of absence.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Pre-release crawl | Firecrawl `firecrawl_crawl`, Screaming Frog, or Semrush Site Audit | Reconstruct from sitemap plus GSC |
| Post-release crawl | Same tool, same settings | Same |
| Ongoing issue detection | Semrush `siteaudit_research` on an existing project | Repeat crawl |
| Historical value of affected URLs | GSC MCP `analytics_query`, `analytics_top_pages` | GA4 landing page export |
| Indexation state | GSC MCP `inspection_batch` | Live checks |
| Sitemap membership | GSC MCP `sitemaps_list`, `sitemaps_get` | Fetch the sitemap directly |
| Structured data validity | GSC MCP `schema_validate` | Any schema validator |
| Core Web Vitals | GSC MCP `pagespeed_core_web_vitals` | PageSpeed Insights |
| What shipped | GitHub or deployment connector | Ask the team for the change list |
| Notifying owners | Slack, Jira, or Linear connector | Return the report for a human to send |

## Workflow

- [ ] 1. Capture and store the pre-release baseline. Record the crawl settings alongside it.
- [ ] 2. After deployment, crawl the same scope with the same settings.
- [ ] 3. Diff every dimension in `references/diff-checks.md`.
- [ ] 4. Join affected URLs with their historical clicks and conversions.
- [ ] 5. Separate expected changes from unplanned ones using the stated change list.
- [ ] 6. Group into P0, P1, and P2 using the severity rules below.
- [ ] 7. Route each group to an owner with evidence and a verification step.
- [ ] 8. After the fix deploys, re-run the affected checks and confirm the acceptance criteria.

Use `scripts/crawl_diff.py` for step 3 on any crawl above a few hundred URLs. Diffing thousands of
rows by reasoning is slow and inconsistent, and this is exactly the kind of deterministic
comparison a script should own.

```bash
python scripts/crawl_diff.py before.csv after.csv --out regressions.csv
```

Step 8 is what makes this agentic rather than a report. When the team says a fix has deployed,
re-run the specific checks for those URLs, compare against the acceptance criteria, and state
plainly whether it passed. Do not accept "fixed" as an input.

## Severity

| Level | Criteria | Response |
|---|---|---|
| P0 | Indexation or availability broken on URLs with meaningful traffic: 5xx, unexpected 404, noindex added, robots disallow added, canonical pointing away, sitemap emptied | Immediate. Consider rollback |
| P1 | Ranking-relevant regressions on valuable URLs: redirect chains, lost internal links, title and H1 loss, structured data broken, rendered content missing | This sprint |
| P2 | Broad but low-value regressions, or cosmetic changes with unclear impact | Backlog |

Severity is the combination of what broke and what it broke on. The same missing canonical is P0 on
a page earning 8,000 clicks a month and P2 on a page earning none. Never rank by issue type alone.

Two P0 patterns deserve their own callout because they are common and easy to miss: a staging
`robots.txt` shipping to production, and a `noindex` left on a template that was only supposed to
be on staging. Check both explicitly on every release regardless of what the diff returns.

## Output

| Severity | Regression | URLs Affected | High-Value URLs | Traffic at Risk | Before | After | Expected? | Owner | Verification Step |
|---|---|---:|---:|---:|---|---|---|---|---|

Lead with a one-line verdict: whether anything needs immediate attention, and if so what. A
regression report that buries a P0 in row 40 has failed at its only job.

Traffic at risk is the historical clicks of the affected URLs over a comparable prior period. It is
an exposure figure, not a forecast, and should be labelled as such.

## Human checkpoint

Require explicit approval before code changes, production configuration changes, applying any fix,
or rolling back. Reporting, diffing, and re-verification run unattended; changes do not.

If a P0 is detected, the correct action is to escalate immediately with evidence, not to fix it.

## Known limitations

- The comparison is only reliable when both crawls cover the same scope with comparable settings.
  State the crawl settings in the output so a reader can judge this.
- Rendering differences between a crawler and a real browser produce false positives on
  JavaScript-heavy sites. Verify content regressions against a rendered fetch before escalating.
- A clean diff does not mean a clean release. Server-side changes, personalisation, geo variation,
  and slow-building performance regressions are invisible to a URL-level comparison.
- Ranking and traffic effects lag deployment by days to weeks. A regression caught here is a
  prediction of harm, not a measurement of it.
- Sampled or capped crawls make absence ambiguous. A URL missing from the post-release crawl may be
  gone, or may simply be past the crawl limit.
