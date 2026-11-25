---
id: bp-reading-record
title: "The reading record: what an AI read, when, and who relied on it"
type: proposal
status: draft
summary: >
  The project's proposal that every bot reading someone relies on leaves a record: the documents read
  (by fingerprint), the bot and its version, its settings, what it found, when, and who chose to rely
  on it. After a loss, only the record can settle whether the bot's price was wrong or the work went
  badly. It is a proposal.
updated: 2026-11-25
audience: [lawyers, insurers, buyers, bidders, auditors, standard writers]
questions:
  - What should be recorded when an AI prices or checks a construction bid?
  - How do you prove which version of a bot read which document?
  - Why does a record matter after a loss?
  - Who keeps the record, the buyer or the bidder?
related:
  - {id: bp-overview, relation: part-of}
  - {id: bp-reference-bot, relation: supports}
  - {id: bp-sign-off, relation: supports}
  - {id: bp-tender-template, relation: see-also}
  - {id: bp-buyer-as-insurer, relation: supports}
  - {id: bp-evaluator, relation: see-also}
  - {id: bp-trax-case, relation: see-also}
  - {id: bp-stakeholder-bidders, relation: see-also}
  - {id: bp-margin-insurance, relation: see-also}
  - {id: bp-model, relation: see-also}
  - {id: bp-stakeholder-lawyers, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 16, 'The estimator and the evaluator: a second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Bot Procurement (book in draft), chapter 17, 'Three standards, and how they could stick'", url: "https://books.andrecomeau.xyz/bot-procurement/working/09-the-protocol-that-follows/"}
book: [07-building-an-estimator-in-public.md, 09-the-protocol-that-follows.md, 06b-the-bot-in-the-witness-box.md]
terms: [Record, Keyholder, Witness and Oracle]
---

# The reading record: what an AI read, when, and who relied on it

> The project proposes a record for every bot reading someone relies on. It is a proposal. In the human book this is kept backstage, as methodology; here it is set out in full.

## In short

- **Fields:** the documents read, by fingerprint; the bot, its version, its prompt and settings; what it found and flagged; when; who asked; who chose to rely on it and with what reason.
- **Chained:** each entry carries the fingerprint of the one before, so a later edit would show.
- **Two copies:** bidders will keep a record only if it is theirs, so the buyer and each bidder keep their own.
- **Where it sits:** the record is a clause in two of the book's three standards, the tool test and the [sign-off](bp-sign-off.md), not a standard of its own. Without it the test cannot be rerun and the sign-off has nothing to point at.
- **Purpose:** after a loss, each side tells the story differently; only the record settles whether the bot's price was wrong or the bidder built badly.

## Why it matters more than accuracy

An accurate bot without a record cannot defend a single number after the fact. A less accurate bot with a record can show exactly what it read and what it said, and a court can rerun it. The project's legal research points the same way: in the first US challenge over an agency's AI-assisted evaluation, the court ordered the AI evaluations into the record ([the Trax case](bp-trax-case.md)). Considered AI output is becoming part of the procurement record whether anyone designed for it or not.

## What the evaluator records

The project's planned [Fair and Reasonable Evaluator](bp-evaluator.md) logs each request: who asked, when, which version of the model answered, which past tenders each price cites (contract, date, item, prices), what was flagged, and what the named reviewer decided and why.

## The bidder's fear

A record that proves a clerical slip also proves that the firm's bot saw an error in the drawings and the firm said nothing. That is why bidders will want their own sealed copy, and why the book treats disclosure of errors as the bidder's decision, not the bot's ([stakeholder: bidders](bp-stakeholder-bidders.md)).

## Aside: Witness and Oracle

When outsiders see a bot's results, the project's design splits the bot in two: a Witness that reads the records and an Oracle that checks what leaves and never touches the files. A buyer running a plain program on its own records needs a simpler safeguard: the AI writes and tests the program on public data, and only the code moves onto the buyer's computer.

## Aside: a public log without a currency

A fingerprint of each issued document, written to a public, append-only, timestamped log that nobody in the tender controls, proves which version existed when. A transparency log of the kind used for web certificates does this without any blockchain or currency.
