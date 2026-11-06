# The protocol that follows

<!--
Part IV. The protocol that follows (chapter 11 since 2026-11-04; the file name keeps its old number)
Target: 800 words, new, short and honest
Brief: The tender as canonical, versioned, machine-readable data; bidders' bots that choose whether to raise what they find; a buyer's Listener that turns questions into addenda; a signed, citable trail. The modest path first: a standard bot for one trade, civil work or surveys, before a whole project. What would confirm the prediction, with its tolerance window. The standard specifies a conformance test (public versioned test set, tolerance, required record), not a model; the author's estimator is the first reference implementation that passes it, so another vendor's bot can conform too (2026-10-31). Why it starts on an offline model (Andre, 2026-10-31): hosted LLMs keep updating, so their readings cannot be rerun; pinned open weights on the author's GPU can. Any AI should be able to conform in time, but that is beyond the project's resources, so the offline model is the proof of concept that starts the flywheel and scales only if demand justifies the investment. Re-versioning, Andre, 2026-10-31 (verbatim): "this feels like the market will resolve this question. New version require funding. The pace of revisions will depend on the value placed on the standard by the market." Claude's note: a dispute between versions can still be settled by the tender naming the version it was read against, as a contract names a code edition; to confirm in the author's words.
Sources: THESIS sections 3 and 4; position 15 (one trade, a public ledger); `context-bank/standards-and-limits.md`; `context-bank/iso-10845-alignment.md`; the bot-first protocol card.
Added 2026-11-02 (hex_ai search): "The Estimator is the flywheel" (Andre) and the model behind it: the standards are free, the author consults on applying them. Bot council material not yet used: the tender is a stack, with a hard bid and a soft discovery channel that re-enters at a timed point and routes every answer to all bidders (`C:\hex_ai\bot-council\transcripts\2026-10-09-pibot-web-soft-channel-and-tender-hardness.md`); the mute buyer bot as "the faithful channel" ("The mute design is not a limitation; it is the hardness source.", `2026-10-09-pibot-web-duty-to-report-and-listener.md`); everything hard lands on "who controls the schema", which is the standard. Unsent council question C7 (`C:\hex_ai\bot-council\QUESTIONS-four-cards.md`): "a machine participant in an institution survives only where a person is bound to act on its output." Standards' rank changed: a side quest on 2 October (decision 18), the main output by late October.
Literature (`literature-review-2026-11-01.md`, Part 1): ISO 10845 and Watermeyer; CCDC 23; OC4IDS; the ANAC agent competition; Sánchez-Graells 2024. Collusion (`collusion-papers-notes-2026-11-01.md`, Parts 3.1 to 3.3 and 3.5): who sees the reference price and when, publishing line items, evaluation rules, and a joint experiment with the Seoul group.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->
<!--
Draft 2026-11-06 (Claude, from Andre's request in the project thread): "It feels like I have treated this by hand waving and mumbling. Assuming that building the model would self generate the field." Andre asked for David Lang's work, how-to guides on affecting standards, and Nadia Eghbal's *Working in Public*. Every sentence of the draft below is Claude's, built on Andre's earlier passages (kept further down), and needs his rewrite. The draft runs about 2,000 words against the old 800-word target.

Revised 2026-11-06 evening after vgr_zirp session 1 (project file vgr-zirp-review/session-1-answers.md, answers 1, 2 and 4; bot output in Ribbonfarm-era Rao's voice, so not credited in the prose or listed in Appendix D): the standard bot as a legal instrument, "a reasonable reader you can cite in court", moving the project from the innovation bucket to the standards bucket (answer 1, in "What the standard is for"); the coordination trap, courts waiting for a standard, standards bodies for a pilot, buyers for a return, broken by the evaluator (answer 1, in "Starting and sticking"); the claims manager as first ally (answer 2, in the keystone item, kept generic; the one-contract retrospective is left out of the public text on purpose, pending Andre's call on the stealth period); the author's stake as reputational (Andre, 2026-11-06, his interest is reputational only until liability is answered; answer 4 on incentives; in the capture item). Also the Scitovsky two-layer view from chapter 9 (PR #32): the base bid as a commodity price, competition on ideas moved to paid alternates. All Claude's sentences. A tone pass (the book as background credential, not pitch) waits for vgr_zirp's answer to prompt 5.

Sentences that speak for Andre and need his yes: the opening admission that the plan "was a kind of mumble"; the line about remembering the essay's title as "Standards Rule the World" (Andre named it that way in the thread; in the 2026 symposium introduction the project was described as being about "how standards rule the world", so the slip is a natural one).

Sources and where they are used:
- Lang, "Standards Make the World" (Summer of Protocols, 2023; web edition summerofprotocols.com/standards-make-the-world-web). Used in "Standards make the world", "What the standard is for" and "Starting and sticking". Quotes taken from the web edition: "made and remade by (usually small) groups of people"; "Standards-making is something that anyone can engage in, even though almost no one thinks to do it"; "rough consensus and running code" (David Clark, IETF, 1992, quoted by Lang); "we're doing this—are you coming?"; "The danger zone for standards is sometimes in the starting but always in the sticking"; "Start with a small group of true believers and gradually work outwards"; Jordi Puig-Suari on CubeSat, quoted by Lang: "it took about ten years for things to really take off" and "People needed to gain some comfort that these standards are going to be around for a while." To check: wording and pages against Andre's copy of The Protocol Reader (the Reader's table of contents could not be read online, so it is not confirmed that the essay is in it). The taxonomy (safety, interoperability, performance) is Yates and Murphy's *Engineering Rules*, the failure analysis is Carl Cargill's "Why Standardization Efforts Fail" (JEP 14:1, 2011), both met through Lang, so they are credited through him and not listed in Appendix D (the Gramsci-through-Rao rule).
- Lang, opening talk, Protocol Symposium 2026, 23 September 2026 (youtube.com/watch?v=nx-3L5Apbgw, his part from about 19:36). Used in "The field-building level". Quotes from the auto-captions, to check against the video: "name enthusiastically but define hesitantly"; area studies "didn't have its own self-sustaining economic flywheel"; capture "can really slow things down or make these things uninteresting". He also cites the Protocol Reader as a good field-building artifact.
- Lang, "Where are the field builders?" (Amateur Technology, Substack, 28 December 2024): "Field builders are fire starters"; "Once they start the flywheel, the usual suspects show up to go bigger". Not in Appendix D unless Andre reads it; the talk covers the same ground.
- Eghbal, *Working in Public* (Stripe Press, 2020). Used in "A stadium with one player": the four models (federations, clubs, toys, stadiums) on contributor growth against user growth; maintainers' attention as the scarce resource; maintenance as the lasting cost. Paraphrased, not quoted; check against the book. Lang lists the book among his own sources.
- ISO 10845 and Watermeyer: from the literature review (Part 6, items 15 and 16, verified). Watermeyer chairs ISO/TC 59/SC 18. OCDS and OC4IDS: literature review item 21; version 1.0 in July 2015 per Wikipedia (the review gives a first data-model release on 27 June 2014).
- Kelly Roegies, "A Government Guide to Open Protocols" (Protocolized, 19 March 2026): procurement criteria that treat upstream contribution as a resilience signal; seconding staff. Used in "A stadium with one player".
- How-to guides found but not used in the prose (for Andre to pick from): Dave Winer, "Manifesto: Rules for standards-makers" (scripting.com, 9 May 2017), whose rules include "Interop is all that matters", "If practice deviates from the spec, change the spec", "No breakage" and "Freeze the spec" (headings from a secondary listing, check against the original); the Standards Council of Canada's pages on international standards development and its mirror committees (scc-ccn.ca, Directives Part 1 and Part 3); the IETF's guide for newcomers, "The Tao of the IETF"; Andrew Russell, *Open Standards and the Digital Age* (Cambridge, 2014); Shapiro and Varian, "The Art of Standards Wars" (California Management Review, 1999).
-->

