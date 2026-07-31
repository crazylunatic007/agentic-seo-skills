# Workflow prompts

One prompt per skill. Fill the bracketed placeholders before running, and start with a scope
small enough that you can read every row of the output.

| # | Prompt | Skill |
|---|---|---|
| 1 | [Diagnose declining content](1-content-decline-diagnosis.md) | `content-decline-diagnosis` |
| 2 | [Site audit to sprint backlog](2-technical-seo-sprint-triage.md) | `technical-seo-sprint-triage` |
| 3 | [Investigate competitor spikes](3-competitor-growth-investigation.md) | `competitor-growth-investigation` |
| 4 | [Opportunity to content brief](4-search-opportunity-to-brief.md) | `search-opportunity-to-brief` |
| 5 | [Internal links and orphans](5-internal-linking-rescue.md) | `internal-linking-rescue` |
| 6 | [Content portfolio decisions](6-content-portfolio-decisions.md) | `content-portfolio-decisions` |
| 7 | [AI citation gaps to PR queue](7-ai-citation-influence-mapping.md) | `ai-citation-influence-mapping` |
| 8 | [Release regression check](8-seo-release-regression-guard.md) | `seo-release-regression-guard` |

## Notes

**Prompts 6 and 8 call scripts.** They tell Claude to run `portfolio_score.py` and
`crawl_diff.py` and to save full output as CSV rather than pasting thousands of rows into chat.
Running those workflows without the scripts on a real site will be slow and inconsistent.

**Prompt 8 comes in two parts.** The main run produces a report and saves it. The
re-verification prompt at the bottom loads that report back and checks each item against its
recorded acceptance criteria. Skipping the save means the second run has nothing to check against.

**Search Console retains 16 rolling months.** Prompt 1 pins a 90-day window compared year over
year, which fits. Longer windows compared year over year will run past the wall.

**Exclusions have to be explicit.** Claude cannot tell which of your URLs are seasonal campaigns
or discontinued products from Search Console and Semrush alone. Give it patterns or a list. The
prompts instruct it to flag rather than guess.
