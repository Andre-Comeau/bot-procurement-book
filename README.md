# Bot Procurement Book

A short book that asks one question: *when a bot causes harm, who pays?*, in construction procurement, public and private, and what has to exist before owners, bidders and courts can rely on a bot's reading of a tender. The working title is *The Reasonable Bot*.

The book is being written in public during the Protocol Institute's [PiBoWriMo 2026](https://protocol-institute.org/events/pibowrimo-2026/), from November 1 to 30. It grows out of Andre Comeau's construction procurement protocols case study for the Institute's Protocols for Business group. The target is 8,000 to 15,000 words of main text, with an illustrated appendix of "Procurement Machines" cards.

**Why:** "I work in this industry, I saw a problem, I built a tool to understand it, and I wrote a book to think it through. The standard is public so anyone can run it. I don't have a plan for what comes after." (Andre Comeau)

**Status:** draft. The outline is settled, the prologue has a first draft, and every chapter now holds its source passages (Andre's quoted sentences and Claude's marked notes) under the sections it will need, ready to cut and rewrite.

## Layout

- `outline.md`: the outline, with each chapter's target length, brief and sources.
- `manuscript/`: one Markdown file per chapter. Each starts with a hidden note (`<!-- -->`) giving its target length, brief, sources and the literature to read first. The note doesn't show in the built book and is deleted when the chapter is done.
  - File names keep their first numbers, so they no longer follow reading order: `PARTS` in `build_site.py` holds the order and the outline holds the numbers. Since 2026-11-07 (vgr_zirp's reading order): chapters 1 to 4 are `07-building-an-estimator-in-public.md`, `03-how-a-price-is-judged-today.md`, `03b-what-do-we-do-with-a-drunken-sailor.md` and `00c-introduction.md` (the zombie garden); chapters 5 and 6 are `01` and `02`; chapters 7 to 10 are `04`, `05`, `06` and `06b`; chapters 11 and 12 are `09` and `10`.
  - `00b-prologue.md` is the author's status write-up for the Institute, placed as the prologue.
- `institute-write-up-review-2026-10-14.md`: a review of that write-up, with the lightly copyedited text.
- `machinery-figure-chat-2026-10.md`: notes on the machinery figure and its eight tension lines.
- `literature-review-2026-11-01.md`: a literature review of about 165 works (1 November 2026). Part 1 is the synthesis: what has been written near the book, the gaps it fills, what cuts against it, and what to read for each chapter. Parts 2 to 6 are the annotated sources, a shelf for Appendix B; Part 6, the verification pass, wins over earlier parts.
- `collusion-papers-notes-2026-11-01.md`: a close reading of the Seoul National University papers on AI bidders colluding in construction tenders, a test of the argument that public bid data commoditizes pricing, and what follows for the book's design.
- `images/`: figures for the book, the site and the listing.
- `TONE.md`: working notes on the book's voice so far, with before-and-after examples from chapter 2 (the delivery methods). Revised as chapters are finished.
- `CLAUDE.md`: house rules for the AI assistant that helps with drafting.

Paths in the chapter notes are relative to the author's `construction-procurement-protocols` repository unless they start with `C:\`.

## Formats

One Markdown source will build the print edition, the EPUB and a website.

## Licence

The text is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0); see [LICENSE](LICENSE). Cover art and typeset files are not covered by this licence and remain © Andre Comeau, all rights reserved.

Nothing in this book is legal or procurement advice.
