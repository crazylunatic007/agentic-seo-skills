# Acceptance criteria patterns

Acceptance criteria exist so that the person who deploys the fix can verify it without asking an
SEO, and so that a regression check has something concrete to test against.

Each criterion needs: the scope, the expected state, and the verification method.

## Patterns

**Directive fixes**
> All URLs matching `/guides/*` return a self-referencing canonical. Verified by inspecting 20
> sampled URLs post-deploy and confirming zero cross-canonical results.

**Status codes and redirects**
> No internal link on the site returns a 3xx or 4xx. Verified by a post-deploy crawl of the same
> scope showing zero internal 3xx and 4xx, down from 412.

**Robots and indexability**
> `/search` and `/*?filter=` are disallowed in robots.txt, and no URL matching those patterns
> appears in the XML sitemap. Verified by fetching robots.txt and grepping the sitemap.

**Template content**
> Every product page renders a unique title in the form `{product} | {category} | {brand}`.
> Verified by crawling 100 product URLs and confirming zero duplicates.

**Structured data**
> All article pages emit valid Article schema with headline, datePublished, and author.
> Verified by running schema validation on 10 sampled URLs with zero errors.

**Performance**
> LCP at the 75th percentile for the template is under 2.5s on mobile. Verified by Core Web Vitals
> field data 28 days after deploy, with lab data used only as an interim signal.

**Investigative items**
> A written answer stating why 3,200 URLs under `/tag/` are indexed, whether they should be, and a
> recommendation. Not a code change.

## Anti-patterns

- "Fix canonicals" — no scope, no verification.
- "Improve page speed" — no target, no measurement point.
- "Reduce crawl errors" — no threshold.
- "Follow SEO best practice" — not checkable by anyone.
- Criteria that can only be verified weeks later by ranking movement. Rankings are an outcome, not
  an acceptance test. Test the implementation; measure the outcome separately.
