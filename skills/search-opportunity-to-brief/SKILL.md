---
name: search-opportunity-to-brief
description: Turns a seed topic or competitive gap into a decision-ready content brief by expanding the keyword space, grouping queries by audience problem rather than by keyword, auditing existing coverage for gaps and cannibalization, reading what currently ranks, and specifying the angle, structure, and evidence a writer needs. Use this whenever the user asks for a content brief, a topic or keyword to be turned into an article plan, wants to know what to write about a subject, mentions a content gap, or asks whether a topic is worth covering.
---

# Search Opportunity to Brief

Move from a seed topic to a brief an editor can approve and a writer can execute, without the
brief becoming a summary of what already ranks.

The tension this workflow manages: SERP analysis tells you what currently satisfies the query,
which is necessary for relevance and useless for differentiation. A brief that only encodes SERP
patterns produces the tenth version of the same article. Every section below that mentions the
SERP is paired with a section that asks what the page will say that the others do not.

## Before you start

Get four things, proposing defaults where possible:

1. **The seed** — a topic, a keyword, a competitor URL, or an identified gap.
2. **The site and its existing coverage** — needed to check for overlap before recommending a new page.
3. **The audience** — practitioner level matters more than persona. A brief for beginners and a
   brief for specialists on the same keyword are different briefs.
4. **Whether the product should appear**, and how directly.

If the user has an in-house brief format, ask for an example and match it. The template in
`references/brief-template.md` is a default, not a requirement.

## Required data

| Need | Preferred tool | If unavailable |
|---|---|---|
| Keyword expansion, questions, related terms | Semrush `keyword_research` | Any keyword tool export |
| Who ranks across the topic | Semrush `organic_research` | SERP capture across the query set |
| What a specific URL ranks for | Semrush `organic_research` / `resource_organic` | Rank tracker |
| SERP shape, features, AI Overview | SerpAPI | Manual SERP capture |
| Existing coverage and current performance | GSC MCP `analytics_query` with `dimensions: ["query","page"]` (no dedicated cannibalization tool exists; read the overlap manually) | Site search plus GSC export |
| Reading competitor pages | Firecrawl `firecrawl_scrape` | `web_fetch` |
| Existing content inventory | CMS, sitemap, or Firecrawl `firecrawl_map` | Ask the user for a URL list |
| Delivering the brief | Google Drive, Notion, or CMS connector | Save as Markdown and present it |

Cap keyword reports at `display_limit: 20` unless the topic genuinely needs more.

## Workflow

- [ ] 1. Expand the seed into related keywords, questions, use cases, and adjacent intents.
- [ ] 2. Identify which domains rank repeatedly across the topic, not just on the head term.
- [ ] 3. Group queries by the underlying audience problem, not by keyword string similarity.
- [ ] 4. Check whether the site already covers each group.
- [ ] 5. Flag missing topics, weak existing pages, cannibalization risks, and product-fit opportunities.
- [ ] 6. Read the top results properly. Note recurring structure, and note what none of them do.
- [ ] 7. Choose the content format the intent actually calls for.
- [ ] 8. Draft the brief.
- [ ] 9. Present the angle and proposed structure for approval before the brief is finalised.

Step 3 is the step that distinguishes a brief from a keyword list. "How to do X", "X best
practices", and "X checklist" are three keyword phrasings of one audience problem, and they belong
in one page. "X vs Y" and "how much does X cost" look adjacent and are different problems at
different stages, belonging in different pages.

Step 6 requires actually reading the pages. Do not infer content from titles and meta descriptions.
The most valuable observation is usually what every ranking page omits, and that is invisible from
the SERP alone.

Step 9 is not optional. Presenting findings and a proposed structure before writing the full brief
saves the editor from rejecting a finished artefact over a decision made in the first ten minutes.

## Choosing the format

Let the dominant intent decide, then check the format against the site's ability to execute it.

| Dominant intent | Format that usually wins | Watch for |
|---|---|---|
| Learn how to do something | Step-based guide with a worked example | Generic steps with no real example |
| Choose between options | Comparison with an explicit recommendation | Refusing to recommend anything |
| Find a tool or vendor | Curated list with selection criteria stated up front | Undifferentiated listicle |
| Understand a concept | Explainer built on one clear framework | Definition padding |
| Solve a specific error or blocker | Direct answer first, then context | Burying the fix under preamble |
| Decide whether something is worth doing | Argument with evidence and a position | Balanced-to-the-point-of-useless |

If the SERP is fractured across several of these, say so and pick deliberately. A fractured SERP is
usually an opportunity, because it means no page has resolved the intent yet.

## Output

Use `references/brief-template.md`. The brief must contain at minimum:

Target reader · Search intent · Core argument or point of view · Recommended headings ·
Questions the page must answer · Evidence or original research required · Internal links ·
Product integration · What this page does that the ranking pages do not

That last field is the one to write first. If it cannot be filled with something specific, the
topic may not be worth a page, and saying so is a legitimate output.

## Human checkpoint

An editor approves the topic, angle, and format before drafting begins.

Never publish the resulting article automatically, and do not set up a workflow that does. The
brief is the deliverable here; drafting and publishing are separate decisions with separate
approvals.

## Known limitations

- SERP patterns show what currently ranks, not what will be uniquely valuable. Editorial judgement
  protects originality and brand fit; this workflow cannot.
- Keyword volumes are estimates, and low-volume terms are frequently misreported. Use them for
  relative comparison, not for forecasting traffic.
- AI Overview presence changes by query, location, personalisation, and date. A single capture is a
  sample, not a fact about the SERP.
- Coverage checks depend on the completeness of the content inventory supplied. A partial inventory
  produces confident recommendations to write pages that already exist.
