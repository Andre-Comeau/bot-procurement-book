---
id: bp-sign-off
title: "The sign-off: who answers for an AI's reading of a construction tender"
type: proposal
status: draft
summary: >
  The third of the three standards Bot Procurement proposes: before anyone relies on a bot's reading of a
  tender, a named person confirms that the bot passed the test for that kind of work, that it read the
  version of the documents that governs, and that someone able to overrule it looked at what it found,
  then puts their name to the reading. It is a proposal; no profession or buyer has adopted it.
updated: 2026-11-25
audience: [buyers, bidders, designers, lawyers, insurers, standard writers]
questions:
  - Who is responsible when someone relies on an AI's reading of a tender?
  - What should a person check before relying on an AI estimate or bid check?
  - Are there professional standards for relying on AI or on someone else's model?
  - Why does Bot Procurement propose three standards?
related:
  - {id: bp-overview, relation: part-of}
  - {id: bp-reference-bot, relation: see-also}
  - {id: bp-tender-template, relation: see-also}
  - {id: bp-reading-record, relation: depends-on}
  - {id: bp-liability-gap, relation: answers}
  - {id: bp-stakeholder-lawyers, relation: see-also}
  - {id: bp-existing-standards, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 17, 'Three standards, and how they could stick'", url: "https://books.andrecomeau.xyz/bot-procurement/working/09-the-protocol-that-follows/"}
  - {title: "Bot Procurement (book in draft), chapter 3, 'Insuring the bidder's margin'", url: "https://books.andrecomeau.xyz/bot-procurement/working/06e-the-underwriters-chapter/"}
  - {title: "Actuarial Standards Board, ASOP No. 56, Modeling"}
  - {title: "RICS, professional standard on the responsible use of AI in surveying practice (mandatory from 9 March 2026)"}
book: [09-the-protocol-that-follows.md, 06e-the-underwriters-chapter.md]
terms: [Sign-off, Tool test, Template, Record, Keyholder]
---

# The sign-off: who answers for an AI's reading of a construction tender

> Bot Procurement proposes a sign-off standard for anyone who relies on a bot's reading of a tender. It is a proposal; no profession or buyer has adopted it.

## In short

- **One of three.** The book proposes three standards: one for the documents a bot reads ([the tender template](bp-tender-template.md)), one to test the bot (the tool test, with [the reference bot](bp-reference-bot.md) as the first tool to sit it), and this one, for the person who signs for what the bot found.
- **What it binds:** the person, not the tool. Whoever relies on the reading signs for it: the buyer's evaluator, the bidder's estimator, or the designer checking that a bot read the drawings as intended.
- **What they check first:** that the bot passed the test for this kind of work, that it read the version of the documents that governs, and that someone able to overrule it looked at what it found.
- **Why a name:** a flag nobody owns is a flag nobody reads.

## Why a test alone is not enough

A testing body measures the product; it does not tell the person using it what to check before relying on it. That takes the kind of standard a profession writes for its own members. The book's example is the railroad: a testing society measures the rail, and the engineer who lays it signs for using it.

## Professions that already work this way

- **Actuaries.** In the United States, the Actuarial Standards Board writes standards of practice through public exposure drafts. ASOP 56 covers models: what an actuary must understand, check and disclose before relying on one, including a model somebody else built. An actuary who skips it answers to the profession.
- **Surveyors.** Since 9 March 2026, members of the Royal Institution of Chartered Surveyors must decide, by name, whether an AI output is reliable enough to use.
- **Engineers.** Engineers already seal drawings, and a highway engineer signs a written justification when a bid looks odd.

The book suggests that engineering regulators and estimating societies could write the same duty into their own practice standards, by public exposure drafts as the actuaries do.

## Where the signed readings would live

Anyone may write an extension to the Open Contracting Data Standard, from the Open Contracting Partnership's template and registry. The book proposes one for signed readings, which would put them beside the contract data governments already publish ([existing standards](bp-existing-standards.md)). The record of what the bot read, by which version and when, is a clause in the tool test and the sign-off rather than a standard of its own: without it the test cannot be rerun and the sign-off has nothing to point at ([the reading record](bp-reading-record.md)).

## Why it comes early

A court can work with the documents and the sign-off long before anyone agrees on a tolerance for the test: the documents show what was asked, and the sign-off shows who relied on the answer and what they checked. So the book's order is the documents now, the sign-off as soon as anyone relies on a bot, which is already, and the test when the project's estimator has produced the evidence to set its tolerance.