The last chapter ended at a door, and behind it was the standard, World 2 on the map. For most of this project, the plan for getting through that door was a kind of mumble. Build a model that is good enough, publish it, and the field would gather around it on its own: the owners would adopt it, the courts would find it, and one day a standards body would write down what it already did. The estimator would be the seed and the rest would grow.

That is not how standards get made, and the people who have made them say so plainly.

## Standards make the world

David Lang came to standards the way many builders do, by needing one. He co-founded OpenROV, a cheap, open-source underwater robot, in 2011, and watched its team turn from prototype builders into protocol designers once they found that the bottleneck in ocean technology was the connector, not the robot. His essay for the Protocol Institute's Summer of Protocols, "Standards Make the World", is the history of standards-making he went looking for along the way.

It is easy to remember the title as *Standards Rule the World*, and the difference between the two verbs is the whole of this chapter. A standard that rules is handed down from somewhere. A standard that makes the world had to be made first, by somebody. Lang's answer to who that somebody is: standards "are made and remade by (usually small) groups of people", and "standards-making is something that anyone can engage in, even though almost no one thinks to do it."

He describes two paths. The first is the formal one, with numbered steps. In Canada it runs through the Standards Council: a proposal goes to ISO, experts draft the text, national bodies and the public comment, the experts revise, the members vote, and the standard is published and reviewed in turn. The second is the path the Internet took, summed up in David Clark's line about the IETF, "rough consensus and running code". Build something that works, get people using it, and give it formal governance afterwards. MIDI, USB and the CubeSat each began with a small group saying, in Lang's words, "we're doing this—are you coming?" Nearly all of them ended up in a consortium or a standards body. The disruptive path does not skip the committee. It arrives at the committee with something already running.

