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
Draft 2026-11-06 (Claude, from Andre's request in the project thread): "It feels like I have treated this by hand waving and mumbling. Assuming that building the model would self generate the field." Andre asked for David Lang's work, how-to guides on affecting standards, and Nadia Eghbal's *Working in Public*. Every sentence of the draft below is Claude's, built on Andre's earlier passages (kept further down), and needs his rewrite. The draft runs about 2,400 words against the old 800-word target.

Revised 2026-11-06 evening after vgr_zirp session 1 (project file vgr-zirp-review/session-1-answers.md, answers 1, 2 and 4; bot output in Ribbonfarm-era Rao's voice, so not credited in the prose or listed in Appendix D): the standard bot as a legal instrument, "a reasonable reader you can cite in court", moving the project from the innovation bucket to the standards bucket (answer 1, in "What the standard is for"); the coordination trap, courts waiting for a standard, standards bodies for a pilot, buyers for a return, broken by the evaluator (answer 1, in "Starting and sticking"); the claims manager as first ally (answer 2, in the keystone item, kept generic; the one-contract retrospective is left out of the public text on purpose, pending Andre's call on the stealth period); a paid gate on a free test as capture from the inside (in the capture item; the earlier line on the author's stake was removed, since Andre asks that his benefit is never described as reputational, see the outline's "The author's intentions"). Also the Scitovsky two-layer view from chapter 9 (PR #32): the base bid as a commodity price, competition on ideas moved to paid alternates. All Claude's sentences. A tone pass (the book as background credential, not pitch) waits for vgr_zirp's answer to prompt 5.

Added 2026-11-06 late (Andre: "we fall off a cliff after the tool has been built... We should have a look at the closest standards and see what we would need to change"): the section "The nearest standards" and the figure images/world-2-standards.png (images/world_2_standards.py, chapter 9's map style). All proposals are Claude's. Facts checked 2026-11-06: OCDS extension template and registry (ocds-standard-development-handbook, github.com/open-contracting/extension_registry); IDS 1.0 final 4 June 2024 (buildingsmart.org); IFC 4.3 as ISO 16739-1:2024 (literature review); ISO 10845-2:2020 scope; ISO/TC 59/SC 18 created 2015, secretariat SABS, chair Alain Jacquet to end of 2027, WG 1 maintains the ISO 10845 series, WG 2 governance (iso.org committee 5726139; so Watermeyer is no longer chair, and the prose now says he chaired it); IEEE 3119-2025 approved 27 March 2025, published 23 May 2025 (standards.ieee.org); AACE RPs open to public review (aacei.org); CCDC 23-2018 (literature review item 18); Rule 707 wording follows the literature review's "safe wording". Not checked: whether Canada is a P- or O-member of SC 18; AACE's authoring rules (its RP development document was not readable); CESMM4's fit for North American civil work (the Texas data uses TxDOT item codes).

Added 2026-11-06, 23:30 UTC (Andre: "name the one specific ask for the documentation standard and the bot standard. The document would probably be a .md/.json template to replace PDFs. For the bots, I do not know.... That is part of the reason to build the estimator. This is a weak link..."): the section "Two asks". The .md/.json template is Andre's idea. Claude's additions, all to confirm: requirement identifiers, the measurement crosswalk, addenda as versions, the public hash log (from Andre's ledger passage, positions §15, below), the PDF keeping the seal at first with the template "for reading" and a later flip of precedence; for the bot, the reading record (documents by hash, model, weights, prompt, settings, findings, time) as the one ask that does not depend on the estimator's answer, with the test set and tolerance left to v3.0.

Restructured 2026-11-06, 23:30 UTC (Andre: "Can you modify the chapter to focus on these ideas?", meaning the two asks): the chapter now leads with the two asks (the .md/.json template and the reading record) and follows them to existing standards. "What the standard is for" is folded into "Two asks"; "Starting and sticking", "The field-building level" and "A stadium with one player" are compressed into "Getting the asks to stick"; "The nearest standards" became "Where the asks land", grouped by ask (the template: measurement crosswalk, IDS, CCDC 23, ISO 10845-3; the record: OCDS extension, IEEE 3119; waiting for the estimator: AACE class, ISO 10845 new part, the courthouse). The JSON pay-item example is Claude's and invented. Dropped in the restructure: the Lang taxonomy (safety, interoperability, performance), the stadium's exploit hunters and bounty (the exploit passages stay below), Ukraine's ProZorro, the Scitovsky commodity line (it lives in chapter 9). The version before the restructure is in project files chapter-drafts/chapter-10-before-two-asks-refocus-2026-11-06.md.

vgr_zirp pass, 2026-11-07 (Andre: "look over the vgr_zirp answers in the other thread and incorporate what you think would be useful for this chapter"; project files vgr-zirp-review/session-1-answers.md and session-2-answers.md, plus edits-to-make.md). Applied here, all Claude's sentences: open with the tool and its numbers before the door and the mumble (session 2, answer 5: "the author built the tool before writing the manifesto. Lead with that every time"; lead with external data; the scores are chapter 9's, from the Texas DOT bid tabulations); name the stakeholders as the ones who adopt the asks early, not only in the villagers ending (answer 1); "less grand" became "more practical" (no apology for the subject); the record names the person who relied on it, building on chapter 9's "A flag without an owner is a flag nobody reads" (answer 4); the record narrows the ground to argue over and shifts the burden of explanation (answer 3, the Serpent point, moved to the record); the Listener explained on first use (answer 4, insider shorthand); "The standard is public so anyone can run it" (Andre's adopted statement, session 1 answer 5). Deliberately not used: the building-code profit frame and any reasoning about the author's benefit (Andre, 2026-11-06: state only the three statements); renumbering and cross-references, left to the thread "Implement vgr_zirp book suggestions" (chapter 10 may become chapter 11 there). Self-deprecation removed (Andre, 2026-11-07: "Yes, we are meant to remove self-deprecation. Not my style, but if we need to get things done, then it may be necessary."): "a kind of mumble" became "rested on one assumption"; "The mumble was about sticking" became "The old plan was weakest at sticking"; the record paragraph now opens on the question being one for evidence; "the weak link stays, but it is named" became "That sets the order of the asks".

Sentences that speak for Andre and need his yes: the opening line that the old plan "rested on one assumption"; the line about remembering the essay's title as "Standards Rule the World" (Andre named it that way in the thread; in the 2026 symposium introduction the project was described as being about "how standards rule the world", so the slip is a natural one).

Sources and where they are used:
- Lang, "Standards Make the World" (Summer of Protocols, 2023; web edition summerofprotocols.com/standards-make-the-world-web). Used in "Standards make the world", "What the standard is for" and "Starting and sticking". Quotes taken from the web edition: "made and remade by (usually small) groups of people"; "Standards-making is something that anyone can engage in, even though almost no one thinks to do it"; "rough consensus and running code" (David Clark, IETF, 1992, quoted by Lang); "we're doing this—are you coming?"; "The danger zone for standards is sometimes in the starting but always in the sticking"; "Start with a small group of true believers and gradually work outwards"; Jordi Puig-Suari on CubeSat, quoted by Lang: "it took about ten years for things to really take off" and "People needed to gain some comfort that these standards are going to be around for a while." To check: wording and pages against Andre's copy of The Protocol Reader (the Reader's table of contents could not be read online, so it is not confirmed that the essay is in it). The taxonomy (safety, interoperability, performance) is Yates and Murphy's *Engineering Rules*, the failure analysis is Carl Cargill's "Why Standardization Efforts Fail" (JEP 14:1, 2011), both met through Lang, so they are credited through him and not listed in Appendix D (the Gramsci-through-Rao rule).
- Lang, opening talk, Protocol Symposium 2026, 23 September 2026 (youtube.com/watch?v=nx-3L5Apbgw, his part from about 19:36). Used in "The field-building level". Quotes from the auto-captions, to check against the video: "name enthusiastically but define hesitantly"; area studies "didn't have its own self-sustaining economic flywheel"; capture "can really slow things down or make these things uninteresting". He also cites the Protocol Reader as a good field-building artifact.
- Lang, "Where are the field builders?" (Amateur Technology, Substack, 28 December 2024): "Field builders are fire starters"; "Once they start the flywheel, the usual suspects show up to go bigger". Not in Appendix D unless Andre reads it; the talk covers the same ground.
- Eghbal, *Working in Public* (Stripe Press, 2020). Used in "A stadium with one player": the four models (federations, clubs, toys, stadiums) on contributor growth against user growth; maintainers' attention as the scarce resource; maintenance as the lasting cost. Paraphrased, not quoted; check against the book. Lang lists the book among his own sources.
- ISO 10845 and Watermeyer: from the literature review (Part 6, items 15 and 16, verified). Watermeyer chairs ISO/TC 59/SC 18. OCDS and OC4IDS: literature review item 21; version 1.0 in July 2015 per Wikipedia (the review gives a first data-model release on 27 June 2014).
- Kelly Roegies, "A Government Guide to Open Protocols" (Protocolized, 19 March 2026): procurement criteria that treat upstream contribution as a resilience signal; seconding staff. Used in "A stadium with one player".
- How-to guides found but not used in the prose (for Andre to pick from): Dave Winer, "Manifesto: Rules for standards-makers" (scripting.com, 9 May 2017), whose rules include "Interop is all that matters", "If practice deviates from the spec, change the spec", "No breakage" and "Freeze the spec" (headings from a secondary listing, check against the original); the Standards Council of Canada's pages on international standards development and its mirror committees (scc-ccn.ca, Directives Part 1 and Part 3); the IETF's guide for newcomers, "The Tao of the IETF"; Andrew Russell, *Open Standards and the Digital Age* (Cambridge, 2014); Shapiro and Varian, "The Art of Standards Wars" (California Management Review, 1999).
-->

The tool exists. On public Texas bid data, the estimator missed the lowest bidders' prices by a median of 21 percent line by line, against 29 percent for the state's own engineer's estimate, and the last chapter showed what an evaluator built on it could save a buyer after the tender. It ended at a door, and behind it was the standard, World 2 on the map.

Until now, the plan for getting through that door rested on one assumption: build a model that is good enough, publish it, and the field would gather around it on its own: the owners would adopt it, the courts would find it, and one day a standards body would write down what it already did. The estimator would be the seed and the rest would grow.

That is not how standards get made, and the people who have made them say so plainly. So this chapter does something more practical. It makes two asks, one for each tool the prologue named: documents written for machines to read, and a standard bot to read them. Both are addressed to the people who already run tenders, the buyers, designers, bidders and their lawyers, because they are the ones who would adopt them. Then the chapter follows each ask to the standards that already exist and could carry it.

## Standards make the world

David Lang came to standards the way many builders do, by needing one. He co-founded OpenROV, a cheap, open-source underwater robot, in 2011, and watched its team turn from prototype builders into protocol designers once they found that the bottleneck in ocean technology was the connector, not the robot. His essay for the Protocol Institute's Summer of Protocols, "Standards Make the World", is the history of standards-making he went looking for along the way.

It is easy to remember the title as *Standards Rule the World*, and the difference between the two verbs is the whole of this chapter. A standard that rules is handed down from somewhere. A standard that makes the world had to be made first, by somebody. Lang's answer to who that somebody is: standards "are made and remade by (usually small) groups of people", and "standards-making is something that anyone can engage in, even though almost no one thinks to do it."

He describes two paths. The first is the formal one, with numbered steps: a proposal, a draft by experts, public comment, a revision, a vote, and publication. The second is the path the Internet took, summed up in David Clark's line about the IETF, "rough consensus and running code". Build something that works, get people using it, and give it formal governance afterwards. MIDI, USB and the CubeSat each began with a small group saying, in Lang's words, "we're doing this—are you coming?", and nearly all of them ended up in a consortium or a standards body. The disruptive path does not skip the committee. It arrives at the committee with something already running.

Construction procurement has walked both paths before. In 2005 Ron Watermeyer made the case for an international procurement standard built on South Africa's national ones, which already worked; ISO 10845 followed in 2010, and he chaired the ISO subcommittee set up in 2015 to maintain it. The Open Contracting Data Standard went the other way round: a small team, backed by the World Bank and the Omidyar Network, wrote a data format for publishing public contracts, released version 1.0 in 2015, and let governments pick it up one at a time. Neither standard computes anything. ISO 10845 fixes the procedure and OCDS fixes the record of the contract, and both stop at the edge of the question this book asks.

## Two asks

That question is who pays when a bot causes harm, and it decides what the standard is for. Someone will have to say what a reasonable bot would have read in the tender, so the standard is there to say which reading binds. Seen this way, the standard bot is a legal instrument before it is a technical one. Nobody is asked to trust the bot; they are given a reasonable reader they can cite in court. That also moves the project out of the innovation bucket, where public buyers are wary, and into the standards bucket, where they already know how to take part.

**The first ask is a template.** It replaces the PDF as the copy a bot reads: a tender package written as plain text, with Markdown for the parts people read and JSON for the parts machines count. Every requirement carries an identifier, every pay item a name from a shared list, and every addendum a new version of the file rather than a new pile of pages. A pay item in the template might read like this:

```json
{"item": "Excavation, common", "unit": "m3", "quantity": 1250,
 "requirement": "02-310-3.2", "version": "addendum 2"}
```

Nothing in it is new technology. A bidder's bot can read it without guessing, a person can read it without software, and two versions can be compared line by line. A fingerprint of each issued version goes on a public log, so anyone can prove later which version existed when. The PDF does not have to die on the first day. It can keep the seal for a while, as the stamped copy a court reads, with the template issued beside it "for reading". The order of precedence flips only when the villagers are ready, and that flip is the moment the zombie is finally laid to rest.

**The second ask is a record.** What a reasonable bot has to do is a question for evidence, not for a drafting committee, and the estimator is being built to answer it. A bot standard written today would be a guess with a version number. One part can be asked for now, though, because it does not depend on that answer. Every reading of a tender, by any bot, would leave the same trail: which documents it read, by their fingerprints; which bot read them, down to the model, its weights, the prompt and the settings; what it found; when; and which person chose to rely on it. That last line matters as much as the others. A flag nobody owns is a flag nobody reads, and a record without a name on it would go the same way. The record is written in the same plain format as the template, so the two travel together.

A court can work with a record long before anyone agrees on a tolerance. It can see what was read, by what, and whether the reading can be run again. The record cannot stop a bidder from gaming a bot, but it narrows the ground to argue over, and that has legal value: a party whose bot kept the record can show what it read, and a party whose bot did not has to explain why. And a record kept from the first day is the raw material the test set will later be built from. The rest of the bot standard, the public test set and the tolerance, is what version 3.0 of the estimator is for.

That sets the order of the asks: a template and a record now, and the test when the estimator has earned it.

## Where the asks land

Neither ask needs a new institution to start. Each can ride on a standard that already exists, kept by people who already meet. The map of World 2 shows them in the order they can be started.

![World 2, the Standard: an overworld map from World 1 through eight levels, each an existing standard with the change it would need (field building; OCDS and OC4IDS; IFC 4.3 and IDS; methods of measurement; CCDC 23; ISO 10845-3; AACE's estimate classes; IEEE 3119), to a castle, a new part of ISO 10845 for the reasonable bot, and past it a courthouse for the first case](../images/world-2-standards.png)

**Where the template goes.** The pay-item names need a shared list, and the lists already exist: a civil engineering method of measurement like CESMM4, or a state transportation department's catalogue of pay items. The template needs a published crosswalk to them, not a new method. On the design side, IFC 4.3 already covers roads, rail and bridges, and buildingSMART's Information Delivery Specification, final since June 2024, lets a designer state requirements a program can check; a use case for the items a bidder prices would tie the template's requirement identifiers to the model. The tender rules come next. In Canada, CCDC 23, the guide to calling bids written by a committee of industry associations, could carry a note on issuing the template beside the PDF and naming which one governs. ISO 10845-3, the standard conditions of tender, could add the rule the book gives the buyer's Listener, the bot that collects bidders' questions: a question raised by any bidder's bot is answered to every bidder, by a new version of the template.

**Where the record goes.** The Open Contracting Data Standard lets anyone write an extension: there is a template on GitHub and a registry kept by the Open Contracting Partnership. An extension for the reading record, and for the questions and versions around it, needs nobody's permission, only work, and it would put the record beside the contract data that governments already publish. On the buyer's side, IEEE 3119, published in 2025, walks a buyer through procuring an AI system, from defining the problem to monitoring the contract. A construction profile could require that any bot the buyer relies on keeps the record.

**What waits for the estimator.** The test itself has three stops. AACE's estimate classes measure how accurate an estimate can be expected to be, given how far the design has come; a conformance class beside them, agreement with a reference reading under a fixed protocol, is where the book's two to three percent belongs, since it measures something different from distance to the low bid. The castle is a new part of ISO 10845 holding the public test set, the tolerance and the record, reached through a national standards body; whether Canada sits on the subcommittee is the first thing to find out, and if it does not, a Canadian mirror committee would itself be a signal. Past the castle is the courthouse. The tests for expert evidence, Daubert in the United States and Mohan in Canada, ask for a method that can be tested and a known error rate, and the proposed federal rule on machine-generated evidence, withdrawn in May 2026, is being redrafted. The castle is built so that both answers are on the shelf when the first case arrives.

The order is the pitch. The extension and the crosswalk need nobody's permission, the guide notes and profiles need a membership and a committee, and the castle needs a national body and years. Each level gives the next one something already running.

## Getting the asks to stick

Lang borrows his best line on failure from Carl Cargill, a veteran of technology standards work: most standards efforts do not fail in the committee. They fail before it, when nobody launches them, or after it, when the finished standard finds no one who wants it. In Lang's words, "the danger zone for standards is sometimes in the starting but always in the sticking." The old plan was weakest at sticking. It assumed that a good model would stick because it was good, which is the one thing Cargill's history says is not enough.

Sticking is also a waiting game. The courts will not lean on a standard that does not exist yet, a standards body will not write one without a pilot, and a buyer will not fund a pilot without a return it can count. Each is being reasonable, and together they keep the door shut. The way out is a benefit one of them can capture now, and that is the evaluator's job: its savings arrive before any standard does. It is also why the two asks are small. A template and a record cost a buyer little, and they start piling up the evidence every later stop will need.

Lang's 2026 Symposium talk on field building adds the rest of the checklist. Fields do not generate themselves; someone builds them, often an outsider. Name the thing enthusiastically and define it hesitantly, so that "the reasonable bot" can grow into its test set instead of being fixed too early. Make artifacts: the estimator is one, the template and the record are two more, and so is this book. Recruit keystone people from neighbouring fields: someone who has sat on a standards committee, a construction lawyer who has argued over a reading, and inside an owner, whoever has to defend a change-order price in a dispute, who knows the pain best and needs no standard to find a reproducible number useful. Beware capture: the likely captor is a platform vendor whose own format becomes the standard by default, which is the strongest reason to keep the template and the record free. The standard is public so anyone can run it. And find the economic flywheel, which Lang says a field cannot live without; here it is the evaluator's savings, the claims never started and the reviews never paid for.

Then there is upkeep. Nadia Eghbal's *Working in Public* sorts open-source projects by how fast their users and contributors grow. The estimator today is a toy, used and maintained by one person. If the plan works it becomes a stadium, with many users and a few people on the field, and the lasting cost of a stadium is the maintainer's attention, not the first build. A liability standard is most fragile at that stage, because a court needs it to still be there, unchanged, when the claim arrives years later. The CubeSat took about ten years to take off for that reason; as one of its inventors, Jordi Puig-Suari, put it, "People needed to gain some comfort that these standards are going to be around for a while." New versions will need funding, and the pace of revisions will follow the value the market places on the standard. The way out of the stadium is the move Lang describes, into a consortium or a standards body where the people who rely on the standard share its upkeep. Owners can help before then: Kelly Roegies's guide to open protocols for governments suggests procurement criteria that reward suppliers who contribute upstream.

## The campaign for World 2

The versions in chapter 9 now line up with the two asks.

**Version 1.0, momentum.** One trade first, probably civil work, where public bid prices already exist. The template published for that trade, with its crosswalk to the pay items. The record kept for every reading, on an offline model whose weights do not change, and the OCDS extension that carries it. A small group of true believers, and this book as the vision paper.

**Version 2.0, proof of work.** The evaluator in an owner's hands, saving money the owner can count, and the first tenders issued with the template beside the PDF. The asks that need a committee go in: the CCDC note, the ISO 10845-3 clause, the IEEE profile.

**Version 3.0, the working model.** By now the records hold enough readings to build a test from. The test is written backwards from what it has to catch, not from the estimator's internals, so that a second vendor's bot can pass it too, and it goes looking for its castle.

The prediction can be wrong, and it should say how. If by 2035 no public owner anywhere runs a tender whose questions, addenda, bids and evaluation pass through agents on a published data format, the forecast failed. The standard itself is further out, in the ten to fifteen years the CubeSat suggests, and its first court challenge will probably come before it, from a dispute fought under the old rules.

The model was never going to generate the field. What it can do is give a small group of people a template to issue, a record to keep and something to argue about. That is how a standard starts, and the villagers, as the introduction promised, are the ones who decide whether it sticks.

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
