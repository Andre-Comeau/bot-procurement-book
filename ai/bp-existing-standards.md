---
id: bp-existing-standards
title: "Standards near AI construction price checks: OCDS, ISO 10845, GAEB and AI frameworks"
type: evidence
status: draft
summary: >
  Several standards sit next to Bot Procurement and none covers its question. The Open Contracting Data
  Standard records public contracts but links tender documents only as files; ISO 10845 fixes
  procurement procedure; Germany's GAEB makes tenders data files; AI frameworks such as AIUC-1 and the
  NIST AI RMF cover controls but set no price-accuracy test. None computes or checks a price, or
  publishes how far a bot that reads the tender misses.
updated: 2026-11-19
audience: [standard writers, researchers, lawyers, buyers]
questions:
  - Is there an existing standard for AI in construction procurement?
  - Does the Open Contracting Data Standard include bills of quantities?
  - What is GAEB?
  - How does Bot Procurement relate to AI standards like AIUC-1 or the NIST AI RMF?
related:
  - {id: bp-tender-template, relation: supports}
  - {id: bp-reference-bot, relation: see-also}
  - {id: bp-procurement-machines, relation: see-also}
  - {id: bp-stakeholder-insurers, relation: see-also}
  - {id: bp-why-not-existing-software, relation: see-also}
sources:
  - {title: "ISO 10845-1:2010, Construction procurement: Processes, methods and procedures", url: "https://www.iso.org/standard/46190.html"}
  - {title: "Open Contracting Data Standard", url: "https://standard.open-contracting.org/"}
  - {title: "GAEB, certification of data-exchange software", url: "https://www.gaeb.de/de/produkte/gaeb-datenaustausch/zertifizierung/"}
  - {title: "Bot Procurement (book in draft), chapter 17, 'The protocol that follows'", url: "https://books.andrecomeau.xyz/bot-procurement/working/09-the-protocol-that-follows/"}
book: [09-the-protocol-that-follows.md, 08b-the-zombie-lost-to-a-file-format.md]
terms: [Template]
allow_words: [certified, certifies]
---

# Standards near AI construction price checks: OCDS, ISO 10845, GAEB and AI frameworks

> Every standard below stops at the edge of the question Bot Procurement asks: how far does a bot that reads a tender miss, and who stands behind its reading?

## In short

| Standard | What it fixes | What it leaves out |
|---|---|---|
| **Open Contracting Data Standard (OCDS)**, v1.0 2015; infrastructure version (OC4IDS) with CoST, 2019 | A public contract's record from plan to payment, including changes and their reasons | The tender documents themselves: linked as files (a bill of quantities can be attached with code `billOfQuantity`), lines not modelled |
| **ISO 10845** (2010), built on South Africa's national standards | Procurement procedure | Any computation or check of a price |
| **GAEB** (Germany), public committee since 1966, data files since the 1980s | The tender as data, file by file from invitation to invoice; programs certified per version for five years | A published error for any bot or program that prices the file |
| **US highway bid files** (44 state agencies) | Pay items and quantities as a data file; bids returned in a shared program | Drawings and specifications, still pages; any price-error standard |
| **AIUC-1** | Controls for AI products: owners, failure plans, change approval, tamper-evident logs, disclosure, third-party testing | A numeric accuracy test |
| **NIST AI Risk Management Framework** | A general structure for governing AI risk | Anything specific to tenders or prices |

## Why OCDS is the closest ally

OCDS gives each contracting process an identifier and a shape that governments already publish; Ukraine's public buying system publishes in it, and the infrastructure version adds the project and the changes to its contracts. It stopped at the tender documents, probably wisely: those are where each country keeps its own law, trade customs and units. The project's [tender template](bp-tender-template.md) is designed to hang off the OCDS frame rather than build a second one. The project's search of the open-contracting discussions found no proposal yet to model bills of quantities or pay items.

## Two ways standards get made

ISO 10845 took the formal path: national standards that already worked, then an international one, with a subcommittee set up in 2015 to maintain it. OCDS took the other: a small team, a working format, governments joining one at a time. The project expects to need both: running code first, a committee after.

## Aside: AI frameworks as the backbone

The project's research suggests the AI controls standards and insurers' product measurements cover two different halves of what Bot Procurement needs: AIUC-1 the controls (who owns the bot, how changes are approved, how logs are kept), an insurer such as Munich Re the numbers (how far a product misses, measured one product at a time). The construction part would then be a profile on top of both rather than a standard built from nothing.
