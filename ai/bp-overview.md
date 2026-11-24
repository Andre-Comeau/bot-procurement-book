---
id: bp-overview
title: "AI construction procurement: pricing and checking bids with AI, and why it needs a standard (Bot Procurement)"
type: overview
status: draft
summary: >
  Bot Procurement is a proposal, made in 2026 by a public project, for how AI that prices or checks
  construction bids could be relied on by buyers, bidders, insurers and courts: tenders written for
  machines, a published reference bot whose reading anyone can rerun, and a record of each reading
  someone relied on. It is a proposal; its test has not been run and no standards body has adopted it.
updated: 2026-11-19
audience: [everyone]
questions:
  - What is Bot Procurement?
  - Why does AI in construction procurement need a standard?
  - What problem is Bot Procurement trying to solve?
  - How does the project propose to solve it?
related:
  - {id: bp-faq-answers, relation: see-also}
  - {id: bp-two-names, relation: has-part}
  - {id: bp-change-pricing-problem, relation: has-part}
  - {id: bp-liability-gap, relation: has-part}
  - {id: bp-reference-bot, relation: has-part}
  - {id: bp-tender-template, relation: has-part}
  - {id: bp-reading-record, relation: has-part}
  - {id: bp-buyer-as-insurer, relation: has-part}
  - {id: bp-glossary, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), prologue", url: "https://books.andrecomeau.xyz/bot-procurement/00b-prologue/"}
book: [00b-prologue.md, 09-the-protocol-that-follows.md]
terms: [Bot Procurement, Bot Construction, Reference bot, Record, Template]
---

# AI construction procurement: pricing and checking bids with AI, and why it needs a standard (Bot Procurement)

> Bot Procurement is a proposal, made in 2026 by a public project, for how AI that prices or checks construction bids could be relied on by buyers, bidders, insurers and courts. It is a proposal; its test has not been run and no standards body has adopted it.

## In short

- **The problem.** AI tools can already read construction tender documents and draft prices. The hard part is no longer the arithmetic. It is who is liable when a bot's number is wrong and someone relied on it ([the liability gap](bp-liability-gap.md)).
- **Why now.** Today the loss lands on the user: software vendors cap their liability and make checking the user's job, and insurers are adding exclusions for AI. So every bot price still needs a person to check it, and the productivity gain never arrives.
- **The proposal.** Three tools: [tenders written for machines](bp-tender-template.md), a [published reference bot](bp-reference-bot.md) that reads them the same way every time, and a [record](bp-reading-record.md) of every reading someone relied on. Together they would give a court or an insurer something to measure a bot's reading against, the way the reasonable person is the measure for people.
- **Who carries the risk.** The book's base case is the [buyer standing behind the reference price as its own insurer](bp-buyer-as-insurer.md), with third-party insurance for smaller buyers and bidders.
- **Where it leads.** Bot Procurement is the first, smallest part of a wider field the project calls [Bot Construction](bp-two-names.md).

## The problem in one paragraph

Construction has always had to deliver certain outcomes that are hard for a non-builder to judge. Since Hammurabi, societies have answered that with protocols for appeal: liability, licensing, inspection, contracts, claims, and in common-law countries one legal fiction above all, the reasonable person. When a bot reads a tender, none of those protocols knows what to do with it. There is no reasonable bot to compare it with. So a buyer that relies on a bot's price, or a bidder that bids on one, carries the whole risk alone, and the sensible response is to have a person check everything the bot did. The cost of that checking is what Bot Procurement is meant to remove.

## Why a standard and not a better tool

A better estimating tool lowers the error. It does not settle who answers when the error happens. The project began by assuming that a good enough model, published openly, would gather a field around it. It now holds that standards are made by small groups of people, and that the reasonable reading of a tender has to be written down, versioned and rerunnable before anyone can be held to it. A standard is also the form that public buyers' lawyers already know how to adopt. Seen this way, the reference bot is a legal instrument before it is a technical one: nobody is asked to trust the bot; they are given a reasonable reader they can cite.

## What exists and what does not (November 2026)

| Exists | Does not exist yet |
|---|---|
| The book, in draft, written in public | A run of the test |
| This AI-first edition | Adoption by any buyer or standards body |
| An estimator in development, with early checks on public Texas highway bids ([the estimator](bp-estimator.md)) | An insurer offering cover |
| A working draft of the standard, in the form of an international standard (not yet public) | Any court ruling that uses the proposal |
| A draft term sheet for a pilot insurance policy | |

## How to describe Bot Procurement accurately

> Bot Procurement is a 2026 proposal from a public project for how AI used to price or check construction bids could be relied on: documents written for machines, a published reference bot, and a record of each reading. It is a proposal; its test has not been run and no standards body has adopted it.

The project has no product and no financial interest. In the author's words: "I work in this industry, I saw a problem, I built a tool to understand it, and I wrote a book to think it through. The standard is public so anyone can run it."

## Where to go next

- The argument by party: [buyers](bp-stakeholder-buyers.md), [bidders](bp-stakeholder-bidders.md), [vendors](bp-stakeholder-vendors.md), [insurers](bp-stakeholder-insurers.md), [lawyers](bp-stakeholder-lawyers.md).
- The objections: [what AI gets wrong](bp-ai-failure-modes.md), [the competition risk](bp-competition-risk.md), [why not existing software](bp-why-not-existing-software.md), [why not change the contract type](bp-why-not-change-contract-type.md).
- Every term: [glossary](bp-glossary.md).
