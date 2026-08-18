# Agentic SEO Skills

Eight Claude Skills for running SEO and content work as agentic workflows rather than as prompts
you retype every week.

Each skill is a self-contained playbook: what data it needs, what order to work in, how to classify
what it finds, what the output has to look like, and where a human has to sign off before anything
changes. They are built to be run in a Claude Project with the relevant connectors attached, or in
Claude Code when the work touches local files, crawls, or a repository.

## The skills

| Skill | What it does | Needs a Semrush project? |
|---|---|---|
| [content-decline-diagnosis](skills/content-decline-diagnosis) | Finds pages losing meaningful organic traffic, classifies the likely cause, returns a prioritized update queue | No |
| [technical-seo-sprint-triage](skills/technical-seo-sprint-triage) | Collapses a site audit issue list into root causes, ranks by value, writes acceptance criteria | Yes, Site Audit |
| [competitor-growth-investigation](skills/competitor-growth-investigation) | Detects real competitor movement, isolates the pages and keywords behind it, recommends a response | Usually no |
| [search-opportunity-to-brief](skills/search-opportunity-to-brief) | Takes a seed topic to a decision-ready content brief with a differentiated angle | Usually no |
| [internal-linking-rescue](skills/internal-linking-rescue) | Finds internal links a reader would actually follow, plus orphans and structural link problems | Only if Semrush supplies the crawl |
| [content-portfolio-decisions](skills/content-portfolio-decisions) | Classifies every URL as keep, update, consolidate, redirect, remove, or investigate | Only for project-specific inputs |
| [ai-citation-influence-mapping](skills/ai-citation-influence-mapping) | Turns AI citation gaps into a realistic digital PR and contribution queue | No |
| [seo-release-regression-guard](skills/seo-release-regression-guard) | Diffs a site before and after a release, ranks regressions by traffic at risk, re-verifies fixes | Only if Semrush supplies the crawl |

Two skills ship with scripts, because the work is deterministic and reasoning over thousands of
rows in context is slow and inconsistent:

- `content-portfolio-decisions/scripts/portfolio_score.py` applies the decision rules to a CSV inventory
- `seo-release-regression-guard/scripts/crawl_diff.py` diffs two crawl exports into a ranked regression list

Both are stdlib-only Python 3, both report rather than change anything, and both accept
Screaming Frog, Sitebulb, and Semrush export headers.

## Prompts

Each skill has a matching workflow prompt in [prompts/](prompts). Fill the bracketed placeholders
and run. Prompts 6 and 8 call the bundled scripts and write CSV rather than pasting thousands of
rows into chat, and prompt 8 comes in two parts because re-verification needs the first run's
output saved.

## Design principles

These are what the skills have in common, and the reason they behave differently from a prompt.

**Diagnosis before prescription.** A page that lost rankings, a page that lost demand, and a page
that lost its canonical all look identical on a traffic chart and need completely different
responses. Every skill that touches a decline classifies the cause before recommending anything.

**Missing is not zero.** A blank conversions column means the data was not supplied, not that the
page converts nobody. Skills escalate on missing data rather than quietly deciding.

**Insufficient evidence is a valid answer.** So is "no action needed". A workflow that always finds
something to do will always find the wrong thing eventually.

**Relative and absolute thresholds together.** Percentage-only filters fill reports with pages that
went from four clicks to one.

**Humans hold the write access.** Analysis and reporting run unattended. Code, redirects, robots,
canonicals, sitemaps, publishing, deletions, and outreach all stop and wait for approval. This is
not a formality; it is the line that makes the rest safe to automate.

Full detail in [docs/conventions.md](docs/conventions.md).

## Install

Pick the path that matches where you work. All eight skills install together in every case.

### Claude Code

```bash
git clone https://github.com/crazylunatic007/agentic-seo-skills.git
mkdir -p ~/.claude/skills
cp -r agentic-seo-skills/skills/* ~/.claude/skills/
```

To scope them to one project instead of your whole machine, copy into `.claude/skills/`
inside that project directory.

For a single skill, copy just that folder:

```bash
cp -r agentic-seo-skills/skills/content-decline-diagnosis ~/.claude/skills/
```

### Claude Code, as a plugin

```bash
claude plugin marketplace add crazylunatic007/agentic-seo-skills
claude plugin install agentic-seo-skills@agentic-seo-skills
```

### Claude on the web or desktop

Skills upload as a zip of the skill folder, one per skill. Zip each folder under `skills/`,
then add it under Settings, Capabilities, Skills. The `dist/` folder in this repo contains
all eight already zipped and ready to upload.

```bash
cd agentic-seo-skills/skills
for d in */; do (cd "$d" && zip -qr "../../dist/${d%/}.zip" .); done
```

If Skills are not available on your plan, paste the contents of a SKILL.md into your Project
instructions instead. You lose the reference files and scripts, so prompts 6 and 8 will not work,
but the rest degrade gracefully.

### Verify the install

Ask Claude: `List the skills you currently have available.` All eight should come back by name.
If they do not, the folder is in the wrong place or the SKILL.md frontmatter did not parse.

## Connectors

The skills were written against this connector set and name real tools, so they work out of the box
if you have the same stack:

- **Google Search Console MCP** for actual performance, indexation, and sitemaps
- **Semrush MCP** for rankings, competitors, keywords, backlinks, and Site Audit
- **Firecrawl** for crawling and reading live pages
- **SerpAPI** for SERP features and AI Overviews
- **GA4** via the same Search Console MCP server (`analytics_advanced`) for engagement and conversions

If a connector is missing, each skill lists a substitute and instructs Claude to say which source it
actually used. None of them require the full set.

## Using them well

Start with a scope small enough to check. Run `content-decline-diagnosis` on one folder, read every
row, and correct the thresholds before pointing it at the whole site. The skills are opinionated
about defaults precisely so that you have something specific to disagree with.

They compose. A `content-portfolio-decisions` run that returns `Update` for forty URLs is the input
to `content-decline-diagnosis`, which tells you why each one declined, which is the input to
`search-opportunity-to-brief` for the ones worth rewriting.

## Contributing

The thresholds and taxonomies here are defaults from one set of sites. If yours behave differently,
the reference files are the place to change them, and the SKILL.md files should mostly stay as they
are. Issues and pull requests welcome, particularly ones that add a decline cause, a growth driver,
or a regression check that the current lists miss.

## License

MIT. See [LICENSE](LICENSE).
