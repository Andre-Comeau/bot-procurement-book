---
id: bp-faq-answers
title: "AI construction procurement in short answers: twenty-four questions"
type: reference
status: draft
summary: >
  Short answers to the questions people most often ask about Bot Procurement, each in a few sentences,
  each linked to the module that explains it.
  Bot Procurement is a proposal; its test has not been run and no standards body has adopted it.
updated: 2026-11-24
audience: [everyone]
questions:
  - What are the short answers about Bot Procurement?
  - What are the four answers to a flood of AI-written bids?
  - What is slack in construction bidding?
  - Who would pay for the estimator and the evaluator?
  - How was the project's estimator checked?
  - Does the evaluator only cut prices?
  - What is margin insurance for bidders?
  - Does Bot Procurement want to replace estimators or reviewers?
  - Where do the book's facts come from?
related:
  - {id: bp-overview, relation: see-also}
  - {id: bp-glossary, relation: see-also}
sources:
  - {title: "Neil Clarke, 'A Concerning Trend', Clarkesworld editor's blog, 15 February 2023", url: "https://neil-clarke.com/a-concerning-trend/"}
  - {title: "NPR, 'A sci-fi magazine has cut off submissions after a flood of AI-generated stories', 24 February 2023", url: "https://www.kunc.org/npr-news/2023-02-24/a-sci-fi-magazine-has-cut-off-submissions-after-a-flood-of-ai-generated-stories"}
  - {title: "European Court of Auditors, Special Report 28/2023, Public procurement in the EU", url: "https://www.eca.europa.eu/ECAHTMLNews/NEWS-SR-2023-28/en/body.html"}
  - {title: "Auditor General of Ontario, Annual Report 2024, 'Procurement and Delivery of Selected Infrastructure Projects'", url: "https://www.auditor.on.ca/en/content/annualreports/arreports/en24/pa_infrastructureON_en24.pdf"}
  - {title: "Bot Procurement (book in draft), chapter 16, 'A second opinion on every price' (the project's own checks on public Texas data; the review-cost figures are the author's experience)", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Rocha, Rezende and Oliveira, 'Alice: desafios, resultados e perspectivas...', Revista da CGU 14(26), 2022", url: "https://revista.cgu.gov.br/Revista_da_CGU/article/download/530/357"}
  - {title: "OECD, DAF/COMP/WP3/WD(2022)31, note by Korea", url: "https://one.oecd.org/document/DAF/COMP/WP3/WD(2022)31/en/pdf"}
  - {title: "Washington Technology, 'Trax loses White Sands protest, but judge hits government over AI disclosures', September 2026", url: "https://www.washingtontechnology.com/contracts/2026/09/trax-loses-white-sands-protest-judge-hits-government-over-ai-disclosures/416334/"}
  - {title: "TRAX International Corp. v. United States, No. 26-796 (Fed. Cl. 2026), opinion", url: "https://www.washingtontechnology.com/media/general/2026/9/trax_army_ai_protest_ruling_20260922.pdf"}
  - {title: "Open Contracting Data Standard", url: "https://standard.open-contracting.org/"}
  - {title: "Open Contracting for Infrastructure Data Standard (OC4IDS), Open Contracting Partnership and CoST", url: "https://standard.open-contracting.org/infrastructure/"}
  - {title: "Open Contracting Partnership, 'The OC4IDS: a new standard for infrastructure transparency', 17 April 2019", url: "https://www.open-contracting.org/2019/04/17/the-oc4ids-a-new-standard-for-infrastructure-transparency/"}
  - {title: "ISO 10845-1:2020, Construction procurement, Part 1: Processes, methods and procedures (first published 2010)", url: "https://www.iso.org/standard/72467.html"}
  - {title: "buildingSMART, IFC schema specifications (IFC 4.3 ADD2 = ISO 16739-1:2024)", url: "https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/"}
  - {title: "buildingSMART, 'Information Delivery Specification (IDS) v1.0 is approved as a final standard', 4 June 2024", url: "https://www.buildingsmart.org/information-delivery-specification-ids-v1-0-is-approved-as-a-final-standard/"}
  - {title: "Bot Procurement (book in draft), chapter 17, 'The protocol that follows' (the 2035 test is the project's own forecast)", url: "https://books.andrecomeau.xyz/bot-procurement/working/09-the-protocol-that-follows/"}
book: [00b-prologue.md, 02-the-tender-is-the-api.md, 06e-the-underwriters-chapter.md, 07-building-an-estimator-in-public.md, 09-the-protocol-that-follows.md]
terms: [Bot Procurement, Estimator (the project's), Fair and Reasonable Evaluator, Keyholder, Margin insurance, Buyer as its own insurer]
---

# AI construction procurement in short answers: twenty-four questions

> Bot Procurement is a proposal, made in 2026 by a public project. Its test has not been run and no standards body has adopted it. Each answer below is a summary; the linked module has the detail and the sources.

## The idea

**What is Bot Procurement, in one sentence?**
A proposal for how a bot that prices or checks a construction bid could be relied on, by documents written for machines to read, a published bot that reads them the same way every time, and a record of each reading someone relied on. See [the overview](bp-overview.md).

**What question does the book ask?**
Who is liable when a bot gets a construction price wrong? Today the answer is usually nobody but the bidder, because software vendors' terms disclaim the result. The book's answer starts with the buyer standing behind a published price. See [the liability gap](bp-liability-gap.md).

**Why now?**
Because AI makes preparing a bid nearly free. A science-fiction magazine closed its submissions in February 2023 when machine-written entries swamped it, and public buyers already draw fewer bidders on large projects than they did a decade ago. A process built for a handful of bids cannot read a flood. See [the tender as interface](bp-tender-as-interface.md).

**What are the four answers to a flood of AI-written bids?**
Software has four: a cap on how many anyone may send, a key that decides who may send, a fee for each request, and a published check that tests every request against rules everyone can read. Construction already has a twin for each (the shortlist, prequalification, the bid bond and bid reviews with written reasons). Bot Procurement builds on the published check, because the other three shut out honest bidders too. See [the glossary](bp-glossary.md#four-answers).

**What is slack in construction bidding?**
The cushion a system keeps so nobody has to know everything: long tender periods, a bidder's allowance for errors in the drawings, the contingency. The book argues for more capacity to read the documents instead of more slack. See [the glossary](bp-glossary.md#slack).

## The tools

**What will the estimator do?**
It will put a price on each line of a tender from what bidders have charged for the same items before, as a second opinion before the tender closes. It is in development. See [the estimator](bp-estimator.md).

**How accurate is it so far?**
On public Texas highway data, line by line, it missed the average of the three lowest bids by a median of 21 percent, against 29 percent for the state's own engineer's estimate. For a whole contract it typically missed by about 10 percent, level with the engineer's estimate. On the same lines the three lowest bidders disagreed with each other by a median of 50 percent. See [estimate accuracy](bp-estimate-accuracy.md).

**How was the project's estimator checked?**
It learned from Texas contracts let before May 2026 and was scored on contracts let after, which it had not learned from. Three versions were scored on the same contracts, each built knowing how the last did, so the figures probably flatter it a little. A check on newer contracts, left alone so far, waits until there is a product and someone who wants the answer. See [the estimator](bp-estimator.md).

**What will the evaluator do?**
It will check the price of a change after the contract is let: price each line from past tenders, cite every tender it used, flag items it has seen too rarely, and draft the fair-and-reasonable memo for a named person, the keyholder, to decide and sign. See [the evaluator](bp-evaluator.md).

**Does the evaluator only cut prices?**
No. It is meant to ask the same question of a change priced too low as of one priced too high, and the book says plainly that a pair of bots that only ever cut would give every contractor a reason to claim. A change approved in days instead of weeks is also paid sooner. See [the evaluator](bp-evaluator.md).

**Who would pay for the estimator and the evaluator?**
The first payer is a buyer: the evaluator's savings arrive after the tender, in reviews not paid for and claims never started, which a buyer can count. The review bill the book cites ($7,500 to $20,000 per million dollars of work) is the author's experience, not a survey. See [the change-pricing problem](bp-change-pricing-problem.md).

**Why not just use existing estimating software?**
Most of it is built for bidders, to check they have not bid too low, and it needs structured data that owners' records rarely have. See [why not existing software](bp-why-not-existing-software.md).

## People and risk

**Does Bot Procurement want to replace estimators or reviewers?**
No. Every design in the book ends with a named person who decides and signs, and the bot's job is to draft and cite. Korea's and Brazil's tender-screening machines sat nearly unused because no one was obliged to act on their flags. See [procurement machines](bp-procurement-machines.md).

**What happens when an AI misreads a tender?**
Today the bidder carries it. The book sorts AI failures into four kinds, by whether words or deeds went wrong and whether anyone meant it, and gives each a remedy; a published reading of the tender narrows all four. See [AI failure modes](bp-ai-failure-modes.md).

**Who carries the risk under the proposal?**
In the base case the buyer runs the published bot, publishes its number, and carries the loss if the number was wrong, so no insurer is needed. See [buyer as insurer](bp-buyer-as-insurer.md).

**What is margin insurance for bidders?**
A proposed policy that would pay part of the shortfall when the average margin across a bidder's covered contracts falls below its target, so one losing job does not trigger it. No insurer offers it yet. See [margin insurance](bp-margin-insurance.md).

**Has any court looked at AI in a public tender?**
Yes, once so far. In Trax v. United States (2026) a losing bidder challenged a US Army award; the court ordered the agency's AI evaluations into the record and let the award stand. See [the Trax case](bp-trax-case.md).

**Could a shared reference price help bidders collude?**
It could, which is why the project's rule is to check and record a price, never to set one. See [competition risk](bp-competition-risk.md).

## The standard and the road ahead

**Is there a standard yet?**
No. There is a draft, and the project's plan is to bring something working to existing standards bodies rather than write a new one alone. See [existing standards](bp-existing-standards.md).

**Which existing standards does it build on?**
The Open Contracting Data Standard for the record of a public contract, its infrastructure version written with CoST in 2019, ISO 10845 for procurement procedure, and the open formats for building models (IFC and IDS). See [existing standards](bp-existing-standards.md).

**What would a machine-readable tender look like?**
The items, units and quantities written as plain data beside the PDF, so a bot can read them without guessing and a person can read them without software. The sealed drawings stay. See [the tender template](bp-tender-template.md).

**When would we know the idea has failed?**
The book commits to a test: if by 2035 no public owner anywhere runs a tender whose questions, addenda, bids and evaluation pass through agents on a published data format, the forecast failed. See [the future](bp-future.md).

**Where does this lead?**
Past the standard lie documents written for machines, bots that keep track of the work rather than the people, and robots on site set up by the trades who use them. See [the future](bp-future.md).

**Where do the book's facts come from?**
Each module lists its sources in its front matter, with a link where one exists, and the book's sources are in its bibliography (Appendix D). Claims that rest on the author's experience or on the project's own data are labelled that way in the text. See [the overview](bp-overview.md).
