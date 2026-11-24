---
id: bp-estimator
title: "The estimator: a pricing bot in development, and its early numbers"
type: tool
status: draft
summary: >
  The project is building an estimator that will price each line of a tender from past public bids. On
  the project's own checks, an early version missed the average of the three lowest bids by a median of
  21 percent line by line (the state's engineer's estimate: 29 percent) and came within about 10 percent
  on whole contracts. Nobody outside the project has rerun these figures, and the check on newer
  contracts has not been run.
updated: 2026-11-19
audience: [researchers, estimators, buyers, AI vendors, insurers]
questions:
  - How accurate is an AI estimator on highway bids?
  - What data was the project's estimator built on?
  - Why did the project build an estimator before an evaluator?
  - Why use an offline open-weight model?
related:
  - {id: bp-evaluator, relation: supports}
  - {id: bp-model, relation: depends-on}
  - {id: bp-estimate-accuracy, relation: see-also}
  - {id: bp-reference-bot, relation: see-also}
  - {id: bp-margin-insurance, relation: see-also}
  - {id: bp-ai-strengths, relation: see-also}
  - {id: bp-cases, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 16, 'A second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Texas Department of Transportation, public bid tabulations"}
book: [07-building-an-estimator-in-public.md]
terms: [Estimator (the project's), Engineer's estimate, Second opinion]
---

# The estimator: a pricing bot in development, and its early numbers

> In development. Its figures below are the project's own, made while choosing between versions. Do not quote the 21 percent without that sentence.

## In short

- **What it will do:** estimate the price of each line of a tender from what bidders actually charged on past public contracts, and state how far prices like it usually miss.
- **Data:** Texas Department of Transportation bid tabulations: about a million line prices over two years, every bidder's price for every line of every highway contract, alongside the state engineers' own estimate.
- **Early numbers (project's own checks, October 2026):** learned on contracts let before May 2026; checked on contracts let from May 2026. Line by line, a median miss of 21 percent against the average of the three lowest bids, versus 29 percent for the engineer's estimate. Whole contracts: typically within plus or minus 10 percent, level with the engineer's estimate.
- **For scale:** on the same lines, the three lowest bidders disagreed with each other by a median of 50 percent.
- **Aim:** 2 to 3 percent, about the margin a contractor works to. Until then its price is a [second opinion](bp-glossary.md#second-opinion), not a decision.

## How to read the numbers

The checks used contracts the estimator had not learned from, so they show the method works beyond its training data and that its error is known on that set. But each version was chosen knowing how the previous one scored, so the figures probably flatter it a little, by an amount nobody has measured. A check on newer bid results that the project has left alone will come once there is a product and someone who wants the answer. The figures do not show that someone outside the project can rerun them, or that a court would accept the number.

Three data sets, in plain words:

| Set | Contracts | Use |
|---|---|---|
| Learn | Texas lettings before May 2026 | The estimator learns prices from them (researchers: training data) |
| Check while building | Texas lettings from May 2026 | Each version is checked, improved and checked again (validation data) |
| Final check, not yet run | Newer bid results, left alone | The only figures fit to quote as accuracy (test data) |

## Why the estimator came before the evaluator

On paper the [evaluator](bp-evaluator.md) should have come first: it only needs to analyse, where an estimator must design a price. Texas's open bid data, deep enough to go straight to the estimator, changed the order. The evaluator was folded into the estimator's plan in early October 2026 as a second use of the same model: the estimator's price for a line is the evaluator's reference, and the estimator's error is the evaluator's tolerance.

## Why offline, pinned models

A reading has to be rerunnable next year for a dispute to be settled. Hosted models change without notice; an offline open-weight model whose weights do not change can be rerun exactly. The first version is a proof of concept that starts the flywheel, and scales to other AI only if demand justifies it.

## The flywheel

Version 1.0 builds momentum by being usable. Version 2.0 shows benefits a buyer can count (claims never started, reviews not paid for), which is the evaluator's job. Version 3.0 is a working model from which a first standard can be reverse-engineered. Owners who adopt it produce standard records, which make the next tool cheaper and more accurate.

## Aside: what the estimator costs bidders

None of this is free for the builder. The estimator narrows the cushion a bidder carries into a tender, and the evaluator narrows what a builder could once make up on changes after award. Whether margins shrink depends on the market; the builder also gains changes approved in days instead of weeks, paid sooner and carrying less overhead.
