# Speech and Hearing Pathways Lab website

This repo is the website for Kevin Sitek's **Speech and Hearing Pathways Lab**, built on the
[al-folio](https://github.com/alshedivat/al-folio) Jekyll starter. The lab opens January 2027 in the Department of
Speech, Language, and Hearing, School of Behavioral and Brain Sciences, at UT Dallas.

The site is served at **https://siteklab.github.io** from the `siteklab` GitHub organization. Because the repo name
matches `<owner>.github.io`, it's an org root site and `baseurl` in `_config.yml` is `""`.

See [About the al-folio starter](#about-the-al-folio-starter) below for links to the upstream project and its
documentation.

## Before going live

**Identity & branding**

- [x] ~~Lab name is still a placeholder~~ — now the Speech and Hearing Pathways Lab.
- [x] ~~Contact email is a placeholder~~ — updated to `kevin.sitek@utdallas.edu`.
- [x] ~~No link preview image~~ — `og_image` is the Callier Center Dallas photo; a lab logo could replace it.
- [x] ~~No CV PDF set~~ — no CV page; the PI bio (`_pages/pi_bio.md`) links to the rendercv PDF on sitek.github.io.

**Socials** (links live in `_data/socials.yml`)

- [x] ~~GitHub~~ — links to the `siteklab` org.
- [x] ~~Bluesky account~~ — created as `siteklab.bsky.social` and linked.
- [ ] Bluesky — populate it (display name, avatar, bio, first posts).
- [ ] LinkedIn — create and populate a lab page, then add `linkedin_username` to `_data/socials.yml`.
- [ ] Mastodon — create and populate a lab account; `_data/socials.yml` still links Kevin's personal
      `sitek@fediscience.org`.
- [ ] ResearchGate — create and populate a lab page; `_data/socials.yml` still links Kevin's personal profile.
- [ ] Lab email address — can't create until January 2027; then replace `kevin.sitek@utdallas.edu` in
      `_data/socials.yml` and `_pages/join.md` if contact should go to the lab address.

**Data integrity**

- [x] ~~Fabricated bibliography author names/titles~~ — fixed; every entry verified against Crossref.
- [x] ~~No way to catch this again~~ — `bin/verify_bibliography.py` checks `_bibliography/papers.bib` entries
      against Crossref; run it after adding or editing entries.
- [x] ~~`_data/coauthors.yml` had al-folio's demo data~~ — emptied; add real co-author links there if wanted.
- [x] ~~`_data/citations.yml` was al-folio's demo (Einstein) data~~ — regenerated from Kevin's Google Scholar profile
      with `bin/update_scholar_citations.py`; `update-citations.yml` refreshes it Mon/Wed/Fri.
- [x] ~~al-folio demo content was publicly reachable~~ — removed the demo blog posts, teaching and book pages,
      repositories/plugins/submenu pages, and their assets (images, audio, video, notebooks, etc.).
- [ ] Audit `_news/`, `_projects/`, `_pages/pi_bio.md` for other fabricated-but-plausible details — only the
      bibliography has been checked so far.
- [ ] More publications can be added to `_bibliography/papers.bib`; currently ports the preprints + peer-reviewed
      papers from Kevin's personal site, not the full conference-abstract list.
- [ ] Additional lab members: duplicate a profile block in `_pages/profiles.md` (image + a new
      `_pages/<name>_bio.md` content file ending in a CV/website links line) as people join. Keep the
      "joining soon" entry last.
- [ ] `_pages/join.md` — add the staff posting and UTD job board link once it's live.

**Hosting & deployment**

- [x] ~~Deploy workflow didn't match the Pages source~~ — switched to native GitHub Actions deploy.
- [x] ~~`baseurl` mismatch causing 404s~~ — fixed.
- [x] ~~Old `gh-pages` branch~~ — deleted (unused now that deploy is Actions-native).
- [x] ~~Repo is private / site lives at a `sitek.github.io/siteklab.github.io/` subpath~~ — moved to the public
      `siteklab/siteklab.github.io` repo, served at https://siteklab.github.io.
- [ ] Custom domain — not set up yet.

**CI / test infrastructure**

- [x] ~~`test/` directory missing, `lint:style-contract` broken~~ — restored from upstream al-folio.
- [x] ~~`unit-tests.yml`, `prettier.yml`, `upgrade-check.yml` missing~~ — restored.
- [x] ~~`update-tocs.yml`, `visual-regression.yml` missing~~ — evaluated and deliberately **not** restored: both are
      upstream-al-folio-project concerns (contributor-docs TOC maintenance, and pixel-diff parity against a
      pre-v1.x architecture baseline) that don't apply to a downstream single-owner site.
- [x] ~~`unit-tests.yml` failed on every push~~ — trimmed to the four integration tests that apply to this site
      (`plugin_toggles`, `bootstrap_compat`, `upgrade_cli`, `css_minify`); the `comments`, `distill` and
      `new_plugins` tests were removed along with the demo posts they built against.
- [ ] Confirm the trimmed `unit-tests.yml` run is green in CI.

**Integrations not yet configured**

- [x] ~~Giscus comments~~ — removed; the site has no comments (`al_comments` dropped from `Gemfile` and `_config.yml`).
- [ ] No analytics configured (Google/Cronitor/Pirsch/Openpanel/Cloudflare all empty in `_config.yml`).
- [ ] No Google/Bing site verification set.

**Final verification**

- [ ] `axe.yml` accessibility check hasn't been run yet (it's `workflow_dispatch`-only, not automatic).
- [ ] `apple_touch_icon` still unset — just the 🧠 emoji favicon, no real image for iOS bookmarks.

## Local development

```bash
bundle install
bundle exec jekyll serve   # → http://localhost:4000/
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
