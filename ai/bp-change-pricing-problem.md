---
id: bp-change-pricing-problem
title: "Pricing change orders after award: the supplier-of-one problem"
type: problem
status: draft
summary: >
  A tender is the one moment a construction buyer learns what the market thinks the work is worth;
  after award, every change is bought from the builder already on site, a supplier of one, so the buyer
  must justify each price in writing without a market. The review is slow and costly, and a slow
  review gives a builder reasons to claim.
updated: 2026-11-19
audience: [buyers, consultants, bidders, auditors]
questions:
  - Why is pricing construction change orders hard?
  - What does "fair and reasonable" mean for a change order?
  - How much does reviewing change orders cost a buyer?
  - Why can a slow change review lead to claims?
related:
  - {id: bp-overview, relation: part-of}
  - {id: bp-evaluator, relation: answers}
  - {id: bp-estimate-accuracy, relation: see-also}
  - {id: bp-stakeholder-buyers, relation: see-also}
  - {id: bp-why-not-change-contract-type, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 16, 'The estimator and the evaluator: a second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Bot Procurement (book in draft), chapter 4, 'Why does the hard bid survive?'", url: "https://books.andrecomeau.xyz/bot-procurement/working/03-how-a-price-is-judged-today/"}
book: [07-building-an-estimator-in-public.md, 03-how-a-price-is-judged-today.md]
terms: [Change (change order), Fair and reasonable, Engineer's estimate]
---

# Pricing change orders after award: the supplier-of-one problem

> After a construction contract is signed, every change is bought from a supplier of one. The buyer has to show the price is fair and reasonable without a market to show it.

## In short

- On closing day a tender tells the buyer what the work is worth to the people who would do it. Then the market leaves and does not come back.
- Changes after award (rock the borehole logs missed, a second door in the lobby) can only practically be done by the builder already on site, and both sides know it.
- A public buyer must justify each change price in writing; private owners who answer to a board or lender do the same under another name.
- The justification is usually written by whoever has time, which pushes it down a chain of consultants and sub-consultants, each adding a review, a delay and an invoice.
- The author's working estimate: reviewing changes costs $7,500 to $20,000 for every million dollars of work.

## How a change gets priced today

The builder sends a price. The buyer's reviewers, efficient but busy, send the hard reviews to a consultant, who may send them on to a sub-consultant; the consultant then has to read what came back before passing it on. The justification is a short essay on what the work should have cost, built from old tenders, price books and judgment. A consultant's review typically has a service standard of about ten working days, which is a target, not a timer.

## What it costs

The author's figures from practice, not a survey: each change takes an hour or more of review at $150 to $200 an hour, and a million-dollar project can see 50 to 100 changes. That puts the review bill between $7,500 and $20,000 per million dollars of work. A consultant's review can cost 2 to 10 percent of the work it checks, so at the top of that range the review costs about as much as a tool with a 10 percent error would get wrong.

## Why slow reviews cause claims

The clock itself is rarely the claim, because contractors are usually warned about review times and cannot claim against them. The danger is motivation. Most contractors clear a change at their margins and move on; they look for claims only when something motivates them. A project that slows production on every change, while the contractor's site overhead keeps running, supplies that motivation, and a motivated contractor can usually find something claimable on the job. A fast answer that is roughly right can be worth more than a slow answer that is exactly right.

## Why a low price is also a warning

A change priced well below what the work should cost is not a gift. Either the builder has misread the work or it plans to recover the difference elsewhere, and a builder losing money on a change has a reason to look for a claim. A check that only flags high prices misses half the risk ([worked case: the fifty-dollar asphalt](bp-cases.md#the-fifty-dollar-asphalt)).

## What the project proposes

A checking bot, the [Fair and Reasonable Evaluator](bp-evaluator.md), that prices each line of a change against what the market has paid, cites the past tenders it used, flags lines that are unusually high or low, and drafts the memo for a named person to decide and sign. It is in development.

## Aside: the lump-sum version of the problem

The data the project started from is the easy case: highway contracts tendered line by line, so every item carries a price. Many buyers tender buildings as lump sums or a few large parts. Before a bot can price a change on such a job it has to read the contract, find past work that looks like it, and combine those prices, which is reading, not arithmetic. That is where an AI earns its place, and it is also why the project argues that a lump sum can act as a forcing function ([why not change the contract type](bp-why-not-change-contract-type.md)).
