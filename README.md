# thomashoward.dev

Thomas Howard's personal website: applied AI, agentic solutions architecture, conversational agents, evaluation, and healthcare decision support.

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
- `projects/` — project overview and five technical essays: `nfl-predictor/`, `sally/`, `symphony/`, `ai-evaluation/`, and `referral-intelligence/`
- `blog/` — all writing and articles
- `styles.css` — shared theme, responsive layouts, and reading styles
- `terminal.js` — progressive typing animation for the homepage introduction
- `favicon.svg` — terminal icon

All content is ordinary HTML. When publishing an article, add it to the writing index; update the homepage's recent-writing cards as appropriate. Keep links relative to the current page and retain each article's existing URL.

## Deploy

Publish the repository as static files using the existing GitHub Pages configuration. `CNAME` preserves the `thomashoward.dev` custom domain. The site also works with any static host.

Project essays use the shared reading styles, local tables of contents, role and stage summaries, and HTML architecture diagrams. They are also listed in Writing. Keep project-stage descriptions grounded in source evidence: synthetic prototypes, local validation, prepared runtimes, and production deployments are different milestones.

NFL Predictor documents an early predictive ML project: data exploration is implemented, with baseline evaluation and model training still ahead. Referral Intelligence distinguishes its deterministic ranking service from the separate synthetic referral-completion modeling project. Update model-performance claims only when supported by measured results.

## NFL Forecast Lab concept

`projects/nfl-predictor/lab/` is a responsive, framework-free interactive concept linked from the homepage, Projects, and the NFL essay. The Lions–Packers pairing is an example, not the current schedule. Clicking **Run demo forecast** reveals hand-authored 62% / 38% values; it performs no inference. The page labels those values as illustrative before and after the click. No forecasts or user actions are persisted, and repeated demos never alter the empty public scorecard. The reveal respects reduced motion and exposes state through native buttons and a live region. Without JavaScript, the page explains that the interaction is unavailable.

Team-logo PNGs are vendored from ESPN's public team assets using URLs from nflverse's teams metadata: `https://github.com/nflverse/nflverse-data/releases/download/teams/teams_colors_logos.csv`. Original images: `https://a.espncdn.com/i/teamlogos/nfl/500/det.png` and `https://a.espncdn.com/i/teamlogos/nfl/500/gb.png`. These identify the teams; the project is independent of the NFL and the clubs.

### Connecting the real model later

- Finish baseline evaluation and out-of-time model validation before displaying live probabilities. Establish a tie policy; the initial experiment excludes tied games.
- Start with one featured game per week, chosen before kickoff. A trained-model job can export versioned JSON to this static site; visitor clicks should reveal the same saved forecast, not retrain the model or mutate its record.
- Each forecast needs a stable game ID, teams, season/week, kickoff timestamp, prediction timestamp, feature cutoff, model version, probabilities, and baseline probabilities. Preserve the pre-kickoff record; corrections or later forecasts need separate versions.
- Ingest final results separately, distinguish pending/postponed/canceled/tied games, and settle only eligible completed games. Retain losses as well as wins. Show the denominator and evaluate the baseline on exactly the same featured games.
- Keep historical holdout metrics separate from the prospective weekly record. Pick accuracy is one view; probability scores and, with sufficient observations, calibration provide another. The model output is authoritative; an eventual explanation agent should not invent new probabilities.

No model service, schedule feed, results job, recurring automation, or public deployment is configured by this concept.

Article titles, summaries, and prose use natural punctuation without em dashes. Article pages and writing cards omit publication dates. Keep writing organized in the main Writing index for now; do not add date-based archive navigation. The former monthly archive URL redirects to Writing so existing links continue to work.

The essay `blog/when-to-use-machine-learning/` compares rules, forecasts, and decision policies using fictional banquet and sub-shop examples. Its three charts have desktop and mobile SVG variants, CSV data, and a reproducible Matplotlib source in `figures/`. All values are illustrative; the demand chart uses a known synthetic generating process, not a fitted model. The inventory chart evaluates explicitly stated demand scenarios and penalties. To regenerate the figures, use Python with matplotlib 3.10.7 and numpy 2.5.4 and run `python3 blog/when-to-use-machine-learning/figures/generate_figures.py`. The website itself has no new runtime dependencies.
