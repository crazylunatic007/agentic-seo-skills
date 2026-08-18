---
name: competitor-growth-investigation
description: Investigates why a competitor's organic visibility changed by isolating the pages and keywords responsible, separating real growth from seasonality, branded lift, and data artefacts, then recommending whether to respond. Use this whenever the user mentions a competitor gaining or losing traffic, asks what a rival is doing in search, wants competitive monitoring or alerts, sees a visibility chart move, or asks whether they should react to something a competitor published.
---

# Competitor Growth Investigation

Detect meaningful competitor movement, explain what actually caused it, and decide whether it
matters enough to change what the team does.

Most competitor reports fail in one of two ways: they report every fluctuation as a threat, or
they report a number going up without explaining what drove it. Both leave the reader unable to
act. This workflow exists to reach a recommendation, including the recommendation to do nothing.

## Before you start

Establish:

1. **The competitor set** — three to five domains, chosen because they compete for the same
   queries, not because they are the same size or in the same funding round. Ask which they care
   about if unclear.
2. **Comparison windows** — default is current month vs the same month last year, plus current
   vs previous month to catch recent moves.
3. **Alert threshold** — default is a change of at least 15% in estimated organic traffic AND a
   change large enough to matter in absolute terms for that domain.
4. **Topic relevance filter** — which topics the business actually cares about. A competitor
   growing 40% on a topic nobody wants to own is not news.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Domain organic performance over time | Semrush `organic_research`, `domain_overview` | Any visibility index |
| Which pages drive the change | Semrush `organic_research` (`resource_organic_unique`, `resource_organic`) | Rank tracker with URL data |
| Which keywords moved | Semrush `organic_research` keyword report | SERP capture over time |
| Traffic and audience context | Semrush `traffic_overview` | Similarweb or equivalent |
| Position tracking against a fixed set | Semrush `position_tracking` | Any rank tracker |
| What the winning page actually says | Firecrawl `firecrawl_scrape` | `web_fetch` |
| Current SERP state | SerpAPI | Manual SERP check |
| Alerting | Slack or email connector | Return the report and let a person send it |

Some Traffic and Market datasets require separate Semrush access. If a report is unavailable, say
so rather than substituting an unrelated metric.

## Workflow

- [ ] 1. Compare each competitor across the defined windows.
- [ ] 2. Drop everything below the alert threshold. Most weeks, most competitors are noise.
- [ ] 3. For each flagged competitor, identify the specific pages responsible for the change.
- [ ] 4. Identify the keywords those pages gained or lost.
- [ ] 5. Attribute the driver using `references/growth-drivers.md`.
- [ ] 6. Read the top two or three winning pages. Do not infer content quality from a URL.
- [ ] 7. Check whether the affected topics matter to the business.
- [ ] 8. Recommend a response, including no response.

The agentic part is step 3 onward. A reporting script stops at "traffic up 22%". This workflow
decides which competitors deserve deeper investigation based on what step 1 returned, then follows
the trail to specific pages and keywords, then reads those pages. Let the intermediate results
determine how deep to go rather than running the same fixed depth on every competitor.

## Attribution

Read `references/growth-drivers.md` for the signature of each driver. The categories:

New content · Ranking improvements on existing pages · Seasonal demand · Branded growth ·
New product or category pages · Migration or domain change · Data artefact

The last one deserves particular attention. Provider index changes, database switches, newly
tracked keywords, and subdomain reattribution all produce dramatic charts with no real-world
event behind them. Check whether the change is concentrated on a single date, whether it affects
the whole domain uniformly, and whether it appears in more than one data source before treating
it as real.

Branded growth is the second most common false alarm. A competitor whose growth is entirely
branded ran a campaign or got press. That is a marketing event, not a search threat, and the
correct response is usually different.

## Output

| Competitor | Traffic Change | Main Growth Pages | Main Keywords | Branded or Non-Branded | Likely Driver | Relevance to Us | Recommended Response | Confidence |
|---|---:|---|---|---|---|---|---|---|

Recommended response is one of: monitor, update an existing page, create new content, investigate
a product or positioning gap, or no action.

Follow with two or three sentences on the single most important thing the reader should take away.
If nothing happened worth acting on, say that plainly. A report that says "no meaningful change
this period, here is the one thing worth watching" is a good report.

## Human checkpoint

Reporting can run unattended and on a schedule. A person approves any content, product, or
positioning response before work starts. Do not send alerts to a channel or a person without
explicit approval of both the content and the recipient.

## Known limitations

- Third-party traffic figures are modelled estimates. They are directionally useful for detecting
  change and unreliable as absolute numbers. Never present them as the competitor's real traffic.
- Keyword databases cover a sample. A competitor can grow substantially on terms the provider does
  not track.
- Estimated traffic conflates rankings with assumed CTR curves, so SERP feature changes can move
  the estimate without any real ranking change.
- Attribution to a single driver is often wrong. Report the dominant driver and note the others.
- Paid, referral, and direct traffic are outside this workflow. A competitor's overall growth may
  have nothing to do with search.
