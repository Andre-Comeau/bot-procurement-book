---
id: bp-tender-as-interface
title: "The tender is the interface: construction procurement as software"
type: problem
status: draft
summary: >
  The book redescribes construction procurement as software: the design, the tender as the interface
  (API), and construction as the compilation. One interface means one builder answers for everything
  behind it, usually with a surety behind the builder. But the interface is a stack of PDFs, called once
  by each bidder, and AI is about to flood it with cheap bids.
updated: 2026-11-19
audience: [everyone, buyers, bidders, AI vendors, researchers]
questions:
  - How is a construction tender like a software API?
  - Why does a single point of responsibility matter in construction?
  - What happens to public tenders when AI makes bidding cheap?
related:
  - {id: bp-pdf-zombie, relation: see-also}
  - {id: bp-stakeholder-buyers, relation: has-part}
  - {id: bp-stakeholder-bidders, relation: has-part}
  - {id: bp-stakeholder-vendors, relation: has-part}
  - {id: bp-tender-template, relation: see-also}
  - {id: bp-future, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 1, 'The tender and the flood of AI bids'", url: "https://books.andrecomeau.xyz/bot-procurement/working/02-the-tender-is-the-api/"}
  - {title: "Neil Clarke, 'A Concerning Trend', Clarkesworld editor's blog, February 2023", url: "https://neil-clarke.com/a-concerning-trend/"}
book: [02-the-tender-is-the-api.md, 02b-the-buyers.md, 02c-the-bidders.md, 02d-the-vendors.md]
terms: [The tender as the interface, Tender]
---

# The tender is the interface: construction procurement as software

> Design, interface, compilation. The tender is the call every bidder makes, and the bid is the answer that comes back.

## In short

- **Three components:** the design; the tender, which is the interface; and construction, which compiles the design. The builder agrees, in an auction, to provide everything needed to compile it.
- **The virtue of an interface:** neither side reads the other's source code. The designer need not know how the builder schedules crews; the builder need not know why the engineer chose that beam.
- **The second virtue:** one door means one builder answers for everything behind it, and on most North American public work a surety stands behind that builder. Hiring a construction manager to buy from the trades for you trades that accountability away.
- **The flaw:** the interface is a stack of PDFs, and unlike software interfaces it is called once per bidder, in a few weeks, with its errors found by the people least placed to say so.
- **The threat:** when writing a bid becomes nearly free, the door floods.

## The Amazon mandate, in construction

The book borrows the 2002 Amazon mandate as told by Steve Yegge: every team exposes its data and functions through a service interface, and no team reaches into another's code. In construction the teams are a design consultant and a builder, and the interface is the tender package. Exposing one's own workings to strangers invites exploitation, so neither side wants to.

## An untested interface

Every other interface in the world is called thousands of times before anyone depends on it. A tender is called once by each bidder before close. BIM, AI review and licensed professionals help screen designs for errors, but bug-free drawings remain a mythical beast. The errors surface during construction, which is where the book's chapter on [who is liable](bp-liability-gap.md) begins.

## The flood

In February 2023 the science-fiction magazine Clarkesworld closed submissions. It had taken stories from anyone since 2006; when chatbots made a passable story free, people following "easy money" advice sent them in. By the twentieth of the month it had received about five hundred machine-written stories and about seven hundred real ones, and its editor could no longer sort the piles fast enough. The real writers lost their door with the fakes. A public tender is a bigger door, and the same crowd is on its way. How each party meets it: [buyers](bp-stakeholder-buyers.md), [bidders](bp-stakeholder-bidders.md), [vendors](bp-stakeholder-vendors.md).

## Aside: four ways software handles a flooded interface

Software has four answers to too many calls: rate limits, keys, fees, and checking each request against a published format. Construction already uses keys (prequalification) and fees (bonds, document charges). Caps mostly fail public procurement's proportionality rules. The missing piece is the fourth: a published check that gives the same answer for the same bid, which is what the [reference bot](bp-reference-bot.md) would be.
