# thomashoward.dev

Thomas Howard's personal website: projects and writing on applied AI, autonomous engineering, leadership, and production systems.

A framework-free static site with a terminal-inspired dark theme. No build step, remote fonts, or package dependencies are required. A small JavaScript enhancement types the homepage name and introduction on page load, updating one text node per line. A head-level loading state prevents the full text from flashing before typing starts. Without JavaScript, with reduced motion, or if the animation script fails to load, the full introduction remains readable. Mobile navigation uses native HTML disclosure controls.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Structure

- `index.html` — terminal introduction, featured work, and recent writing
- `about/` — biography and engineering interests
- `projects/` — selected projects
- `blog/` — all writing, articles, and monthly archives
- `styles.css` — shared theme, responsive layouts, and reading styles
- `terminal.js` — progressive typing animation for the homepage introduction
- `favicon.svg` — terminal icon

All content is ordinary HTML. When publishing an article, add it to the writing index and its monthly archive; update the homepage's recent-writing cards as appropriate. Keep links relative to the current page and retain each article's existing URL.

## Deploy

Publish the repository as static files using the existing GitHub Pages configuration. `CNAME` preserves the `thomashoward.dev` custom domain. The site also works with any static host.
