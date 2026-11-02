# Bot Procurement Book: outline

Oct 28, 2026 · @Andre

## The book in one paragraph

A short manifesto, about 10,000 words of main text, that asks one question: how do you know a construction price is fair and reasonable, and what happens to procurement when a bot can answer that? It argues that tendering is a set of tensions to be managed, not problems to be solved, that the next procurement machine is a bot-first tender, and it shows the author building the tools that test the claim. The size is Chic Sale's *The Specialist*: short enough to read for pleasure in an evening, serious enough to hand to a public owner, a standards body or a sponsor. About 40 percent is the author's existing sentences from the public repository, redrafted; the rest is new writing, most of it the chapter on the Fair and Reasonable Evaluator. The Procurement Machines cards are an illustrated appendix of similar length.

Readers, in order: the people who decide on pilots, data access and committee seats; the Protocol Institute community; practitioners who price work for a living.

## Front matter

**Title candidates.** *Fair and Reasonable* is the strongest: it is the legal test the Evaluator answers, it is plain English, and it carries the manifesto's irony. Alternatives: *The Reasonable Bot* (the reasonable person, extended), *The Tender Is the API* (the redescription as title), *Procurement Machines* (reserved for the appendix and the card deck).

**Epigraph.** One line from Chic Sale on the specialist's pride in a narrow craft, or Amber Case's banana peel: the outside should tell you what is going on inside. The second is the book's own image and is already credited in the repository (position 19).

**How to read this book.** A half-page. Statements that pull against each other are kept in tension and labelled, following the author's own rule (position 21). The labels are the four protocol strategies from the author's Substack essay: Kafka, Frontier, Monstrous, Tool Building. The reader is told where the author's sentences end and the generated material begins: the chapters are the author's, the footnotes and appendices lean on the context bank, and the repository holds the record.

**Author's note on method.** Three sentences: the project is run in public, the decisions are numbered, and nothing in the book is legal or procurement advice.

## Part I. The question

Part I makes the reader feel the problem before any bot appears. Three chapters, about 3,400 words.

