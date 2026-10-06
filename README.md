# Sitek Lab website

This repo is Kevin Sitek's future lab website, built on the [al-folio](https://github.com/alshedivat/al-folio)
Jekyll starter. The lab opens January 2027 in the Department of Speech, Language, and Hearing, School of
Behavioral and Brain Sciences, at UT Dallas. **The lab doesn't have an official name yet**, so the repo, site
title, and URL currently use "Sitek Lab" / `siteklab.github.io` as placeholders.

See [About the al-folio starter](#about-the-al-folio-starter) below for links to the upstream project and its
documentation.

## Renaming the lab

When an official lab name is chosen, update all of the following together:

1. **GitHub repo name** — rename `siteklab.github.io` to `<new-name>.github.io` (repo Settings → rename). GitHub
   automatically redirects the old repo name for a while, but update any external links (CV, faculty page, social
   profiles) to the new URL.
2. **`_config.yml`** — `title`, `url` (and `baseurl` stays `""`).
3. **`_data/cv.yml`** — `label` field (currently "Principal Investigator, Sitek Lab").
4. **Content mentioning "Sitek Lab"** — search for the literal string across `_pages/`, `_news/`, and this README;
   as of this writing it's isolated to `_pages/about.md`, `_pages/profiles.md`, `_news/announcement_1.md`, and this
   file. Each spot is marked with a `PLACEHOLDER` comment.

## Before going live

**Identity & branding**

- [ ] Lab name is still a placeholder ("Sitek Lab") — see "Renaming the lab" above.
- [x] ~~Contact email is a placeholder~~ — updated to `kevin.sitek@utdallas.edu`.
- [x] ~~No CV PDF set~~ — `_pages/cv.md` `cv_pdf:` links to the rendercv PDF on sitek.github.io.

**Data integrity**

- [x] ~~Fabricated bibliography author names/titles~~ — fixed; every entry verified against Crossref.
- [x] ~~No way to catch this again~~ — `bin/verify_bibliography.py` checks `_bibliography/papers.bib` entries
      against Crossref; run it after adding or editing entries.
- [ ] `_data/coauthors.yml` still has al-folio's demo (Einstein-era) data — regenerate or remove.
- [ ] `_data/citations.yml` — confirm it's fully real data from `bin/update_scholar_citations.py`, not a demo/live
      mix.
- [ ] Audit `_news/`, `_projects/`, `_teachings/`, `_pages/pi_bio.md` for other fabricated-but-plausible details —
      only the bibliography has been checked so far.
- [ ] More publications can be added to `_bibliography/papers.bib`; currently ports the preprints + peer-reviewed
      papers from Kevin's personal site, not the full conference-abstract list.
- [ ] Additional lab members: duplicate a profile block in `_pages/profiles.md` (image + a new
      `_pages/<name>_bio.md` content file) as people join.

**Hosting & deployment**

- [x] ~~Deploy workflow didn't match the Pages source~~ — switched to native GitHub Actions deploy.
- [x] ~~`baseurl` mismatch causing 404s~~ — fixed; site is served at the `/siteklab.github.io` subpath.
- [x] ~~Old `gh-pages` branch~~ — deleted (unused now that deploy is Actions-native).
- [ ] Repo is private — confirm your GitHub plan actually supports private-repo Pages long-term, or decide whether
      to make the repo public.
- [ ] Current URL is the subpath `sitek.github.io/siteklab.github.io/` — decide if that's acceptable long-term vs.
      renaming the repo or adding a custom domain.
- [ ] Custom domain — not set up yet.

**CI / test infrastructure**

- [x] ~~`test/` directory missing, `lint:style-contract` broken~~ — restored from upstream al-folio.
- [x] ~~`unit-tests.yml`, `prettier.yml`, `upgrade-check.yml` missing~~ — restored.
- [x] ~~`update-tocs.yml`, `visual-regression.yml` missing~~ — evaluated and deliberately **not** restored: both are
      upstream-al-folio-project concerns (contributor-docs TOC maintenance, and pixel-diff parity against a
      pre-v1.x architecture baseline) that don't apply to a downstream single-owner site.
- [ ] First real run of `unit-tests.yml` hasn't been confirmed green in CI yet.

**Integrations not yet configured**

- [ ] Giscus comments: `repo_id` and `category_id` are empty in `_config.yml` — set up at giscus.app.
- [ ] No analytics configured (Google/Cronitor/Pirsch/Openpanel/Cloudflare all empty in `_config.yml`).
- [ ] No Google/Bing site verification set.

**Final verification**

- [ ] `axe.yml` accessibility check hasn't been run yet (it's `workflow_dispatch`-only, not automatic).
- [ ] `apple_touch_icon` still unset — just the 🧠 emoji favicon, no real image for iOS bookmarks.

## Local development

```bash
bundle install
bundle exec jekyll serve   # → http://localhost:4000/siteklab.github.io/
```

---

## About the al-folio starter

This site's starter wiring, layouts, and plugin runtime come from [al-folio](https://github.com/alshedivat/al-folio),
a Jekyll starter for academic websites — see that repo for installation, customization, and plugin-ecosystem docs
that aren't specific to this site. This repo also carries its own local copies of the same architecture docs
(`AGENTS.md`, [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/BOUNDARIES.md](docs/BOUNDARIES.md)) for coding
agents working on this site.

- [al-folio repository](https://github.com/alshedivat/al-folio)
- [al-folio documentation index](https://github.com/alshedivat/al-folio/blob/main/docs/README.md)
- [al-org-dev](https://github.com/al-org-dev) — organization publishing al-folio's plugin gems

## License

This site is released under the same [MIT License](LICENSE) as al-folio.
