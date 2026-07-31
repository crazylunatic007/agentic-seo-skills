# Turn a Site Audit Into a Technical SEO Sprint

Use the Technical SEO Sprint Triage Skill to analyze the latest completed Site Audit for [domain/project].

Prerequisite: Confirm that the correct Site Audit project exists, its most recent crawl completed on [date], and it covers [crawl scope]. If the project or crawl is unavailable, stop and report the missing prerequisite. If the crawl is more than [30] days old, say so before proceeding, because triaging a stale crawl produces tickets for issues that are already fixed.

Our sprint capacity for this work is [X developer days]. Size the final list to that.

Use the impact, effort, confidence, and fix-type definitions in the Skill's reference file at `references/root-cause-grouping.md`, and the acceptance criteria patterns in `references/acceptance-criteria.md`. Do not invent your own scales.

Use:
- Semrush Site Audit for technical issues and affected URLs
- Google Search Console for organic performance and indexation context
- Semrush organic data for keyword and ranking value
- GA4 or conversion data where available
- [GitHub/Jira/Linear] only for additional context or draft output

Analyze [entire project/specific subfolder/templates]. Exclude [staging URLs, parameter URLs, intentionally blocked pages, or other exclusions].

For each audit issue:
1. Confirm the number and type of affected URLs.
2. Group duplicate symptoms that appear to share one root cause. Test whether affected URLs share a path pattern, a template, a generation source, a rendering path, or a single upstream directive before treating them as separate issues.
3. Identify whether the likely fix is template-level, page-level, configuration-level, infrastructure-level, or investigative.
4. Join affected URLs with traffic, rankings, conversions, backlinks, and business importance.
5. Distinguish probable causes from symptoms reported by the crawler.
6. Estimate impact, effort, and confidence using the reference definitions.
7. Verify the top [5] items against live pages before they reach the table. Crawlers routinely flag JavaScript-rendered content as missing and report redirect chains that resolve fine for users.
8. Prioritize issues that affect valuable pages or create crawling, rendering, indexation, or migration risk.
9. Write measurable acceptance criteria for each proposed fix.

Return the top [10-15] items for the next sprint:

| Rank | Issue | URLs Affected | High-Value URLs | Traffic at Risk | Likely Root Cause | Fix Type | Impact | Effort | Confidence | Recommended Fix | Acceptance Criteria |
|---|---|---:|---:|---:|---|---|---|---|---|---|---|

Acceptance criteria must be checkable by someone who is not an SEO, and must name the scope, the expected state, and the verification method. "Canonical tags fixed" is not acceptance criteria.

After the table, include:
- Issues that require further investigation
- Issues excluded as low-value or intentional
- Missing data or incomplete crawl coverage
- Dependencies between recommended fixes, and the order they should be done in

Do not modify code, robots.txt, canonicals, redirects, sitemaps, or production configuration. Do not create external tickets or open pull requests without approval. Draft specifications or tickets only when explicitly requested.