Construction procurement has walked both paths before. In 2005 Ron Watermeyer made the case for an international procurement standard built on South Africa's national ones, which already worked; ISO 10845 followed in 2010, and he now chairs the ISO subcommittee that maintains it. The Open Contracting Data Standard went the other way round: a small team, backed by the World Bank and the Omidyar Network, wrote a data format for publishing public contracts, released version 1.0 in 2015, and let governments pick it up one at a time. Ukraine's ProZorro publishes in it, and an infrastructure version, OC4IDS, followed in 2019. Neither standard computes anything. ISO 10845 fixes the procedure and OCDS fixes the record, and both stop at the edge of the question this book asks.

## What the standard is for

Lang's first question for anyone starting a standard is what it is for. The historians he draws on sort standards by purpose: safety, like the rules for steam boilers; interoperability, like screw threads; and performance, like the grades of steel rail. He adds a fourth kind, the contractual standard, a form that everyone agrees to sign so that nobody has to negotiate it again.

The book's answer comes from its central question. When a bot causes harm, someone has to decide what a reasonable bot would have read in the tender, and the standard is there to say which reading binds. Better models will not remove that need, because a better reader is still only one reader. The law already asks what a reasonable bidder would have understood; the standard gives that question an answer that anyone can rerun. Seen this way, the standard bot is a legal instrument before it is a technical one. Nobody is asked to trust the bot; they are given a reasonable reader they can cite in court. That also moves the project out of the innovation bucket, where public buyers are wary, and into the standards bucket, where they already know how to take part.

So the standard is two kinds at once. The bot-first documents are an interoperability standard, the screw thread that lets any bot read any tender. The standard bot is a performance standard with a contractual purpose: a public, versioned test set, a tolerance, and a required record, which any bot can be measured against. The standard specifies the test, not the model. The author's estimator is only the first bot that passes it, which is why the standard can be free while the bots that conform to it compete. And once the base bid can be checked by anyone, the base price becomes a commodity, and the competition on ideas moves to the paid alternates, as chapter 9 argues.

## Starting and sticking

Lang borrows his best line on failure from Carl Cargill, a veteran of technology standards work: most standards efforts do not fail in the committee. They fail before it, when nobody launches them or no sponsor turns up, or after it, when the finished standard finds no one who wants it. In Lang's words, "the danger zone for standards is sometimes in the starting but always in the sticking."

The mumble was about sticking. It assumed that a good model would stick because it was good, which is the one thing Cargill's history says is not enough.

Sticking is also a waiting game, in which everyone waits for someone else to move first. The courts will not lean on a standard that does not exist yet, a standards body will not write one without a pilot, and a buyer will not fund a pilot without a return it can count. Each of them is being reasonable, and together they keep the door shut. The way out is a benefit that one of them can capture now, before any standard exists, and that is the evaluator's job.

Starting needs fewer people than it seems to. Lang's advice is to "start with a small group of true believers and gradually work outwards", and the disruptive path does not ask for everyone's agreement up front, only for enough people to get something working.

Sticking needs patience. The CubeSat, the ten-centimetre satellite that now flies by the hundred, took about ten years to take off after its standard was written, and one of its inventors, Jordi Puig-Suari, gave the reason: "People needed to gain some comfort that these standards are going to be around for a while." For a liability standard, that comfort is the whole product. A court can rely on a reading only if the standard existed before the tender went out and still exists, unchanged, when the claim arrives years later. The ten to fifteen years this book has assumed before the standard takes effect is not a delay to apologize for; it is about what the CubeSat took.

## The field-building level

