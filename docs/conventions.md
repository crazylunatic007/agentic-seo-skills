# Shared conventions

Every skill in this repo follows the same rules. They are restated compactly inside each
SKILL.md so the skills stay self-contained when copied out, but this is the canonical version.

## 1. Evidence discipline

SEO diagnosis is mostly inference from incomplete data. The failure mode that destroys trust is
a confident wrong answer, not a hedged right one.

- Every claim in an output table names the metric and comparison window it came from.
- If a field cannot be filled from retrieved data, write `unknown`. Never estimate to fill a cell.
- Correlation is not cause. Label causes as hypotheses unless a direct mechanism was observed
  (for example: the canonical tag changed, the page returns 404, the sitemap no longer lists it).
- If a tool call fails or returns nothing, say so in the output. Do not silently drop the check.

## 2. Confidence scale

| Level | Meaning |
|---|---|
| High | Two or more independent sources agree AND a direct mechanism was observed. |
| Medium | One strong signal, or several weak signals pointing the same way. Alternatives not fully excluded. |
| Low | Pattern is suggestive but the available data cannot separate it from at least one rival explanation. |

Anything that would be Low is usually better reported as `Insufficient evidence` with a note on
what data would resolve it.

## 3. Human checkpoints

Analysis and reporting run unattended. Anything that changes the site, the code, or a
relationship stops and waits for a person.

Always stop before:
- Editing code, templates, or CMS content
- Changing robots.txt, canonicals, redirects, sitemaps, or indexing directives
- Deleting, unpublishing, or noindexing a page
- Opening or merging a pull request
- Publishing content
- Sending outreach

Present the proposed change set, then wait for explicit approval. Approval for one action is not
approval for the batch.

## 4. Threshold discipline

Ranking by percentage alone surfaces noise from tiny pages. Every filter uses both a relative
and an absolute floor, for example "down at least 30% AND at least 100 clicks". Defaults live in
each skill and should be treated as starting points, not constants.

## 5. Tool routing

These skills were built against a specific connector set. If a connector is missing, substitute
the equivalent and say which one was used in the output.

| Need | Preferred | Substitute |
|---|---|---|
| Actual search performance | Google Search Console MCP (`analytics_query`, `analytics_compare`) | GSC UI export, Looker Studio export |
| Indexation state of a URL | GSC `inspection_inspect` | Live crawl plus `site:` check |
| Rankings, competitors, keyword data | Semrush MCP (`organic_research`, `keyword_research`, `domain_overview`) | Ahrefs, Sistrix, or another rank dataset |
| Backlinks | Semrush MCP `backlinks_research` | Ahrefs, Majestic, Moz |
| Site crawl and technical issues | Semrush MCP `site_audit` (needs an existing Site Audit project) | Screaming Frog or Sitebulb export, Firecrawl `firecrawl_crawl` |
| Reading live page content | Firecrawl `firecrawl_scrape` / `firecrawl_crawl` | `web_fetch`, headless browser |
| SERP features and AI Overviews | SerpAPI | Manual SERP capture |
| Engagement and conversions | GA4 via GSC MCP `analytics_advanced`, or GSC MCP `analytics_*` GA4 tools | GA4 UI export |
| Raw Semrush reports | Semrush `get_report_schema` then `execute_report` | Semrush API directly |

Cap every report at a sensible `display_limit` (20 is usually enough for analysis) so a single
run does not burn the account's API units.

## 6. Output format

Each skill defines a required table. Produce the table first, then a short written summary. The
table is the deliverable; the prose is context. Save the artifact as Markdown or CSV rather than
pasting a 60-row table into chat.
