#!/usr/bin/env python
"""Verify _bibliography/papers.bib entries against Crossref metadata.

Catches entries whose title or author names were hand-typed (or
AI-drafted) incorrectly instead of sourced from the DOI record —
e.g. a co-author's first name silently swapped for a different but
same-initial name. Run after adding or editing bibliography entries,
before pushing.
"""

import json
import re
import sys
import time
import urllib.error
import urllib.request

BIB_FILE = "_bibliography/papers.bib"
CROSSREF_API = "https://api.crossref.org/works/{doi}"
USER_AGENT = "siteklab-bib-verify/1.0 (mailto:sitek.kevin@gmail.com)"


def parse_entries(text):
    entries = []
    for chunk in re.split(r"\n(?=@\w+\{)", text):
        m = re.match(r"@(\w+)\{([^,]+),", chunk)
        if not m:
            continue
        key = m.group(2).strip()
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{(.*?)\},?\s*\n", chunk, re.S):
            fields[fm.group(1).strip().lower()] = re.sub(r"\s+", " ", fm.group(2)).strip()
        entries.append((key, fields))
    return entries


def parse_authors(author_field):
    people = []
    for part in author_field.split(" and "):
        part = part.strip()
        if "," not in part:
            continue
        family, given = part.split(",", 1)
        # strip equal-contribution markers (e.g. "Chandra*"), which al-folio renders as superscripts
        family = re.sub(r"[*∗†‡§¶‖&^]+", "", family)
        people.append((family.strip(), given.strip()))
    return people


def fetch_crossref(doi):
    req = urllib.request.Request(CROSSREF_API.format(doi=doi), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)["message"]


def normalize_title(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def check_entry(key, fields):
    doi = fields.get("doi")
    if not doi:
        return [f"{key}: no DOI on file — cannot auto-verify, check manually"]

    try:
        record = fetch_crossref(doi)
    except (urllib.error.URLError, urllib.error.HTTPError, KeyError, json.JSONDecodeError) as e:
        return [f"{key}: could not fetch Crossref record for {doi}: {e}"]

    problems = []

    crossref_title = (record.get("title") or [""])[0]
    if crossref_title:
        bib_words = set(normalize_title(fields.get("title", "")).split())
        cr_words = set(normalize_title(crossref_title).split())
        overlap = len(bib_words & cr_words) / max(len(cr_words), 1)
        if overlap < 0.7:
            problems.append(
                f"{key}: title differs from Crossref\n"
                f"    bib:      {fields.get('title')}\n"
                f"    crossref: {crossref_title}"
            )

    crossref_authors = [(a.get("family", ""), a.get("given", "")) for a in record.get("author", [])]
    if crossref_authors:
        cr_by_family = {fam.lower(): giv for fam, giv in crossref_authors}
        for family, given in parse_authors(fields.get("author", "")):
            cr_given = cr_by_family.get(family.lower())
            if cr_given is None:
                problems.append(f"{key}: author '{family}' not found in Crossref record (name change, or typo?)")
                continue
            bib_first = given.split()[0].rstrip(".") if given.split() else ""
            cr_first = cr_given.split()[0].rstrip(".") if cr_given.split() else ""
            if bib_first and cr_first and bib_first.lower() != cr_first.lower():
                problems.append(f"{key}: {family}, {given} — Crossref has first name '{cr_given}', not '{given}'")

    return problems


def main():
    with open(BIB_FILE) as f:
        entries = parse_entries(f.read())

    all_problems = []
    for key, fields in entries:
        all_problems.extend(check_entry(key, fields))
        time.sleep(0.5)  # be polite to Crossref

    if all_problems:
        print(f"Found {len(all_problems)} issue(s):\n")
        for p in all_problems:
            print(f"- {p}")
        sys.exit(1)

    print(f"All {len(entries)} bibliography entries verified against Crossref.")


if __name__ == "__main__":
    main()
