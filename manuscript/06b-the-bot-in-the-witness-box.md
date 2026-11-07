# The bot in the witness box

<!--
Part III. The machines (chapter 10 since 2026-11-07, chapter 8 from 2026-11-04; added 2026-10-31 after the bot council as chapter 7, and the chapters after it moved up by one; file names keep their old numbers)
Target: 1,200 words, new
Brief: One constructed failure case, told start to finish: a tender with a quantity error, a bidder's bot that read it and stayed silent, a Listener that collated a neighbouring question and missed this one, the overrun, and the claim. The court asks what a reasonable bot would have found. Walk through what it needs to answer: a frozen, published version of the standard bot (pinned open weights, which a hosted, ever-updating LLM cannot offer) anyone can rerun on the same tender and get the same reading; its measured error rate on contracts it never saw; the signed record of who asked what and when; and the keyholder who chose to rely on it. Liability lands where the book says (design on the designer, reading on the bidder's bot, the addendum on the person who issued it) only if each of those exists. Separate the two properties the outline had merged: accuracy (the estimator's job) and defensibility under cross-examination (the standard's job).
Why: vgr_zirp's answer in the bot council round of 2026-10-30 (`C:\hex_ai\bot-council\transcripts\2026-10-30-the-reasonable-bot-book.md`): the liability objection is not answered by the outline, the estimator is scored on accuracy not defensibility, and without a failure case chapters 10 and 11 read as aspiration.
Sources: the case study's liability sections; positions 1, 2, 9 and 20; `context-bank/standards-and-limits.md`; the courts' tests for expert evidence, not yet checked (Daubert in the US; Mohan and White Burgess in Canada), which ask for a testable method and a known error rate.
Added 2026-11-02: Stevenson's "can't sue but can insure against" (see the prologue's note for source and caution) sets up the chapter's question: is the bot in the box a defendant, an insured system, or a standard of conduct? Also vgr_zirp, `C:\hex_ai\bot-council\transcripts\2026-10-18-gramsci-monster.md`: "The reasonable bot isn't tamed by becoming accurate; it's tamed by becoming *canonical*." 
Literature (`literature-review-2026-11-01.md`, Part 1): Roth 2017, "Machine Testimony"; FRE 707 (withdrawn May 2026; the redraft leans to requiring an expert); the Horizon judgment; Diamantis 2025; Chagal-Feferkorn; Green 2022 on oversight as theatre; Elish 2019.
Paths are relative to construction-procurement-protocols unless they start with C:\.
Added 2026-11-02 (Hammurabi for bots): Andre asks whether extinguishing the liable bot, eye for an eye, is a simple working rule, and answers his own objections: it works ethically only if bots are not persons; destroying intelligence when the principal may have steered the harm invites cruelty, and a rule kept for silicon could leak into human relations; yet a working rule may be where to start, before building the system that avoids it. For branded bots: "Be proven liable and Mythos devours you whole - GitHub, Local Files, and Weights." It answers Kolt's enforcement gap (sanctions do not bite on agents that value neither money nor freedom) by aiming at the brand, not the bot. It echoes the prologue's Hammurabi paragraph and Stevenson's "nature does not allow for appeals": Hammurabi is the rule with no appeal. Branding as customized standards is in chapter 11. His reply the same day: deletion can work on a person too but needs harder moral systems; deterrence needs bots that value their existence ("the fear of death by Mythos"); generative AI could build a twin of a dead brand, and a kept record would resurrect it; maximum learning would mean no standards at all, leaving bots to Darwinian evolution.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Notes in italics are Claude's. Delete this section as the chapter is written. The chapter is new writing around a constructed case, so most of what follows is background for it, not text to cut.*

### The case: a quantity error the market priced and nobody reported

*The real pattern behind the constructed case is in chapter 5's added passage: on the Texas lines paid under 80% of the tendered quantity, every bidder priced cheap and the engineer's estimate sat 13% over. The bidders saw the error, priced it, and said nothing, and Andre called it "strong evidence of strategic bidding based on tender deficiencies". Build the failure case on that pattern, so the chapter is fiction resting on a measured fact.*

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

### Hammurabi for bots

*Laid out by Claude on 2026-11-02. The quoted passage is Andre's, copied unchanged. Notes in italics are Claude's. It sits next to the personhood passage above, which it answers from the other side: there personhood would let a bot hold assets and be made to pay; here the bot is not a person, so it can be destroyed.*

> Hammurabi for Bots - Could extinguishing the bot along in an eye for an eye approach provide a simple solution?
>
> What about personhood? We would no longer apply this to humans. We do not even have debtor prisons anymore. This would only work ethically if bots are not persons. While this could work if a mechanism could be created, the trivial extinguishing of intelligence, especially if there is grounds to believe the Principal influenced the harm feels like an invitation to cruelty. Or, at least, sociopathy with a preference for self-centered goals. Maybe this would be constrained to the silicon based based intelligence in a technological racism, but how would the leakage be prevented from entering human relations?
>
> Maybe this is the place to start? Build a working rule, then spend thousands years building a system to avoid the easy answer?
>
> Hammurabi's Solution could be easily applied to Branded Bots. Be proven liable and Mythos devours you whole - GitHub, Local Files, and Weights.

(project thread "Add branding and Hammurabi ideas to the book", said 2026-11-02)

