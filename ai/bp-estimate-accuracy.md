---
id: bp-estimate-accuracy
title: "How accurate are construction estimates? Fifty years of human figures"
type: evidence
status: draft
summary: >
  Human estimates of the lowest construction bid are looser than most people assume: United States
  highway engineer's estimates land within 10 percent of the low bid on about a third (Washington State)
  to a half (national review) of jobs, and contractors' own bids for one job typically spread about 6
  percent around their average. Any AI price check has to be judged against these figures, not against
  an exact answer.
updated: 2026-11-19
audience: [researchers, estimators, buyers, insurers, standard writers]
questions:
  - How accurate are engineer's estimates on highway projects?
  - How much do contractors' bids for the same job differ?
  - What accuracy should an AI construction estimate be held to?
  - What is the difference between estimate accuracy against bids and against final cost?
  - How often does the low bid come in far below the engineer's estimate?
  - How often is the lowest construction bid far below the second-lowest bid?
  - How often do contractors underprice construction work?
related:
  - {id: bp-estimator, relation: see-also}
  - {id: bp-change-pricing-problem, relation: see-also}
  - {id: bp-sureties, relation: see-also}
  - {id: bp-stakeholder-insurers, relation: see-also}
sources:
  - {title: "FHWA, National Review of State Cost Estimation Practice, February 2015", url: "https://www.fhwa.dot.gov/construction/contracts/2014cost.pdf"}
  - {title: "Okere (2017), Construction Economics and Building 17(2): 92-114 (4,062 Washington State DOT projects, 1992-2016)", url: "https://epress.lib.uts.edu.au/journals/index.php/AJCEB/article/download/5348/6036/24688?inline=1"}
  - {title: "Pearl, Akintoye, Bowen and Hardcastle (2003), on bias and consistency in South African and UK estimating", url: "https://journals.ufs.ac.za/index.php/as/article/download/1991/1959/3838"}
  - {title: "TxDOT letting archive of bid tabulations (2017 to 2024) and Caltrans bid summaries (2000 to 2008), counted by the project", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Hinze, Selstead and Mahoney (1992), Cost Overruns on State of Washington Construction Contracts, Transportation Research Record 1351", url: "https://onlinepubs.trb.org/Onlinepubs/trr/1992/1351/1351-013.pdf"}
  - {title: "Dyer, Kagel and Levin (1989), Economic Journal 99: 108-115, experienced construction bidders in common value auctions", url: "https://core.ac.uk/download/357544725.pdf"}
  - {title: "Dyer and Kagel (1996), Management Science 42(10): 1463-1475, how the construction industry corrects for the winner's curse", url: "https://doi.org/10.1287/mnsc.42.10.1463"}
  - {title: "Survey: 1 in 3 Construction Companies Earning Less Than Expected (Intuit QuickBooks and TSheets, 2019)", url: "https://www.forconstructionpros.com/business/business-services/financing-insurance-leasing/news/21067180/intuit-quickbooks-survey-1-in-3-construction-companies-earning-less-than-expected"}
  - {title: "Liu et al. (2014), Underpricing for construction projects: a double-edged sword, PMI Learning Library", url: "https://www.pmi.org/learning/library/underpricing-construction-projects-8958"}
book: [03-how-a-price-is-judged-today.md, 07-building-an-estimator-in-public.md, 06e-the-underwriters-chapter.md]
terms: [Engineer's estimate, Bid spread]
---

# How accurate are construction estimates? Fifty years of human figures

> The bar for an AI price check is set by people, and people miss by more than most assume.

## In short

- **US highways, national:** the low bid fell within plus or minus 10 percent of the engineer's estimate on 48 percent of projects (774 of 1,611, from 2012 and 2013; FHWA, 2015).
- **US highways, Washington State:** about a third of 4,062 projects from 1992 to 2016 within 10 percent (Okere, 2017).
- **Bids on one job:** contractors' tenders for the same project spread around their average with a mean coefficient of variation of 5.65 percent (Pearl et al., 2003). An early UK study saw "little prospect" of getting that spread below 8 percent (Beeston, 1975, as cited there).
- **Quantity surveyors (UK and South Africa):** about 52 percent of estimates within 5 percent of the accepted tender and 75 to 84 percent within 10 percent (figures collected by Pearl et al.).
- **Consequence:** a check that aims closer than about 6 percent to any single bid is aiming inside the noise. A check is more useful at flagging outliers than at predicting the winning number.

## How often a price comes in low

"Low" means three different things, and only two of them are public.

**Against the buyer's estimate.** The project counted state highway construction contracts. Texas, 2017 to 2024 (5,718 contracts): the low bid was more than 10 percent under the engineer's estimate on 32 percent, more than 20 percent under on 12.5 percent, and more than 30 percent under on 4 percent. California, 2000 to 2008 (5,072 contracts): 49, 32 and 17 percent. The share swings with the market, from 16 to 43 percent a year in Texas and from 25 to 82 percent in California, where 2008 was the crash.

**Against the other bids.** The second-lowest bid was more than 10 percent above the low bid on 33 percent of Texas contracts and 35 percent of California contracts, and more than 20 percent above on about one in eight in both. Against the median of the other bids, the low bid was more than 20 percent lower on 28 percent (Texas) and 31 percent (California). The bids on one contract spread with a median coefficient of variation of about 12 percent in both states, about twice the spread reported for South African building tenders. On 468 Washington State contracts (Hinze and others, 1992), a wide gap between the two lowest bids did not predict a larger overrun.

**Against the winner's own cost.** This is the low that loses money, and it is rarely public. In a 2019 survey of 666 US construction firms (Intuit QuickBooks and TSheets), 29 percent said they usually make less profit than estimated. In a 2014 survey in New South Wales (43 responses), 38.5 percent said their last completed project was underpriced. In laboratory auctions, experienced construction executives bid below break-even on 16 of 24 winning bids (Dyer, Kagel and Levin, 1989), yet in the field the industry corrects for the winner's curse through learned habits and ways back from a bid that went too low (Dyer and Kagel, 1996).

**What follows.** Human prices run far below the market often, and lose money less often. A low bid's distance from the rest says the winner priced differently, not that it priced wrongly. Any AI price check needs to report its own lean, the share of contracts where it falls far below the bids, beside its typical miss, and name the period, because the lean moves with the market. For what bonding companies (sureties) do with the spread, see [sureties](bp-sureties.md).

## Two numbers, not one

Since the 1970s the quantity-surveying literature has split accuracy into **bias** (the average signed error: does the estimator lean high or low?) and **consistency** (the spread of errors: how far can one estimate be trusted?). A bias can be corrected with one factor; poor consistency cannot. A standard that reports only a median miss mixes the two.

## Two kinds of range, never mixed

Cost-engineering ranges such as AACE's estimate classes compare an estimate with the **final cost**, after contingency and scope change. Highway figures (FHWA, Okere) and quantity-surveying figures (Pearl) compare an estimate with **bids**. A bid-day second opinion is the second kind. Megaproject overrun figures (for example Flyvbjerg's) measure something else again: years of scope change and incentives, not bid-day error.

## How the project's estimator compares

On the project's own checks, an early version came within about 10 percent on whole contracts, level with the state engineer's estimate, and missed by a median of 21 percent line by line ([the estimator](bp-estimator.md)). Those are the project's own figures; nobody outside has rerun them.

## Aside: what courts have called a reasonable margin

Negligence cases on cost advice have tolerated a "reasonable margin" (about 10 percent in older cases) and later looked for a specific failing in how the estimate was made rather than the size of the miss alone. The project reads this as support for recording method, not only result ([the reading record](bp-reading-record.md)). *Case names and holdings are in the project's research notes and need reading at the source before citation.*

## Aside: what a standard should report

From the project's research: report hit rates in bands (within 5, 10 and 15 percent) so results line up with fifty years of human figures; report bias and spread separately; and treat a bias that persists across periods as a sign of pressure on estimators, not only as noise.
