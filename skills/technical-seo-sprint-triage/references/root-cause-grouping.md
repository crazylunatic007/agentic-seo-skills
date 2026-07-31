# Root cause grouping, fix types, and scoring

## Grouping heuristics

Before treating a set of flagged URLs as one issue, test whether they share:

1. **A path pattern** — `/blog/*`, `/product/*/reviews`. Strong signal of a template cause.
2. **A content type or CMS template** — same layout, same partial, same component.
3. **A generation source** — paginated series, faceted navigation, tag archives, programmatic pages.
4. **A rendering path** — client-rendered pages flagged for missing content usually share a
   component, not a content problem.
5. **A single upstream directive** — one robots rule or one canonical rule can produce thousands
   of downstream rows.

If they share none of these, the issue is genuinely page-level and should be scoped by value
rather than fixed exhaustively.

Common collapses worth checking explicitly:

| Reported as | Often actually |
|---|---|
| Thousands of duplicate titles | One template not interpolating a variable |
| Thousands of missing meta descriptions | Template has no field, or the CMS field is optional |
| Large redirect chain count | Two rules stacking, e.g. protocol plus trailing slash |
| Widespread thin content | Faceted or paginated URLs that should not be indexable |
| Many 4xx internal links | One shared nav, footer, or sidebar module |
| Orphan pages | Missing hub or listing page, not missing links on individual pages |

## Fix types

| Type | Meaning | Typical owner |
|---|---|---|
| Template | One change in a layout or component fixes every affected URL | Frontend engineering |
| Page | Each URL needs individual attention | Content or SEO |
| Configuration | CDN, server, robots, sitemap, or CMS setting | DevOps or platform |
| Infrastructure | Rendering, performance, hosting, or architecture | Engineering, usually multi-sprint |
| Investigative | Cause is not yet known; the deliverable is an answer, not a fix | SEO |

Investigative items are legitimate sprint items. Do not disguise an unknown as a fix.

## Impact scoring

Score on value at risk, not issue count.

| Impact | Criteria |
|---|---|
| High | Affects indexation or ranking of URLs carrying meaningful traffic or revenue, or blocks a launch |
| Medium | Affects URLs with ranking potential but little current traffic, or degrades crawl efficiency at scale |
| Low | Cosmetic, or affects URLs with no traffic and no strategic role |

## Effort scoring

| Effort | Criteria |
|---|---|
| S | Single config or template change, no dependencies, under half a day |
| M | Template change with testing, or a bounded content batch, one to three days |
| L | Cross-team, needs design or backend changes, or touches routing and redirects |
| XL | Architectural, spans multiple sprints, needs its own plan |

Effort is the developer's estimate, not the SEO's hope. Where genuinely unsure, mark it and say so
rather than guessing low to get it into the sprint.

## Confidence

Confidence describes whether the fix produces the expected outcome, separately from whether the
issue is real.

- **High** — directive, status code, and sitemap fixes with a directly observable mechanism.
- **Medium** — internal linking, structured data, and template content changes.
- **Low** — anything whose payoff depends on re-evaluation, competition, or ranking movement.

A High-impact, Low-confidence item is still worth doing, but should be framed as an experiment
with a measurement window rather than a guaranteed win.
