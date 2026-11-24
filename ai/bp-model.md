---
id: bp-model
title: "The Model: the pricing model behind the estimator (in development)"
type: tool
status: outline
summary: >
  The Model will be the pricing model that the project's estimator and evaluator share: it will learn
  from past public bids and give each tender line an expected price and a usual error. It is in
  development, built offline on open-weight software whose weights do not change, so that any reading
  can be rerun later. Technical details and a how-to guide will follow as an appendix.
updated: 2026-11-19
audience: [researchers, AI vendors, estimators, insurers]
questions:
  - What model does the Bot Procurement estimator use?
  - Why use an offline open-weight model for procurement?
  - Can a procurement AI's reading be rerun later?
related:
  - {id: bp-estimator, relation: supports}
  - {id: bp-evaluator, relation: supports}
  - {id: bp-reading-record, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 16, 'A second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
book: [07-building-an-estimator-in-public.md]
terms: [Estimator (the project's), Fair and Reasonable Evaluator]
---

# The Model: the pricing model behind the estimator (in development)

> Outline. The Model is in development; nothing here describes a finished tool.

## In short

- **What it will do:** give each line of a tender an expected price, learned from what bidders actually charged on past public contracts, and the usual size of its miss on lines like it.
- **Who will use it:** the [estimator](bp-estimator.md) (a price for a line) and the [Fair and Reasonable Evaluator](bp-evaluator.md) (a check of a price against the same reference, with the usual miss as its tolerance).
- **Why offline and pinned:** a reading may need to be rerun years later in a dispute. Hosted models change without notice; an open-weight model run offline with fixed weights can be rerun exactly ([the reading record](bp-reading-record.md)).
- **Data kept apart:** newer bid results are left out of the Model's training so that a later check on them can show how it does on work it has not learned from.

## To write

Technical details and a how-to guide, planned as an appendix to the book, once the Model's design settles.
