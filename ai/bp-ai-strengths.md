---
id: bp-ai-strengths
title: "What AI does well in procurement: averages, speed and reading"
type: risk
status: draft
summary: >
  AI's strengths for tender work are the other side of its weaknesses. It finds averages across far more
  past prices than a person can hold, works at a speed no office can match, and reads messy documents
  well enough to match new work to similar past work. Because it works on probabilities, its error can be
  made small and measured but never zero, which is why the project pairs it with a named reviewer and a
  published error.
updated: 2026-11-19
audience: [everyone, buyers, estimators, insurers, AI vendors]
questions:
  - What is AI good at in construction procurement?
  - Can AI read old tender documents and turn them into data?
  - Why can AI estimating error never reach zero?
  - Are general AI models as good as specialised tools?
related:
  - {id: bp-ai-failure-modes, relation: contrasts}
  - {id: bp-estimator, relation: see-also}
  - {id: bp-margin-insurance, relation: see-also}
  - {id: bp-why-not-existing-software, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 3, 'The insurable event'", url: "https://books.andrecomeau.xyz/bot-procurement/working/06e-the-underwriters-chapter/"}
  - {title: "Bot Procurement (book in draft), chapter 16, 'A second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Vals AI, legal research benchmark, October 2025, as reported by LawNext, 23 October 2025"}
book: [06e-the-underwriters-chapter.md, 07-building-an-estimator-in-public.md, 02d-the-vendors.md]
terms: [Estimator (the project's), Second opinion]
---

# What AI does well in procurement: averages, speed and reading

> The strengths and the weaknesses are one property seen from two sides: a model that predicts from probabilities is fast and broad, and is never exactly right.

## In short

- **Averages:** a model can draw on every past price for similar work, not the handful a person remembers. On the project's own development checks, its [estimator](bp-estimator.md) missed the average of the three lowest bids by a median of 21 percent line by line, against 29 percent for the state engineer's estimate. These are the project's own figures, made while choosing between versions, and nobody outside has rerun them.
- **Speed:** a reading that takes an office days takes a bot minutes, so a check can run on every price instead of a sample.
- **Reading:** general assistants can already read a messy bid summary and fill a standard table from it. That opens a way out of the problem of old tenders locked in PDFs ([the PDF zombie](bp-pdf-zombie.md)), with a person checking each converted file.
- **Matching work to similar work:** where a contract is priced as lump sums rather than line by line, pricing a change means finding past work that looks like it and combining those prices. That is reading, not arithmetic, and it is where AI earns its place.
- **The limit that comes with it:** error can be measured and reduced, never removed. The tails stay, and the project's answer is to publish the error and decide who carries it ([margin insurance](bp-margin-insurance.md), [the buyer as its own insurer](bp-buyer-as-insurer.md)).

## Why zero error is the wrong goal

The book's underwriters' chapter puts it this way: bringing a pricing bot's error to zero would lose the prediction that makes it useful. Its strength lies in discovering averages and reaching answers at superhuman speed; the tails are part of the product. The practical questions are how big the usual miss is, who reads the flags outside it, and where an underwriter draws the line between error that comes with the product and a defect.

## Aside: general models against specialised tools

The one head-to-head comparison the project has found comes from another profession. In a 2025 legal research benchmark (Vals AI), a general AI model scored about 80 percent, specialised legal tools 79 to 81 percent, and practising lawyers 71 percent. The specialists kept a small edge on citing the right authority (76 against 70 percent), drawn from their own databases. The project's reading: the data was the advantage, the writing was not. If the same holds in construction, a general model with access to open bid data could match a specialised estimating tool, which is why the project cares about a public test that any tool can take ([the reference bot](bp-reference-bot.md)).

## Aside: what the strengths do not cover

Speed and breadth do not make a reading accountable. A bot cannot sign, and a court will ask what a person considered ([TRAX v United States](bp-trax-case.md)). The project's design keeps a named person on every decision and treats the bot's price as a [second opinion](bp-glossary.md#second-opinion).
