# Appendix C. Glossary

<!--
Appendices
Target: about 600 words
Brief: Keyholder, Witness and Oracle, Listener, pinned and published specifications, the four protocol strategies, bot nomenclature.
Sources: `glossary.yaml` and position 6.
Added 2026-11-09: Rehearsal contracts and the final test (Andre's wording rule; see the entry for rehearsal contracts in the source-passages list).
Added 2026-11-02: Robotic construction, defined from the field notes as construction by robots "meant to be controlled by *other programs*" (see chapter 12's note). Faithful channel (the Listener that never answers). Patent and latent errors, as the published checks divide them.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. `glossary.yaml` turned out to hold the cards' acronyms (AASHTO, CCDC, GAEB and so on), not the project's own terms, so it serves the acronym half of this appendix. The project's terms are defined in these places; the wording of each is Andre's meaning, edited by Claude, unless marked.*

- **Bot Construction and Bot Procurement** (Andre, 2026-11-14; Claude's wording): Bot Construction is the field, where the work leads, from documents written for machines to robots on site. Bot Procurement is the book and the standard, the part kept small enough to test: the price on a tender and who pays when a bot gets it wrong. It has to be earned before the field can lean on it. Stated in the prologue.
- **Listener**: "The Listener's primary role is collating questions from Bidders, whether human or bot. It may communicate the equivalent of a head bow, a shake or a shrug" (positions §6). The name is C3PO's, for a bot with no outward voice.
- **Witness and Oracle**: the World Machines pair; one searches the full corpus, the other publishes and never sees the files (case study, "The testing device"; positions §6: they describe the inside of any owner-side bot).
- **Keyholder**: the person who signs the number and adjusts the flagged lines (Andre's term; THESIS section 4, decision 45).
- **Pinned and published specifications**: "Must-have and critical systems would be *pinned*; portions of the specification that need a baseline to guide bidders, without needing specific performance, would be *published*" (positions §8).
- **The four tension labels**: Frontier, Monstrous, Kafka and Tool-building (positions §21), defined in Andre's Substack essay "Age of AI, the age of protocols".
- **Bid cushion**: what is paid to owners before profit, which Andre puts "in the variable cost pile" and not in overhead (positions §23).
- **Rehearsal contracts and the final test** (Claude's wording, 2026-11-09, to confirm; Andre's rule that the book never calls the check "sealed", "blind" or "scored once"): the book's plain names for two of the three sets of data an estimator meets. The estimator *learns* from past contracts (researchers: training data). It is *rehearsed* on contracts set aside while it is built, and each version is chosen knowing how the last one scored (researchers: validation data, the data used to tune and to choose between versions). It is *finally tested* on newer bid results the project has left alone (researchers: test data), once there is a product and someone interested in the answer. Researchers use "validation" and "test" in this order, so a paper on this project says validation data for the rehearsal and test data for the final check; some medical and statistics writing uses "validation" for the final check instead, so define the words wherever they are used. Accuracy and error bands for any pitch come only from the final test.
- **F&R (fair and reasonable) Reviewer and Evaluator**: the reviewer folded into the estimator on 2026-10-05 (decision 46); the Evaluator is the tool chapter 1 describes, a stepping stone toward the standard. Fair and reasonable is the public buyer's price test, narrower than the book's question (who pays when a bot causes harm).
