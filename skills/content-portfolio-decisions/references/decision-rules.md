# Decision rules

Rules are ordered. The first rule that matches wins, which is why protective rules come first.

Thresholds are defaults for a mid-sized content library. Scale them to the site: a threshold of
100 clicks a year is meaningless on a site where the median page earns 10,000.

## Signals

| Signal | Source | Notes |
|---|---|---|
| Clicks, current window | GSC | Absolute, not relative |
| Clicks, prior window | GSC | For trend direction |
| Impressions and average position | GSC | Catches pages with potential but no clicks |
| Ranking keyword count | Semrush | Coverage breadth |
| Referring domains | Backlink tool | The single most protective signal |
| Conversions or assisted conversions | GA4 | Ask for it. Do not assume zero |
| Last meaningful update | CMS | Publish date alone is misleading |
| Indexable | Crawl or inspection | A noindexed page with traffic is a data error worth checking |
| Topic overlap | Query overlap plus content similarity | Needs a named counterpart URL |
| Strategic flag | The user's business rules | Set before the audit runs, not after |
| Citations | AI citation export, press, academic | Often invisible in every other signal |

## Rules

**R1 — Protected**
Page carries a strategic flag, legal or compliance importance, meaningful referring domains, or
recorded conversions.
→ `Investigate`, with the protecting signal named. Never `Remove`.

**R2 — Missing critical data**
Conversions or backlink data unavailable for this URL and the page is otherwise a removal or
redirect candidate.
→ `Investigate`. Do not treat missing as zero.

**R3 — Performing**
Clicks above the site's meaningful floor and stable or growing.
→ `Keep`.

**R4 — Declining with a foundation**
Clicks down materially year over year, but the page still holds ranking keywords, links, or
impressions at a recoverable position.
→ `Update`. Pair with the content decline diagnosis skill to establish why before scoping the work.

**R5 — Overlapping**
Substantial query overlap with a stronger URL on the same domain, and the two pages serve the same
intent.
→ `Consolidate` into the stronger URL. Name the destination. If the destination is unclear or both
pages are weak, escalate instead.

This is checked before unrealised potential on purpose. A page stuck at position 14 is often stuck
because another page on the same domain is competing with it, and calling that an update
opportunity treats the symptom.

**R6 — Unrealised potential**
Low clicks but meaningful impressions at positions 8 to 20, on a topic that matters, with no
overlapping counterpart.
→ `Update`.

**R7 — Dead but inherited value**
No traffic, no rankings, no conversions, but has referring domains or historical significance, and
a genuine topical equivalent exists.
→ `Redirect` to that equivalent. If no genuine equivalent exists, do not redirect to the homepage
or a category page as a default. Escalate.

**R8 — Genuinely dead**
No traffic, no impressions worth noting, no rankings, no links, no conversions, no strategic role,
outdated content, and no redirect target.
→ `Remove`.

**R9 — Anything else**
→ `Investigate`, with a note on which signal is ambiguous.

## Conflicting signals

Record the conflict rather than resolving it silently. Common ones:

| Conflict | Why it matters |
|---|---|
| High links, no traffic | Redirect candidate, never a removal candidate |
| High traffic, no conversions | May be top-of-funnel by design, or may be attracting the wrong audience |
| Recently updated, still declining | The update did not address the actual cause |
| High impressions, near-zero CTR | Ranking for the wrong intent, or losing clicks to a SERP feature |
| Noindexed but receiving clicks | Data reconciliation problem. Check before acting |
| Old and untouched but stable | Evergreen. Leave it alone rather than refreshing it for the sake of a date |

The last one is worth stating explicitly to the user. A stable old page is often stable because it
is right, and updating it to change the visible date is a common way to break something that works.

## Consolidation and redirect validation

Before recommending either, confirm:

- The destination URL exists and returns 200.
- The destination genuinely serves the same intent. Similar topic is not sufficient.
- The destination is not itself a removal or redirect candidate.
- The redirect will not create a chain with an existing rule.
- Any content worth keeping from the source is identified specifically, so it survives the merge.

A redirect to a broadly related category page is usually a soft 404 in practice. If nothing
genuinely equivalent exists, say so and let a person decide between leaving the page in place and
accepting the loss.
