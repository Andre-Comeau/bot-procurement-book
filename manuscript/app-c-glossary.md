# Appendix C. Glossary

<!--
Appendices
Target: about 600 words
Brief: Keyholder, Witness and Oracle, Listener, pinned and published specifications, the four protocol strategies, bot nomenclature.
Sources: `glossary.yaml` and position 6.
Added 2026-11-09: Rehearsal contracts and the final test (Andre's wording rule; see the entry for rehearsal contracts in the source-passages list).
Added 2026-11-02: Robotic construction, defined from the field notes as construction by robots "meant to be controlled by *other programs*" (see chapter 12's note). Faithful channel (the Listener that never answers). Patent and latent errors, as the published checks divide them.
Paths are relative to construction-procurement-protocols unless they start with C:\.
Added 2026-11-19 (Claude, thread "Build the source ledger, glossary and FAQ", for Andre to cut and rewrite): a reader's list of terms, drawn from the chapters that use them, and a list of acronyms. Each entry names its chapter so the definition can be checked against it. Wording rules followed: the book's question is "Who is liable?"; the estimator and the model are described in the future tense; the standard is a proposal. Two items wait on Andre: the C3PO line in the Listener passage below (C-3PO is the droid who talks; a bot with no outward voice sounds more like R2-D2), and whether the "Rehearsal contracts and the final test" passage should be renamed in plain words; the reader's entry "Checking the estimator" below avoids both terms meanwhile. The two "who pays" phrasings in the source passages, both Claude's wording, now read "who is liable".
-->

## Terms

*Each term names the chapter where it is used most.*

**Bid bond.** A guarantee, usually from a surety, that a bidder who wins will sign the contract at the price it bid. It is one of the four answers highway construction already has to a flood of bids (chapter 1).

**Bid cushion.** The money a bidder adds to cover what it could not check in the time it had: errors in the drawings, unclear quantities, risk it cannot price. The book calls it slack (chapter 1).

**Bid depository.** An office that receives trade contractors' sealed prices on bid day, stamps them with its own clock and passes them to the general contractors bidding the job (chapter 7c).

**Bill of quantities.** A list of every item of work in a tender with its measured quantity, so that each bidder prices the same list. Highway agencies call the items pay items (chapters 2 and 5).

**Bot admin.** The project's name for the far world where machines keep track of the work and the documents, not the people. It replaced "bot monitoring" (chapters 7c and 10).

**Bot Construction.** The wider field: construction arranged, priced, run and eventually built with bots, from documents written for machines to robots on site (prologue).

**Bot Procurement.** This book, and the proposal inside it: the part of Bot Construction kept small enough to test first, which asks what price a bot puts on a tender and who is liable when it gets it wrong (prologue).

**Buyer as insurer.** The base case of the book's plan: the buyer runs the standard bot, publishes its number and carries the loss if the number was wrong, so no insurer is needed (chapter 3).

**Cap.** One of the four answers to a flood of requests: a limit on how many anyone may send. Construction's cap is the shortlist (chapter 1).

**Change order.** A signed change to the work after the contract is let, with its price. Every change is a purchase from a supplier of one, because only the builder already on site can do it (chapter 10).

**Checking the estimator.** The estimator learned from Texas contracts let before May 2026 and was checked, version by version, on contracts let after, which it had not learned from. Because each version was chosen knowing how the last one scored, those scores probably flatter it a little. A check on newer contracts, left alone so far, will be run once there is a product and someone who wants the answer (chapter 10).

**Construction Manager.** A builder hired early, for its qualifications, to advise on the design and then manage the building of it, usually at a price agreed with open books (chapter 4).

**Cost plus.** A contract that pays the builder what the work costs plus a fee, instead of a price fixed in advance (chapter 4).

**Design-Bid-Build.** The traditional order: the owner's designers finish the drawings, builders bid on them, and the winner builds what was drawn (chapter 4).

**Design-Build.** One firm both designs and builds, under one contract. In progressive Design-Build the team is chosen for its qualifications and the price is agreed in packages as the design firms up (chapter 4).

**Engineer's estimate.** The price the buyer's own engineers put on the work before the tender. It is the yardstick the estimator will be measured against (chapter 10).

**Estimator.** A bot the project is building that will put a price on each line of a tender from what bidders have charged before, as a second opinion before the tender closes (chapter 10).

**Evaluator.** The estimator pointed the other way: a tool that will check the price of a change after the contract is let, draft the memo that says whether it is fair and reasonable, and hand it to a person to sign (chapter 10).

**Fair and reasonable.** The test a public buyer has to meet, in writing, before paying a price nobody competed for, such as the price of a change (chapter 10).

**Fee.** One of the four answers to a flood of requests: making each sender pay. Construction's nearest twin is the bid bond and the cost of preparing a bid (chapter 1).

**Flag.** A mark the estimator or the evaluator will put on a line it has seen too rarely to price with confidence, so that a person prices it instead. A flag only works if someone has to act on it (chapter 10).

**General Contractor.** The builder that holds the contract with the owner and hires the trade contractors who do most of the work (chapter 4).

**Hard bid.** A tender won on price alone, usually a lump sum, by the lowest bidder that meets the terms (chapter 4).

**Jig, jigbot.** A jig holds the work and the tool in the right relation so a hard cut can be made again, safely, by anyone on the crew. A jigbot is what a tradesperson will build when they set up and teach a robot for the task at hand, the way they would build a jig (chapter 7c).

**Key.** One of the four answers to a flood of requests: deciding who may send one. Construction's keys are prequalification and capacity ratings (chapter 1).

**Keyholder.** The named person who reviews what a bot drafted, adjusts the flagged lines, decides and signs, with a reason (chapters 10 and 11a).

**Listener.** A bot that collects bidders' questions during a tender, from people or bots, and answers with no more than a nod, a shake or a shrug (chapter 11).

**Lump sum.** One price for the whole of the work, or for a few large parts, instead of a price for each line (chapters 4 and 10).

**Margin insurance.** The bidder's cover in the book's plan: a policy that would pay part of the shortfall when the average margin on a bidder's covered contracts falls below its target. No insurer offers it yet (chapter 3 and Appendix E).

**Patent and latent errors.** A patent error is one a careful bidder should have spotted in the tender; a latent one could not have been seen. A bidder who should have seen a patent error and did not ask usually cannot charge for it later (chapter 11a).

**PDF zombie.** The tender document that died as a technology but kept walking as a protocol, because it carries the seal and the signatures the law still asks for (chapters 5 and 9).

**Pinned and published.** Two kinds of specification: pinned parts are the must-have and critical systems, fixed in detail; published parts set a baseline to guide bidders without fixing how the work is done (chapter 11).

**Prequalification.** Checking that a bidder has the capacity and record for the work before it may bid (chapters 1 and 7a).

**Published check.** One of the four answers to a flood of requests: checking every request against rules that everyone can read. It is the answer this book builds on (chapter 1).

**Reasonable bot.** The bot a judge would compare others against when asking what a careful reader should have understood from a tender, the way the law already asks what a reasonable bidder would have understood (prologue and chapter 8).

**Record.** What is kept each time a bot's reading is relied on: the tender, the version of the standard it was read against, and the reading, so a court can check it later (chapter 11).

**Second opinion.** What the estimator and the evaluator will offer: a price drawn from past tenders, beside the price the buyer is being asked to pay, for a person to weigh (chapter 10).

**Slack.** Time, money and cushion kept between the parts of a system so that nobody has to know everything. Construction has always chosen slack; the book asks for more capacity to read instead (chapter 1).

**Standard bot.** A proposal: a published bot that reads a tender the way the standard says it should be read, so anyone can rerun it and a judge can measure other bots against it (chapters 8, 9 and 11).

**Stipend.** A payment from the buyer to the losing bidders on a large job, to cover part of what their bids cost to prepare (chapters 1 and 9).

**Template.** A tender's items, units and quantities written as plain data beside the PDF, so a bot can read them without guessing and a person can read them without software (chapter 11).

**Tender.** The package a buyer issues to invite priced offers for construction work, and the competition that follows until the bids are opened. The book's first chapter treats it as an interface between the buyer and everyone who bids (chapter 1).

**Thicket.** The crowd of new bids that springs up once bidding becomes nearly free, the way a thicket fills the clearing where an old oak fell (chapters 1 and 9).

**Witness and Oracle.** A pair of bots inside any buyer-side system: the Witness reads the full records, and the Oracle checks what leaves, so the bot that faces outward never touches the files (chapter 10).

## Acronyms

- **AACE.** AACE International, which publishes the estimate classes used to say how accurate an estimate can be at each stage of design.
- **AI.** Artificial intelligence; in this book, mostly the language models that read and write text.
- **BIM.** Building information modelling: a shared digital model of a building or structure.
- **CCDC.** Canadian Construction Documents Committee, which publishes Canada's standard construction contracts.
- **FAR.** The US Federal Acquisition Regulation.
- **GAEB.** The German standard for exchanging bills of quantities as data.
- **IDS.** Information Delivery Specification, a buildingSMART format that says what information a model must contain.
- **IFC, IFCX.** Industry Foundation Classes, the open format for building models; IFCX is the next version, being written as small JSON records.
- **ISO 10845.** The international standard for construction procurement procedure.
- **OCDS, OC4IDS.** The Open Contracting Data Standard, for publishing public contracts as data, and its version for infrastructure projects.
- **RFI.** Request for information: a question from the builder about the drawings or specifications.

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. `glossary.yaml` turned out to hold the cards' acronyms (AASHTO, CCDC, GAEB and so on), not the project's own terms, so it serves the acronym half of this appendix. The project's terms are defined in these places; the wording of each is Andre's meaning, edited by Claude, unless marked.*

- **Bot Construction and Bot Procurement** (Andre, 2026-11-14; Claude's wording): Bot Construction is the field, where the work leads, from documents written for machines to robots on site. Bot Procurement is the book and the standard, the part kept small enough to test: the price on a tender and who is liable when a bot gets it wrong. It has to hold up before the field can lean on it. Stated in the prologue.
- **Listener**: "The Listener's primary role is collating questions from Bidders, whether human or bot. It may communicate the equivalent of a head bow, a shake or a shrug" (positions §6). The name is C3PO's, for a bot with no outward voice.
- **Witness and Oracle**: the World Machines pair; one searches the full corpus, the other publishes and never sees the files (case study, "The testing device"; positions §6: they describe the inside of any owner-side bot).
- **Keyholder**: the person who signs the number and adjusts the flagged lines (Andre's term; THESIS section 4, decision 45).
- **Pinned and published specifications**: "Must-have and critical systems would be *pinned*; portions of the specification that need a baseline to guide bidders, without needing specific performance, would be *published*" (positions §8).
- **The four tension labels**: Frontier, Monstrous, Kafka and Tool-building (positions §21), defined in Andre's Substack essay "Age of AI, the age of protocols".
- **Bid cushion**: what is paid to owners before profit, which Andre puts "in the variable cost pile" and not in overhead (positions §23).
- **Rehearsal contracts and the final test** (Claude's wording, 2026-11-09, to confirm; Andre's rule that the book never calls the check "sealed", "blind" or "scored once"): the book's plain names for two of the three sets of data an estimator meets. The estimator *learns* from past contracts (researchers: training data). It is *rehearsed* on contracts set aside while it is built, and each version is chosen knowing how the last one scored (researchers: validation data, the data used to tune and to choose between versions). It is *finally tested* on newer bid results the project has left alone (researchers: test data), once there is a product and someone interested in the answer. Researchers use "validation" and "test" in this order, so a paper on this project says validation data for the rehearsal and test data for the final check; some medical and statistics writing uses "validation" for the final check instead, so define the words wherever they are used. Accuracy and error bands for any pitch come only from the final test.
- **F&R (fair and reasonable) Reviewer and Evaluator**: the reviewer folded into the estimator on 2026-10-05 (decision 46); the Evaluator is the tool chapter 10 describes, a stepping stone toward the standard. Fair and reasonable is the public buyer's price test, narrower than the book's question (who is liable when a bot causes harm).
