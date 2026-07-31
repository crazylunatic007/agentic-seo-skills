# Monitor SEO Regressions After a Release or Migration

Use the SEO Release Regression Guard Skill to compare the pre-release baseline from [date/build] with the post-release crawl from [date/build] for [domain or migration scope].

The release involved [migration, redesign, CMS change, deployment, template change, or other release].

The approved-change list is [attached / at this location]. This is required. Without it every deliberate change reads as a regression and the report is unusable. If it is missing, say so and state clearly that everything in the output is unclassified rather than confirmed unplanned.

Before comparing results, confirm that both crawls use comparable:
- URL scope
- Crawl settings
- User agent
- Rendering mode
- Authentication
- Parameter handling
- Inclusion and exclusion rules

If the crawl configurations are not comparable, stop and report the differences. Do not produce a partial comparison.

Use:
- Pre-release crawl
- Post-release crawl
- Semrush Site Audit where available
- XML sitemaps
- Google Search Console
- Historical traffic and conversion data
- GitHub or deployment information where connected
- The approved-change list for this release

Run `scripts/crawl_diff.py` on the two crawl exports to produce the raw diff, then apply judgment to the results. Save the full output as CSV. In chat, show the P0 items in full, summarize P1 by root cause group, and give counts only for P2.

Compare:
- Status codes
- Redirects and redirect chains
- Canonical tags
- Robots directives
- XML sitemap membership
- Internal links
- Titles and headings
- Structured data
- Rendered content
- Indexability

Check two things explicitly regardless of what the diff returns: whether a staging robots.txt shipped to production, and whether a noindex intended for staging is live on any template.

Complete these steps:
1. Identify differences between the baseline and post-release state.
2. Classify each difference as expected, expected but implemented incorrectly, or unplanned, using the approved-change list.
3. Group repeated regressions by likely template or root cause.
4. Join affected URLs with historical traffic, conversions, rankings, and backlinks.
5. Assign P0, P1, or P2 severity using the definitions in the Skill. Severity is the combination of what broke and what it broke on, never the issue type alone.
6. Show before-and-after evidence.
7. Identify the likely owner.
8. Write acceptance criteria and a reproducible verification step with an expected result for each item.
9. Verify any content-loss findings against a rendered fetch before escalating them. Crawler rendering differences look identical to real content loss.

Open with a one-line verdict: whether anything needs immediate attention, and if so what.

Return:

| Severity | Regression | URLs Affected | High-Value URLs | Traffic or Revenue at Risk | Before | After | Likely Root Cause | Expected? | Owner | Acceptance Criteria | Verification Step |
|---|---|---:|---:|---:|---|---|---|---|---|---|---|

Traffic at risk is historical clicks for the affected URLs over a comparable prior period. Label it as an exposure figure, not a forecast.

Follow the table with:
- Immediate release risks
- Template-level patterns
- Expected changes that were excluded
- Missing or incomparable data
- Recommended order of investigation

Save this output to [file path or Drive location] as `regression-baseline-[date]`. The re-verification run needs it.

Do not modify code, configuration, robots directives, canonicals, redirects, or sitemaps. Do not initiate a rollback. If a P0 is found, escalate with evidence rather than fixing it.

---

## Re-verification prompt (run after fixes deploy)

Use the SEO Release Regression Guard Skill. Load the original regression report from [file path or Drive location] and the new post-fix crawl from [date/build].

Do not accept "fixed" as an input. Re-run only the checks relevant to the items in the original report, and evaluate each one against the acceptance criteria recorded in that report.

Report each item as fixed, partially fixed, still failing, or unable to verify, with the evidence for each verdict. List any new regressions the fix introduced.
