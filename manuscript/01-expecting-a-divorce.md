# Starting a relationship expecting a divorce

<!--
Part II. The question (chapter 5 since 2026-11-07; it was chapter 1)
Target: 1,200 words, redraft
Brief: The tensions of tendering: the one-shotted design, the long compile, the bidder who prices the errors and sues later. The three-way nexus from the case study's opening paragraph is the chapter's spine.
Sources: `case-studies/andre-comeau/README.md` (opening and "Who bears the cost of finding errors"), the two paragraphs on tenders ignored or overpriced from `sentences-since-3-october.md`. Andre, 2026-10-31, after reading Galbraith (verbatim): "Our work would raise the organizational capacity to process information. This feels like the correct approach since the current system of PDFs and digital drawings does not seem to produce any slack over the use of paper plan's room. They did raise processing capacity by removing the need to travel to bid, but the actual attention needed remained the same." (In Jay Galbraith's terms the bidder's cushion for drawing errors is slack; the book's choice is to raise processing capacity instead.)
Literature (`literature-review-2026-11-01.md`, Part 1): Bajari, Houghton & Tadelis 2014 (adaptation costs 7.5 to 14 percent of the winning bid puts a number on pricing the errors); Thaler, *The Winner's Curse*; Latham 1994; Tirole 2009.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-10-30. Every quoted passage is the author's, copied unchanged from the file named under it. Notes in italics are Claude's. Delete this section as the chapter is written.*

*The spine, the three-way nexus from the case study's opening:*

> Construction procurement runs on protocols that are better described as tensions to be managed by the parties involved than as problems waiting for a solution.

> The heart of the problem lies in the nexus between three things: the strict design lock-in needed for baselining projects for Tenders; the challenge of applying a software level of version control, with live updates, in a world where most workers do not have access to a computer and where constant review of the "code" would be expected to decrease productivity; and the additional low-cost review of documentation that AI now provides.

(`case-studies/andre-comeau/README.md`, opening)

*The one-shotted design and the long compile. These are also chapter 6 material, so keep them here only as far as the tensions need them:*

> **One-shotted design.** While there is iteration within the Design, it needs to ship with all desired features. Some "softer" elements such as interior design can remain flexible, but most systems are resistant to anything but marginal changes.

> **Long compile times.** Even the sub-modules take a long time to compile, which makes changes expensive. For a Change Order, the typical flow is: Design, Tender, Contract Award, Compile, Error (RFI), Design for the bug fix, discussion about cost impacts and, if there are any, pricing for the bug fix, review of the pricing, formal modification of the code and costs, communication of the change to the hardware processing the code, and performance of the changes.

(`case-studies/andre-comeau/README.md`, "Procurement redescribed as software development")

*The bidder who prices the errors and sues later, with the chapter's title line:*

> Bidder bots would need to be able to read and interpret drawings and specs. Ideally, they would detect and communicate discrepancies, underdefined requirements, or unaccounted-for unknown conditions in the plans and specifications.

> While many companies make their margin by pricing projects accounting for unresolved errors in the bid, this generates a lot of animosity and requires active legal claims. It moves the profit and skill away from the field and into the meta-game. It also distracts the effort from product delivery to protection from legal proceedings. Some of this is needed to ensure remedies exist for unknown unknowns, but starting a relationship expecting a divorce feels like an incredibly ineffective system.

(`case-studies/andre-comeau/README.md`, "Who bears the cost of finding errors")

*Tenders ignored or overpriced, from the collated process note. The outline asks for two paragraphs: the first is the one it names, and the second is my best match. Swap it out if you meant another.*

> These days a tender with too many issues is ignored or overpriced since the work to ask questions is greater than the likely reward. It does not help that the questions often go unanswered since there is often insufficient time or resources to address multi-sub-consultant issues.

> One major issue with any bot procurement are real world issues that live outside the Tender. Subsurface conditions is one, but road closures, weather delays, etc. are hard to factor and would still create ambiguous bids. We may need to accept this. The CCDC contracts have already resolved standard solutions for equitable splits of risk and rewards for this.

(`case-studies/andre-comeau/sentences-since-3-october.md`, quoting the collated process note, said 2026-10-06)

*Optional, on the book's method of labelling tensions. It may belong in "How to read this book" instead:*

> Perhaps the best approach would be to keep things in tension until a trade-off decision needs to be made. In the meantime, they should be labeled as Frontier, Monstrous, Kafka, or Tool-building tensions, based on my essay on the subject.

(positions §21, recorded 2026-10-11)

*Word count of the passages above is about 470 of the 1,200 target. Left for chapter 8: the duty-to-report passages, the banana peel and the construction manager as a fourth party.*

*Added 2026-11-02: evidence that bidders already price the errors. Andre's reaction on reading what the Texas payment reports show of quantities bid and paid:*

> This feels like strong evidence of strategic bidding based on tender deficiencies, the type we debated in the project's discovery phase.

(positions §2.7, added 2026-10-16)

*Claude's figures behind it, from the same section (1,230 Texas contracts paid out): 40% of priced lines were paid under 95% of the tendered quantity. On lines paid under 80%, every bidder had priced cheap against the middle of the bids (the low bidder 21% under) while the engineer's estimate sat 13% over: the overstated quantities were visible to the market and priced, not reported. In 20% of contracts another bidder would have been cheapest at the quantities actually paid, at a cost of 1.5% of all that was paid. In one sentence: the present system prices the deficiencies into the bids and pays for the order of the bids being wrong about one time in five. Check the figures against `work-packages/estimator/RESULTS.md` before printing them.*

*The word for the bidder's cushion. Andre's Galbraith note (in the hidden note above) frames it: the cushion is slack, and the book's choice is to raise processing capacity instead. His older sentence on the limit of any tool:*

> The tool is a hack that cuts across the tensions created by these artifacts: the procurement documents, the construction contract and the building model. The tool can work without understanding those forces, but the existing literature could give insight for building it. More importantly, the research should expose the limits of bot procurement. The Bidder's bot can only be as accurate as the Buyer's data.

(`context-bank/background-notes.md`, "The tool and the artifacts it cuts across", recorded 2026-10-01)
