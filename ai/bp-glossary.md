---
id: bp-glossary
title: "Glossary of AI construction procurement terms (Bot Procurement), one meaning each"
type: reference
status: draft
summary: >
  The terms used across the Bot Procurement modules, each with one meaning. Where a module uses one of
  these terms, it means what this glossary says. Bot Procurement itself is a proposal; its test has not been run.
updated: 2026-11-25
audience: [everyone]
questions:
  - What does a term used in Bot Procurement mean?
  - What is a keyholder?
  - What is a reference bot?
  - What is the difference between Bot Procurement and Bot Construction?
  - What is a bid spread?
  - What is a construction surety?
related:
  - {id: bp-faq-answers, relation: see-also}
  - {id: bp-overview, relation: see-also}
  - {id: bp-pdf-zombie, relation: see-also}
  - {id: bp-two-names, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), appendix C, 'Glossary'", url: "https://books.andrecomeau.xyz/bot-procurement/working/app-c-glossary/"}
book: [app-c-glossary.md]
---

# Glossary of AI construction procurement terms (Bot Procurement), one meaning each

> Every Bot Procurement module uses these terms in the meanings below. Bot Procurement itself is a proposal; its test has not been run and no standards body has adopted it.

Each heading carries an anchor, so a term can be cited as `bp-glossary.md#<anchor>`. Where a term names something the project proposes, the definition says "proposal" in the same sentence.

### Bot Procurement {#bot-procurement}
A proposal, made in 2026 by a public project, for how a bot that prices or checks a construction bid could be relied on, through three standards: documents written for machines to read (the template), a public test of the bot (the tool test), and a sign-off by the person who relies on its reading. It is also the name of the book that argues for it. Bot Procurement is a proposal; its test has not been run.

Not to be confused with procurement of bots (buying AI software); the proposal is about bots used inside procurement.

### Bot Construction {#bot-construction}
The wider field Bot Procurement belongs to: construction work arranged, priced, administered and eventually built with bots, from documents written for machines to robots on site, built on what the trades already know. Bot Construction is where the work leads; Bot Procurement is the part kept small enough to test first.

### Tender {#tender}
The package a buyer issues to invite priced offers for construction work (drawings, specifications, a list of pay items with quantities, and the conditions of contract), and the competition that follows until the bids are opened.

Also called: solicitation, bid package, invitation to tender.

### The tender as the interface {#tender-as-interface}
The book's picture of the tender as the single point of contact between the design side and the building side, like a software interface: each side answers through it and neither has to show the other its internal workings. The bill of quantities is the call; the bid is the answer.

### Change (change order) {#change}
A priced alteration to the work after the contract is signed. Because only the builder already on site can practically do the work, every change is a purchase from a supplier of one, and the buyer has to justify the price without a market.

### Fair and reasonable {#fair-and-reasonable}
The test a public buyer applies to a price it cannot get from competition, such as a change: a written justification that the price is in line with what the work should cost, built from past tenders, price books and judgment.

### Engineer's estimate {#engineers-estimate}
The price a buyer's own engineers put on the work before the tender, used to judge the bids.

### Estimator (the project's) {#estimator}
A pricing bot the project is building, which will estimate the price of each line of a tender from past public bids. It is in development. Its early versions were checked on public Texas highway bids (see BP-CLAIM-005).

### Fair and Reasonable Evaluator {#evaluator}
A checking bot the project plans to build on the estimator, which will price each line of a change, compare it with what the market has paid, flag lines that are unusually high or low, and draft the fair-and-reasonable memo for a named person to decide and sign.

### Second opinion {#second-opinion}
What a pricing bot's number is until its error is small enough and well enough known to stand on its own: a check beside the engineer's estimate and the reviewer's judgment, not a replacement for them.

### Keyholder {#keyholder}
The named person who reviews a bot's draft, adjusts the flagged lines, decides and signs, with a reason. A flag is sent to a keyholder; a bot does not sign.

### Flag {#flag}
A written note from a bot that a price, an item or a document needs a person's decision, sent to someone whose job it is to act on it. The book's rule of thumb: a flag without an owner is a flag nobody reads.

### Reference bot {#reference-bot}
A published, versioned bot whose reading of a tender others can rerun and get the same answer, proposed as the measure against which any other bot's reading is judged, in the way the reasonable person is the measure for people. A proposal; no reference bot has been adopted.

Also called: standard bot, reasonable bot.

In the book: Reference bot (standard bot).

### Reasonable bot {#reasonable-bot}
The legal idea the book proposes: a standard of conduct for a bot's reading of a tender, modelled on the reasonable person of the common law, and given a concrete form by the reference bot.

### Template {#template}
The proposed form of a tender written for machines: plain text, Markdown for the parts people read, JSON for the parts machines count, an identifier on every requirement, a shared name for every pay item, and a new version of the file for every addendum. A proposal.

In the book: Template (tender template).

