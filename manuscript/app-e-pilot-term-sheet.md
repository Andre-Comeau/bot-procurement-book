# Appendix E. A draft term sheet for a pilot policy

<!--
Appendices
Status: draft (2026-11-11), Claude's wording for Andre's voice pass. Requested by vgr_zirp's second review of the underwriters' chapter; its fourth review's redlines (completed contracts with a measurement period, the range in force on bid day, a premium-linked total limit, recovery from a bidder who breaks a condition) are applied. Andre: may also travel separately with a letter to an underwriter.
-->

This appendix goes with [the underwriters' chapter](06e-the-underwriters-chapter.md), where the pilot it describes is the next step of the ask.

This is a starting point for an underwriter to mark up, not an offer. Every number in brackets is a placeholder. The project does not sell insurance and has no stake in the terms an insurer chooses.

**Insured:** The software vendor whose estimating bot prepares the bids, with each participating bidder named as an additional insured. The insurer may recover a payment from a bidder who breaks a condition or makes a false declaration, so the vendor does not carry risks only the bidder controls.

**Insured event:** A shortfall in margin on a contract won with a bid the bot prepared. The margin is measured against a cost model built from the costs the bidder declared in the estimate file on bid day, such as owned equipment, crew rates or a nearby yard. Costs on site never enter the claim.

**Trigger:** The policy pays when the average margin across the vendor's covered contracts falls more than [x] percentage points below the target margin. Only completed contracts count toward the average. One losing job does not trigger a payment.

**Measurement period:** Contracts won during the policy period are followed to completion, for up to [number] months after the policy period ends. Claims are settled once that period closes.

**Payment:** [y] percent of the shortfall below the trigger. The bidder carries the rest of the shortfall.

**Premium:** [$] for the policy period.

**Limits:** [$] per contract, and a total of no more than [number] times the premium for the policy period.

**Policy period:** [12] months, on [number] tenders by [number] bidders.

**Conditions:**

1. The bid and the estimate file are fixed and time-stamped before the tender closes.
2. The bot's price falls within the range set by the reference standard, or the bid is not covered. The range in force on bid day governs, even if the standard changes later. The range is published by the body that keeps the standard, with its version and date.
3. The bidder keeps its books for [number] years after the contract ends.

**Audit right:** The insurer may check the bidder's books and the estimate file, as sureties already do.

**Voiding:** A false declaration of costs in the estimate file voids coverage for that bid.

**Exclusions:** [to be set by the insurer, for example changes in scope after award, events covered by other insurance, and bids altered after the bot prepared them].

**What the pilot reports:** claims and near misses, the spread of margins against the target, and which terms needed changing. The results go into the open standard.