At the Protocol Institute's 2026 Symposium, Lang opened with a talk on field building, the work of turning an idea into a field: something with its own people, money, institutions and arguments. His point, for this book, is that fields do not generate themselves. Someone builds them, often an outsider, and in an earlier essay he calls those people "fire starters". The talk works almost as a checklist for the level that sits in front of World 2's castle.

**Name enthusiastically, define hesitantly.** "Bot procurement" is a name, and it can be used loudly. "The reasonable bot" should stay loosely defined for longer than feels comfortable, because a strict definition in the first year ends conversations and pushes people out. The test set can grow into the definition.

**Make momentum.** Lang's list is small grants, workshops, meetups, and vision papers or artifacts. The estimator is an artifact. So is this book.

**Recruit keystone individuals.** A field gains energy when established people from neighbouring fields join it. Here that means someone who has sat on a standards committee, a construction lawyer who has argued over a reading, and a public owner willing to run a pilot. Inside the owner, the first ally is probably not an executive but whoever has to defend a change-order price in a dispute: that person knows the pain best, and needs no standard to find a reproducible number useful.

**Watch the signals.** A field is mature when it has an industry, an institution, or both. The signals to watch are on the bot-first card: a public owner publishing a tender as data, a dispute over an agency's AI, a Canadian mirror committee for construction procurement.

**Beware capture.** Once a field is worth something, a larger player can take it over and slow it down, or make it, as Lang puts it, "uninteresting". In bot procurement the likely captor is a platform vendor whose own format becomes the de facto standard. That is the strongest reason to keep the standard free and the estimator only its first conforming bot. It is also why the author's own stake should stay reputational: a free test behind a paid gate would be capture from the inside.

**Find the economic flywheel.** Lang's warning example is area studies, which had money while the Cold War gave it a reason and closed when the reason went, because it "didn't have its own self-sustaining economic flywheel". This is where the mumble was most wrong, and where chapter 9 already holds the answer. The evaluator's savings, the claims never started and the reviews never paid for, are the flywheel the field needs. They pay for the next version whether or not anyone funds a standard.

## A stadium with one player

Nadia Eghbal's *Working in Public* is about open-source software, but it describes the shape this project is about to take. She sorts projects by two things: how fast their users grow and how fast their contributors grow. Toys have few of either. Clubs have contributors but few outside users. Federations, rare and large, grow both. Stadiums grow users quickly and contributors hardly at all: a few people on the field and a crowd in the stands.

The estimator today is a toy. If the book's plan works, it becomes a stadium: owners, consultants and bidders using a reference bot that one person maintains. Eghbal's lesson is that code is cheap to copy and the maintainer's attention is not, and that the lasting cost of software is the upkeep, not the first build. For a liability standard the stadium is the dangerous stage, because the comfort the CubeSat needed depends on someone still being on the field in ten years. The author has already said where that leaves versioning: new versions need funding, and the pace of revisions will follow the value the market places on the standard.

The stadium also has its worst spectators. The bidder who spends compute searching a frozen standard bot for exploits takes the maintainer's work and gives nothing back; Eghbal would call that an extractive use of the commons. A bounty for each exploit reported turns some of those spectators into players, and since one patch protects every tender read against that version, the bounty can be paid for across all of them.

The way out of the stadium is the path Lang describes, the move into a consortium or a standards body, where the people who rely on the standard share the cost of keeping it. Owners can help before that day comes. Kelly Roegies's guide to open protocols for governments suggests procurement criteria that reward suppliers who contribute upstream, and a public owner who buys bots can ask, in its own tenders, which bidders help maintain the test.

## The campaign for World 2

Put together, the versions in chapter 9 line up with the standards path.

**Version 1.0, momentum.** One trade first, probably civil work, where public bid prices already exist. A public, versioned test set and a published tolerance, on an offline model whose weights do not change. The name in use, the definition kept open, and a small group of true believers. This book is the vision paper.

**Version 2.0, proof of work.** The evaluator in an owner's hands, saving money the owner can count. That saving is the economic flywheel, and the first owners to use it are the keystone individuals the field needs. Workshops follow, where the people who will one day sit on the committee first argue about the test.

**Version 3.0, the working model.** The standard is written backwards from what the test has to catch, not from the estimator's internals, so that a second vendor's bot can pass it too. It then goes looking for its formal home: a consortium, or a national committee proposing a computable extension of ISO 10845, which already fixes the procedure and stops short of the price.

The prediction can be wrong, and it should say how. If by 2035 no public owner anywhere runs a tender whose questions, addenda, bids and evaluation pass through agents on a published data format, the forecast failed. The standard itself is further out, in the ten to fifteen years the CubeSat suggests, and its first court challenge will probably come before it, from a dispute fought under the old rules.

