# The monsters we kept

<!--
Updated 2026-11-18 (Claude): "who pays" no longer framed as the book's spine question (Andre, 18 Nov); estimator references in future tense (Andre, 18 Nov: the Estimator and Model are in development); wording rule fixes.
New chapter (Andre, 16 Nov 2026, in the swarm thread): "Maybe we craft this into a chapter. If it does not fit within the book, we place it in an appendix. I supposed part of the reason to keep it in the book is the desire for this section to read close to protocol fiction. Appendix are usually for boring overflow."
His framing, carried in Claude's words: the discussion of discarded approaches belongs in the methodology of an experiment; these ideas are set aside mostly because the technology is assumed to be further out than the timeline for building a standard; "Based on the last two years of AI progress, this may prove to be wrong. AI swarms may gain enough stability to avoid the need for standards." He prefers "monstrous" to "failed": "Ideas that could be promising if it was not for their monstrous caracteristics." Placement: maybe at the end, "in order to keep narrative energy from dissipating".
Proposed place: Part IV, just before the meta-goal chapter, so the reader sees what the standard chose not to do before the book looks at where the field leads. Number waits for the whole-book pass. In the repo since 18 Nov 2026 as 09b-the-monsters-we-kept.md, after the trades chapter.
Target: about 3,000 words, new.

Draft 2026-11-16 (Claude). Every sentence is Claude's and needs Andre's voice pass. TONE.md was read first. Voice modelled on the zombie chapter (open on a scene, one image carried through, deadpan). The carried image is the cage; the refrain is "What would open the cage". The opening scene is invented (protocol fiction) and says so.

Field name: every creature here belongs to Bot Construction, the field, not to Bot Procurement, the standard. The wording rule of 14 Nov holds: the standard is never called earned, tested or defended.

Sources and backstage theory (not for the reader):
- The parliament and the gardener: Andre's idea of 14 Nov (requirements animated with their own bots, a negotiated solution instead of a central model dictating, consultants as "bot gardeners", good or bad depending on enjoyment of the design steps). Claude's three conditions (one shared score, vetoes for code, a kept record). Precedent not used in the text: Boehm's WinWin (USC, 1990s), not re-checked. Research note: project files research-library/swarm-coordination/swarms-read-aloud-2026-11-14.md.
- The hive: Jha and others, "s³: Simple Scaling of Swarms via Cooperative Multi-agent RL", arXiv 2611.08615 (5 Nov 2026), scalingswarms.com. Used: shared score, any member's right answer wins, a charge for words; the silent member; "speak once, to everybody, before reading" (about 80% of teams); personal rewards make sharing collapse (the authors' "public goods" framing, not used by name); remaining failures include trusting "unchecked reports". Small models, two puzzles, one run each. Add to Appendix D if kept.
- Many doors: chapter 12's staged section "One door or many" and research-library/one-door-or-many/. New York's Wicks Law; the studies disagree (Rojas 2008; NY Division of the Budget 1987, seen only through a critic). No figures printed here on purpose. Do not use vgr_zirp's "consistent finding".
- The flood: research-library/construction-software-vendors/flooded-tender-four-answers-2026-11-13.md (caps, keys, fees, published checks). Chapter 6 opens on the magazine editor (Clarkesworld, 2023), so this chapter only points back to it.
- A sixth creature, "the judge with a paper bond", was taken out on 18 Nov before this chapter went online, pending Andre's call (rewrite as a general idea or cut).
- The swarm that needs no standard: Andre's 16 Nov line. Scaffolding image is Claude's.
- The bid depository: checked 18 Nov for Yukon (Yukon Contractors Association rules, 1 March 2023), Saskatchewan (Saskatchewan Bid Depository Inc., against bid shopping) and Quebec (BSDQ); full sources in the trades chapter's note. Which provinces in all, and since when, is still not found.
- Wording to check with Andre: "bot gardener" is his; "parliament", "hive", "hydra" are Claude's names.
-->

