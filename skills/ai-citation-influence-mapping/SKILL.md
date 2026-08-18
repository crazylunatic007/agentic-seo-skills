---
name: ai-citation-influence-mapping
description: Maps which third-party sources repeatedly influence AI answers in a category, finds where competitors are cited and the brand is absent, scores each source on realistic winnability, and turns the gaps into a prioritized digital PR and contribution queue. Use this whenever the user mentions AI citations, LLM or AI visibility, GEO or AEO, ChatGPT and Perplexity mentions, being missing from AI answers, or wants a digital PR, outreach, or unlinked-mention target list.
---

# AI Citation Influence Mapping

Work out which sources AI assistants actually draw on for a category, where competitors appear in
those sources and the brand does not, and which of those gaps are realistically closable.

The output of most AI visibility tooling is a list of prompts and whether the brand appeared. That
identifies the symptom. This workflow goes one step further: it looks at what the models cited,
treats those sources as a distribution channel, and produces a queue of specific, plausible actions
against specific publications. The word that carries the weight is plausible. A target list that
includes sources nobody will ever place content in is a list nobody works.

## Before you start

Establish, and be blunt about the data quality:

1. **The citation dataset** — which platform, which prompt set, which geography, which dates. This
   determines everything downstream and must be stated in the output.
2. **The prompt set** — do the tracked prompts represent how buyers actually ask, or how the
   marketing team wishes they asked? A biased prompt set produces a biased target list.
3. **The competitor set** — who counts as a competitor for comparison.
4. **The brand's actual assets** — original data, practitioners who can be quoted, a product worth
   reviewing, an existing media relationship. The recommended plays depend on what exists.

If no citation dataset exists, say so plainly. This workflow needs observed citations. Do not
substitute organic ranking data and present it as AI visibility; they overlap but they are not the
same thing, and conflating them is the most common error in this area.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Cited sources per prompt | The user's AI visibility export or connected dataset | Cannot proceed. Say so |
| Domain authority and backlink profile of cited sources | Semrush `backlinks_research`, `domain_overview` | Any authority metric |
| Organic visibility of cited sources | Semrush `organic_research` | Any visibility index |
| What a cited page actually says | Firecrawl `firecrawl_scrape` | `web_fetch` |
| Competitor mentions across sources | Firecrawl `firecrawl_search`, or the citation export | Manual review |
| Contributor guidelines and contact routes | Firecrawl `firecrawl_scrape` on the source site | Manual research |
| Existing relationships | CRM or media database connector | Ask the user |

## Workflow

- [ ] 1. Group tracked prompts by topic and buying-stage intent, not by prompt wording.
- [ ] 2. Identify the domains and specific pages cited most often across each group.
- [ ] 3. Separate source types: the same play does not work on a review aggregator, a trade
      publication, a community forum, and a competitor's own blog.
- [ ] 4. Find sources that cite competitors and never the brand. These are the gaps.
- [ ] 5. Read the cited pages. What earns a mention in a listicle is different from what earns a
      mention in an analysis piece.
- [ ] 6. Score each source using `references/source-scoring.md`.
- [ ] 7. Match a play to each source using `references/outreach-plays.md`.
- [ ] 8. Rank by expected influence divided by realistic effort, and cut the list to what the team
      can actually work.

Step 3 does more work than it looks. A citation from a G2-style aggregator is won by having
reviews and a complete profile. A citation from a trade publication is won by a relationship and
something worth publishing. A citation from a forum thread cannot be won by outreach at all and
should be scored accordingly rather than dropped into the same queue.

Step 5 is where the specific angle comes from. Reading the page that cited the competitor usually
reveals exactly what the brand would need to supply to be included in the next update.

## Scoring

Read `references/source-scoring.md`. Sources are scored on citation frequency, topical relevance,
independent organic visibility, authority, competitor presence, and openness to contribution.

The last dimension is the one most often skipped and the one that determines whether the queue gets
worked. A source cited in 40% of answers that has never accepted an outside contribution is a
lower-priority target than a source cited in 12% that runs a submissions process.

## Output

| Domain | Cited Pages | Citation Frequency | Cited Topics | Competitors Present | Brand Present | Why It Matters | Recommended Asset | Outreach Angle | Effort | Priority |
|---|---|---:|---|---|---|---|---|---|---|---|

Then state the dataset caveat explicitly: platform, prompt count, geography, and collection dates.
Anyone reading this table six weeks later needs to know how much of it still holds.

Include a short section on sources where the correct answer is no outreach, and why. Usually:
competitor-owned properties, forums, sources with a policy against vendor contributions, and
sources whose citation is incidental rather than editorial.

## Human checkpoint

A person reviews and sends every outreach message. Do not send email, submit forms, or contact
publications through any connector.

Relationship decisions, correction requests, and partnership approaches all carry reputational
weight. Draft them; do not deliver them.

Corrections deserve particular care. Approaching a publication to correct information about the
brand is legitimate. Approaching one to change how a competitor is described is not, and should not
appear in the queue.

## Known limitations

- AI citation datasets vary by platform, prompt set, geography, personalisation, and collection
  date. They are a sample of visibility, not a map of all AI answers.
- Citation does not imply influence on the answer. A source may be cited decoratively after the
  answer was formed from parametric knowledge.
- Models change retrieval behaviour frequently. A target list has a shelf life measured in weeks
  to months, not quarters.
- Being cited more does not reliably produce more customers. Treat the queue as a visibility
  hypothesis to be measured, not a growth forecast.
- Correlation between organic authority and citation frequency is real but loose. Do not substitute
  one for the other.
