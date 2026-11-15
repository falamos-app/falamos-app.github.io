# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

This repository is the public site of the Falamos mobile app (iOS and Android, built elsewhere): the home page,
`privacy/`, and `config.json`, which every installed app reads.

## Stack

Static HTML/CSS on GitHub Pages (repo `falamos-app/falamos-app.github.io`, custom domain falamos.app). No build step,
no framework.

## Users

People who are moving to Portugal or have just moved there, and need European Portuguese for real life: letters from
the tax office, renting, the doctor, the bank, school. First focus is Ukrainian speakers (most competitors are
English-only); English-speaking expats are served from the first release. Many need level A2 for permanent residence or
citizenship (the CIPLE exam). The author is moving to Porto and is the first user.

## Product Purpose

Falamos teaches only European Portuguese (pt-PT) through short daily sessions (~5 minutes) built around real relocation
situations. Success: a newcomer can handle the bureaucracy and daily life in Portuguese and reach A2.

## Positioning

- Only pt-PT, never Brazilian («chamo-me», not «me chamo»; comboio, autocarro, telemóvel). Duolingo teaches Brazilian.
- The course is the relocation itself: lines for Finanças and NIF, renting, the city, the doctor (SNS), not «Lesson 7».
- Photo of any real text (a letter, a contract, a sign) → explained in the user's own language → words go into review.
- A path to A2 and practice exams in the CIPLE format.
- Explanations in the user's language (Ukrainian or English), not via English for everyone.

## Operating Context

The site is visited from links in Ukrainian and expat communities, store listings and the app itself (privacy,
support). Visitors are mostly on phones.

## Capabilities and Constraints

- Interface languages: English and Ukrainian. The site defaults to English and switches to Ukrainian by `#uk`, the same
  way `privacy/` does.
- The app is not in the stores yet: store buttons read «coming soon» for both App Store and Google Play until the real
  links exist. The page must not claim the app is available.
- No prices or free-tier limits on the site (decision 2026-11-15): prices are still working hypotheses.
- `privacy/` and `config.json` must stay untouched by design work.
- Contact: support@falamos.app.

## Brand Commitments

- Name **Falamos** («we speak», and the Portuguese goodbye «Falamos!»).
- Logo: «F» in a white speech bubble with an ink outline and a hard shadow (`assets/brand/` in the app repo).
- Visual direction «B · Eléctrico», shared with the app: Lisbon/Porto tram — tram yellow by day, warm graphite by night,
  2px outlines, hard offset shadows; Geologica for interface text, Bricolage Grotesque only for Portuguese.
- The night tram scene (App Store header video) is an approved brand asset.
- Voice: short, plain, warm; second person; no hype.

## Evidence on Hand

- Store screenshot copy in English and Ukrainian (app repo, `scripts/store-screenshots/strings/{en,uk}.json`).
- Header video and poster of the night tram (app repo, `scripts/store-screenshots/out/header/`).
- No reviews, users, press, download counts or ratings yet: never invent them.

## Product Principles

1. Real life first: every example is a situation a newcomer actually meets.
2. Portugal's Portuguese, always; a Brazilian form is a bug.
3. Explain in the learner's own language, briefly.
4. Honest and calm: no fake urgency, no claims ahead of the product.

## Accessibility & Inclusion

Bilingual (Latin and Cyrillic); Bricolage has no Cyrillic, so Ukrainian text never uses it. Day and night themes.
