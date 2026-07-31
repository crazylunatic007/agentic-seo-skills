# Diagnose Declining Content

Use the Content Decline Diagnosis Skill to analyze URLs under [domain or folder, such as example.com/blog/] for [country] on [desktop/mobile/all devices].

Compare [current 90-day period] with [the same 90 days last year].

Search Console retains a rolling 16 months, so a 90-day window compared year over year fits with room to spare. A window longer than about four months compared year over year runs past the retention wall. Shorten the window rather than extending the lookback, and tell me if the requested comparison is not available.

Include only URLs that:
- Lost at least [30%] of organic clicks
- Lost at least [100] clicks
- Received at least [200] clicks during the earlier period

Exclude these URL patterns: [/promo/*, /black-friday*, /author/*, /tag/*, or other patterns]
Exclude these specific URLs: [paste the list of new pages, redirected URLs, discontinued products, and campaign pages]

Do not infer which pages are seasonal, branded, or discontinued. You cannot determine that from Search Console or Semrush. If a page looks like it belongs in an exclusion category but is not on the list I gave you, include it and flag it in the output rather than dropping it silently.

Use:
- Google Search Console for clicks, impressions, CTR, average position, queries, pages, country, and device data
- Semrush for ranking keywords, search demand, competitors, SERP changes, and backlink context
- Site Audit or crawl data for technical and indexation checks
- GA4 for engagement or conversion context

Check indexation state first. A deindexed, canonicalised, or non-200 URL ends the investigation for that page, and confirming it is cheap.

For each qualifying URL:
1. Calculate its absolute and percentage change in clicks, impressions, CTR, and average position.
2. Identify the queries responsible for most of the loss.
3. Determine whether search demand, rankings, or CTR declined.
4. Check for lost keywords, backlinks, or internal links.
5. Look for cannibalization from another URL on our domain.
6. Review new competitors and meaningful SERP-feature changes.
7. Check for technical, indexation, or content-freshness problems.
8. Classify the most likely cause.
9. Cite the evidence supporting that classification.
10. Recommend one primary action and one fallback action.

Use one of these classifications:
- Search demand declined
- Rankings declined
- CTR declined while rankings remained stable
- Competitor replaced the page
- Cannibalization
- Technical or indexation issue
- Lost links or internal authority
- Content is outdated
- SERP or AI answer reduced click opportunity
- Insufficient evidence

Where a decline has more than one cause, report the dominant one and note the secondary cause in the evidence column rather than forcing a single label.

Return only the top [10-20] actionable URLs:

| Priority | URL | Clicks Lost | Click Decline | Impression Change | Position Change | Likely Cause | Supporting Evidence | Primary Action | Fallback Action | Confidence |
|---|---|---:|---:|---:|---:|---|---|---|---|---|

Rank priority on absolute clicks lost weighted by how fixable the cause is. A page that lost 400 clicks to a broken canonical outranks a page that lost 600 to a demand collapse, because one is recoverable.

Separate confirmed findings from hypotheses. Label a finding "insufficient evidence" when the available data does not support a reliable conclusion, and say which specific check would resolve it.

Keep all connected systems read-only. Do not update, consolidate, redirect, delete, or publish any page. Report missing records and failed tool calls rather than estimating them.
