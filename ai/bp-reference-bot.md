---
id: bp-reference-bot
title: "The reference bot: a reasonable reader a court can rerun"
type: proposal
status: draft
summary: >
  The project's proposal for a published, versioned reference bot whose reading of a tender anyone can
  rerun and get the same answer, so that courts, insurers and buyers have a concrete measure of what a
  reasonable bot would have read, as the reasonable person is the measure for people. It is a proposal;
  no reference bot has been adopted and its test has not been run.
updated: 2026-11-25
audience: [lawyers, standard writers, buyers, researchers, AI vendors]
questions:
  - What is a reference bot in construction procurement?
  - What would a "reasonable bot" standard look like?
  - Why does a reference bot need to give the same answer every time?
  - Why would a court care about a reference bot?
related:
  - {id: bp-overview, relation: part-of}
  - {id: bp-liability-gap, relation: answers}
  - {id: bp-tender-template, relation: depends-on}
  - {id: bp-reading-record, relation: depends-on}
  - {id: bp-sign-off, relation: see-also}
  - {id: bp-estimator, relation: see-also}
  - {id: bp-competition-risk, relation: contrasts}
  - {id: bp-ai-failure-modes, relation: see-also}
  - {id: bp-stakeholder-lawyers, relation: see-also}
  - {id: bp-existing-standards, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 17, 'The protocol that follows'", url: "https://books.andrecomeau.xyz/bot-procurement/working/09-the-protocol-that-follows/"}
  - {title: "Bot Procurement (book in draft), prologue", url: "https://books.andrecomeau.xyz/bot-procurement/00b-prologue/"}
  - {title: "David Lang, 'Standards Make the World', Summer of Protocols (Protocol Institute)"}
book: [00b-prologue.md, 09-the-protocol-that-follows.md, 06b-the-bot-in-the-witness-box.md]
terms: [Reference bot, Reasonable bot, Record, Template, Tool test, Sign-off]
---

# The reference bot: a reasonable reader a court can rerun

> Bot Procurement proposes a published, versioned reference bot as the measure of a reasonable bot's reading of a tender. It is a proposal; no reference bot has been adopted and its test has not been run.

## In short

- **What it is:** a bot, frozen at a named version, that reads a tender and states what it found and what it priced, with its error stated.
- **What makes it a reference:** anyone can rerun it on the same documents and get the same answer. The project's early work uses offline open-weight models for this reason: pinned weights make a reading reproducible a year later, where hosted models keep changing.
- **What it is for:** a measure, not an oracle. A court asking whether a bidder's bot read the tender reasonably, or an insurer asking whether a loss came from the bot or from the bidder, compares with what the reference read.
- **What it is not:** a price-setter. The project's rule is "check and record, never set": the reference flags lines for people to review, and nothing it produces is released to bidders before bids close ([the competition risk](bp-competition-risk.md)).

## Why a legal instrument before a technical one

Courts already have a fiction for judging conduct: the reasonable person. The fiction works because people share an intuition of reasonableness. A bot's reading has no such intuition behind it. Two models can read the same drawing differently; the same model can read it differently twice. The reference bot makes the fiction concrete for bots: the standard says which reading binds, so a reasonable reading can be pointed at, rerun and argued about. Nobody is asked to trust the bot. They are given a reasonable reader they can cite.

This also moves the project from the "innovation" bucket, where public buyers are cautious, into the "standards" bucket, where they already know how to take part.

## What it needs to work

1. **Documents it can read without guessing.** A PDF tender forces every bot to guess at tables and drawings, and guesses differ. The [tender template](bp-tender-template.md) gives the reference the same text every bidder's bot reads.
2. **A record of each reading.** Without a record of which version read which document with what settings, a later dispute cannot rerun anything. The record is a clause in the tool test and the sign-off, not a standard of its own ([the reading record](bp-reading-record.md)).
3. **A stated error.** A reference that does not say how far it misses invites being treated as exact. This is the tool test, the second of the book's three standards: the reference is the first tool to sit it, and any other vendor's bot can sit it too. The project's draft standard measures misses on contracts let after the bot's version was frozen (the project's draft standard, not yet public).
4. **Someone who stands behind it.** A measure with nobody liable for it is a suggestion. Whoever relies on a reading signs for it ([the sign-off](bp-sign-off.md)), and the book's base case is the buyer as its own insurer ([buyer as insurer](bp-buyer-as-insurer.md)).

## How a standard like this gets made

The project once assumed a good enough model, published, would gather the field on its own. It now follows David Lang's account of standards-making: standards "are made and remade by (usually small) groups of people", along one of two paths. The formal path runs proposal, expert draft, public comment, revision, vote and publication. The Internet's path is "rough consensus and running code": build something that works, get it used, and bring it to a committee with something already running. Construction procurement has walked both: ISO 10845 grew from South Africa's national standards; the Open Contracting Data Standard was written by a small team and adopted one government at a time ([existing standards](bp-existing-standards.md)).

## Aside: why one reference and not many

A single reference makes every bidder's bot comparable with one thing. It also creates the risk the project takes most seriously: if every bot leans on the same reference, their errors stop being independent and their prices can move together. The draft standard's answer is to keep the reference as a check, never a price, to release nothing before close, and to measure the independence of any two implementations before calling them separate ([the competition risk](bp-competition-risk.md)).

## Aside: what the reference can and cannot catch

Sorted by the book's four failure modes ([what AI gets wrong](bp-ai-failure-modes.md)): the reference is strongest against miscommunication (everyone reads the same text), useful against misadventure (there is always a last version to roll back to), weak against deliberate manipulation (publishing it shows a manipulator where to aim, so bonds and escrow carry that weight), and has nothing to add against outright malice.
