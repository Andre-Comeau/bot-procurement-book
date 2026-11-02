# The protocol that follows

<!--
Part IV. The protocol that follows (chapter 10 since 2026-10-31; the file name keeps its old number)
Target: 800 words, new, short and honest
Brief: The tender as canonical, versioned, machine-readable data; bidders' bots that choose whether to raise what they find; a buyer's Listener that turns questions into addenda; a signed, citable trail. The modest path first: a standard bot for one trade, civil work or surveys, before a whole project. What would confirm the prediction, with its tolerance window. The standard specifies a conformance test (public versioned test set, tolerance, required record), not a model; the author's estimator is the first reference implementation that passes it, so another vendor's bot can conform too (2026-10-31). Why it starts on an offline model (Andre, 2026-10-31): hosted LLMs keep updating, so their readings cannot be rerun; pinned open weights on the author's GPU can. Any AI should be able to conform in time, but that is beyond the project's resources, so the offline model is the proof of concept that starts the flywheel and scales only if demand justifies the investment. Re-versioning, Andre, 2026-10-31 (verbatim): "this feels like the market will resolve this question. New version require funding. The pace of revisions will depend on the value placed on the standard by the market." Claude's note: a dispute between versions can still be settled by the tender naming the version it was read against, as a contract names a code edition; to confirm in the author's words.
Sources: THESIS sections 3 and 4; position 15 (one trade, a public ledger); `context-bank/standards-and-limits.md`; `context-bank/iso-10845-alignment.md`; the bot-first protocol card.
Literature (`literature-review-2026-11-01.md`, Part 1): ISO 10845 and Watermeyer; CCDC 23; OC4IDS; the ANAC agent competition; Sánchez-Graells 2024. Collusion (`collusion-papers-notes-2026-11-01.md`, Parts 3.1 to 3.3 and 3.5): who sees the reference price and when, publishing line items, evaluation rules, and a joint experiment with the Seoul group.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->


## Source passages: exploits (to cut and rewrite)

*Laid out by Claude on 2026-11-02, from the Scitovsky thread of 1 November 2026. Quoted passages are Andre's, copied unchanged from that thread. Notes in italics are Claude's. Andre asked for this discussion to go into the manuscript as the book's example of exploits. Delete this section as the chapter is written.*

*Why a public standard invites exploits:*

> There would be the risk of vendors gaming the system, but the below costs bids on line items is evidence that this is already happening. The standards we are working for may need to be accompanied by other AI reviewers to validate proposals and reduce the risks of accepting proposals exploiting the system.

> System exploits should be a risk. Based on complex video games, I am thinking about the world modelling series from Paradox games, there is usually sets of rules that allow for outcomes outside the intended framework. [...] Patches fix this, but since there is little real money flowing out of real accounts, the exploits can be fun if not used in a multiplayer game.

*The example, in Andre's words. The Luxembourg write-up he remembers has not been found online, so tell it as the author's own memory of the game rather than as a citation:*

> The main exploit was the paradrop. Surrounding enemy lines with paratroopers would prevent retreats and speed capture enormous territory. There was a step where war was declared against a country that could never be able to attack you. Tanu Tavu?

> The Tannu Tuva world conquest write-up is an even better example of the exploitability of computer programs. This was done by observant humans, image what trillions of tokens would do!

*Citable versions if wanted. Hearts of Iron IV players conquering the world as Tannu Tuva, a one-province nation, are documented on the Paradox forum ("Tannu Tuva World Conquest", thread 959544; "I managed to world conquest as Tannu Tuva (w/ tutorial)", thread 1500616); the forum blocked automated reading on 2026-11-02, so check the details by hand. A Steam thread of 31 January 2018 asks Paradox to fix the "Paradrop England exploit" (steamcommunity.com/app/394360/discussions/0/1700541698681349596). The lesson for the chapter: every move obeys the rules, but together the moves reach an outcome the designers never intended. That is what a bidder can do to a frozen, published standard bot.*

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
