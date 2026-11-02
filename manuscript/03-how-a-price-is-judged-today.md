# How a price is judged today

<!--
Part I. The question
Target: 1,200 words, mostly new
Brief: What "fair and reasonable" means to a public buyer, the engineer's estimate, the sold price books and the free bid tabulations, and the author's finding that a bot comes within about 20 percent of a human price line by line and must come within 2 to 3 percent before anyone trusts it alone.
Sources: positions 18, 22 and 23 (margins, return on capital, the bid cushion); `context-bank/what-buyers-pay.md`; `context-bank/bot-procurement-process.md`; `context-bank/contractor-margins.md` for one or two figures only.
Correction (2026-11-02, checked against `C:\hex_ai\estimator-workspace\RESULTS.md`): "within 20 percent" is slightly generous. Line by line on the locked test set, v0.3 misses the mean of the three lowest bids by a median 21.0% against the engineer's estimate's 28.6%; at the contract total by 13.0% against 14.4%. Say "about 20 percent" or "about a fifth". Useful for the chapter: the target itself is noisy, since the three lowest bidders differ from each other by a median 50% line by line, and one of them misses the other two by a median 25%. The engineer's estimate misses the three-lowest total by a median 11.2%.
Literature (`literature-review-2026-11-01.md`, Part 1): FHWA 2004 guidelines and 2015 review (engineer's estimates within 10 percent of the low bid on 48 percent of projects); USDOT OIG 2019; De Silva et al. 2008 (publishing the estimate lowered bids); UK Should Cost Model guidance; PSPC 2023 pricing guide; AACE 18R-97 and 98R-18; the $600-hammer story as a possible opening. Andre keeps the 2 to 3 percent target as a contractor's standard, not an engineer's (2026-11-01).
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Notes in italics are Claude's. Delete this section as the chapter is written. The outline calls this chapter "mostly new", so there is less of Andre's text here than elsewhere.*

### What "fair and reasonable" means to a public buyer

*Two moments when a price must be judged: at tender, by the market, and after award, when there is no market. Andre's sentences on both:*

> Comparing bot-based procurement with integrated project delivery could provide high-level protocol evaluations for future presentations. Integrated delivery already exists as a procurement approach, but it is not dominant. The market-rate verification inherent in the traditional competitive tender continues to provide significant value that is difficult to replicate in an integrated approach. This is especially true in the public sector, where procurement policies restrict non-competitive awards to prevent patronage and the appearance of conflicts of interest.

> Integrated delivery should stay in the background as a meta-goal. Competitive tendering makes the tender stage adversarial, but once the contract is awarded, changes are usually resolved in an integrated way, because many factors make it unfeasible to put changes on an ongoing project out to open tender.

> That post-award situation is the use case for the F&R Reviewer. The Reviewer provides a protocol for evaluating prices on an ongoing project without needing to go to open tender.

(`context-bank/background-notes.md`, sections 2 and 3, recorded 2026-10-01. In 2026-10 Andre kept the reviewer's use case out of the case study as "too technical for industry outsiders"; on 2026-11-02 he cleared it for the book as a side quest, see chapter 8's note.)

### The engineer's estimate, the price books and the bid tabulations

*No passage of Andre's on file. Claude's summary of `context-bank/what-buyers-pay.md` (searched 2026-10-18), for the chapter's money picture: bidders pay hundreds to a few thousand dollars a seat a year (electronic bidding about $60 a month; cost data from about $400 to $2,300 a year; a heavy-civil estimating seat about $4,000). Owners pay millions for platforms and estimate contracts (one state's year of the AASHTOWare suite about $2.15 million; a California on-call independent cost estimator contract listed at $4 to $6.5 million). Nobody pays for a standard directly. Most of these are third-party figures; check before printing.*

*Claude's summary of THESIS section 2, for the cost-data machine: the price book is being split between sold databases and free bid tabulations, and its accuracy, measured by this project on a million Texas rows, is level with a moving average. The evidence that bids lean on the errors (Texas payment reports, Andre's "strong evidence of strategic bidding") is laid out in chapter 1; it also shows the engineer's estimate sitting 13% over on the lines where bidders priced cheap.*

### Within a fifth, and the 2 to 3 percent a bot must reach

> With a divergence of more than 20% on multi-million dollar contracts, it seems unlikely that bots would replace humans any time soon.

> For Bot Procurement to be automated and trustworthy, the range would probably have to close to within 2% to 3% of human pricing. Perhaps unfeasible with today's technology, standards and datasets, but higher variance would simply default to human effort duplication, since the spread is greater than the cost of the estimator.

(positions §18, recorded 2026-10-11)

*Andre's answer to the literature review (2026-11-01, from project memory, to be put in his words): the 2 to 3 percent stays, because it is a contractor's standard, not an engineer's. Contractors carry the pricing risk, and 10 percent on a $10 million job is $1 million. Set against it, from the review: the FHWA found engineer's estimates within 10 percent of the low bid on only 48 percent of 1,611 projects. The current numbers are in the hidden note above.*

### Margins, return on capital and the bid cushion

> Perhaps one method to gain insight would be to research the annual reports of publicly traded construction companies, especially any with heavy civil specializations. This could give us insight on profit margins, which likely cloud the estimation process. The consultants and owner pay the total price, but actual costs may be more fixed than costs plus profits.

(positions §18, recorded 2026-10-11)

> We may need to model profitability differently. The return on revenue is too small to justify investment. Treasury yields provide a better investment.

> The proper mechanism would be to look at return on capital and free cash flow. This would drive the own versus lease choice, since leases pass the costs to the buyer on a winning bid and allow the bidder to operate with less capital.

> Many of the low-bid items would be owned equipment. Assuming that they would sit at the yard if unused, giving them away through the low bid would only cost wear and tear, which may be similar in asset depreciation effect to sitting in the yard. The low bids in these common low-bid items may be reflective of actual costs.

(positions §22, recorded 2026-10-12)

> Assuming that most companies have pay structures more closely linked to performance, we are starting to see a "bid cushion". When we add profits, executive compensation, unrealized depreciation, perks, and arms-reach deals, what are we looking at? What about political patronage, event sponsorship and charitable activity? If these are paid before profits, then they should be in the variable cost pile. We can look at fancy offices, company trucks for everyone, executive retreats, travel allowances, etc. later.

> I want to avoid the use of overhead for these items, since this term is usually used for expenses that are hard to assign to individual projects, but are still necessary for project success.

(positions §23, recorded 2026-10-12)

*The outline allows one or two figures from `context-bank/contractor-margins.md`; none are chosen yet. Keep this section short, since the book's focus is the framework.*
