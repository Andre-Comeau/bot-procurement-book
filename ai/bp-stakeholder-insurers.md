---
id: bp-stakeholder-insurers
title: "Stakeholders: what insurers stand to gain"
type: stakeholder
status: draft
summary: >
  Insurers already measure AI products one at a time, with custom validation each time. A shared
  reference standard, a proposal, would give them a baseline for measuring how far any estimating
  product deviates, and the project proposes insuring margin across many tenders rather than any
  single low bid.
updated: 2026-11-19
audience: [insurers, sureties, AI vendors]
questions:
  - Would insurers cover AI construction estimating?
  - How would a standard help insurers price AI risk?
  - What do insurers need to see before covering an AI tool?
  - Where do sureties fit among the insurers of AI construction estimating?
related:
  - {id: bp-margin-insurance, relation: has-part}
  - {id: bp-buyer-as-insurer, relation: see-also}
  - {id: bp-liability-gap, relation: see-also}
  - {id: bp-existing-standards, relation: see-also}
  - {id: bp-sureties, relation: has-part}
  - {id: bp-estimate-accuracy, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 3, 'Insuring the bidder's margin'", url: "https://books.andrecomeau.xyz/bot-procurement/working/06e-the-underwriters-chapter/"}
  - {title: "Bot Procurement (book in draft), chapter 13, 'The insurers: a pilot, then a standard'", url: "https://books.andrecomeau.xyz/bot-procurement/working/06f-the-insurers/"}
book: [06e-the-underwriters-chapter.md, 06f-the-insurers.md, app-e-pilot-term-sheet.md]
---
# Stakeholders: what insurers stand to gain

> Underwriters put a price on harm before it happens. To underwrite a risk, they need to measure it. Bot Procurement is a proposal; its test has not been run.

## In short

- **Today:** insurers measure AI products one at a time, each with custom validation, which makes it hard for a vendor to shop for a better price. General liability insurers are adding exclusions for generative AI.
- **The pitch:** a reference standard as a common baseline for measuring how far any estimating product deviates; a record that settles, after a loss, whether the bot or the bidder caused it.
- **The product the project proposes:** [margin insurance](bp-margin-insurance.md), paid when a bot's bids keep falling short of a target margin across many completed contracts; one losing job is not a claim. A draft term sheet exists for an underwriter to mark up.
- **Bonding companies (sureties):** they guarantee the builder, not the price, and lose money mainly on firms that grow too fast; the project's one standing surety use case is the SBA guarantee program ([sureties](bp-sureties.md)).
- **The base rate:** human prices run far below the market often (the low bid more than 20 percent under the engineer's estimate on one Texas highway contract in eight) and lose money less often ([estimate accuracy](bp-estimate-accuracy.md)).
- **The base case for large buyers:** the buyer as its own insurer, with third-party cover essential for small buyers and marginal bidders ([buyer as insurer](bp-buyer-as-insurer.md)).

## Why insurance speeds adoption

The adoption bottleneck for AI tools is the trial period. Munich Re's public material on AI cover argues that no model can be perfect, that the tails will always exist, and that insurance-backed guarantees can replace long proofs of concept. For the project: insurers picking up the tail risk would let buyers and bidders use a tool before its trials end, and give vendors cash flow for the next version.

## What an insurer would need to see

1. Where the product's normal error ends and a defect begins.
2. How the tails are capped or priced.
3. A record fixed before bid close: the bid, the estimate file and the declared costs, time-stamped.
4. A reference range in force on bid day that does not move afterwards.

## Aside: correlated failure

A standard makes bots alike, and alike bots fail together in the same week. That correlation is what an insurer cannot diversify, and it is the strongest argument for a measured independence requirement between implementations (the project's draft standard, not yet public).