### Record {#record}
The entry kept for each bot reading someone relies on: which documents were read (by fingerprint), which bot and version, with what settings, what it found, when, and who chose to rely on it. It is what lets a dispute be settled after a loss. A proposal; it is a clause in the tool test and the sign-off rather than a standard of its own.

In the book: Record (run record).

### Tool test {#tool-test}
The second of Bot Procurement's three standards: a public set of tenders a pricing bot has never seen, one fixed way of scoring its prices against what bidders bid, and a published miss rate with a tolerance around it. A proposal; it has not been run, and its tolerance waits for evidence from the project's estimator.

### Sign-off {#sign-off}
The third of Bot Procurement's three standards: before relying on a bot's reading of a tender, a named person confirms that the bot passed the tool test for that kind of work, that it read the version of the documents that governs, and that someone able to overrule it looked at what it found, then puts their name to the reading. A proposal.

### PDF zombie (the zombie garden) {#pdf-zombie}
The book's image for tender documents issued as PDFs: dead as a technology, still walking as a protocol, because the PDF inherited the stamped paper set's place in law. It is safe (nothing changes) and has no liveness (nothing can grow). The garden is the set of practices built to live with them.

### Witness and Oracle {#witness-oracle}
A design for an owner's bot split in two: the Witness reads the records; the Oracle checks what leaves and never touches the files. Used when outsiders see a bot's results.

### Listener {#listener}
A proposed buyer-side bot that collects bidders' questions during a tender, whether from people or bots, and may answer only by signs: the equivalent of a head bow, a shake or a shrug.

### Buyer as its own insurer {#buyer-as-insurer}
The book's base case for who carries the risk of relying on a reference bot: the buyer stands behind the reference price itself, under a rule fixed before the bids open, with third-party insurance for the smaller buyers and bidders it would not cover. A proposal.

### Margin insurance {#margin-insurance}
A proposed insurance product for bidders who rely on an estimating bot: it pays when the bot's bids keep falling short of a target margin across many tenders, measured against costs the bidder declared on bid day, not when one job loses money. No insurer offers it.

### Patent and latent errors {#patent-latent}
Errors in tender documents that a careful bidder should see (patent) and those it could not reasonably find (latent). Tender law treats them differently, and a reference bot would sharpen the line between them.


### Bill of quantities {#bill-of-quantities}
A list of every item of work in a tender with its measured quantity, so that each bidder prices the same list. Highway agencies call the items pay items, and their bids already travel as a price per item.

### Hard bid {#hard-bid}
A tender won on price alone, usually as a lump sum, by the lowest bidder that meets the terms.

### Lump sum {#lump-sum}
One price for the whole of the work, or for a few large parts, instead of a price for each line. A lump-sum contract gives a price check no line prices to compare, so the check first has to break the work into parts it has seen before.

### Slack {#slack}
Time, money and cushion kept between the parts of a system so that nobody has to know everything: the long tender period, the bidder's cushion for errors in the drawings, the contingency. The book argues for more capacity to read instead of more slack.

### Cap, key, fee and published check {#four-answers}
The four ways software handles a flood of requests, used in the book for a flood of AI-written bids: a cap limits how many anyone may send (construction's shortlist), a key decides who may send (prequalification), a fee makes each sender pay (the bid bond and the cost of bidding), and a published check tests every request against rules everyone can read. Bot Procurement builds on the published check.

### Thicket {#thicket}
The crowd of new bids that springs up once preparing a bid becomes nearly free, as a thicket fills the clearing where an old oak fell. The oak is the old cost of bidding, which kept the stack of bids small enough for a committee to read.

### Stipend {#stipend}
A payment from the buyer to losing bidders on a large job, to cover part of what their bids cost to prepare. United States design-build rules allow it.

### Bid depository {#bid-depository}
An office that receives trade contractors' sealed prices on bid day, stamps them with its own clock and passes them to the general contractors bidding the job. Some Canadian provinces and territories run them.

### Bid spread {#bid-spread}
The gap between the lowest bid and the next one, as a percentage. Bonding companies (sureties) read it first: one large bonding company asks its contractor for a letter of explanation when the next bid is more than 10 percent higher. On US highway contracts that happens on about a third of contracts ([sureties](bp-sureties.md)).

### Surety {#surety}
The industry's word for a bonding company: a company that guarantees a builder's promise to the buyer through a bid bond and, if the builder wins, performance and payment bonds. The builder and its owners sign an indemnity agreement to repay any loss, so a surety underwrites the firm rather than the price ([sureties](bp-sureties.md)).

### Jigbot {#jigbot}
A robot a tradesperson sets up and teaches for the task at hand, the way they would build a jig: a device that holds the work and the tool in the right relation so a hard cut can be repeated safely. The setting stays with the person who made it. A term the book proposes.

### Bot admin {#bot-admin}
The project's name for the far stage where machines keep track of the work and the documents on a project, not the people. It replaced "bot monitoring".
