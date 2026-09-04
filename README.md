# thomashoward.dev

A deliberately simple static site for Thomas Howard's writing on platform engineering, Kubernetes, AI, and production systems.

## Local preview

From the repository root:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000

## Structure

- `index.html` — homepage
- `about/` — about page
- `blog/` — writing index
- `blog/why-im-building-an-engineering-os/` — first article
- `styles.css` — site-wide styles

## Deploy

This site is intentionally framework-free and can be hosted on GitHub Pages, Cloudflare Pages, Netlify, or any static web host.
