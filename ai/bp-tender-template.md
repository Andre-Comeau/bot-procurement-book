---
id: bp-tender-template
title: "The tender template: tender documents written for machines"
type: proposal
status: draft
summary: >
  The project's proposal for a tender package a bot can read without guessing: plain text, Markdown for
  the parts people read, JSON for the parts machines count, an identifier on every requirement, a shared
  name for every pay item, and a new version of the file for every addendum, while the engineer still
  certifies the canonical copy. It is a proposal; no buyer issues tenders this way yet.
updated: 2026-11-19
audience: [buyers, designers, standard writers, AI vendors, bidders]
questions:
  - What would a machine-readable construction tender look like?
  - Why are PDF tender documents a problem for AI?
  - How would a tender template fit with the Open Contracting Data Standard?
  - Does a machine-readable tender replace the sealed drawings?
related:
  - {id: bp-overview, relation: part-of}
  - {id: bp-pdf-zombie, relation: answers}
  - {id: bp-reference-bot, relation: supports}
  - {id: bp-reading-record, relation: see-also}
  - {id: bp-existing-standards, relation: depends-on}
  - {id: bp-stakeholder-designers, relation: see-also}
  - {id: bp-tender-as-interface, relation: see-also}
  - {id: bp-why-not-change-contract-type, relation: see-also}
  - {id: bp-sign-off, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 17, 'The protocol that follows'", url: "https://books.andrecomeau.xyz/bot-procurement/working/09-the-protocol-that-follows/"}
  - {title: "Bot Procurement (book in draft), chapter 5, 'The zombie lost to a file format'", url: "https://books.andrecomeau.xyz/bot-procurement/working/08b-the-zombie-lost-to-a-file-format/"}
  - {title: "GAEB, certification of data-exchange software", url: "https://www.gaeb.de/de/produkte/gaeb-datenaustausch/zertifizierung/"}
book: [09-the-protocol-that-follows.md, 08b-the-zombie-lost-to-a-file-format.md, 00c-introduction.md]
terms: [Template, PDF zombie (the zombie garden), Tender]
allow_words: [certified, certifies]
---

# The tender template: tender documents written for machines

> The project proposes a tender format written for machines, kept beside the engineer's certified copy. It is a proposal; no buyer issues tenders this way yet.

## In short

- **Plain text.** Markdown for what people read, JSON for what machines count.
- **Identifiers.** Every requirement carries one, every pay item a name from a shared list.
- **Versions, not piles.** Every addendum is a new version of the file, so two versions can be compared line by line.
- **Fingerprints.** Each version gets a fingerprint (a hash), so anyone can later prove which version a bot read.
- **The seal stays.** Engineers and architects still certify the canonical copy; the template is the copy a bot reads.

## Why the PDF fails a bot

A PDF tender is a picture of paper. Machines read its tables and drawings unreliably, it carries no metadata a bot can use, and two bots can extract two different quantity tables from the same page. It survives because it inherited the stamped paper set's place in law: it is the frozen copy a court reads ([the PDF zombie](bp-pdf-zombie.md)). The template does not fight that. It adds a second, machine-readable copy whose fingerprint is tied to the sealed one.

## What a pay item looks like

From the book's example:

```json
{"item": "Excavation, common", "unit": "m3", "quantity": 1250,
 "requirement": "02-310-3.2", "version": "addendum 2"}
```

Nothing in it is new technology. A bidder's bot can read it without guessing, a person can read it without software, and two versions can be diffed.

## How it fits existing standards

- **Open Contracting Data Standard (OCDS).** OCDS records a public contract from plan to payment and is published by governments today. It carries the tender documents only as links; a bill of quantities can be attached as a document, but its lines are not modelled. The template is designed to hang off the OCDS frame rather than build a second one ([existing standards](bp-existing-standards.md)).
- **Germany's GAEB.** German public tenders have travelled as data files since the 1980s under a format kept by a public committee since 1966; buyers can require it and software reading it is certified. GAEB shows a tender-as-data standard can work at national scale. It does not publish a price error for any bot that reads it.
- **United States highways.** State transportation agencies measure their own designs and issue pay items with quantities; on the lettings of 44 state agencies that list arrives as a data file, bidders return unit prices in a free program the states own together through their national association, and an addendum is a new version of the same file. Only the drawings and specifications are still read as pages. North American building work, by contrast, still tenders mostly as PDFs that every bidder measures for itself.

## Who pays for it

The designer carries more cost and more risk, because paper can be checked by eye more easily than a model. The book's answer is that the template is cheap (plain text), that buyers can phase it in item by item starting with pay items, and that a richer building model could later become the specification itself.

## Aside: the zombie that lost to a file format

In March 2019 a German firm sent the cheapest bid for a public contract and lost it over a file. The buyer had asked for the priced bill as a GAEB data file; the firm sent PDFs and was excluded. In 2023 the Federal Court of Justice held that the electronic means a buyer asks for are part of a bid's form, as much as a signature, and sent the case back; in 2024 the court in Cologne found the exclusion lawful. The lesson the project draws: a format wins when a buyer can require it, a court upholds the requirement, and a market of programs competes to read it. All three are needed; a good format alone does not move a market.
