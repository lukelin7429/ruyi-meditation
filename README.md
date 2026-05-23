# Ru-Yi Meditation Center — Website

The English-language website of Ru-Yi Meditation Center (南投信義鄉如意禪修中心), built as a Jekyll site served from GitHub Pages.

- Live (preview): https://lukelin7429.github.io/ruyi-meditation/
- Target production domain: `ruyimeditation.org` (after DNS cutover from GoDaddy Website Builder)

## Structure

```
ruyi-meditation/
├── _config.yml              site metadata + Jekyll config
├── _layouts/                default, column, discourse layouts
├── _includes/               header, footer, etc.
├── _columns/                Luke + guest author columns (markdown collection)
├── _discourses/             Pali Canon discourse pages (collection)
├── assets/
│   ├── css/style.css        design system
│   └── images/
├── index.html               homepage
├── about/index.html         team & founders
├── columns/index.html       column listing (auto from collection)
└── discourses/index.html    Discourses landing (Majjhima Nikāya for now)
```

## Content sources

- Columns: imported from Obsidian vault `組織事務/Ru-Yi Meditation Center/Columns/` (Phase 2 migration 2026-05-23). 60 articles by Luke Lin, Jennafer Duerden, Emily Hogle, Quentin Gooch.
- Discourses (MN 1-9): canonical version lives on academy.ruyimeditation.org; this site currently links out and will absorb the content when the two sites merge.

## Conventions

- Style: white background, saffron accent (#C9521F), serif headlines, sans body
- Tone: "Plain English, no jargon hidden" (matches academy brand voice)
- No Christian/angel imagery; subtle East Asian temple aesthetic
- Buddhist terms get parenthetical Pali on first mention, not as primary label

## Local preview

```bash
bundle exec jekyll serve
# or
jekyll serve
```

## Deploy

Pushing to `main` triggers GitHub Pages build automatically. No GitHub Actions needed (uses Pages' built-in Jekyll).
