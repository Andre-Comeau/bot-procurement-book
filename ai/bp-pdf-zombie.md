---
id: bp-pdf-zombie
title: "The PDF zombie: why construction tenders are still PDFs"
type: problem
status: draft
summary: >
  Construction tender documents still travel as PDFs because the PDF inherited the stamped paper set's
  place in law: it is the frozen copy a court reads. The book calls it an undead protocol, safe but
  without liveness, and the practices built around it a walled garden. Bots read it unreliably, which
  is why the project proposes a machine-readable copy beside it.
updated: 2026-11-19
audience: [everyone, buyers, designers, AI vendors]
questions:
  - Why do construction tenders still use PDF documents?
  - What is the "zombie garden"?
  - Why is the PDF a problem for AI in procurement?
related:
  - {id: bp-tender-template, relation: answers}
  - {id: bp-tender-as-interface, relation: see-also}
  - {id: bp-glossary, relation: see-also}
  - {id: bp-why-not-existing-software, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 15, 'What AI gets right'", url: "https://books.andrecomeau.xyz/bot-procurement/working/00c-introduction/"}
  - {title: "William H. Sewell Jr., 'Three Temporalities: Toward an Eventful Sociology', in Logics of History (2005)"}
book: [00c-introduction.md]
terms: [PDF zombie (the zombie garden)]
---

# The PDF zombie: why construction tenders are still PDFs

> As a technology the PDF died with the fax machine. As a protocol it keeps walking, because it carries the seal.

## In short

- Standard paper sizes let printers, copiers and fax machines produce an analog final copy of a digital product; the PDF carried that paper sheet into the digital age.
- The paper set carries the engineer's seal and the contract's signatures, so the file inherited the paper's place in law: stamped, issued, frozen, and read by a court when a dispute arrives.
- A protocol owes its users safety (nothing bad happens) and liveness (something good eventually happens). The PDF has safety in abundance and no liveness: it cannot be modified. That is what makes it undead.
- Construction procurement built a walled garden of practices to control the damage and refuses to kill the zombies. Only the people who live with them, buyers, consultants, bidders and courts, can decide to.

## What it costs

Every drawing, specification and addendum is a file that needs zooming on a phone, wastes screen space on margins, and resists both human and AI reading. People count take-offs by hand, retype quantities from one document into another, and hunt through three addenda for the one that changed a detail. The book calls this the cognitive serfdom of documentation; freeing people from it is the treasure the project is after.

## Why the garden is hard to leave

The garden is slow, but it moves information between buyers and bidders reliably, and the courts have settled most of its disputes. Anyone proposing to replace it has to keep what it guarantees: one frozen, sealed, citable copy. The project's answer keeps the sealed copy and adds a machine-readable one tied to it by fingerprint ([the tender template](bp-tender-template.md)).

## Aside: an eventful explanation

The book borrows William Sewell's idea that social mechanisms are best explained by the order of events. The PDF's dominance in contracting is a relic of past events (paper standards, fax machines, the seal), not the result of anyone's design or experiment. That matters for strategy: a relic falls to a new event, such as a court upholding a buyer's demand for data files, as happened in Germany in 2023 ([the tender template](bp-tender-template.md#aside-the-zombie-that-lost-to-a-file-format)).

## Aside: the treasure

The book's list of what killing the zombie would release: productivity in construction, lower costs and wider options; certainty when reviewing a bidder's sealed alternate, because a standard bot reads the alternate the same way the buyer does; and above all the release of people from documentation to exploration, creation and community building.