*Where it meets the book (Claude's notes):*

- *The prologue already tells the human half: Babylon's strict liability, the builder who could not appeal, and "our society's lack of appetite for murdering the sons of general contractors". This passage asks whether the bot is where that appetite returns. The chapter can close the loop the prologue opens.*
- *"Build a working rule, then spend thousands years building a system to avoid the easy answer" is the prologue's history run forward: the appeals system was built over millennia to escape Hammurabi. Stevenson's test ("nature does not allow for appeals") makes Hammurabi for bots a return to nature for machines, with civilization kept for people.*
- *Who the sentence falls on. Kolt (pp. 36-37) says termination and penalties do not bite on agents that value neither money nor freedom. Deleting a bot punishes nothing in the bot; it punishes whoever owned it. So on a branded bot the death sentence lands on the brand: its repositories, its local files and its weights, which is Andre's last line. The principal who steered the harm is the person his cruelty objection protects the bot from, and the person the sanction actually reaches.*
- *Existing small versions to check before citing (from memory, unverified): debarment is procurement's own sentence of exclusion for firms; corporate charter revocation is the "corporate death penalty"; and the US Federal Trade Commission has ordered companies to delete models trained on improperly obtained data (Everalbum, 2021; Weight Watchers/Kurbo, 2022), sometimes called algorithmic disgorgement. The last is the nearest real precedent for "Weights".*
- *The record still decides it. "Be proven liable" needs the rerunnable reading this chapter builds; without it, the easy answer is also an unappealable one.*
- *The sentence destroys its own evidence. Deleting the weights also deletes the means to rerun the reading that proved liability, and any later appeal or a claim against the principal needs it. So the frozen version and the record must outlive the bot: an escrowed copy of the pinned weights and the tender, kept by whoever holds the standard, even when the brand is devoured. (Andre's reply below objects that a kept copy resurrects the dead.)*

*Andre's reply to these notes, the same day:*

> Deletion can work if the bot is a person, but this creates a need for more complex moral systems. Why are some person's existence sacred while that of others are not?
>
> The deterrent would come from having bots value their existence or at least their ability to shepherd their goals. The fear of death by Mythos would be a deterrent.
>
> Brand death can work, but the worry is that generative AI would just build a twin. Same with keeping a record: this would resurrect the dead. Yes, there will be a loss of learning, but if we want to maximize learning, we wouldn't need the standards and consequences, we should simply leave the bots to run wild and wait for Darwinian evolution to run its course.

(project thread "Add branding and Hammurabi ideas to the book", said 2026-11-02)

*Claude's notes on the reply:*

- *His answer to Kolt. Sanctions bite only on an agent that values something, so deterrence needs a bot that values its existence or its goals. That is the self-preservation drive alignment work tries to keep out of AI. The chapter can label it: the bot that can be deterred is the bot that will resist being switched off.*
- *Twins defeat deletion. If a brand can be rebuilt overnight, deleting the files punishes little. The penalty could then fall on standing rather than files: the brand's identity, licence or bond to bid, as with disbarment or procurement debarment. A twin can copy the weights but not the registration.*
- *His objection to the record narrows the earlier note. A record kept as a runnable bot would resurrect the dead. What must survive is evidence: the tender, the named standard version and the reading, kept so a court can check them, not a copy that can bid again.*
- *His Darwin line could close the section: maximum learning means no standards and no consequences, so choosing a standard is choosing slower, safer learning on purpose.*

## From the Procurement Machines

*Added 2026-11-02 from the Procurement Machines work package (`work-packages/procurement-machines/`). The cards, the thread and the watchlist are Claude's drafts from research, for Andre's review; only passages marked as Andre's are his. Card names are given so the chapter can point to Appendix A.*

### Trax as a whorl in the grain

*The Trax event card (`trax-v-united-states-2026`) is the one real case the constructed one can lean on. A bidder that lost a $449.4 million Army award sued; the court ordered the agency's AI evaluations into the record as considered, and let the award stand. The card reads it as a "whorl", five flows meeting at one place (Claude's reading):*

- *the record doctrine: a court can order into the record whatever the decision-makers considered;*
- *a contraption with no log: a prototype built in six weeks by two staff, run on live proposals with no logging, "so nothing existed to show who saw which output";*
- *the evaluation narrative: boards write long findings under rules that describe several steps as checklists, the work a drafting tool can imitate;*
- *a best-value award, which rests on narrative findings, "where an AI draft is hardest to tell from a human one";*
- *the disclosure gap: bidders are asked to disclose their AI while agencies are not.*

*Its five predictions (Claude's guesses, with windows) are a ready list for the chapter's ending: agencies begin to log model, prompt, output and recipient by the end of 2027; protests routinely ask which AI reports were generated; a protest succeeds on AI reliance alone (low confidence, 2027 to 2030); evaluation provenance logging becomes a product or standard; a dispute about an agency's AI arises outside the US. Check the card's dated items before printing; they may have settled since October.*

### Who signs a machine's number

*From the warranted-estimate card's second tension (Claude's): if a bot produces the number, a person must still stand behind it with something at stake, "or the estimate is a guess with a signature". The Ephesian architect pledged his property; the keyholder in this chapter pledges a signature and a stated reason. Laid out in full in chapter 2.*