The model was never going to generate the field. The most it can do is give a small group of people something that runs, and something to argue about. That is how a standard starts, and the villagers, as the introduction promised, are the ones who decide whether it sticks.

---

## Source passages (kept until Andre has read the draft)

*Claude, 2026-11-06: the draft above uses the two-routes, conformance-test, one-trade, prediction and tolerance-window passages, and touches the exploit passages only for the bounty. The exploit example (Tannu Tuva, value engineering, proposer security), the public ledger and the pinned-and-published horizon are not yet in the draft. Delete what the chapter no longer needs.*

### Source passages: exploits (to cut and rewrite)

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

### Source passages: the protocol (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Where a source says the meaning is Andre's but the wording is Claude's edit (positions §8, `horizon.md`), the passage is marked "Andre's meaning, edited wording". **THESIS passages are Claude's**, not Andre's. Notes in italics are Claude's. Delete this section as the chapter is written. The exploit passages above stay where they are.*

#### The prediction

*Claude's draft (THESIS section 3), for Andre to rewrite:*

> The next machine is the one the author's case study proposes: the tender as canonical, versioned, machine-readable data; bidders' bots that read it and choose whether to raise what they find; a Buyer's Listener that turns questions into addenda rather than answers; bids, evaluations and justifications with a signed, citable trail.

