---
name: internal-linking-rescue
description: Finds contextually genuine internal linking opportunities for priority pages and surfaces orphaned pages, broken internal links, and pages whose only inbound links come from low-value sections. Recommends the exact source page, destination, anchor, and placement sentence. Use this whenever the user asks about internal links, internal linking strategy, orphan pages, link equity distribution, or wants to strengthen a specific page without building external links.
---

# Internal Linking Rescue

Find internal links worth adding, specified precisely enough to implement, and identify the
structural link problems that no amount of new linking will fix.

Most internal linking tools match keywords and produce lists that read like spam when
implemented. The test applied here is different and stricter: would a reader partway through this
sentence actually want to go there next? If not, the link does not go in the list, however well
the keyword matches.

## Before you start

Establish:

1. **Priority destinations** — which pages should be strengthened, and why. Usually pages with
   commercial value, ranking on page two, or newly published. Ask for a list rather than inferring;
   inferred priorities produce recommendations nobody implements.
2. **Content scope** — the whole site, a folder, or a defined set.
3. **Whether page content is accessible** — recommendations are only as good as the ability to read
   the source pages. Say up front if content access is limited.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Site structure and URL inventory | Firecrawl `firecrawl_map`, or Semrush `siteaudit_research` | Sitemap plus CMS export |
| Internal link graph | Semrush `siteaudit_research` (existing project), or a crawler export | Firecrawl `firecrawl_crawl` and parse links |
| Page content | Firecrawl `firecrawl_scrape` or `firecrawl_crawl` | `web_fetch` per URL |
| Which pages have authority to lend | GSC MCP `analytics_top_pages`, Semrush `url_research` | Any traffic export |
| Backlinks per page | Semrush `backlink_research` | Ahrefs or Majestic |
| Applying changes | CMS connector | Output a change list for a human |

## Workflow

- [ ] 1. Confirm the priority destination pages.
- [ ] 2. Build the candidate source pool: pages that already rank, earn links, or receive traffic.
- [ ] 3. Read those pages and locate passages that genuinely relate to each destination.
- [ ] 4. Exclude pages that already link to the destination appropriately.
- [ ] 5. Apply the reader-value test in `references/link-quality-rubric.md`. Drop anything failing it.
- [ ] 6. Write each recommendation with source, destination, anchor, exact placement, and reasoning.
- [ ] 7. Separately, run the structural checks: orphans, broken internal links, over-linked pages,
      and important pages linked only from low-value sections.

Step 2 matters because a link from a page with no authority and no traffic transfers very little.
Ordering candidate sources by their own performance means the first ten recommendations do more
than the next fifty.

Step 3 requires the rendered content. Links recommended from a URL slug or a title alone will land
in the wrong place or in a section where they make no sense.

Step 7 is a separate deliverable from steps 1 to 6, and often the more valuable one. A page with
no internal links at all is a structural problem; adding one contextual link is a patch, and
fixing the missing hub page is the fix.

## Writing the recommendation

Each row needs enough detail that an editor can implement it without judgement calls:

- **Source URL** and **destination URL**
- **Suggested anchor** — descriptive, natural in the sentence, varied across recommendations.
  Exact-match anchors repeated across dozens of links is the pattern that reads as manipulation.
- **Placement** — the specific section and the sentence it attaches to. Quote a short fragment so
  the implementer can find it.
- **Reason** — why a reader at that point in the page benefits from going there.

If the reason can only be stated as "both pages are about X", the link is a keyword match rather
than a reader path. Drop it.

## Output

Primary table:

| Source URL | Source Value | Target URL | Suggested Anchor | Placement | Reader Reason | Confidence |
|---|---|---|---|---|---|---|

Structural findings table:

| Issue Type | URL | Detail | Why It Matters | Recommended Fix |
|---|---|---|---|---|

Issue types: orphan, broken internal link, excessive internal links, important page linked only
from low-value sections such as footers, tag pages, or paginated archives.

Order the primary table by expected value, which is the source page's own authority combined with
the strength of the contextual fit, not by keyword match score.

## Human checkpoint

A person reviews anchors and placements before anything is applied in bulk. Do not edit CMS content
or push link changes automatically, even with a CMS connector available.

Bulk-applying twenty links at once to a single destination is a pattern worth flagging to the user
rather than executing, regardless of approval, because it looks engineered and usually is.

## Known limitations

- Without full rendered page content, placement and anchor recommendations lack context and should
  be marked low confidence.
- Crawl-based link graphs miss links injected client-side and links in components that vary by user
  state.
- Internal linking rarely moves a page on its own. It compounds with content quality and external
  authority, so recommendations here should not be sold as a standalone ranking fix.
- Orphan detection depends on crawl completeness. A page missing from the crawl is not necessarily
  an orphan; it may simply be outside the crawl scope.
