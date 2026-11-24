---
id: bp-competition-risk
title: "The competition risk: when every bidder leans on the same bot"
type: risk
status: draft
summary: >
  A shared reference price can act as a focal point that moves bids together, and bots built alike make
  the same mistakes at the same time. The evidence on publishing a buyer's estimate cuts both ways. The
  project's draft standard therefore releases nothing to bidders before bids close and treats the
  reference as a check, never a price. The question is open and belongs with competition lawyers.
updated: 2026-11-19
audience: [lawyers, bidders, buyers, standard writers, researchers]
questions:
  - Could a shared AI reference price help bidders collude?
  - What happened when a highway agency published its engineer's estimate?
  - Why does the project say "check and record, never set"?
related:
  - {id: bp-reference-bot, relation: contrasts}
  - {id: bp-buyer-as-insurer, relation: see-also}
  - {id: bp-ai-failure-modes, relation: see-also}
  - {id: bp-stakeholder-bidders, relation: see-also}
sources:
  - {title: "De Silva, Dunne, Kankanamge and Kosmopoulou (2008), 'The impact of public information on bidding in highway procurement auctions', European Economic Review 52(1): 150-181", url: "https://eprints.lancs.ac.uk/id/eprint/52461"}
  - {title: "Bot Procurement (book in draft), chapter 8, 'The bidders: racing for the light'", url: "https://books.andrecomeau.xyz/bot-procurement/working/02c-the-bidders/"}
book: [02b-the-buyers.md, 02c-the-bidders.md, 05-liability-shifts.md]
terms: [Reference bot]
allow_words: [tested]
---

# The competition risk: when every bidder leans on the same bot

> The project's rule: check and record, never set. The open question is whether that is enough.

## In short

- **The worry:** a reference price everyone can see before close becomes a target. Bids cluster around it; estimating effort weakens; collusion gets easier. Japan's ministries warn of exactly this about published reserve prices.
- **The evidence the other way:** when Oklahoma began releasing its engineer's estimate to bidders (from 1999 to 2000), average bids fell about 5 percent relative to Texas and their spread narrowed; winning bids did not move significantly (De Silva et al., 2008).
- **The correlated-error worry:** the winner's curse works because each bidder's estimate has its own error. If every bidder uses the same bot, errors stop being independent, and the same mistake lands in every bid in the same week.
- **The project's position:** the reference is a check that flags lines for each firm's own review; nothing it produces is released to bidders before close; the firm sets its own spread.

## Where the line is in competition law

Bidders may not discuss prices with each other. Pooling non-public competitor data through a shared tool is where recent cases have drawn the line. A public reference built on public bid results, used by each firm privately to check its own bid, is different from a shared engine setting prices, but the boundary has not been tested in a tender case. The project leaves the question to competition counsel and asks for a competition authority's view before any part of the standard goes beyond trial use.

## How the draft standard handles it

From the project's working draft (not public): no release of any output to bidders before close by anyone acting under the standard; no shared no-cost reference; no public per-contract price vectors; and before two implementations are called independent, their independence is measured and published (from the project's draft standard, not yet public).

## Aside: never say winning bids fell

The Oklahoma result is easy to overstate. Average bids fell and tightened; the winning bid did not move significantly. A later experiment (Oo, 2017) found lower, tighter bids but no clearly lower winning bid. The honest reading is that public information disciplines the field without obviously changing the price the buyer pays.

## Aside: the smaller ambitious firm

The case for a shared check is strongest for a smaller firm stretching to a bigger job. It cannot ask competitors what they think; a check is the respectable way to confirm its own hand calculation. The case against is strongest for the largest jobs, with few bidders, where a focal point matters most.
