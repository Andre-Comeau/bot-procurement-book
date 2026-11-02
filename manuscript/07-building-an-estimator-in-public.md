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

