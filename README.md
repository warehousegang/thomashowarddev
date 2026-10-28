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
- `projects/` — project overview and six technical essays: `busynow/`, `nfl-predictor/`, `sally/`, `symphony/`, `ai-evaluation/`, and `referral-intelligence/`
- `blog/` — all writing and articles
- `styles.css` — shared theme, responsive layouts, and reading styles
- `terminal.js` — progressive typing animation for the homepage introduction
- `favicon.svg` — terminal icon

All content is ordinary HTML. When publishing an article, add it to the writing index; update the homepage's recent-writing cards as appropriate. Keep links relative to the current page and retain each article's existing URL.

## Deploy

Publish the repository as static files using the existing GitHub Pages configuration. `CNAME` preserves the `thomashoward.dev` custom domain. The site also works with any static host.

Project essays use the shared reading styles, local tables of contents, role and stage summaries, and HTML architecture diagrams. They are also listed in Writing. Keep project-stage descriptions grounded in source evidence: synthetic prototypes, local validation, prepared runtimes, and production deployments are different milestones.

The Fourth Down technical article retains its existing `/projects/nfl-predictor/` URL and section anchors. Its architecture, implemented capabilities, limitations, and 2023 validation table are grounded in the application artifacts; the prospective record is kept separate. The featured card now links to Fourth Down at `/fourth-down/`: a separately developed frozen-model application with upcoming forecasts, evaluation and research demonstrations. Referral Intelligence distinguishes its deterministic ranking service from the separate synthetic referral-completion modeling project. Update model-performance claims only when supported by measured results.

## Fourth Down static application

`fourth-down/` contains only the compiled application and its checksummed `release.json` receipt. Source, tests, model training and forecast generation stay in the separate Fourth Down repository. Its artifact installer replaces only this directory; the existing `main`/root Pages deployment and `CNAME` stay unchanged. Import a verified build, review the diff, then publish through the normal approved main-branch merge. Reverting the integration commits in reverse order restores the prior website; a squash publication can be rolled back by reverting its single merge commit. The pre-integration baseline is `0df446445f199b0e7f1329f5817b97b22cf7b1e8`. There is no cross-repository token or automatic publication job.

## NFL Forecast Lab concept

`projects/nfl-predictor/lab/` is an archived, responsive interface prototype linked from the Fourth Down article. Its archive banner points to the current application. The Lions–Packers pairing is an example, not the current schedule. Clicking **Run demo forecast** reveals hand-authored 62% / 38% values; it performs no inference. The page labels those values as illustrative before and after the click. No forecasts or user actions are persisted, and repeated demos never alter the empty public scorecard. The reveal respects reduced motion and exposes state through native buttons and a live region. Without JavaScript, the page explains that the interaction is unavailable.

Team-logo PNGs are vendored from ESPN's public team assets using URLs from nflverse's teams metadata: `https://github.com/nflverse/nflverse-data/releases/download/teams/teams_colors_logos.csv`. Original images: `https://a.espncdn.com/i/teamlogos/nfl/500/det.png` and `https://a.espncdn.com/i/teamlogos/nfl/500/gb.png`. These identify the teams; the project is independent of the NFL and the clubs.

### Current application and archived prototype

The real inference and lifecycle pipeline is implemented in Fourth Down, not in this archived lab. The article documents frozen-model inference, current-season ingestion, saved forecast receipts, reconciliation and evaluation. Injury/news context does not change probabilities; the research walkthrough is deterministic, not LLM-powered; no automatic retraining or prospective accuracy is claimed. The historical table is checked against `/fourth-down/data/demo.json` by the separate source repository's portfolio tests.

The portfolio has no active refresh workflow. Current artifacts expire honestly until a newly reviewed artifact is imported. The archive prototype remains illustrative and never contributes to the application's prospective record.

Article titles, summaries, and prose use natural punctuation without em dashes. Article pages and writing cards omit publication dates. Keep writing organized in the main Writing index for now; do not add date-based archive navigation. The former monthly archive URL redirects to Writing so existing links continue to work.

The essay `blog/when-to-use-machine-learning/` compares rules, forecasts, and decision policies using fictional banquet and sub-shop examples. Its three charts have desktop and mobile SVG variants, CSV data, and a reproducible Matplotlib source in `figures/`. All values are illustrative; the demand chart uses a known synthetic generating process, not a fitted model. The inventory chart evaluates explicitly stated demand scenarios and penalties. To regenerate the figures, use Python with matplotlib 3.10.7 and numpy 2.5.4 and run `python3 blog/when-to-use-machine-learning/figures/generate_figures.py`. The website itself has no new runtime dependencies.

## BusyNow public description

Founder of BusyNow, a live software product running on AWS ECS.

BusyNow helps people decide where to go by comparing nearby coffee shops, restaurants, and bars using crowd information, opening hours, and distance. It helps reduce the guesswork of choosing a place, while clearly showing when crowd information is recent, historical, or unavailable.

BusyNow currently runs on AWS ECS. Keep Kubernetes and Go as separate areas of engineering expertise and interest. The homepage, About, Projects, and dedicated BusyNow pages use `assets/busynow-logo.png`, the official PNG supplied by Thomas, unchanged. A light CSS background keeps its dark wordmark readable. This content update does not change BusyNow infrastructure or deployment.

The dedicated product and engineering writeup is `/projects/busynow/`. Homepage, Projects, About, Writing, and the GitHub profile link to that page. Preserve the About section anchor for existing bookmarks. The writeup explains the consumer decision, the comparison flow, evidence provenance and freshness, shared contracts, report integrity, provider controls, and ECS operation. Historical patterns and estimates are conditional; reduced uncertainty is the intended benefit, not a measured adoption or accuracy claim.