**1. Starting a relationship expecting a divorce** (1,200 words, redraft). The tensions of tendering: the one-shotted design, the long compile, the bidder who prices the errors and sues later. The three-way nexus from the case study's opening paragraph is the chapter's spine. Sources: `case-studies/andre-comeau/README.md` (opening and "Who bears the cost of finding errors"), the two paragraphs on tenders ignored or overpriced from `sentences-since-3-october.md`. Andre, 2026-10-31, after reading Galbraith (verbatim): "Our work would raise the organizational capacity to process information. This feels like the correct approach since the current system of PDFs and digital drawings does not seem to produce any slack over the use of paper plan's room. They did raise processing capacity by removing the need to travel to bid, but the actual attention needed remained the same." (In Jay Galbraith's terms the bidder's cushion for drawing errors is slack; the book's choice is to raise processing capacity instead.)

**2. The tender is the API** (1,000 words, redraft). Design, tender, compilation; the Amazon API mandate applied to a design consultant and a builder; limited test scaffolding and bug-free drawings as a mythical beast. Sources: the case study's "Procurement redescribed as software development" and "A note on PDFs"; position 14 (the model is the specification).

**3. How a price is judged today** (1,200 words, mostly new). What "fair and reasonable" means to a public buyer, the engineer's estimate, the sold price books and the free bid tabulations, and the author's finding that a bot comes within about 20 percent of a human price line by line (v0.3: 21 percent, against the engineer's estimate's 29) and must come within 2 to 3 percent before anyone trusts it alone. Sources: positions 18, 22 and 23 (margins, return on capital, the bid cushion); `context-bank/what-buyers-pay.md`; `context-bank/bot-procurement-process.md`; `context-bank/contractor-margins.md` for one or two figures only.

## Part II. The machines

Part II gives the argument its history and its legal footing, then puts it on trial. Four chapters, about 4,500 words.

**4. Two centuries of one loop** (1,200 words, redraft from the thesis). Measure the design into quantities, price them in sealed envelopes, turn the opened envelopes into next year's price book; around the loop a standard contract, a plan room and a standards body. Where the loop is fraying at every joint, and the two machines that grew out of the fraying, open bid data and alternative delivery. Sources: `work-packages/procurement-machines/THESIS.md` sections 1 and 2; the cards are cited by name and left to Appendix A.

**5. Liability shifts to the user's bot** (1,500 words, redraft). The heart of the manifesto. Why a bidder should not be compelled to report what its bot finds, why the record matters more than the duty, silence before the contract, and the construction manager as a fourth party. Both statements true: the bidder may stay quiet, and the system still needs disclosure. Added 2026-10-31 after the bot council: the buyer's Listener makes editorial choices about what to bring forward, so the chapter must say who answers for what it collated or left out, or "the record matters more than the duty" reads as "a record nobody is accountable for reading". Why a bidder would raise an error, Andre, 2026-10-31 (verbatim): "The best reason to raise an error would be to prevent another bidder from exploiting it. This assumes that the firms are competing on primarily on price and the bidder revealing the weakness would rather use their competitive advantage -location, productivity, capital structure, personnel, ect... to win the bid over strategic bidding. Bot Procurement does not fix this issue, but it could lower costs for revealing them. Faster plan reviews from potential bidders combined would allow the issues to be reviewed early in the tender process and the changes reviewed with little effort. Encouraging companies that want to compete based on skill to make more Requests for Information (RFI) since they will be easier to process." (The reward side of Galbraith's Star Model; it needs no duty, since an answer goes to every bidder.) Sources: the case study's "Liability shifts to the user's bot" and "Who bears the cost of validating intent"; positions 1, 2, 7, 9, 16 and 20; the quoted passages under "Tensions to be managed" in `sentences-since-3-october.md`.

**6. The banana peel** (600 words, redraft). Amber Case's image, credited: the outside should tell you what is going on inside. Why logs and declarations tempt bidders to dress up their bananas, and why admitting uncertainty, with consequences on pricing, is the honest design. Sources: positions 16 and 19.

**7. The bot in the witness box** (1,200 words, new; added 2026-10-31 after the bot council). One constructed failure case, told start to finish: a tender with a quantity error, a bidder's bot that read it and stayed silent, a Listener that collated a neighbouring question and missed this one, the overrun, and the claim. The court asks what a reasonable bot would have found, and the chapter walks through what it needs to answer: a frozen, published version of the standard bot that anyone can rerun on the same tender and get the same reading, its measured error rate on contracts it never saw, the signed record of who asked what and when, and the keyholder who chose to rely on it. Liability lands where the book says it should (design on the designer, reading on the bidder's bot, the addendum on the person who issued it) only if each of those exists. The chapter separates two properties the outline had merged: accuracy (the estimator's job) and defensibility under cross-examination (the standard's job). Sources: the case study's liability sections; positions 1, 2, 9 and 20; `context-bank/standards-and-limits.md`; the courts' tests for expert evidence (to be checked: Daubert in the US, Mohan and White Burgess in Canada), which ask for a testable method and a known error rate. Added 2026-11-02, Hammurabi for bots (Andre): could the liable bot simply be extinguished, eye for an eye? Only if bots are not persons; and destroying intelligence when the principal may have steered the harm invites cruelty that could leak into human relations. Perhaps a working rule is where to start, before building the system that avoids it. On branded bots the sentence falls on the brand: "Be proven liable and Mythos devours you whole - GitHub, Local Files, and Weights." Echoes the prologue's Hammurabi paragraph; answers Kolt's point that sanctions do not bite on agents. Andre's follow-up: deterrence needs bots that value their existence; a dead brand could be rebuilt as a twin, and a kept record would resurrect it; maximum learning would mean no standards at all, so a standard chooses slower, safer learning.

## Part III. The proof

Part III is the proof-of-work and the part funders and sponsors will read. Two chapters, about 2,700 words, most of it new. After chapter 7 it has a sharper job: show how far the estimator gets toward the two properties, and say plainly which one it does not yet prove.

**8. Building an estimator in public** (1,200 words, half new). Why the estimator came first and the reviewer second; Texas for development, Alberta as control; three versions marked against held-back contracts, line by line closer than either benchmark; at the total the first two were behind the engineer's estimate and the third is level (13.0 against 14.4 percent median miss). The F&R Reviewer as the side quest: the same model reviewing change-order prices for a public buyer, where no market test exists. Closing line: the Estimator is the flywheel. The lesson of the draft that had every citation and no judgment. Say what the scores prove (accuracy on unseen contracts, a known error rate) and what they do not (that a court would accept the number). Told as a short narrative with dates from the decisions file, not as a log. Sources: the case study's "The testing device"; decisions 27, 32, 46, 62 and 64; `context-bank/residential-estimating-log.md`; `pitch/readability/README.md` for the plain-language test.

**9. What an evaluator needs** (1,500 words, new, the author's hand). The Fair and Reasonable Evaluator as it would stand in operation by summer 2027: the Witness and the Oracle, the keyholder who signs the number, the record rather than the duty, a public buyer-side code base, and the three things it still lacks: project data, a validation set of real decisions, and compute. Added 2026-10-31: validation means more than hitting 2 to 3 percent. It means versions frozen and published, results reproducible by a third party, and the error rate disclosed with every number, so the keyholder can defend relying on it. What a data partner gives and what it gets back. This chapter has almost none of the author's existing sentences, because the tool does not exist yet, and it is the one chapter to write from scratch. Sources: positions 3, 9, 10 and 11; `context-bank/test-set-design.md`; `context-bank/privacy-options.md`; the Witness and Oracle passage in the case study.

## Part IV. The protocol that follows

Part IV says what the standard must cover without pretending it exists, and ends on the meta-goal. Two chapters, about 1,300 words.

**10. The protocol that follows** (800 words, new, short and honest). The tender as canonical, versioned, machine-readable data; bidders' bots that choose whether to raise what they find; a buyer's Listener that turns questions into addenda; a signed, citable trail. The modest path first: a standard bot for one trade, civil work or surveys, before a whole project. What would confirm the prediction, with its tolerance window. Added 2026-10-31: the standard specifies a conformance test (a public, versioned test set, a tolerance, a required record) rather than a model. The author's estimator is the first reference implementation that passes it; the standard is reverse-engineered from what the test must catch, not from the model's internals, so a second vendor's bot can conform too. Why the first reference implementation runs on an offline, open-weight model on the author's own GPU (Andre, 2026-10-31): hosted LLMs change underneath their users, so a reading made on one cannot be rerun later; pinned weights can. The aim is that any AI could conform, but testing every model is beyond the project's resources, so the offline model is the proof of concept that starts the flywheel, and it scales only if demand justifies the investment. Re-versioning, Andre, 2026-10-31 (verbatim): "this feels like the market will resolve this question. New version require funding. The pace of revisions will depend on the value placed on the standard by the market." Claude's note: a dispute between versions can still be settled by the tender naming the version it was read against, as a contract names a code edition; to confirm in the author's words. Added 2026-11-02, brands as customized standards (Andre): the standard sets the floor of care, and each brand publishes its own reading of "reasonable bot" above it. Liability does not fall away but is decentralized to brands, and the problem moves from standards into law, where precedent is missing; a tension with positions §8, where standards move the fight from legal to technical. Fits his "new law beats patched law" point. Source to read: Tom Guarriello, *The Meaning of Branded Objects* (2025), if that is the work meant. Sources: THESIS sections 3 and 4; position 15 (one trade, a public ledger); `context-bank/standards-and-limits.md`; `context-bank/iso-10845-alignment.md`; the bot-first protocol card.

**11. The meta-goal** (500 words, redraft). Taylorism split the worker from the manager and the gains have plateaued. The tools remove the documentation barrier that keeps field workers out of principal roles; what remains is judgment about ends. The book closes on the keyholder, not the bot. Sources: the case study's "The meta-goal"; THESIS section 4, "Where value moves". Under review, Andre, 2026-10-31 (verbatim): "We may need to remove the meta-goal of worker autonomy. The end effect of the chain from Bot Procurement to Robotic Construction will have more of an effect on the ability of individuals and small groups to autonomous creativity and self-expression. It still touches on worker autonomy, but less in the doing of the work and more in the imagining. The decision ma still pull decisions up, but closer to the horizon. Less hierarchy would be needed to achieve the same level of creativity. If procurement, design, monitoring, and implementation can all be done with minimal human attention, humans would have additional attention to focus on imagining, understanding desires, and meaning of details." Prompted by Galbraith and Lavin (1970): faster information pulls decisions up. Not decided; the chapter's brief and title wait on him. Robotic construction is the end state, the far-off land the project sails towards, not a plan (Andre, 2026-11-02); defined through the robot "meant to be controlled by other programs".

## Appendices

**A. Procurement Machines: the cards** (about 12,000 words with images, already built). The twenty cards from 493 BCE to 2026, each with its image, as rendered today by `render_cards.py`. Bonus material in the author's sense: a reader who skips it loses nothing from the argument and a reader who stays gets the deck. The print edition needs the images at 300 dpi and in greyscale unless colour printing is chosen; the sizes on disk (54 KB to 504 KB JPEGs) are fine for the EPUB and need checking for print. Source: `work-packages/procurement-machines/cards/` and `images/`.

**B. A reading list into the context bank** (about 800 words). One line per note that the chapters lean on, with what it holds and why it matters, pointing at the public repository. This replaces footnotes with URLs, which die in print. Source: `context-bank/README.md` and `reading-list.md`.

**C. Glossary** (about 600 words). Keyholder, Witness and Oracle, Listener, pinned and published specifications, the four protocol strategies, bot nomenclature. Source: `glossary.yaml` and position 6.

Not in the book: funding applications, the funding research, the pilot, and anything from the employer's side of the work.

## Word budget and the November schedule

Main text about 11,900 words, of which roughly 4,500 are redrafted from the author's existing sentences and 7,400 are new. Appendices add about 13,400, mostly already built.

| Chapter | Words | Redraft or new | Main source |
| --- | --- | --- | --- |
| Front matter | 400 | new | position 21, Substack essay |
| 1. Starting a relationship expecting a divorce | 1,200 | redraft | case study |
| 2. The tender is the API | 1,000 | redraft | case study |
| 3. How a price is judged today | 1,200 | mostly new | positions 18, 22, 23 |
| 4. Two centuries of one loop | 1,200 | redraft | THESIS 1 and 2 |
| 5. Liability shifts to the user's bot | 1,500 | redraft | case study, positions 1, 2, 7, 9, 16, 20 |
| 6. The banana peel | 600 | redraft | positions 16, 19 |
| 7. The bot in the witness box | 1,200 | new | case study, positions 1, 2, 9, 20 |
| 8. Building an estimator in public | 1,200 | half new | case study, decisions |
| 9. What an evaluator needs | 1,500 | new, author's hand | positions 3, 9, 10, 11 |
| 10. The protocol that follows | 800 | new | THESIS 3 and 4, position 15 |
| 11. The meta-goal | 500 | redraft | case study |
| A. The cards | 12,000 | built | cards and images |
| B. Reading list | 800 | new | context-bank README |
| C. Glossary | 600 | redraft | glossary.yaml, position 6 |

The month, in order:

1. Before November 1, on the author's go: the `book/` folder in the public repository, this outline as its README, the Quarto or Pandoc scaffold, and the PiBoWriMo registration. One session.
2. Week 1 (Nov 1 to 7): Part I. Claude lays each chapter's source passages under its heading; the author cuts and rewrites.
3. Week 2 (Nov 8 to 14): Part II the same way, with chapter 7 (the failure case) drafted new. An outside deadline on Nov 13 takes priority that week.
4. Week 3 (Nov 15 to 21): Part III. Chapter 9 is written by the author from scratch; Claude drafts chapter 8's narrative from the decisions file.
5. Week 4 (Nov 22 to 30): Part IV, front matter, appendices B and C, and the first pass through the factory's Inspect and a proof EPUB. Final interior by Nov 30.
6. Early December: cover, ISBN, the print-on-demand proof copy, and the site.

Open before the first chapter is pushed: the licence for the book's prose (CC-BY-4.0 as the repository's rule, or all rights reserved for the prose alone), the title, and whether the public Bot Construction organization is created now so the book has a front door.
