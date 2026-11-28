# thomashoward.dev

Thomas Howard's personal website: applied AI, agentic solutions architecture, conversational agents, evaluation, healthcare decision support, and BusyNow.

A framework-free static site with a terminal-inspired dark theme. No build step, remote fonts, or package dependencies are required. A small JavaScript enhancement types the homepage name and introduction on page load, updating one text node per line. A head-level loading state prevents the full text from flashing before typing starts. Without JavaScript, with reduced motion, or if the animation script fails to load, the full introduction remains readable. Mobile navigation uses native HTML disclosure controls.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Structure

- `index.html` — terminal introduction, featured work, and recent writing
- `about/` — applied AI experience and approach to solutions architecture
- `resume/` — readable résumé in the site’s dark terminal theme, with green headings, section navigation, and a green PDF download button
- `projects/` — project overview and five technical essays: `busynow/`, `sally/`, `symphony/`, `ai-evaluation/`, and `referral-intelligence/`
- `blog/` — essays and long-form writing
- `notes/` — shorter frontier notes, linked as Notes in the main navigation. Each note lives at `notes/<slug>/`; add new notes to the top of `notes/index.html`. Notes stay off the homepage and the Writing index. `blog/the-model-did-nothing-wrong/` redirects to the note's new URL.
- `styles.css` — shared theme, responsive layouts, and reading styles
- `terminal.js` — progressive typing animation for the homepage introduction
- `favicon.svg` — terminal icon

All content is ordinary HTML. When publishing an article, add it to the writing index; update the homepage's recent-writing cards as appropriate. Keep links relative to the current page and retain each article's existing URL.

## Deploy

Publish the repository as static files using the existing GitHub Pages configuration. `CNAME` preserves the `thomashoward.dev` custom domain. The site also works with any static host.

Project essays use the shared reading styles, local tables of contents, role and stage summaries, and HTML architecture diagrams. They are also listed in Writing. Keep project-stage descriptions grounded in source evidence: synthetic prototypes, local validation, prepared runtimes, and production deployments are different milestones.

Referral Intelligence distinguishes its deterministic ranking service from the separate synthetic referral-completion modeling project. Update model-performance claims only when supported by measured results.

## Retired project

Fourth Down was removed from the public portfolio at the owner’s request on November 27, 2026. Its compiled application, technical article, prototype and refresh workflow are no longer published. The V1 Cloudflare cron triggers were removed and its GitHub refresh workflow was disabled. The source repository and the retained `.fourth-down-state/` evidence remain available; the full former site is recoverable from Git commit `d454513c75d0caa19911d8bc2cd5032f835621b2`. Do not restore automatic publication without a new owner request.

Article titles, summaries, and prose use natural punctuation without em dashes. Article pages and writing cards omit publication dates. Keep writing organized in the main Writing index for now; do not add date-based archive navigation. The former monthly archive URL redirects to Writing so existing links continue to work.

The essay `blog/when-to-use-machine-learning/` compares rules, forecasts, and decision policies using fictional banquet and sub-shop examples. Its three charts have desktop and mobile SVG variants, CSV data, and a reproducible Matplotlib source in `figures/`. All values are illustrative; the demand chart uses a known synthetic generating process, not a fitted model. The inventory chart evaluates explicitly stated demand scenarios and penalties. To regenerate the figures, use Python with matplotlib 3.10.7 and numpy 2.5.4 and run `python3 blog/when-to-use-machine-learning/figures/generate_figures.py`. The website itself has no new runtime dependencies.

## BusyNow public description

Founder of BusyNow, helping people see what’s busy nearby before heading out.

It helps reduce the guesswork of choosing a place, while clearly showing when crowd information is recent, historical, or unavailable.

Public introductions describe the consumer problem BusyNow helps solve. Keep hosting details in the dedicated technical architecture and operations sections, not in founder taglines, summaries, or project-card badges. BusyNow currently runs on AWS ECS. Keep Kubernetes and Go as separate areas of engineering expertise and interest. The homepage, About, Projects, and dedicated BusyNow pages use `assets/busynow-logo.png`, the official PNG supplied by Thomas, unchanged. A light CSS background keeps its dark wordmark readable. This content update does not change BusyNow infrastructure or deployment.

The dedicated product and engineering writeup is `/projects/busynow/`. Homepage, Projects, About, Writing, and the GitHub profile link to that page. Preserve the About section anchor for existing bookmarks. The writeup explains the consumer decision, the comparison flow, evidence provenance and freshness, shared contracts, report integrity, provider controls, and ECS operation. Historical patterns and estimates are conditional; reduced uncertainty is the intended benefit, not a measured adoption or accuracy claim.
