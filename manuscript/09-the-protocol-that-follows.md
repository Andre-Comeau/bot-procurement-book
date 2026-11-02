# The protocol that follows

<!--
Part IV. The protocol that follows (chapter 11 since 2026-11-04; the file name keeps its old number)
Target: 800 words, new, short and honest
Brief: The tender as canonical, versioned, machine-readable data; bidders' bots that choose whether to raise what they find; a buyer's Listener that turns questions into addenda; a signed, citable trail. The modest path first: a standard bot for one trade, civil work or surveys, before a whole project. What would confirm the prediction, with its tolerance window. The standard specifies a conformance test (public versioned test set, tolerance, required record), not a model; the author's estimator is the first reference implementation that passes it, so another vendor's bot can conform too (2026-10-31). Why it starts on an offline model (Andre, 2026-10-31): hosted LLMs keep updating, so their readings cannot be rerun; pinned open weights on the author's GPU can. Any AI should be able to conform in time, but that is beyond the project's resources, so the offline model is the proof of concept that starts the flywheel and scales only if demand justifies the investment. Re-versioning, Andre, 2026-10-31 (verbatim): "this feels like the market will resolve this question. New version require funding. The pace of revisions will depend on the value placed on the standard by the market." Claude's note: a dispute between versions can still be settled by the tender naming the version it was read against, as a contract names a code edition; to confirm in the author's words.
Sources: THESIS sections 3 and 4; position 15 (one trade, a public ledger); `context-bank/standards-and-limits.md`; `context-bank/iso-10845-alignment.md`; the bot-first protocol card.
Added 2026-11-02 (hex_ai search): "The Estimator is the flywheel" (Andre) and the model behind it: the standards are free, the author consults on applying them. Bot council material not yet used: the tender is a stack, with a hard bid and a soft discovery channel that re-enters at a timed point and routes every answer to all bidders (`C:\hex_ai\bot-council\transcripts\2026-10-09-pibot-web-soft-channel-and-tender-hardness.md`); the mute buyer bot as "the faithful channel" ("The mute design is not a limitation; it is the hardness source.", `2026-10-09-pibot-web-duty-to-report-and-listener.md`); everything hard lands on "who controls the schema", which is the standard. Unsent council question C7 (`C:\hex_ai\bot-council\QUESTIONS-four-cards.md`): "a machine participant in an institution survives only where a person is bound to act on its output." Standards' rank changed: a side quest on 2 October (decision 18), the main output by late October.
Literature (`literature-review-2026-11-01.md`, Part 1): ISO 10845 and Watermeyer; CCDC 23; OC4IDS; the ANAC agent competition; Sánchez-Graells 2024. Collusion (`collusion-papers-notes-2026-11-01.md`, Parts 3.1 to 3.3 and 3.5): who sees the reference price and when, publishing line items, evaluation rules, and a joint experiment with the Seoul group.
Paths are relative to construction-procurement-protocols unless they start with C:\.
Added 2026-11-02 (branding): Andre asks whether brands could be customized standards. The standard sets the floor of care (his position of 2026-11-01); each brand would publish its own reading of "reasonable bot" above it, and answer for it. Liability does not fall away but is decentralized to brands, and the problem moves from standards into law, where precedent is missing. That pulls against his own line in positions §8 that standards "open the opportunity to move beyond legal issues into the technical ones"; keep both and label the tension. Source: Tom Guarriello (see the passages below). Ties to his "new law beats patched law" point (workers' compensation as the precedent) and to Kolt on special skills raising the standard of care. The brand's death sentence (Hammurabi for branded bots) is laid out in chapter 7.
-->


## Source passages: exploits (to cut and rewrite)

*Laid out by Claude on 2026-11-02, from the Scitovsky thread of 1 November 2026. The Scitovsky source is "The Benefits of Asymmetric Markets" (Journal of Economic Perspectives, 1990), listed in Appendix D (Andre, 2026-11-05). Quoted passages are Andre's, copied unchanged from that thread. Notes in italics are Claude's. Andre asked for this discussion to go into the manuscript as the book's example of exploits. Delete this section as the chapter is written.*

*Why a public standard invites exploits:*

> There would be the risk of vendors gaming the system, but the below costs bids on line items is evidence that this is already happening. The standards we are working for may need to be accompanied by other AI reviewers to validate proposals and reduce the risks of accepting proposals exploiting the system.

> System exploits should be a risk. Based on complex video games, I am thinking about the world modelling series from Paradox games, there is usually sets of rules that allow for outcomes outside the intended framework. [...] Patches fix this, but since there is little real money flowing out of real accounts, the exploits can be fun if not used in a multiplayer game.

*The example, in Andre's words. The Luxembourg write-up he remembers has not been found online, so tell it as the author's own memory of the game rather than as a citation:*

> The main exploit was the paradrop. Surrounding enemy lines with paratroopers would prevent retreats and speed capture enormous territory. There was a step where war was declared against a country that could never be able to attack you. Tanu Tavu?

> The Tannu Tuva world conquest write-up is an even better example of the exploitability of computer programs. This was done by observant humans, image what trillions of tokens would do!

*Citable versions if wanted. Hearts of Iron IV players conquering the world as Tannu Tuva, a one-province nation, are documented on the Paradox forum ("Tannu Tuva World Conquest", thread 959544; "I managed to world conquest as Tannu Tuva (w/ tutorial)", thread 1500616); the forum blocked automated reading on 2026-11-02, so check the details by hand. Andre, 2026-11-05: the threads he found are not as good as the write-up he remembers, so the Tannu Tuva example may be dropped; not in Appendix D. A Steam thread of 31 January 2018 asks Paradox to fix the "Paradrop England exploit" (steamcommunity.com/app/394360/discussions/0/1700541698681349596). The lesson for the chapter: every move obeys the rules, but together the moves reach an outcome the designers never intended. That is what a bidder can do to a frozen, published standard bot.*

*Compute is the new asymmetry (Scitovsky's gap between expert and non-expert returns as search power):*

> AI will cut both ways on this. It will be able to provide more audits from different angles, but the race for compute may advantage the vendors. If spending 1% of project funds on estimating increases marginal profits without lowering costs (see Scitovsky), then we can expect firms to make this choice. (1% = $10,000/$1,000,000 - once projects climb to the multi-million dollar range, pre-paying for estimating compute to exploit the standardized bot will become an issue.

> There is high likelihood that additional controls would need to be incorporated in the contracts and tenders to control exploits. Stress testing it against powerful AI could help. This would be expensive and continuous, so legal protections may be required. (Maybe bounties for exploit reveals could be useful? Could many low power reviews form bounty hunters = high powered exploit expedition from a potential bidder?)

*Claude's note on bounties: one exploit found and patched protects every tender read against that version, so a bounty can be funded across all of them, while a bidder's exploit search is paid for by a single project. The bounty has to pay more than the exploit is worth to a bidder who keeps it secret.*

*Where exploits do the most harm:*

> The exploits would be more of an issue for value engineering proposals than low bid procurement. Exploiting the low bid would likely lead to lower prices (or lower quality). Exploiting value engineering could easily lead to higher costs without benefits when a buyer is bound to a promising idea that fails to deliver.

*The control Andre prefers, out of five Claude proposed (a public test set with a private holdout replaced at each version, several independent AI reviewers, proposer security, bounties per version, and a tender clause that readings obtained through a known exploit are not relied on):*

> Placing the onus on the proponent would allow for an equitable distribution of risks and rewards.

> The pass/fail approach for proposals could also help, but the proposer security method helps control for latent risks.

*The control in full, as Claude put it in the thread and Andre picked it: "The proposer posts security on its alternative and pays if the owner has to revert." Gaming already has a rule against it in US federal procurement: offers with line items "significantly overstated or understated" must be analysed for unbalanced pricing and may be rejected if the risk is unreasonable (FAR 15.404-1(g)). Fuller notes, with Scitovsky's argument, are in the Claude Doc "The Reasonable Bot, read through Scitovsky" (claude.ai/artifact/YD4MKxFj1b7hvU7MNkhq5x).*

## Source passages: the protocol (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Where a source says the meaning is Andre's but the wording is Claude's edit (positions §8, `horizon.md`), the passage is marked "Andre's meaning, edited wording". **THESIS passages are Claude's**, not Andre's. Notes in italics are Claude's. Delete this section as the chapter is written. The exploit passages above stay where they are.*

### The prediction

*Claude's draft (THESIS section 3), for Andre to rewrite:*

> The next machine is the one the author's case study proposes: the tender as canonical, versioned, machine-readable data; bidders' bots that read it and choose whether to raise what they find; a Buyer's Listener that turns questions into addenda rather than answers; bids, evaluations and justifications with a signed, citable trail.

*The tolerance window: the bot-first protocol card puts first instances at 2028 to 2035, with four confirming signals (a public owner publishing a tender as data; a dispute over an agency's AI, of which Trax v. United States in 2026 is the first; a Canadian mirror committee for construction procurement; an agent-protocol foundation accepting a tender profile). Andre took 10 to 15 years (2036 to 2041) as the working assumption for the standard itself to take effect and perhaps meet its first court challenge (positions §13, placement note, 2026-10-09).*

### Two routes: bot-readable documents or a standard bot

> There are two ways to make this happen: produce specifications and drawings with bot-based APIs, or create a bot standard. With a bot standard, the buyer and consultants would run the tender through the bot and verify that the outputs it generated reflect the design intent. The bot would be available to vendors, but vendors could choose other bots as well. The advantage is a baseline that could be reproduced.

> The challenge of that model is verification. The consultants would need to prepare the documents and then check the outputs. That incurs additional cost that the Owner would have to bear. Unless the savings from the bidders are greater than the cost to the consultants, this approach has a misaligned payout structure that will inhibit its adoption.

> As a protocol, the standardized bot has the advantage of shifting verification to the side that benefits most from removing discrepancies in the requirements. That would work in favour of adoption even if the cost implications are ambiguous.

> Perhaps it is better viewed as a missing-tool issue. The standards could be updated to improve both bot-first specifications and standardized bots. Based on current AI progress, the technological developments needed to make this approach profitable could simply be a matter of time. If the groundwork has been done, the technology would be adopted much faster.

(positions §13, recorded 2026-10-09)

*The institute write-up review notes that the prologue leaves out the cost side of these passages (the second paragraph); this chapter is where it belongs.*

### A conformance test, not a model

*Andre's earliest sentence on the idea the outline now calls the conformance test:*

> I suppose that this could be part of the standard building. A standard battery of tests for bots to sign-off against. This would allow them to provide differentiated results based on bidder preferences while ensuring that the bidder has been made aware these potential discrepancies. There is probably something here, but we will leave its development to future version.

(the collated process note, said 2026-10-06)

### The modest path: one trade first

> Decomposing a project into requirements for one bid may be the equivalent of using PDFs in the age of scrolling. Perhaps there is a path that falls short of full project bot procurement but allows standards, or a standardized bot, to be applied to a limited scope of work or a trade. Civil work may be a good candidate, thanks to the existing database that could be used to train bots. Surveys could also be a good place to start. Or landscaping?

(positions §15, recorded 2026-10-09)

*Claude's comparison there: surveys are the cleanest for verification (the deliverable is a dataset checked against a schema) and the weakest for price data; civil items are the reverse, with the Texas prices this project already uses; landscaping priced as highway items is a low-stakes way into the civil data but the least machine-checkable at acceptance. A scope is ready when the task can be specified in machine terms, an executor found by program, completion verified by machine, and payment follow verification.*

### A public ledger for the record

> More importantly, the use of blockchain, while an unlikely form of payment for public procurement or for major contracts, is interesting because it ties the record to a publicly inspectable source, avoiding the issues with version control that come from depositories or downloads.

(positions §15, recorded 2026-10-09)

*Claude's note there: the property needs less than a payment system. A hash of each issued document, written to a public, append-only, timestamped log nobody in the tender controls, proves which version existed when; a transparency log of the kind used for web certificates does this without a currency.*

### Pinned and published: the horizon past the standard

*Andre's meaning, edited wording:*

> Must-have and critical systems would be *pinned*; portions of the specification that need a baseline to guide bidders, without needing specific performance, would be *published*.

> In human-led procurement, bid leveling for mild discrepancies between bids is tedious and often delays project implementation. Bots could remedy this, and would allow bidders to submit multiple bids for various combinations of offers: a blend of spec-build and design-build. Value engineering would move to the tender stage, which should allow better matching between vendors and buyers, with benefits to both parties.

> The challenge would be building a standard tender format to allow this. Without a standard, the legal battles over an AI's choice of "best" options will certainly be litigated. They will likely be litigated no matter the standard, but standards would open the opportunity to move beyond legal issues into the technical ones, as principles of equity are developed for AI.

(positions §8, recorded 2026-10-05; Andre called it "speculative and long-term at best", a horizon and not a change of approach, decision 48)

*The exploit passages above say value engineering is where exploits do the most harm; the pinned-and-published horizon is exactly where value engineering moves to the tender. The chapter can let the two meet.*

### Why the standards are the end-boss

*Andre's meaning, edited wording, on why speculation belongs in the book at all:*

> A weak point of the whole project is financial compensation. Taking the whole pie would prevent adoption; having no pie will starve the project and keep it from its full potential. Speculation about the future is meant to guess its shape, so that failing to have a slice now does not mean having none later.

(`context-bank/horizon.md`, "Why speculate at all: the slice of pie", recorded 2026-10-05; the "end-boss" passage from the same file is in chapter 9)

## Source passages: brands as customized standards (to cut and rewrite)

*Laid out by Claude on 2026-11-02. The quoted passage is Andre's, copied unchanged. Notes in italics are Claude's. Delete this section as the chapter is written.*

> Could Branding be considered as customized Standards? The liability for harm issue does not fall away, but becomes decentralized to individual brands. The Brand sets its Standard based on their interpretation of "Reasonable Bot". This would be challenging due to the lack of legal precedents. It would transform the problem from the field of standards to that of legal. See work by Tom Guarriello.

(project thread "Add branding and Hammurabi ideas to the book", said 2026-11-02)

*Andre's position of 2026-11-01 frames it: "The purpose of the standards would be to create a floor for the required standard of care for construction procurement." On that reading the public standard is the floor and a brand is a promise made above it: a vendor's own, published reading of what its reasonable bot does. The floor stays common; the ceiling is sold.*

*Tensions the chapter can label (Claude's):*

- *Standards against law. In positions §8 Andre wrote that standards "would open the opportunity to move beyond legal issues into the technical ones". Branding moves the question back: whether a brand kept its own promise is for a court, and no court has yet ruled on what a brand's "reasonable bot" meant. Both statements are true, and the floor is what keeps them from colliding: a brand can be sued for falling short of its promise, but never argue that its promise lowered the floor.*
- *Kolt's open problem, from the brand side. Agency law raises the standard of care for an agent that claims special skill (Restatement (Third) of Agency §8.08; Kolt pp. 46-47). A brand is such a claim, so a brand that promises more is held to more. Kolt worried this would push capable vendors away from specialist agents; with a public floor, the brand chooses how far above it to promise and prices that liability in.*
- *New law, not patched law. Andre's point of 2026-11-02 (lit review thread): employment law grew beside agency law rather than out of it. Branded bots with no precedent are the case for a new statute that names the floor and leaves the brands to contract and consumer law above it, as building codes are adopted by statute rather than made by courts.*

*Older still: hallmarks and makers' marks on silver and gold came before any standards body. The assay office set the floor (the metal's fineness) and the maker's mark said whose work it was, so a maker could promise more but never less. That is the floor-and-brand shape in its oldest form.*

*A precedent worth checking (Claude's, from memory, not yet verified): certification marks are brands that became standards. UL's mark began as one firm's testing promise and is now referenced by codes. The trade-mark law of certification marks may be the nearest existing law for "a brand that sets its own standard".*

*Tom Guarriello, as found on 2026-11-02 (web search; Andre to say which of his works he means): psychologist, faculty of the School of Visual Arts Masters in Branding programme, host of the RoboPsych podcast on how people relate to robots and AI, and author of* The Meaning of Branded Objects: Why Some Things Matter More Than Others *(Rockport, October 2025), which treats brands as how people attach meaning and identity to objects. If that is the source, the book's use is the trust side: people already relate to a bot through its brand, so the brand is where they will look for the standard it keeps.*

## From the Procurement Machines: the projected card

*Added 2026-11-02 from the Procurement Machines work package (`work-packages/procurement-machines/`). The cards, the thread and the watchlist are Claude's drafts from research, for Andre's review; only passages marked as Andre's are his. Card names are given so the chapter can point to Appendix A.*

### The six tensions on the bot-first card

*The card `bot-first-procurement-protocol-EXTRAP` is the chapter's prediction stated so it can be wrong. Its tensions, in Claude's words except where marked:*

1. *Speed against reviewability: an agent-generated evaluation must still be a record a human board checked (Trax is the first test).*
2. *Disclosure asymmetry: bidders must disclose their AI while agencies' own use is undisclosed.*
3. *Compelled disclosure of deficiencies: answered by Andre's five reasons against (chapter 6).*
4. *Open protocol against platform capture: the first agent-commerce rails are consumer rails built by payment and platform companies. The signal to watch is a government publishing its own bid-and-award schema under an open foundation rather than a vendor's. This tension is the reason the standard should be free and the estimator only its first conforming bot.*
5. *The unpinned specification (Andre's horizon, positions §8): let the specification stay live and bids be multivariate, "and the lowest price stops being computable by a person".*
6. *Packaged for a reasonable human, not a reasonable bot (Andre's, positions §13, quoted above).*

### Why a better reader does not remove the need for a standard

*From the card's notes, Claude's summary of Andre's argument (put it in his words): if models come to read documents as well as a competent person, a standard is still needed for a legal reason, because "a standard says which reading binds, which a better reader cannot supply." Claude's addition there: the law already asks what a reasonable bidder would have understood; a reference bot would define that reading, and its version would have to be pinned and logged in the record, as Trax shows. This is the hinge between this chapter and chapter 8.*

### The tolerance window

*The card's window, first instances 2028 to 2035, is Claude's guess, offered so the card can be wrong: "if by 2035 no public owner anywhere runs a tender whose questions, addenda, bids and evaluation are mediated by agents on a published data format, the card was wrong." Andre's own working assumption is 10 to 15 years (2036 to 2041) for the standard to take effect. Research note F reconciles the two: agent-mediated tenders will run on the old rules before any standard exists, so the first precedent comes from Trax-type disputes, not from a standard.*

### Weights declared before the bids open

*The watchlist's expected site "declared weights" (Claude's): best-value evaluations state their factors in prose. A machine-readable declaration, fixed before bids open, "is what would make an AI's choice of best checkable afterwards". It is the precondition for the pinned-and-published horizon above.*
