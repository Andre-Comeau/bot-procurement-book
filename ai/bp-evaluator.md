---
id: bp-evaluator
title: "The Fair and Reasonable Evaluator: a second opinion on every change order price"
type: tool
status: draft
summary: >
  A checking bot the project plans to build on its estimator: it will price each line of a construction
  change against what the market has paid, cite the past tenders behind each price, flag lines that are
  unusually high or low, and draft the fair-and-reasonable memo for a named person to decide and sign.
  It is in development.
updated: 2026-11-19
audience: [buyers, consultants, auditors, bidders]
questions:
  - Can AI check whether a change order price is fair and reasonable?
  - Who decides when an AI flags a change order price?
  - What should an AI price check cite?
  - Should a price check flag low prices as well as high ones?
related:
  - {id: bp-change-pricing-problem, relation: answers}
  - {id: bp-estimator, relation: depends-on}
  - {id: bp-reading-record, relation: see-also}
  - {id: bp-procurement-machines, relation: see-also}
  - {id: bp-cases, relation: see-also}
  - {id: bp-stakeholder-buyers, relation: see-also}
  - {id: bp-model, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 16, 'A second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
book: [07-building-an-estimator-in-public.md]
terms: [Fair and Reasonable Evaluator, Keyholder, Flag, Fair and reasonable]
---

# The Fair and Reasonable Evaluator: a second opinion on every change order price

> The tool drafts, a person decides. In development.

## In short

- **Prices** each line of a change against what the market has already paid.
- **Cites** the past tenders behind every price: contract, date, item and the prices used, so a reviewer can go to the source.
- **Flags** items it has seen too rarely, never pricing them silently, and prices well outside its usual error in either direction.
- **Drafts** the fair-and-reasonable memo and hands it to a named reviewer, the keyholder, who reviews, decides and signs with a reason.
- **Logs** each request: who asked, when, which model version answered, what was flagged, and what the reviewer decided and why ([the reading record](bp-reading-record.md)).

## How the arithmetic works

If the estimator says a tonne of asphalt should cost about $95 and is usually right within 20 percent, the evaluator can call a change at $105 within range, ask why one at $150 is so high, and ask the same of one at $50. A price that low is rarely a gift: the builder has misread the work or plans to recover the difference elsewhere ([worked cases](bp-cases.md)). The evaluator's question ends in yes or no, so the arithmetic belongs more naturally to it than to the estimator, but the two share it. Every price the evaluator checks after award becomes evidence for the next estimate.

## Why a person signs

A flag is worth something only if someone has to act on it. A flag that nobody owns costs nothing to ignore: no one answers for missing it, so a busy office misses it ([procurement machines](bp-procurement-machines.md)). The evaluator is designed around the person who signs.

## Why it is worth building even at 10 percent error

Reviewing changes costs a buyer, on the author's working figures, $7,500 to $20,000 per million dollars of work, and slow reviews give contractors reasons to claim ([the change-pricing problem](bp-change-pricing-problem.md)). A tool that answers in minutes need not be perfect: even with some minor overpayments, it pays for itself the first time it keeps a contractor from finding a reason to claim.

## Built for buyers, not bidders

Commercial estimating software is built for bidders: it checks that a bid is not too low to make money. The evaluator's question runs the other way: is the buyer paying more than the market has paid? ([why not existing software](bp-why-not-existing-software.md)).

## Aside: lump-sum contracts

Where contracts are priced line by line, every item has a price. Where they are lump sums, the evaluator must first read the contract, find past work that looks like it, and combine those prices. Matching work to similar work is reading, not arithmetic, and it is where AI earns its place.
