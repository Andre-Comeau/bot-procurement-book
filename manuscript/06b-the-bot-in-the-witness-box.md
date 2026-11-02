# The bot in the witness box

<!--
Part II. The machines (chapter 7, added 2026-10-31 after the bot council; chapters 7 to 10 after it moved up by one, and their file names keep their old numbers)
Target: 1,200 words, new
Brief: One constructed failure case, told start to finish: a tender with a quantity error, a bidder's bot that read it and stayed silent, a Listener that collated a neighbouring question and missed this one, the overrun, and the claim. The court asks what a reasonable bot would have found. Walk through what it needs to answer: a frozen, published version of the standard bot (pinned open weights, which a hosted, ever-updating LLM cannot offer) anyone can rerun on the same tender and get the same reading; its measured error rate on contracts it never saw; the signed record of who asked what and when; and the keyholder who chose to rely on it. Liability lands where the book says (design on the designer, reading on the bidder's bot, the addendum on the person who issued it) only if each of those exists. Separate the two properties the outline had merged: accuracy (the estimator's job) and defensibility under cross-examination (the standard's job).
Why: vgr_zirp's answer in the bot council round of 2026-10-30 (`C:\hex_ai\bot-council\transcripts\2026-10-30-the-reasonable-bot-book.md`): the liability objection is not answered by the outline, the estimator is scored on accuracy not defensibility, and without a failure case chapters 9 and 10 read as aspiration.
Sources: the case study's liability sections; positions 1, 2, 9 and 20; `context-bank/standards-and-limits.md`; the courts' tests for expert evidence, not yet checked (Daubert in the US; Mohan and White Burgess in Canada), which ask for a testable method and a known error rate.
Added 2026-11-02: Stevenson's "can't sue but can insure against" (see the prologue's note for source and caution) sets up the chapter's question: is the bot in the box a defendant, an insured system, or a standard of conduct? Also vgr_zirp, `C:\hex_ai\bot-council\transcripts\2026-10-18-gramsci-monster.md`: "The reasonable bot isn't tamed by becoming accurate; it's tamed by becoming *canonical*." 
Literature (`literature-review-2026-11-01.md`, Part 1): Roth 2017, "Machine Testimony"; FRE 707 (withdrawn May 2026; the redraft leans to requiring an expert); the Horizon judgment; Diamantis 2025; Chagal-Feferkorn; Green 2022 on oversight as theatre; Elish 2019.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Notes in italics are Claude's. Delete this section as the chapter is written. The chapter is new writing around a constructed case, so most of what follows is background for it, not text to cut.*

### The case: a quantity error the market priced and nobody reported

*The real pattern behind the constructed case is in chapter 1's added passage: on the Texas lines paid under 80% of the tendered quantity, every bidder priced cheap and the engineer's estimate sat 13% over. The bidders saw the error, priced it, and said nothing, and Andre called it "strong evidence of strategic bidding based on tender deficiencies". Build the failure case on that pattern, so the chapter is fiction resting on a measured fact.*

### Who decides what is reasonable

> How would estoppel be enforced for AI? On an international blockchain, localized courts would not have jurisdiction to enforce judgements. Smart contracts only work if all the terms are defined and verifiable on-chain. Once real-world liability and variability come into play, who becomes responsible for determining "reasonable"?
>
> This would imply the need for localized control of AI assets through escrow, bonding, or insurance. It also implies giving AI personhood like corporations: a need to give AI the legal right to assets, not only the chain-defined assets.
>
> The need to resolve disputes about real-world variability implies the need for AI judges. (Or human judges able to alter the chain.) Lots of questions on how this would work. Are blockchains even blockchains if they are mutable? How would AI judges work? Civil vs common law? Council vs monolith?

(`work-packages/procurement-machines/bot-philosophy.md`, "Bot procurement implications", said 2026-10-11. Andre opened this box to keep such thinking apart from the pragmatic build; it is offered here because the chapter is where the book meets that limit. His reference to the Protocol Institute's Town Hall on New Nature is cut from the quote.)

### Why the standard, not insurance alone

> Even AI will not help unless it can be liable for errors. The two low-hanging options for resolving this are insurance and standardization. Insurance may be difficult to implement, since the size and probability of claims will be hard to assess. AI companies could potentially self-insure, but the life-safety element would almost certainly lead to massive payouts. That is partly justified, since loss of life is to be avoided, but as with self-driving cars the accident rate can never be zero without a society-wide loss in quality of life.

> This points to standardization as the mechanism for risk mitigation. It would restrict the liability of the practitioner by acting as a checklist, and it would provide risk controls for potential insurers.

(`context-bank/background-notes.md`, "Priority topic", recorded 2026-10-01)

*Claude's note from the same file: in Canadian negligence law following a standard is evidence of reasonable care, not a complete defence (*Ryan v. Victoria*, 1999), so a checklist alone does not limit liability; that takes contract terms or legislation. The UK made self-driving cars insurable by statute, which suggests standardization and insurance work as a pair. This meets Stevenson's "can't sue but can insure against" in the hidden note: the chapter can set the insured system against the standard of conduct.*

### The record the court would ask for

> Record keeping would have helped the Army's case: recording what the bot did, and when, and why.

(positions §9, recorded 2026-10-07)

*Claude's note: the Army's case is* Trax v. United States*, filed 29 May 2026 and decided 22 September 2026: the court ordered the AI evaluations into the record and let the award stand (THESIS section 3, Claude's summary). It is the nearest real case to this chapter's trial; check the citation before printing.*

### What a reasonable bidder's bot would have found

*Claude's mechanism, not Andre's (positions §2.7, mechanism 1): in the United States a bidder who knew, or should have known, of a patent error and did not ask cannot price it later, and "should have known" is judged by what a reasonable bidder would have found. Once a reasonable bidder's bot would have found it, the error is patent. No new duty is written; the existing one bites harder. The frozen, published standard bot is what lets a court say what a reasonable bidder's bot would have found. The gap is Canadian, where the rule is less settled (`context-bank/disclosure-duty-research.md`).*

### The keyholder

*The keyholder is Andre's term for the person who signs the number and adjusts the flagged lines (THESIS section 4, citing decision 45). The chapter's last witness is a person: the keyholder who chose to rely on the bot.*
