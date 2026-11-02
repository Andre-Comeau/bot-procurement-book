# Building an estimator in public

<!--
Part III. The proof (chapter 8 since 2026-10-31; the file name keeps its old number)
Target: 1,200 words, half new
Brief: Why the estimator came first and the reviewer second; Texas for development, Alberta as control; three versions marked against held-back contracts, line by line closer than either benchmark; at the total the first two were behind the engineer's estimate and the third (v0.3) is level. The lesson of the draft that had every citation and no judgment. Told as a short narrative with dates from the decisions file, not as a log. Say what the scores prove (accuracy on unseen contracts, a known error rate) and what they do not yet prove (that a court would accept the number).
Sources: the case study's "The testing device"; decisions 27, 32, 46, 62 and 64; `context-bank/residential-estimating-log.md`; `pitch/readability/README.md` for the plain-language test.
Correction (2026-11-02, checked against `C:\hex_ai\estimator-workspace\RESULTS.md`): "two versions … at the total still behind" predates v0.3. Median miss at the contract total on the locked test set: engineer's estimate 14.4%; v0.1 16.3% and v0.2 16.1% (behind); v0.3, 13 October, 13.0% (level, about a point ahead). Line by line v0.3 21.0% against 28.6%. The two lean opposite ways: v0.3 about 5% low at the total, the engineer about 4% high. So: three versions, the third level at the total.
The F&R Reviewer as a side quest (Andre, 2026-11-02): the estimator was the main line and the reviewer folded into it (decision 46), but the same model serves a second use for a public buyer: reviewing a proposed price on a running project, such as a change order that cannot be re-tendered, by comparing it with the price the model would give. After award a change has no market test (`context-bank/background-notes.md`).
"The Estimator is the flywheel" (Andre, 2026-11-02, from the portfolio handoff): the standards are free, and the estimator is what turns, funds and proves them. A good closing line for the chapter or a bridge to chapter 10.
Literature (`literature-review-2026-11-01.md`, Part 1): Mohamed & Moselhi 2022; CEQuest; Abdelaty's WYDOT engineer's-estimate project, for comparable accuracy figures and why a public test set matters.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Notes in italics are Claude's. Delete this section as the chapter is written. The book's focus is the framework, so this is the one development chapter; keep the details for the general reader light.*

### Why the estimator came first

> In a bot-based procurement system, the Bidder's bot would be the critical piece of infrastructure. If this were easy to build, the work could start there. The original plan was to start elsewhere: since the entire process is untested, and the best-practices for this type of system are still being developed, a simpler owner-side bot would provide a training ground for bot construction and system building. If human engineering provides an appropriate analogy, the F&R bot would only need to analyze, while the estimator would need to design.

> It would still be easier to build an analyzer than a designer from a theoretical perspective. However, the discovery of several public databases of bid prices, and of the Texas Department of Transportation's open bid tabulations in particular, should give enough depth to go straight to the estimator. Since the estimator is the more complex of the two, the reviewer can then be based on this work.

(`case-studies/andre-comeau/README.md`, "The testing device"; the order was set by decision 32 on 2026-10-03, and the reviewer folded into the estimator by decision 46 on 2026-10-05)

### Texas for development, Alberta as control

> On one hand, the larger Texas database seems like it should be used, since it has the larger sample size. On the other, the smaller Alberta set may be better for system building, since the larger Texas set could then act as the population. Which test set is usually used in these conditions?

(`context-bank/test-set-design.md`, Andre's question of 2026-10-03)

*Claude's answer there, which matches decision 27: build on Texas and test on a part of Texas held back by date, with Alberta as a second, separate check. Texas and Alberta are two populations, not a sample and its population. Andre on why the project began in heavy civil at all:*

> The publicly available heavy civil price data is of interest because a private company has expressed interest in using AI for estimating. I have done some work in heavy civil, but my expertise is more in buildings, and I had been picturing the building sector for this project without making that explicit. Since Alberta publishes unit price data that is almost ready-made for our approach, I should move out of my comfort zone and start there.

(`context-bank/background-notes.md`, section 1)

### Heavy civil is the proving ground; buildings are the target

> The current approach was designed around the available resources, especially the datasets. Take-off capacity is a high-value target for future versions. We may be over-indexing on heavy civil construction. OpenTakeoff is closer to my end goal of self-performing tenders. Civil packages come with drawings that inform line-item prices for specific specifications.

(positions §11, recorded 2026-10-07)

> The primary users of the bot procurement system we are building would involve projects where complexity prevents line by line negotiations because no one has enough expertise to serve as a single point of contact. When negotiating a tender would require negotiating with a committee.

(positions §11, added 2026-10-17)

### The versions as experiments

> Besides a better estimating tool, one of the main goals is to discover the best structures for bot based estimating. Run the different attempts as experiments in an attempt to isolate which variables improve and which decrease precision and accuracy.

(decision 62, said 2026-10-10, when a local Mistral model was set to write its own estimator under Claude's direction)

> Keep the current format. The line by line approach helps visualize the range between owner, bidder, engineer.

(decision 64, said 2026-10-11)

*The scores for the three versions are in the hidden note above. The narrative's dates: Texas for development and Alberta as control 2026-10-02, the estimator first 10-03, the reviewer folded in 10-05, the experiments 10-10, the line-by-line form 10-11, v0.3 level at the total 10-13.*

### The draft with every citation and no judgment

> The most useful lesson so far came from a live draft that had every citation present and every box checked while avoiding the judgment underneath, which only surfaced when a person read it and said, plainly, that it did not work.

(`case-studies/andre-comeau/README.md`, "The testing device"; the sentence may be Claude's, since Claude wrote the case study's description of the app. Ask Andre whose it is and which draft it was before telling the story.)

### The estimator as a souvenir, and as the flywheel

*Andre's meaning, edited wording:*

> The standards were always going to be the end-boss. We are still too early in the journey to know whether the fight will be worth it, hence the side-quest formulation. If the doors open easily, early involvement with the standards organizations could give the project a lot of energy. If it is hard, or the project fizzles or is replaced by another interest, we should still have an artifact: the estimator, as a souvenir.

(`context-bank/horizon.md`, recorded 2026-10-05)

*Set beside "the Estimator is the flywheel" (hidden note above), this gives the chapter its arc: the estimator began as the souvenir in case the standards fight failed, and became the thing that turns, funds and proves the standards.*
