# Find Internal-Linking Opportunities and Orphaned Pages

Use the Internal Linking Rescue Skill to find internal-linking opportunities for these priority destination pages:
- [target URL 1]
- [target URL 2]
- [target URL 3]

Build the source pool before reading anything. Take the top [150] pages under [domain/folder] ranked by organic clicks over the last 90 days, and read full content for those only. Do not crawl or scrape beyond that set. If the set is too small to produce useful recommendations, tell me and propose a larger cap rather than expanding it yourself.

Exclude [navigation pages, tag archives, paginated URLs, legal pages, noindex pages, or other exclusions].

Use:
- The latest crawl or Site Audit
- Full page text or rendered content for the source pool
- Existing internal-link data
- GSC and Semrush performance data
- Project knowledge describing strategic pages and topics

For each target page:
1. Find source pages within the pool with relevant topical context.
2. Order candidates by source value, meaning the source page's own traffic, rankings, backlinks, or strategic importance.
3. Verify that the source does not already contain a suitable link to the target.
4. Identify the exact section, sentence, or paragraph where a link would fit.
5. Suggest a natural anchor that accurately describes the destination.
6. Explain how the link helps the reader continue their task.
7. Reject keyword matches that are not contextually useful. If the only justification is that both pages are about the same topic, drop it.

Return no more than [maximum] recommendations:

| Source URL | Target URL | Suggested Anchor | Exact Placement | Reader Benefit | Source Value | Confidence |
|---|---|---|---|---|---|---|

Quote a short fragment of the host sentence in the placement column so an editor can find it without searching.

Separately report:
- Orphaned priority pages
- Broken internal links
- Important pages receiving links only from low-value areas
- Pages with excessive or repetitive internal links

Treat that second list as a distinct deliverable. Those are structural problems with a different owner, and mixing them into the recommendations means neither gets done.

Do not recommend sitewide exact-match anchors, and vary the anchor text across recommendations pointing at the same destination. Do not invent a placement if full page content is unavailable; lower the confidence or report that placement cannot be verified.

Keep the CMS read-only. Do not insert or change links without human approval.
