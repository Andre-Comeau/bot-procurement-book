---
id: bp-why-not-existing-software
title: "Why not use existing estimating software?"
type: alternative
status: draft
summary: >
  Existing construction estimating software is good, but almost all of it is built for bidders: it checks
  that a bid is not too low. A buyer checking a price needs the opposite, a look back at what the market
  has already paid. The tools also need structured data that owners' records rarely provide, and no
  vendor publishes how far its prices miss. Bot Procurement is a proposal to fill that gap, not to
  replace the tools.
updated: 2026-11-19
audience: [buyers, estimators, AI vendors, everyone]
questions:
  - Why not use existing construction estimating software to check prices?
  - Do construction software vendors publish how accurate their AI is?
  - Who is liable when a vendor's AI estimate is wrong?
  - What are construction software vendors building with AI?
related:
  - {id: bp-stakeholder-vendors, relation: see-also}
  - {id: bp-ai-strengths, relation: see-also}
  - {id: bp-pdf-zombie, relation: see-also}
  - {id: bp-existing-standards, relation: see-also}
  - {id: bp-why-not-change-contract-type, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 16, 'A second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Bot Procurement (book in draft), chapter 11, 'The vendors: players, not referees'", url: "https://books.andrecomeau.xyz/bot-procurement/working/02d-the-vendors/"}
book: [07-building-an-estimator-in-public.md, 02d-the-vendors.md]
terms: [Second opinion, Fair and reasonable]
allow_words: [certified]
---

# Why not use existing estimating software?

> The tools answer the bidder's question. The buyer's question runs the other way.

## In short

- **Built for bidders:** a bidder asks whether it has priced low enough to win and high enough not to lose money. Its software checks that it is not underbidding. A buyer asks whether it is overpaying against what the market has already paid, which needs a tool that looks backwards at past bids.
- **Data:** the tools need structured data. Owners' records are not standard, because every project arrives with its own consultants, forms and way of describing the same trench. The history that should teach a tool the market is locked in PDFs ([the PDF zombie](bp-pdf-zombie.md)).
- **Lock-in:** a vendor's price book and private formats tie the buyer to one product.
- **No published error:** the project's survey found no platform, estimating specialist, startup or certified German program that publishes how far its prices miss.
- **Who is liable:** the major vendors' AI terms cap liability at about a year's fees or a small fixed sum, call outputs recommendations only, and leave verification to the user. Today the user carries the loss when the number is wrong ([the liability gap](bp-liability-gap.md)).

## Three ways to get the data

1. The owner mandates standard documents: works, but takes years ([the tender template](bp-tender-template.md)).
2. Staff convert old records by hand: works, but costs more than the tool saves.
3. An AI converts each old tender into one standard table, with a person checking each file before use. This is the newest and least proven route, and the one the project is betting on.

## What the vendors are building (survey, 2026)

| Group | What it sells | What it does not do |
|---|---|---|
| Large platforms | Reading drawings, counting and measuring, comparing revisions, plugs for outside AI | Check a price against the market |
| Estimating specialists | A bidder's first estimate from its own past jobs, with a person approving | A public market check |
| Startups | Pricing straight from PDF plans with a general model and a supplier's list | Publish a miss rate |
| The US highway bid platform | The agencies' bid files, results and analysis, licensed back to the industry | Price a tender |
| German certified programs | Reading and writing standard tender data files | Publish a price error |

Company names and dated terms are in the book's hidden notes and have not been checked for this module; read the vendors' current terms at the source.

## How Bot Procurement relates to them

The project's proposal sits beside the tools, not against them: a public test any tool can take, a published error, and a [second opinion](bp-glossary.md#second-opinion) for the buyer. For vendors it would be a target to build to and a measured error an insurer could price from ([stakeholders: AI vendors](bp-stakeholder-vendors.md)). Bot Procurement is a proposal; its test has not been run.
