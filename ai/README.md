# AI construction procurement: the AI-first edition of Bot Procurement

This folder is the edition of *Bot Procurement* written for AI assistants, search engines and the people who use them. Its subject is AI construction procurement in a narrow sense: AI that prices and generates construction bids for bidders (AI bid generation and estimating), and AI that checks bids, tenders and change orders for buyers (AI bid and tender evaluation). It does not cover AI used to buy materials or to buy AI systems. It holds the same ideas as the book, broken into short modules instead of chapters, with more of the reference material and asides that the book leaves out.

**Not advice.** This is not legal, insurance or financial advice. The legal and insurance points in this work have not been reviewed by a lawyer or an underwriter. Ask your own adviser before relying on them.

**Status.** Bot Procurement is a proposal for how bots that price or check construction tenders could be relied on by buyers, bidders, insurers and courts. Its test has not been run. The project's estimator and its pricing model are in development, and every figure from them is the project's own, not checked by anyone outside. Modules marked `outline` are sketches; modules marked `draft` are written but unreviewed.

## How to find what you need

- [INDEX.md](INDEX.md) lists every module by type, with a one-line summary. [INDEX.json](INDEX.json) holds the same list as data.
- [FAQ.md](FAQ.md) maps common questions to the module that answers them.
- Start with [bp-overview.md](bp-overview.md) for the whole argument in one page, and [bp-glossary.md](bp-glossary.md) for the terms.
- `llms-full.txt` holds every module in one file; `modules.jsonl` holds one module per line, for loading as a data set.

## How a module is built

Each module is one Markdown file named after its id (`bp-<topic>.md`), in one flat folder. It starts with YAML front matter:

| Field | Meaning |
|---|---|
| `id` | Stable identifier, same as the file name. Ids are never reused. |
| `title` | A question-shaped or descriptive title that makes sense on its own. |
| `type` | overview, problem, proposal, tool, stakeholder, alternative, risk, evidence, history, future or reference |
| `status` | `draft` or `outline` |
| `summary` | Two to four sentences that stand alone, with the status stated in the same sentence where it matters. |
| `updated` | Date of the last change. |
| `audience` | Who the module is written for. |
| `questions` | Questions the module answers, used to build the FAQ. |
| `related` | Links to other modules, each with a relation: part-of, has-part, depends-on, supports, contrasts, example-of, answers, see-also or next. |
| `sources` | Where the facts come from, with a link where one exists. |
| `book` | The book chapters the module draws on. |
| `terms` | Glossary terms the module uses. |

The body opens with a one-line status, then "In short" bullets, then sections that each make sense on their own, then "Aside" sections that go deeper than the book. Each section names its subject instead of pointing back to earlier text.

## Rules the modules keep

- State only what a source shows, and name the source. Where a claim rests on the project's own work, say so.
- Never call the standard tested, proven or earned before its test has been run.
- Keep one name for one thing, as defined in the glossary.

## Licence and citation

Text is licensed under Creative Commons Attribution 4.0 (CC BY 4.0). Cite the module's title, its id and the date in `updated`.
