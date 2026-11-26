# Appendix E. A draft term sheet for a pilot policy

This appendix goes with [chapter 13, the insurers](06f-the-insurers.md), where the pilot it describes is the next step of the ask.

This is a starting point for an underwriter to mark up, not an offer. Every number in brackets is a placeholder. The project does not sell insurance and has no stake in the terms an insurer chooses.

**Insured:** The software vendor whose estimating bot prepares the bids, with each participating bidder named as an additional insured. The insurer may recover a payment from a bidder who breaks a condition or makes a false declaration, so the vendor does not carry risks only the bidder controls.

**Insured event:** A shortfall in margin on a contract won with a bid the bot prepared. The margin is measured against a cost model built from the costs the bidder declared in the estimate file on bid day, such as owned equipment, crew rates or a nearby yard. Costs on site never enter the claim.

**Trigger:** The policy pays when the average margin across the vendor's covered contracts falls more than [x] percentage points below the target margin. Only completed contracts count toward the average. One losing job does not trigger a payment.

**Measurement period:** Contracts won during the policy period are followed to completion, for up to [number] months after the policy period ends. Claims are settled once that period closes.

**Payment:** [y] percent of the shortfall below the trigger. The bidder carries the rest of the shortfall.

**Premium:** [p] percent of the contract price on each contract won, paid at award, the way a bond premium is. For scale, the project's model puts the lowest fair price at about 0.11 to 0.15 percent: $8,800 to $12,000 on an $8 million contract (chapter 3).

**Limits:** [$] per contract, and a total of no more than [number] times the premiums paid in the policy period.

**Policy period:** [12] months, on [number] tenders by [number] bidders.

**Conditions:**

1. The bid and the estimate file are fixed and time-stamped before the tender closes.
2. The bot's price falls within the range set by the reference standard, or the bid is not covered. The range in force on bid day governs, even if the standard changes later. The range is published by the body that keeps the standard, with its version and date. A bidder who sees the bot's price fall below the range may change the bid or send it in at its own risk. Either way, the policy does not pay for a gap the bidder could see on bid day.
3. The bidder keeps its books for [number] years after the contract ends.

**Audit right:** The insurer may check the bidder's books and the estimate file, as bonding companies already do.

**Voiding:** A false declaration of costs in the estimate file voids coverage for that bid.

**Exclusions:** [to be set by the insurer, for example changes in scope after award, events covered by other insurance, and bids altered after the bot prepared them].

**Suggested starting values.** These are the project's suggestions, not terms, taken from its insurance model (chapter 3). The model measured each job's miss on its own, while this sheet pays on an average across jobs, so an underwriter would need to convert them.

| Blank | Suggested value | Where it comes from |
|---|---|---|
| Trigger [x] | 5 percentage points below the target margin | The bidder keeps the first 5 percent of a miss |
| Payment [y] | 80 percent of the shortfall below the trigger | The cover pays 80 percent of the rest |
| Range edge (condition 2) | 15 percent below the reference standard | Where a small bidder and the insurer meet |
| Limit per contract [$] | 8 percent of the contract price | 80 percent of the band from 5 to 15 percent |
| Total limit | A yearly cap for each version of the bot, about twice the payouts expected in a year | Shared errors that more clients cannot average out |
| Premium [p] | About 0.15 percent sold on its own; about 0.11 percent sold by the vendor | The insurer's lowest price for a typical bot whose bids are checked |

The other blanks, the measurement period, the numbers of tenders and bidders and the years of books kept, are for the insurer and the pilot's partners to set.

**What the pilot reports:** claims and near misses, the spread of margins against the target, and which terms needed changing. The results go into the open standard.
