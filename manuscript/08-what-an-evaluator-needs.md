# What an evaluator needs

<!--
Part III. The proof (chapter 9 since 2026-10-31; the file name keeps its old number)
Target: 1,500 words, new, the author's hand
Brief: The Fair and Reasonable Evaluator as it would stand in operation by summer 2027: the Witness and the Oracle, the keyholder who signs the number, the record rather than the duty, a public buyer-side code base, and the three things it still lacks: project data, a validation set of real decisions, and compute. Validation is more than hitting 2 to 3 percent: versions frozen and published, results a third party can reproduce, and the error rate disclosed with every number, so the keyholder can defend relying on it (bot council, 2026-10-31). What a data partner gives and what it gets back. This chapter has almost none of the author's existing sentences, because the tool does not exist yet, and it is the one chapter to write from scratch.
Sources: positions 3, 9, 10 and 11; `context-bank/test-set-design.md`; `context-bank/privacy-options.md`; the Witness and Oracle passage in the case study.
Added 2026-11-02: two uses for the Evaluator, cleared by Andre for the book: pricing a tender before it goes out, and reviewing change-order prices on a running project, where no market test exists (see chapter 8's note on the F&R Reviewer side quest). Rare items are flagged, never silently priced.
Literature (`literature-review-2026-11-01.md`, Part 1): Canada's Directive on Automated Decision-Making and its impact assessment (a template for public test plus required record); Chen, Zaharia & Zou 2023; Thinking Machines 2025 (pin the prompt, harness and inference stack, not only the weights). Collusion (`collusion-papers-notes-2026-11-01.md`, Part 3.4): screens the Evaluator could run on the same bid tabs, which flag for review and never auto-reject.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Notes in italics are Claude's. Delete this section as the chapter is written. The outline says this chapter is written from scratch in Andre's hand; these passages are the few he has already said about the tool, to draw on or set aside.*

### The Witness and the Oracle

> The base structure is a two-bot system, duplicating the one the World Machines project uses to control copyrighted material. One bot does the searching, with access to the full corpus, and hands off the required information to the second bot, which publishes it. The split helps prevent accidental slippage, since the outward-facing bot does not have direct access to the files. World Machines calls the two bots the Witness and the Oracle.

> Procurement will likely want stronger controls for document sharing, so having the Oracle review the information from the Witness for accidental transmittals would be a useful tool, since some information could be transmitted with complete data and other information would need to be sanitized. There would likely need to be information and keys associated with the data to allow this, which the Oracle could verify for potentially sensitive information.

(`case-studies/andre-comeau/README.md`, "The testing device")

*Claude's note from `context-bank/privacy-options.md`: the published designs (Willison's dual LLM pattern, DeepMind's CaMeL) put the gate in code rather than trusting a model to follow a rule; CaMeL is the published form of "information and keys associated with the data", and costs some capability (77% of test tasks solved with protection, 84% without).*

### The bots make the choices; the keyholder signs

> Not bad ideas. A little more knobs and dials than I want for now. These are specialist tools; the bots should eventually do this work without inputs from an occasional user. Add them as features for future versions.

(positions §10, recorded 2026-10-07, on the parameters of a commercial estimating suite)

*Claude's reading there: each such choice enters as one the Witness makes and records in the ledger, which the keyholder can see and overturn, not as a setting a person has to know. Rare items are included and flagged for the keyholder (decision 45).*

### The record, and a public buyer-side code base

> Record keeping would have helped the Army's case: recording what the bot did, and when, and why. Part of the goal is lessening the time needed by a human reviewer, so punting all the reviews to the carbon machine does not help. Perhaps the code for the Buyer-side bot would be public.

(positions §9, recorded 2026-10-07; also in chapter 5, so quote it in one place)

> Perhaps the bid evaluating bot, to be true named later since this would not be the Listener, could be published to the bidders? This would allow them to see how their bid will be reviewed and sorted. Would this approach be supported by the current legislation and related court cases?

(the collated process note, said 2026-10-06)

*Claude's note from positions §9: built so far is a run-time ledger with one hash-chained entry per bot action as the release key, human review concentrated on flagged lines, and the keyholder's reason as the record of judgment. Public code makes the clerical steps auditable once; it does not make a model's output reproducible, so the output itself is logged. Chapter 10's exploit passages are the risk on the other side of publishing the evaluator.*

### Two uses: before the tender and after award

> That post-award situation is the use case for the F&R Reviewer. The Reviewer provides a protocol for evaluating prices on an ongoing project without needing to go to open tender.

(`context-bank/background-notes.md`, section 3; quoted with its context in chapter 3)

### What it still lacks: data, a validation set, compute

*Decision 40 (2026-10-05, the decision's wording): "The public bid databases are used to train the bots; the goal is the application of the system to the user's own data. Public data teaches the market price; a user's own cost history stays in their own Witness." That is the core of what a data partner gives (its history, kept in its own Witness) and gets back (a market price checked against it).*

*Claude's note from `context-bank/privacy-options.md`: three different things need protecting in a partner's data, with different rules: identifying information, copyright in tender documents and standards, and commercially sensitive prices (with competition law if several bidders' prices are pooled). The collusion notes add the fourth: pooled bid data can help tacit collusion (Part 3.4).*

*No passage of Andre's on compute is on file beyond the offline-model reasoning in chapter 10's hidden note (pinned open weights on his own GPU). This is the part of the chapter that is his to write.*