A paper about an experiment usually has a section that most readers skip, where the authors list the approaches they considered and set aside. It is the least exciting part of the paper and one of the most honest, because it tells you what the authors bet against. This chapter is that section, moved to the end so that it doesn't slow down the story, and written with a little more affection than a methods section allows.

Bot Procurement is deliberately small. It asks for a readable tender, a published test, and a clear rule for when a bot is wrong. Everything in this chapter is bigger, bolder, and in several cases more interesting. The ideas here were not set aside because they are wrong. Most were set aside because they assume machines that are further along than the time it takes to write a standard, and writing a standard takes years. The next open format for building models, visited in the chapter on file formats, is planned to become an international standard at the end of 2029, and it started well before this book did.

That is a bet on timing, and timing bets can be lost. The last two years of progress in AI have embarrassed a good many careful forecasts. So the monsters are kept, not slain. Each one is described below with what it promises, the trait that makes it a monster, and what would open the cage. If the cage opens early, the book should say so first.

## The parliament of requirements

The first creature is the boldest.

Today the requirements of a building are gathered into one central model, and the model dictates. The fire separation is drawn. The accessible route is drawn. The budget is a number someone checks against the drawings afterwards, usually with a sigh. Once the documents are written for machines first, each requirement could instead be given its own advocate, a bot that speaks for it and bargains for it. The design becomes whatever the advocates agree on.

The promise is large. A negotiation can search far more arrangements than a design team has evenings, and every requirement gets a voice, including the ones that are usually remembered at the last coordination meeting. It is also, in a way, an old idea in new clothes. A good design meeting already works like this, with people in the chairs.

The monstrous trait is authorship. A negotiated building has no author. When it fails, every advocate did its job and the failure lives in the space between them, which is a space no court has ever sued.

Three things would have to be true before it could be let out. The advocates would need one shared score, for the building as a whole, because an advocate rewarded only for its own requirement never gives ground. Some advocates would need a veto instead of a vote, because the building code is not a preference to be traded for floor area. And the bargaining would need a record a stranger can read, every offer and every concession, so that when something fails, someone can find where.

Then there is the gardener. In this world the consultant stops drawing the solution and starts tending the advocates that produce it: deciding what gets planted, how much room each plant gets, and what to prune. Whether that is a promotion depends on the person. A designer who loves finding the form by hand loses the part of the work they enjoy most. A designer who loves weighing one need against another gets more of it. The profession would likely split along that line, and nobody should pretend it wouldn't.

What would open the cage: an insurer willing to cover a negotiated design, and a regulator willing to let a person sign for a negotiation instead of a drawing.

## The hive

The second creature lives on the builder's side, and it is already half out.

A general contractor pricing a building runs a small swarm of its own. Every trade sends in a price, and the bid fails if one is missing, if two trades price the same piece of work, or if a piece of work falls between them. In November 2026, a team of researchers at the University of Washington and the Allen Institute for AI published an experiment that looks a great deal like this. They gave small teams of identical AI agents a job that none of them could do alone, let them message each other whenever they liked, and gave the whole team one score: a win if any member handed in the right answer, minus a small charge for every word the team used. Nobody was told how to organize.

The teams organized themselves anyway, and the way they did it is worth a builder's attention. Early on, many teams had a silent member who never shared what it knew, and those teams lost. Later, members whispered to each other one at a time, then shouted at everyone, over and over. By the end, most teams had settled on a habit nobody taught them: each member says what it knows once, to everybody, before reading anything. Speak first, then listen.

When the researchers rewarded each member only for its own answer, the habit collapsed. Sharing only helped the others, so every member learned to wait for someone else to go first, and in the end nobody went. Builders will recognize the trades who send their prices four minutes before the general contractor's deadline, so that nobody has time to shop them to a competitor. Parts of Canada answered that with a closed box, the bid depository, which every trade price has to go into before a set time. It is the same habit, enforced with a lid.

The promise of the hive is a builder's estimating team that organizes itself, divides the drawings without being told, and stops measuring the same walls six times. Inside one firm, that is not very monstrous at all, because the firm answers for its bid whoever in the hive got it wrong.

