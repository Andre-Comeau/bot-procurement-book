# Bot Procurement Book

A short book that asks one question: *when a bot causes harm, who is liable?*, in construction procurement, public and private, and what has to exist before owners, bidders and courts can rely on a bot's reading of a tender. The working title is *The Reasonable Bot*.

The book is being written in public during the Protocol Institute's [PiBoWriMo 2026](https://protocol-institute.org/events/pibowrimo-2026/), from November 1 to 30. It grows out of Andre Comeau's construction procurement protocols case study for the Institute's Protocols for Business group. The target is 8,000 to 15,000 words of main text, with an illustrated appendix of "Procurement Machines" cards.

**Why:** "I work in this industry, I saw a problem, I built a tool to understand it, and I wrote a book to think it through. The standard is public so anyone can run it. I don't have a plan for what comes after." (Andre Comeau)

**Status:** draft. Most chapters are drafted; chapters marked as outlines hold the plan for the chapter.

## Layout

- `manuscript/`: one Markdown file per chapter. Working notes for each chapter (brief, sources, open questions) are kept outside this repository.
  - File names keep their first numbers, so they no longer follow reading order: `PARTS` in `build_site.py` holds the order and the chapter numbers. Since 2026-11-19 the order follows Andre's outline: Part I the problem (`02`, `01`); Part II the solution (`06e`, with `05` to fold in); Part III why not something else (`03`, `08b`, `09b`); Part IV what each party gains (`02b`, `02c`, `09a`, `02e` designers, `02d`, `06c`, `06f` insurers, split from `06e`); Part V how we get there (`03b` with `06`, `00c` as what AI gets right, `07`, `09` with `06b`); Part VI past and future (`04`, `10`). Chapters 3 and 4 take a section heading as their title (2026-11-19).
  - `00b-prologue.md` is the author's status write-up for the Institute, placed as the prologue.
- `outline.md`: a map of the book in reading order, one paragraph per chapter.
- `images/`: figures for the book, the site and the listing.
- `TONE.md`: working notes on the book's voice so far, with before-and-after examples from chapter 4 (the delivery methods; chapter 2 when the notes were written). Revised as chapters are finished.
- `CLAUDE.md`: house rules for the AI assistant that helps with drafting.

Paths in the chapter notes point to the author's own working folders, which are not part of this repository.

## Formats

One Markdown source will build the print edition, the EPUB and a website.

## Licence

The text is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0); see [LICENSE](LICENSE). Cover art and typeset files are not covered by this licence and remain © Andre Comeau, all rights reserved.

Nothing in this book is legal or procurement advice.
