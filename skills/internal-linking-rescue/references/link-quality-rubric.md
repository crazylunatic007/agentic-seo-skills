# Link quality rubric

Apply to every candidate before it reaches the output table. Recommendations that fail any hard
test are dropped, not downgraded.

## Hard tests

**1. Reader continuity**
Would someone reading this specific passage plausibly want the destination next? If the link only
makes sense to someone thinking about site architecture, it fails.

**2. Topical genuineness**
The passage discusses the destination's subject, not merely a word that appears in its title.
"Analytics" appearing in a sentence about web analytics does not justify a link to a page about
analyst relations.

**3. Non-duplication**
The source does not already link to the destination in a comparable position. A second link to the
same destination from the same page is almost never worth it.

**4. Placement viability**
There is a real sentence or section where the link fits. If the recommendation requires inserting a
new sentence purely to host the link, it fails. The exception is when the new sentence adds
information the reader wanted anyway, in which case say that explicitly.

## Scoring the survivors

Rank remaining candidates on source value and fit strength.

**Source value**

| Level | Criteria |
|---|---|
| High | Page earns meaningful organic traffic, ranks well, or holds external links |
| Medium | Page ranks but earns little traffic, or is topically central without performance |
| Low | Page has no traffic, no links, and no rankings |

Low-value sources are not worthless, but twenty links from low-value pages will not do what two
links from high-value pages do. Order accordingly.

**Fit strength**

| Level | Criteria |
|---|---|
| Strong | The passage raises a question the destination answers directly |
| Moderate | Same topic area, useful but not required by the reader at that moment |
| Weak | Related category only |

Weak fit does not ship regardless of source value.

## Anchor guidance

- Descriptive over exact-match. "How CTR is calculated in Search Console" beats "CTR".
- Vary anchors across recommendations pointing at the same destination. Identical anchors repeated
  site-wide is the clearest engineered-linking signal there is.
- Anchor text must read naturally in the sentence as written. If the sentence has to be contorted
  to accommodate the anchor, rewrite the anchor rather than the sentence.
- Avoid "click here", "read more", and bare URLs. They tell the reader and the crawler nothing.

## Structural issues worth flagging

| Issue | Why it matters | Usual fix |
|---|---|---|
| Orphan page | Receives no internal links, so it depends entirely on the sitemap for discovery | Add it to the relevant hub or listing page |
| Broken internal link | Wastes crawl and drops the reader | Update or remove the link |
| Excessive internal links | Dilutes the signal and degrades readability | Prune to the links that serve the reader |
| Linked only from footers, tags, or paginated archives | Site-wide boilerplate links carry little weight and no context | Add contextual links from relevant body content |
| Deep click depth on a valuable page | Distance from the homepage correlates with weaker discovery | Shorten the path via a hub page |

Report these separately from the contextual recommendations. They are a different kind of fix,
usually owned by a different person, and mixing them into one list means neither gets done.
