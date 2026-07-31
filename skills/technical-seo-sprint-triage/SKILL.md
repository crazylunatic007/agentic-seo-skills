---
name: technical-seo-sprint-triage
description: Turns a large site audit issue list into a ranked sprint backlog by grouping issues to their root cause, joining affected URLs with traffic and ranking value, and writing acceptance criteria for each fix. Use this whenever the user has a Semrush Site Audit, Screaming Frog crawl, or any technical SEO issue export and wants to know what to fix first, mentions a technical backlog, crawl errors, a site health score, or asks a developer team to pick up SEO work.
---

# Technical SEO Sprint Triage

Site audits report thousands of issues across a handful of actual causes. A single missing
template partial can produce 4,000 rows. The job here is to collapse symptoms into causes, value
them against traffic, and hand a development team ten to fifteen items with clear acceptance
criteria, rather than a spreadsheet nobody opens.

## Before you start

**A crawl must already exist.** Semrush MCP can read Site Audit data but cannot create a project
or trigger a crawl. If the user has no Site Audit project, say so and offer the alternatives:
create the project in Semrush first, or supply a Screaming Frog or Sitebulb export, or run a crawl
with Firecrawl `firecrawl_crawl`.

Confirm the crawl is recent and covers the scope being triaged. Triaging a three month old crawl
produces tickets for issues that were already fixed, which is the fastest way to lose developer
trust.

Also confirm the sprint capacity. Ten items for a team with two days of SEO capacity is a
different list from ten items for a dedicated squad.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Issue list | Semrush `siteaudit_research` on an existing project | Screaming Frog / Sitebulb export |
| Which project IDs exist | Semrush `projects_research` | Ask the user |
| Traffic value of affected URLs | GSC MCP `analytics_query`, `analytics_top_pages` | GA4 landing page export |
| Ranking value of affected URLs | Semrush `url_research` | Rank tracker export |
| Indexation reality check | GSC MCP `inspection_batch` | Live crawl |
| Live page or template inspection | Firecrawl `firecrawl_scrape` | `web_fetch` |
| Ticket creation | GitHub, Jira, or Linear connector | Output a ticket-ready Markdown block |

## Workflow

- [ ] 1. Retrieve the latest audit issues and record the crawl date and scope.
- [ ] 2. Group issues by root cause and template, not by issue type. See `references/root-cause-grouping.md`.
- [ ] 3. Join affected URLs with clicks, impressions, and ranking keywords.
- [ ] 4. Classify each group's fix type: template, page, configuration, infrastructure, or investigative.
- [ ] 5. Score impact, effort, and confidence.
- [ ] 6. Sanity-check the top items against live pages. Audit tools produce false positives.
- [ ] 7. Cut to the 10 to 15 items worth doing next, sized to the stated capacity.
- [ ] 8. Write acceptance criteria for every item.
- [ ] 9. Optionally draft tickets or a code specification.

Step 2 is where the value is. "1,847 pages missing meta descriptions" is one ticket if they all
share a template and forty tickets if they do not. Check whether the affected URLs share a path
pattern, a content type, or a rendering path before assuming either.

Step 6 matters more than it sounds. Crawlers routinely flag JavaScript-rendered content as
missing, report redirect chains that resolve fine for users, and count duplicate titles across
paginated series that are working as designed. Verify the top few before writing tickets.

## Scoring

Impact is the organic value at risk or unlocked, not the issue count. Ten broken links on a page
that earns nothing is a low-impact group. One canonical error on a page earning 3,000 clicks a
month is not.

Effort is engineering effort, estimated conservatively. A template change is usually cheaper per
URL than it looks and a configuration change is usually more political than it looks.

Confidence is whether the fix will actually produce the expected result. High for directive and
status code fixes, lower for anything that depends on how search engines re-evaluate the page.

Full scoring guidance and fix-type definitions are in `references/root-cause-grouping.md`.

## Output

| Rank | Issue | URLs Affected | High-Value URLs | Traffic at Risk | Likely Root Cause | Fix Type | Impact | Effort | Confidence | Recommended Fix | Acceptance Criteria |
|---|---|---:|---:|---:|---|---|---|---|---|---|---|

Acceptance criteria must be checkable by someone who is not an SEO. "Canonical tags fixed" is not
acceptance criteria. "All URLs under /guides/ return a self-referencing canonical, verified on a
sample of 20 URLs post-deploy" is. See `references/acceptance-criteria.md` for patterns.

Follow the table with four short sections:

- Issues that require further investigation
- Issues excluded as low-value or intentional, with the reason
- Missing data or incomplete crawl coverage
- Dependencies between recommended fixes, and the order they should be done in

The excluded list is often the more useful half of the conversation, and the dependency list is
what stops a team fixing canonicals before the redirects those canonicals depend on.

## Human checkpoint

Require explicit approval before any of these, and never perform them autonomously:

- Editing code or templates
- Changing robots.txt
- Changing canonical tags
- Altering redirects
- Modifying sitemaps
- Opening or merging a pull request

Drafting a ticket or a code specification is fine. Applying it is not.

## Known limitations

- Audit tools report symptoms and causes in the same list. Issue counts are not fix counts.
- Crawlers approximate rendering. Anything JavaScript-dependent needs manual verification.
- Severity labels in audit tools are generic and ignore the specific site's traffic distribution.
  Always re-rank against actual value rather than trusting the tool's priority column.
- A crawl is a snapshot. Issues introduced after the crawl are invisible here; use the release
  regression skill for that.