The monstrous trait shows only when the hive crosses a property line. The researchers' teams worked because nobody inside them was credited or blamed. That is excellent for a team that shares one wallet and terrible for a group of separate firms, each with its own margin, its own insurer and its own lawyer. The researchers also listed the faults their teams kept, and one of them is the oldest risk in estimating: members sometimes trusted a report they had not checked.

What would open the cage: a hive that checks its members' reports as a matter of habit, and a way for separate firms to share one score without sharing one wallet. Until then, the hive lives inside the firm, and between firms the tender stays.

## The hydra

The third creature has many heads, one for each trade.

It is a fair question. If machines can read the documents, why should a buyer go through one general contractor at all? The buyer could tender each trade separately, through many doors instead of one, and keep the general contractor's margin for itself.

The promise is a cheaper building, at least on paper. New York has required separate trade contracts on many public buildings for most of a century, and the studies of whether that saves money disagree with each other, which is itself a kind of answer.

The monstrous trait is that each head can be held responsible for its own piece, and none for how the pieces fit. A single door survives because there is one party behind it to answer for the whole, with a surety behind that party to make the answer worth something. Cut off the general contractor and the buyer becomes the one holding everything together, whether or not it meant to.

What would open the cage: someone, bot or firm, who coordinates the pieces and can be sued for the coordination, with a bond to match.

## The flood

The fourth creature arrived before this book did. In February 2023 a science-fiction magazine closed its submissions because machines had learned to write stories faster than people could read them.

The promise, for tenders, is more competition. If a bot can prepare a bid in an hour, small firms that could never afford an estimator could bid on work they are qualified to build, and a buyer who used to see three bids might see thirty.

The monstrous trait is the same as the magazine's. A buyer who sees three hundred bids, most of them plausible and many of them careless, cannot read them, and the cheapest of them is not the best one. The flood does not have to be malicious to drown a buyer. It only has to be cheap.

The tools to tame it are old and dull: limits on how many bids one firm may send, a key that proves a bid came from a real firm, a fee or a bond that makes a careless bid cost something, and a published check that every bid must pass before anyone reads it. Highway buyers already use rough versions of all four.

What would open the cage: a published check that a buyer can trust to sort the plausible from the careless, which is, as it happens, roughly what this book asks for.

## The swarm that needs no standard

The last creature is the one that could eat this book, and it would be dishonest to leave it out.

Everything in Bot Procurement assumes that machines will need help being trusted: a readable tender, a published test, a clear payer. That assumption rests on how unreliable today's bots are, and on how long it takes them to get better. If swarms of bots become stable enough, quickly enough, they might simply be trusted the way a large, well-run firm is trusted today, on its record, without anyone writing down a standard first. The machines would be the standard.

It is a real possibility, and the last two years make it more real, not less.

What can be said for the cage is that even a reliable swarm will one day be wrong about a bridge, and on that day someone will have to make it good. A standard is the answer written down in advance, before the bridge, by people who have time to think. If the swarms arrive first, that answer will be written afterwards, by a court, in a hurry.

And if the swarms do arrive early and well, the standard will have been scaffolding. Scaffolding comes down when the building can stand on its own, and nobody calls that a failure of the scaffolding.

What would open the cage: a buyer's legal department that signs off on a swarm's evaluation of a public tender without asking for a test, and an insurer that covers it without asking for one either. Watch for that day. If it comes, this book should be the first to say so.

## Feeding the monsters

A cage is not a grave. Every creature in this chapter is fed a little, on purpose.

The standard asks for documents written for machines first, which is what the parliament of requirements would need. It asks for a record of what a bot read and decided, which is what anyone would need to find the failure between two advocates, or two members of a hive. It asks who makes good when a bot is wrong, which the hydra cannot yet answer. And it asks for a published test, which is the only thing that could tell anyone, early, that the swarm no longer needs one.

So the small project and the big creatures are not at war. Bot Procurement is the part small enough to try first. Bot Construction, the field, is where the monsters live, and where some of them will one day be let out.
