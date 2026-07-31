# Build a Content Portfolio Decision Engine

Use the Content Portfolio Decisions Skill to evaluate URLs under [domain/folder].

The business priorities are [products, audiences, markets, conversions, or topic areas].

Apply the ordered decision rules in the Skill's reference file at `references/decision-rules.md`. Do not invent your own thresholds. Our appetite for this run is [conservative/balanced/aggressive].

For any inventory above [300] URLs, run `scripts/portfolio_score.py` to apply the rules deterministically rather than reasoning row by row. Save the full output as CSV. In chat, show only the decision counts, the escalated Investigate set, and the summary sections below. Do not paste the full table into the conversation.

Use:
- The CMS or URL inventory
- Google Search Console
- GA4 and conversion data
- Semrush rankings and backlink data
- Crawl or Site Audit data
- Publication and update dates
- AI citation data where available

Reconcile trailing slashes, protocols, and parameters before joining these sources, or the join will drop rows silently.

Treat a missing value as missing, not as zero. A blank conversions column means the data was not supplied. Escalate those URLs rather than deciding on them.

Exclude [legal pages, account pages, support utilities, campaign URLs, or other out-of-scope content], but list every exclusion.

Evaluate each URL using:
- Organic traffic and trend
- Ranking and query coverage
- Backlinks and referring domains
- Conversions and assisted conversions
- Content freshness
- Strategic relevance
- Topic overlap
- Indexability and technical status
- AI citations or brand visibility where available

Assign one proposed decision: Keep, Update, Consolidate, Redirect, Remove, or Investigate.

For every URL:
1. Show the signals supporting the recommendation.
2. Show any conflicting signals.
3. Identify a destination when consolidation or redirection is proposed.
4. Explain why the destination satisfies the same user intent.
5. Assign a confidence level.
6. Use "investigate" when evidence or business context is insufficient.

Before recommending any redirect, confirm the destination returns 200, serves the same intent, is not itself a removal candidate, and will not create a chain. Do not default to the homepage or a category page when no genuine equivalent exists. Escalate instead.

Automatically escalate pages with:
- Valuable backlinks
- Historical or assisted conversions
- Significant citations
- Legal or compliance importance
- Strategic relevance not reflected in traffic
- No clear replacement destination

Return, as CSV:

| URL | Proposed Decision | Supporting Signals | Conflicting Signals | Proposed Destination | Reason | Confidence | Required Reviewer |
|---|---|---|---|---|---|---|---|

In chat, follow with:
- Decision counts
- Potential consolidation groups
- High-risk decisions
- Pages requiring business-owner input
- Missing data that could change a recommendation, and how many URLs it affects
- Total historical clicks and conversions covered by the proposed removals and redirects

That last figure is what makes this approvable or not. Include it.

Do not redirect, remove, unpublish, consolidate, or noindex anything. Every destructive or irreversible action requires human approval, one batch at a time.