*The tolerance window: the bot-first protocol card puts first instances at 2028 to 2035, with four confirming signals (a public owner publishing a tender as data; a dispute over an agency's AI, of which Trax v. United States in 2026 is the first; a Canadian mirror committee for construction procurement; an agent-protocol foundation accepting a tender profile). Andre took 10 to 15 years (2036 to 2041) as the working assumption for the standard itself to take effect and perhaps meet its first court challenge (positions §13, placement note, 2026-10-09).*

#### Two routes: bot-readable documents or a standard bot

> There are two ways to make this happen: produce specifications and drawings with bot-based APIs, or create a bot standard. With a bot standard, the buyer and consultants would run the tender through the bot and verify that the outputs it generated reflect the design intent. The bot would be available to vendors, but vendors could choose other bots as well. The advantage is a baseline that could be reproduced.

> The challenge of that model is verification. The consultants would need to prepare the documents and then check the outputs. That incurs additional cost that the Owner would have to bear. Unless the savings from the bidders are greater than the cost to the consultants, this approach has a misaligned payout structure that will inhibit its adoption.

> As a protocol, the standardized bot has the advantage of shifting verification to the side that benefits most from removing discrepancies in the requirements. That would work in favour of adoption even if the cost implications are ambiguous.

> Perhaps it is better viewed as a missing-tool issue. The standards could be updated to improve both bot-first specifications and standardized bots. Based on current AI progress, the technological developments needed to make this approach profitable could simply be a matter of time. If the groundwork has been done, the technology would be adopted much faster.

(positions §13, recorded 2026-10-09)

*The institute write-up review notes that the prologue leaves out the cost side of these passages (the second paragraph); this chapter is where it belongs.*

#### A conformance test, not a model

*Andre's earliest sentence on the idea the outline now calls the conformance test:*

> I suppose that this could be part of the standard building. A standard battery of tests for bots to sign-off against. This would allow them to provide differentiated results based on bidder preferences while ensuring that the bidder has been made aware these potential discrepancies. There is probably something here, but we will leave its development to future version.

(the collated process note, said 2026-10-06)

#### The modest path: one trade first

> Decomposing a project into requirements for one bid may be the equivalent of using PDFs in the age of scrolling. Perhaps there is a path that falls short of full project bot procurement but allows standards, or a standardized bot, to be applied to a limited scope of work or a trade. Civil work may be a good candidate, thanks to the existing database that could be used to train bots. Surveys could also be a good place to start. Or landscaping?

(positions §15, recorded 2026-10-09)

*Claude's comparison there: surveys are the cleanest for verification (the deliverable is a dataset checked against a schema) and the weakest for price data; civil items are the reverse, with the Texas prices this project already uses; landscaping priced as highway items is a low-stakes way into the civil data but the least machine-checkable at acceptance. A scope is ready when the task can be specified in machine terms, an executor found by program, completion verified by machine, and payment follow verification.*

#### A public ledger for the record

> More importantly, the use of blockchain, while an unlikely form of payment for public procurement or for major contracts, is interesting because it ties the record to a publicly inspectable source, avoiding the issues with version control that come from depositories or downloads.

(positions §15, recorded 2026-10-09)

*Claude's note there: the property needs less than a payment system. A hash of each issued document, written to a public, append-only, timestamped log nobody in the tender controls, proves which version existed when; a transparency log of the kind used for web certificates does this without a currency.*

#### Pinned and published: the horizon past the standard

*Andre's meaning, edited wording:*

> Must-have and critical systems would be *pinned*; portions of the specification that need a baseline to guide bidders, without needing specific performance, would be *published*.

> In human-led procurement, bid leveling for mild discrepancies between bids is tedious and often delays project implementation. Bots could remedy this, and would allow bidders to submit multiple bids for various combinations of offers: a blend of spec-build and design-build. Value engineering would move to the tender stage, which should allow better matching between vendors and buyers, with benefits to both parties.

> The challenge would be building a standard tender format to allow this. Without a standard, the legal battles over an AI's choice of "best" options will certainly be litigated. They will likely be litigated no matter the standard, but standards would open the opportunity to move beyond legal issues into the technical ones, as principles of equity are developed for AI.

(positions §8, recorded 2026-10-05; Andre called it "speculative and long-term at best", a horizon and not a change of approach, decision 48)

*The exploit passages above say value engineering is where exploits do the most harm; the pinned-and-published horizon is exactly where value engineering moves to the tender. The chapter can let the two meet.*

#### Why the standards are the end-boss

*Andre's meaning, edited wording, on why speculation belongs in the book at all:*

> A weak point of the whole project is financial compensation. Taking the whole pie would prevent adoption; having no pie will starve the project and keep it from its full potential. Speculation about the future is meant to guess its shape, so that failing to have a slice now does not mean having none later.

(`context-bank/horizon.md`, "Why speculate at all: the slice of pie", recorded 2026-10-05; the "end-boss" passage from the same file is in chapter 9)

### From the Procurement Machines: the projected card

*Added 2026-11-02 from the Procurement Machines work package (`work-packages/procurement-machines/`). The cards, the thread and the watchlist are Claude's drafts from research, for Andre's review; only passages marked as Andre's are his. Card names are given so the chapter can point to Appendix A.*

#### The six tensions on the bot-first card

*The card `bot-first-procurement-protocol-EXTRAP` is the chapter's prediction stated so it can be wrong. Its tensions, in Claude's words except where marked:*

1. *Speed against reviewability: an agent-generated evaluation must still be a record a human board checked (Trax is the first test).*
2. *Disclosure asymmetry: bidders must disclose their AI while agencies' own use is undisclosed.*
3. *Compelled disclosure of deficiencies: answered by Andre's five reasons against (chapter 6).*
4. *Open protocol against platform capture: the first agent-commerce rails are consumer rails built by payment and platform companies. The signal to watch is a government publishing its own bid-and-award schema under an open foundation rather than a vendor's. This tension is the reason the standard should be free and the estimator only its first conforming bot.*
5. *The unpinned specification (Andre's horizon, positions §8): let the specification stay live and bids be multivariate, "and the lowest price stops being computable by a person".*
6. *Packaged for a reasonable human, not a reasonable bot (Andre's, positions §13, quoted above).*

#### Why a better reader does not remove the need for a standard

*From the card's notes, Claude's summary of Andre's argument (put it in his words): if models come to read documents as well as a competent person, a standard is still needed for a legal reason, because "a standard says which reading binds, which a better reader cannot supply." Claude's addition there: the law already asks what a reasonable bidder would have understood; a reference bot would define that reading, and its version would have to be pinned and logged in the record, as Trax shows. This is the hinge between this chapter and chapter 8.*

#### The tolerance window

*The card's window, first instances 2028 to 2035, is Claude's guess, offered so the card can be wrong: "if by 2035 no public owner anywhere runs a tender whose questions, addenda, bids and evaluation are mediated by agents on a published data format, the card was wrong." Andre's own working assumption is 10 to 15 years (2036 to 2041) for the standard to take effect. Research note F reconciles the two: agent-mediated tenders will run on the old rules before any standard exists, so the first precedent comes from Trax-type disputes, not from a standard.*

#### Weights declared before the bids open

*The watchlist's expected site "declared weights" (Claude's): best-value evaluations state their factors in prose. A machine-readable declaration, fixed before bids open, "is what would make an AI's choice of best checkable afterwards". It is the precondition for the pinned-and-published horizon above.*
