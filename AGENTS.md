# Repository Guidelines

## Project Structure & Module Organization
- Source: `_pages/` (static pages), `_posts/` (blog posts), `_news/` (updates), `_projects/` (projects), `assets/` (images, css, js), `_data/` (YAML data), `_includes/` (partials), `_layouts/` (templates), `_sass/` (styles), `_plugins/` (Jekyll plugins), `_bibliography/` (BibTeX).
- Config: `_config.yml` controls site/global options. Build output goes to `_site/` (generated).

## Build, Test, and Development Commands
- Install deps: `bundle install` (Ruby), optional: `npm i -g purgecss` for CSS pruning.
- Local dev: `bundle exec jekyll serve --livereload` then open `http://localhost:4000`.
- Production build: `JEKYLL_ENV=production bundle exec jekyll build --lsi`.
- Docker (no local Ruby): `docker-compose up` then open `http://localhost:8080`.
- Optional CSS prune after build: `purgecss -c purgecss.config.js` (expects `_site/` present).

## Coding Style & Naming Conventions
- Markdown + Liquid: prefer readable Markdown; keep Liquid filters simple in pages, move snippets to `_includes/`.
- Front matter: use YAML with minimal keys (`title`, `date`, `layout`, `tags`, `categories`).
- Indentation: 2 spaces for YAML, HTML/Liquid, and SCSS.
- Filenames: posts/news as `YYYY-MM-DD-title.md` in `_posts/` and `_news/`. Pages live in `_pages/` with dashed-lowercase names.
- Assets: place under `assets/` and reference with `{{ '/assets/...' | relative_url }}`.

## Testing Guidelines
- Sanity checks: `bundle exec jekyll doctor` and a full `build` before pushing; fix warnings/errors.
- Visual check: run `serve` locally and click through new/changed pages.
- Lint basics: `pre-commit install && pre-commit run -a` (trailing whitespace, EOF, YAML checks).

## Commit & Pull Request Guidelines
- Commits: concise, imperative summaries (e.g., "fix: correct navbar link", "content(post): add UCSB recap"). Group related changes.
- PRs: include a short description, screenshots or links for visual changes, and reference related issues. Ensure local build is clean and CI green.

## Security & Configuration Tips
- Do not commit secrets. Site settings live in `_config.yml`; review diffs carefully.
- CI deploy (see `.github/workflows/deploy.yml`) builds with `--lsi` and runs PurgeCSS. Keep local builds aligned with CI for predictable output.
