---
id: bp-buyer-as-insurer
title: "The buyer as its own insurer: who stands behind the reference price"
type: proposal
status: draft
summary: >
  The book's base case for who carries the risk of a reference bot's price is a proposal: the buyer
  stands behind the reference price itself, under a payment rule fixed and fingerprinted before bids
  open, with third-party insurance for the smaller buyers and bidders it would not cover. Over enough
  tenders, cheaper bids should outweigh the occasional payout.
updated: 2026-11-19
audience: [buyers, insurers, lawyers, bidders]
questions:
  - Who should pay when a reference bot's price is wrong?
  - Can a public buyer self-insure an AI price?
  - How would a buyer stop bidders from bidding low and claiming high?
  - What happens with lump-sum contracts?
related:
  - {id: bp-overview, relation: part-of}
  - {id: bp-liability-gap, relation: answers}
  - {id: bp-margin-insurance, relation: contrasts}
  - {id: bp-reading-record, relation: depends-on}
  - {id: bp-stakeholder-insurers, relation: see-also}
  - {id: bp-stakeholder-buyers, relation: see-also}
  - {id: bp-competition-risk, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 3, 'The insurable event'", url: "https://books.andrecomeau.xyz/bot-procurement/working/06e-the-underwriters-chapter/"}
  - {title: "US Federal Acquisition Regulation 52.211-18, Variation in Estimated Quantity", url: "https://www.acquisition.gov/far/52.211-18"}
book: [06e-the-underwriters-chapter.md]
terms: [Buyer as its own insurer, Reference bot]
---

# The buyer as its own insurer: who stands behind the reference price

> This is the book's base case, and it is a proposal. The mechanism below is the project's working sketch and has not been checked by counsel.

## In short

- **The tension:** a probabilistic process that lowers costs for all parties, against the question of who carries the cost when it is wrong.
- **The move:** the buyer insures the reference price, not the bidder's performance. Over many tenders, cheaper and tighter bids outweigh the occasional payout.
- **The trigger:** a formula fixed before bids open, computed by a neutral party after, using the market (bids on this tender and the same items in other lettings), never the winning firm's own costs.
- **Who else:** third-party insurance remains essential for small buyers and for marginal bidders the self-insurer will not sponsor.

## Why the buyer

The buyer already controls its cost through the reverse auction and already carries estimate risk on unit-price jobs: when a real quantity departs far from the tendered one, the price is reset (the US federal clause FAR 52.211-18 uses a 15 percent band; many highway agencies use about 25). That reset is negotiated from the costs of the overrun, which is where claims live, so it is a warning about how not to settle, not a model. The bidder has no matching control: it shifts risk down to subcontractors and keeps the upside when costs come in low.

## The rule, fixed before opening

1. Before bids open, the buyer fixes the reference price and its method and records a fingerprint of both, so it can never be revised. Whether the reference itself is revealed before close is an open question: the draft standard releases nothing to bidders before close, for competition reasons ([the competition risk](bp-competition-risk.md)).
2. After opening, a neutral party compares the reference with the market: the bids received and the same items in other lettings that quarter.
3. If the reference missed by more than the agreed band, the buyer pays a set amount (the gap times the quantity, minus a deductible, capped). Otherwise nothing.

This is parametric insurance, like area-yield crop insurance, which pays on the county's harvest rather than one farm's.

## Gaming, and what stops it

| Who | The game | What stops it |
|---|---|---|
| Bidder | Bid low, claim high | Its own costs never enter the formula; unbalanced-bid rules still apply; payouts are capped and shared |
| Buyer | Shade the reference low to pull bids down, then deny | The reference is fixed and fingerprinted before opening; anyone can rerun it on the pinned model; a third party computes the trigger |
| Bidders together | Steer the market average | The trigger uses many lettings and regions; existing bid-rigging screens |

## Where it is hardest

Lump-sum jobs. Counterparties would argue hard about whether other jobs are comparable. On unit-price roadwork, line items make comparison straightforward; on lump sums the comparison set itself has to be fixed before opening. Basis risk (the formula paying when the bidder was fine, or not paying when it was not) is the price of avoiding a cost-based dispute.

## Aside: alike bots fail together

A standard makes bots alike, and alike bots make the same mistake in the same week. An insurer cannot spread that risk across bidders, which is one reason the buyer, who sees the whole market, is a better first insurer than a carrier pricing one bidder at a time.
