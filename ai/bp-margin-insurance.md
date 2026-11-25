---
id: bp-margin-insurance
title: "Margin insurance for construction bids: covering an AI pricing tool across many tenders"
type: proposal
status: draft
summary: >
  The project's proposal for insuring bidders who rely on an estimating bot: a policy that pays when the
  bot's bids keep falling short of a target margin across many completed contracts, measured against
  costs the bidder declared on bid day, not when one job loses money. It is a proposal; no insurer
  offers it, and a draft term sheet exists for an underwriter to mark up.
updated: 2026-11-19
audience: [insurers, AI vendors, bidders, sureties]
questions:
  - Can you insure an AI construction estimating tool?
  - Why not insure a low bid directly?
  - What is the insurable event for a pricing bot?
  - How would margin insurance stop a bidder inflating costs?
related:
  - {id: bp-buyer-as-insurer, relation: contrasts}
  - {id: bp-stakeholder-insurers, relation: part-of}
  - {id: bp-estimator, relation: see-also}
  - {id: bp-reading-record, relation: see-also}
  - {id: bp-ai-strengths, relation: see-also}
  - {id: bp-stakeholder-bidders, relation: see-also}
  - {id: bp-stakeholder-vendors, relation: see-also}
  - {id: bp-sureties, relation: contrasts}
sources:
  - {title: "USDA Risk Management Agency, Margin Protection insurance", url: "https://www.rma.usda.gov/en/Policy-and-Procedure/Insurance-Plans/Margin-Protection"}
  - {title: "Bot Procurement (book in draft), chapter 3, 'Insuring the bidder's margin'", url: "https://books.andrecomeau.xyz/bot-procurement/working/06e-the-underwriters-chapter/"}
  - {title: "Bot Procurement (book in draft), appendix E, 'A draft term sheet for a pilot policy'", url: "https://books.andrecomeau.xyz/bot-procurement/working/app-e-pilot-term-sheet/"}
book: [06e-the-underwriters-chapter.md, app-e-pilot-term-sheet.md]
terms: [Margin insurance]
---

# Margin insurance for construction bids: covering an AI pricing tool across many tenders

> A proposal to test with underwriters. One losing job is not a claim.

## In short

- **The model it follows:** crop margin insurance, such as the US Department of Agriculture's Margin Protection plan. It pays when an area's average margin (revenue less set input costs) falls below a trigger, so one farmer's own costs cannot drive a claim. This design does the same for construction bids: an average across contracts, measured against costs declared on bid day.
- **Why not insure the low bid:** the bidder controls costs and could make every line pay out; a clever bot may bid low on purpose when the firm can still profit; and every winning low bid makes the bidder's finances worse before data arrives.
- **The insurable event:** a shortfall in margin, measured against a cost model built from costs the bidder declared in the estimate file on bid day (owned equipment, crew rates, a nearby yard).
- **The trigger:** the average margin across the covered, completed contracts falls more than a set number of points below the target. One losing job does not trigger anything.
- **Guards:** costs on site never enter the claim, so inflating them gains nothing; a false declaration voids cover; the insurer keeps a right to audit, as bonding companies do; the bidder carries a share of any shortfall.

## The draft term sheet (Appendix E, placeholders in brackets)

| Term | Draft |
|---|---|
| Insured | The software vendor whose bot prepares the bids; each bidder an additional insured, with recovery from a bidder who breaks a condition |
| Insured event | Margin shortfall on contracts won with the bot's bids, against declared bid-day costs |
| Trigger | Average margin on completed covered contracts more than [x] points below target |
| Measurement | Contracts followed to completion, up to [n] months after the policy period |
| Payment | [y] percent of the shortfall below the trigger; the bidder carries the rest |
| Premium | [p] percent of the contract price on each contract won, paid at award like a bond premium; the book's model puts the lowest fair price at about 0.11 to 0.15 percent ($8,800 to $12,000 on an $8 million contract) |
| Limits | [$] per contract; total no more than [n] times the premiums paid in the policy period |
| Key conditions | Bid and estimate file fixed and time-stamped before close; the bot's price within the range set by the reference standard, the range in force on bid day governing; a bid sent in below the range is not covered, because the bidder could run the public standard and see the gap before closing |

The project does not sell insurance and has no stake in the terms an insurer chooses.

## Four open questions for underwriters

1. Where does a probabilistic product's normal error end and a defect begin? Bringing error to zero would destroy the averaging that makes the tool useful.
2. Could insurance speed up adoption by replacing long trial periods? (Munich Re's public material makes this argument for AI cover generally.)
3. How should the tails be covered: capped, leaving vendor and client exposed, or priced in, making deals harder to close?
4. Would a shared reference standard lower premiums, by giving every product the same baseline to be measured against?

## Aside: the winner's curse

In a reverse auction the winning bid is often the one that most underestimated the cost. A bot that is right on average still wins disproportionately the jobs it got wrong. Unlike poker, the loss can exceed the stake. This is why margin, measured across many jobs, is the right unit, and why a bidder's market-tracking score alone does not tell an insurer what it needs.
