# Diff checks

Every dimension to compare between the pre-release and post-release crawls, what a regression looks
like, and why it matters. Ordered roughly by severity.

## 1. Availability and status codes

| Check | Regression |
|---|---|
| Status code per URL | 200 becomes 4xx or 5xx |
| URL presence | Present before, absent after |
| New URLs | Large unexpected sets appearing, often faceted or parameterised |

A 200 becoming a 404 on a URL with traffic is the single highest-severity finding in this workflow.
5xx is worse but usually self-evident from monitoring.

## 2. Indexing directives

| Check | Regression |
|---|---|
| Meta robots | `index` becomes `noindex` |
| X-Robots-Tag | Header appears or changes |
| robots.txt | New disallow covering previously crawlable paths |

Check robots.txt as a whole file, not just per-URL results. A single staging rule shipped to
production affects everything and may not show up as a per-URL change if the crawl respected it.

## 3. Canonicals

| Check | Regression |
|---|---|
| Canonical target | Self-referencing becomes cross-canonical |
| Canonical presence | Present becomes absent |
| Canonical consistency | Points to a URL that is itself canonicalised or non-200 |

Cross-canonicals introduced by a template change are a common replatform casualty and are usually
invisible to everyone except a crawl diff.

## 4. Redirects

| Check | Regression |
|---|---|
| New redirects | 200 becomes 301 or 302 unexpectedly |
| Redirect type | 301 becomes 302 |
| Chains and loops | Chain length increases, or a loop appears |
| Redirect target | Target changed, or now returns a non-200 |

Migrations commonly stack rules, for example protocol plus trailing slash plus locale, producing
three-hop chains that were single hops before.

## 5. XML sitemaps

| Check | Regression |
|---|---|
| Sitemap membership | URL present before, absent after |
| Sitemap validity | Fetch fails, or the index no longer lists child sitemaps |
| Sitemap contents | Contains non-200, noindexed, or non-canonical URLs |

Compare sitemap membership against the crawl. A sitemap that still lists URLs the release deleted
is a slow-burning crawl waste problem rather than an emergency.

## 6. Internal links

| Check | Regression |
|---|---|
| Inbound internal link count per URL | Material drop, especially to zero |
| Newly orphaned URLs | Had internal links, now has none |
| Broken internal links | Links now pointing at non-200 URLs |
| Navigation and footer links | Global modules changed |

A redesign that removes a hub page can orphan hundreds of URLs without changing a single one of
them, which is why link-graph comparison belongs in the diff rather than in a separate audit.

## 7. Titles, headings, and meta

| Check | Regression |
|---|---|
| Title tag | Missing, truncated, templated over, or duplicated across URLs |
| H1 | Missing, or now duplicated site-wide |
| Meta description | Missing where previously present |
| Duplicate rate | Site-wide duplicate title or H1 rate increases |

Watch for the specific failure of a template shipping with an uninterpolated variable, which shows
up as thousands of identical titles rather than as missing ones.

## 8. Structured data

| Check | Regression |
|---|---|
| Schema presence | Present before, absent after |
| Schema validity | Now emits errors |
| Required properties | Dropped from the template |

## 9. Rendered content

| Check | Regression |
|---|---|
| Word count | Material drop, particularly to near zero |
| Main content presence | Body content absent in the rendered crawl |
| Client-side rendering | Content that previously appeared server-side now requires JS |

This dimension produces the most false positives. Always verify a sample against a real rendered
fetch before escalating, because a crawler configuration difference looks identical to a genuine
content loss.

## 10. Performance and hreflang

| Check | Regression |
|---|---|
| Core Web Vitals | Field data degrades after the release |
| hreflang | Annotations missing, or return tags broken |
| Locale routing | Users or crawlers redirected by geography where they were not before |

Performance regressions appear in field data weeks later. Use lab data as an interim signal and say
which one is being reported.

## Expected versus unplanned

Every regression must be labelled against the stated change list:

- **Expected** — intended, and the report confirms it landed as designed.
- **Expected but wrong** — the intended change shipped incorrectly. Frequently the most valuable row.
- **Unplanned** — nobody intended this.

Without the change list, everything looks unplanned, the report reads as alarmist, and the team
stops opening it.
