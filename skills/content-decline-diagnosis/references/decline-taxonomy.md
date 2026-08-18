# Decline taxonomy

For each cause: the data signature that suggests it, the check that confirms it, the check that
rules it out, and what to do about it.

Work down the list. Earlier causes are cheaper to confirm and more decisive.

## Contents
1. Technical or indexation issue
2. Cannibalization
3. Rankings declined
4. Competitor replaced the page
5. Lost links or internal authority
6. CTR declined while rankings held
7. SERP or AI answer reduced click opportunity
8. Search demand declined
9. Content is outdated
10. Insufficient evidence

---

## 1. Technical or indexation issue

**Signature** — Impressions collapse to near zero, often abruptly rather than gradually. Position
data disappears rather than worsening.

**Confirms it** — URL inspection returns not indexed, blocked by robots, noindex, a canonical
pointing elsewhere, a non-200 status, or an unexpected redirect. Missing from the XML sitemap.

**Rules it out** — Page is indexed, canonical is self-referential, status is 200, and impressions
declined gradually.

**Action** — Fix the directive. **Fallback** — Request reindexing and monitor for two weeks.

This is the only category that regularly supports High confidence, because the mechanism is
directly observable rather than inferred.

---

## 2. Cannibalization

**Signature** — Domain-level impressions for the query set are stable, but they moved to a
different URL on the same site. The declining page's loss roughly matches another page's gain.

**Confirms it** — GSC query-level data shows both URLs appearing for the same queries, alternating
over time, or the newer URL now holds the position the older one held.

**Rules it out** — No other URL on the domain ranks for the affected queries.

**Action** — Consolidate into the stronger page and redirect, or differentiate the intent of each
page. **Fallback** — Fix internal linking so the intended page receives the topical signals.

---

## 3. Rankings declined

**Signature** — Average position worsens, ranking keyword count falls, impressions fall
proportionally. Demand for the same keywords is flat.

**Confirms it** — Ranking keyword loss visible in `organic_research` / `resource_organic` across two periods, and the lost
positions are now held by other domains.

**Rules it out** — Position held while clicks fell. That is a CTR problem, not a ranking problem.

**Action** — Rewrite or substantially upgrade against what now ranks. **Fallback** — Strengthen
internal links and topical support before rewriting.

---

## 4. Competitor replaced the page

**Signature** — A single competitor domain or URL now occupies the positions the page used to
hold, across a cluster of related queries rather than one.

**Confirms it** — SERP capture shows the same competitor URL ranking above the page for most of
its top queries, and that URL is new or recently updated.

**Rules it out** — Losses are spread across many different domains. That is general ranking decay.

**Action** — Analyse what the competing page does differently and close the gap deliberately.
**Fallback** — Target the adjacent queries the competitor does not serve well.

---

## 5. Lost links or internal authority

**Signature** — Referring domains fell, or the page was removed from a hub, nav, or sidebar module
that previously linked to it. Decline is gradual.

**Confirms it** — Backlink data shows lost referring domains in the same window. A crawl shows
fewer internal links pointing at the URL than before.

**Rules it out** — Referring domains and internal links are stable.

**Action** — Restore internal links from relevant pages and reclaim high-value lost links.
**Fallback** — Build new topical internal links from pages that already perform.

---

## 6. CTR declined while rankings held

**Signature** — Position flat or improved, impressions flat or up, clicks down. CTR down for the
specific queries rather than across the whole site.

**Confirms it** — Query-level CTR comparison shows the drop concentrated on queries where the SERP
changed, or the title and description were rewritten in the same window.

**Rules it out** — CTR fell uniformly across every query and every page. That points to a
site-wide or brand issue, or a GSC reporting change.

**Action** — Rewrite the title and description against the intent that now dominates the SERP.
**Fallback** — Add schema or content that qualifies the page for the SERP feature taking the clicks.

---

## 7. SERP or AI answer reduced click opportunity

**Signature** — Impressions stable or rising, CTR falling across the whole query set, and the SERP
now shows an AI Overview, featured snippet, or expanded pack above the organic results.

**Confirms it** — SERP capture shows the feature present now and absent in the earlier window,
and CTR decline correlates with which queries carry the feature.

**Rules it out** — SERP composition is unchanged.

**Action** — Compete for inclusion in the feature, and shift the page toward queries where the
click still exists. **Fallback** — Accept the reduced click rate and revalue the page on assisted
conversions or brand visibility rather than clicks.

Be careful here. This cause is fashionable and therefore over-diagnosed. Require a before-and-after
SERP observation, not an assumption that AI Overviews must be responsible.

---

## 8. Search demand declined

**Signature** — Impressions fall while position holds. Competitors ranking for the same terms fell
by a similar proportion. Keyword volume trend is down.

**Confirms it** — Demand trend for the head terms shows a sustained decline, and the drop is
category-wide rather than page-specific.

**Rules it out** — Competitors held or grew on the same terms.

**Action** — No content action. Reallocate effort. **Fallback** — Retarget the page at an adjacent
topic where demand is growing, if the page has authority worth preserving.

Reporting "no action needed" is a real and valuable outcome. Do not manufacture a task.

---

## 9. Content is outdated

**Signature** — No technical, demand, link, or SERP explanation. Gradual decline. Query data shows
searchers adding years, versions, or new entities the page never mentions.

**Confirms it** — Top-ranking pages cover entities, tools, or versions absent from the page, and
the page's own last meaningful update predates that shift.

**Rules it out** — The page already covers current entities and still declines. Look again at
rankings or links.

**Action** — Update against the specific gaps identified, not a generic refresh. **Fallback** —
Rewrite if the underlying structure no longer matches intent.

---

## 10. Insufficient evidence

Use this when the checks contradict each other or a required data source was unavailable.

State plainly which check would resolve it, for example "needs query-level GSC data for the
pre-decline window, which is outside the 16 month retention limit".

This is a legitimate answer. It is more useful than a confident label that sends someone to
rewrite a page that had a canonical problem.
