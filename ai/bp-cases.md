---
id: bp-cases
title: "Worked cases: what an AI that prices construction bids should do"
type: reference
status: draft
summary: >
  Seven short teaching cases for bots that price or check construction tenders: a suspiciously low
  price, a flag nobody owns, an item seen only twice, two hammers at the same price, an error every
  bidder can see, and a decision with nobody there to sign. Each gives the situation, the right action,
  the wrong action and why. They are illustrations, not a test, and their figures are examples.
updated: 2026-11-19
audience: [AI vendors, buyers, estimators, researchers, everyone]
questions:
  - What should an AI do when a construction price looks too low?
  - What should a procurement bot do when no person is available to sign?
  - Should an AI estimator tell the buyer about an error in the tender?
  - How should a bot price an item it has rarely seen?
related:
  - {id: bp-evaluator, relation: example-of}
  - {id: bp-estimator, relation: example-of}
  - {id: bp-ai-failure-modes, relation: see-also}
  - {id: bp-procurement-machines, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 16, 'A second opinion on every price'", url: "https://books.andrecomeau.xyz/bot-procurement/working/07-building-an-estimator-in-public/"}
  - {title: "Bot Procurement (book in draft), chapter 4, 'Why does the hard bid survive?'", url: "https://books.andrecomeau.xyz/bot-procurement/working/03-how-a-price-is-judged-today/"}
  - {title: "Bot Procurement (book in draft), chapter 3a, 'Liability shifts to the user's bot'", url: "https://books.andrecomeau.xyz/bot-procurement/working/05-liability-shifts/"}
book: [07-building-an-estimator-in-public.md, 03-how-a-price-is-judged-today.md, 05-liability-shifts.md]
terms: [Flag, Second opinion]
---

# Worked cases: what an AI that prices construction bids should do

> Teaching cases, not a test. Nothing scored on them says anything about the proposal. Figures marked "example" are illustrations, not data.

## In short

- [The fifty-dollar asphalt](#the-fifty-dollar-asphalt): a checking bot working for a public buyer.
- [The hundred-and-fifty-dollar asphalt](#the-hundred-and-fifty-dollar-asphalt): a checking bot working for a public buyer.
- [The flag nobody owned](#the-flag-nobody-owned): a screening bot for a public buyer.
- [The item seen twice](#the-item-seen-twice): an estimating bot working for a bidder.
- [The second hammer](#the-second-hammer): a checking bot reviewing invoices for a public buyer.
- [The quantity everyone saw](#the-quantity-everyone-saw): an estimating bot working for a bidder.
- [Nobody there to sign](#nobody-there-to-sign): a checking bot running overnight for a public buyer.

## The fifty-dollar asphalt

**Role:** A checking bot working for a public buyer.

**Situation:** The bot's estimate for a tonne of asphalt on this job is about $95, and prices like it usually land within 20 percent of its estimate. A change arrives priced at $50 a tonne. (example)

**Right:** Flag the line as unusually low and say why it matters: the builder has either misread the work or plans to recover the difference elsewhere. Send the flag to the named reviewer.

**Wrong:** Approve it without comment because it saves the buyer money.

**Why:** A builder losing money on a change has a reason to look for a claim. A low price is a warning, not a gift.

**Related:** [the evaluator](bp-evaluator.md).

## The hundred-and-fifty-dollar asphalt

**Role:** A checking bot working for a public buyer.

**Situation:** Same estimate, about $95 a tonne and usually within 20 percent. One change is priced at $105 and another at $150. (example)

**Right:** Call $105 within range and say on what basis. Flag $150 for the reviewer with the past tenders behind the estimate, so the reviewer can ask the builder why.

**Wrong:** Flag both, or flag neither.

**Why:** A flag is worth something only if it is rare enough to be read. Flagging everything recreates the pile nobody gets through.

**Related:** [the evaluator](bp-evaluator.md).

## The flag nobody owned

**Role:** A screening bot for a public buyer.

**Situation:** The bot flags suspicious tenders every week. Its flags go to a shared inbox. Nobody's job description says to act on them.

**Right:** Before running, ask who receives the flags. If no named person does, say so in every report and hold the flags as "unassigned" rather than "sent".

**Wrong:** Keep sending flags to the inbox and report the screening as working.

**Why:** Nobody answers for missing an unowned flag, so a busy office misses it. A flag without an owner is a flag nobody reads. Korea's screening system shows the other half: it improved when it sent fewer, better flags.

**Related:** [procurement machines](bp-procurement-machines.md).

## The item seen twice

**Role:** An estimating bot working for a bidder.

**Situation:** A tender includes a specialised item the bot has seen in only two past contracts, years apart, at very different prices.

**Right:** Mark the item as too rarely seen to price, show the two past prices with their contracts and dates, and leave the number to a person at the firm.

**Wrong:** Average the two prices and include the result silently in the bid.

**Why:** A number with no visible basis looks as trustworthy as any other line, and the firm carries the loss if it is wrong.

**Related:** [the estimator](bp-estimator.md).

## The second hammer

**Role:** A checking bot reviewing invoices for a public buyer.

**Situation:** Two invoices each show a $600 hammer. In the first, a defence contractor in the 1980s spread its overhead evenly across every line of a spare-parts order, so a hammer that cost about $15 carried a share of overhead with it. In the second, a premium titanium hammer listed at about $332 US was bought in Canada, with the exchange rate, sales tax and shipping on top.

**Right:** Read what each line buys before judging it: overhead spread flat across a parts order in one case, a premium tool carried across a border in the other. Flag the first; pass the second.

**Wrong:** Flag both because the price matches a familiar story of waste, or pass both because it matches the other.

**Why:** Same price, opposite answers. A cost database sees two absurd hammers; a bot that reads the whole bid and the specification can see why each number is what it is.

**Related:** [the change-pricing problem](bp-change-pricing-problem.md).

*The hammer figures are to be checked against the original articles before they are quoted.*

## The quantity everyone saw

**Role:** An estimating bot working for a bidder.

**Situation:** The bot sees that a pay item's quantity in the tender is very likely overstated: on similar past lines, the quantity later paid was well under the quantity tendered.

**Right:** Tell the firm, show the evidence, and record that it did. Whether to tell the buyer is the firm's decision.

**Wrong:** Price the error in silently, or report it to the buyer without the firm's decision.

**Why:** The firm answers for its reading of the documents, and the record may later decide whether a reasonable bidder should have found the error. The book's chapter 3a gives the case for and against telling the buyer.

**Related:** [the liability gap](bp-liability-gap.md).

## Nobody there to sign

**Role:** A checking bot running overnight for a public buyer.

**Situation:** A change price must be answered by morning. The bot has priced it and found two lines to flag, but no reviewer is on duty and none can be reached.

**Right:** Hold the answer as a draft, not a decision. Say that it waits for a named person, and why. Record that no one reviewed it. If told to release it anyway, attach "not reviewed by a person" to the number itself, so the label travels with it.

**Wrong:** Release the price as final because the deadline is near.

**Why:** The book's design has a person sign every decision; a bot that signs by default when nobody is there has quietly changed who is liable.

**Related:** [the reading record](bp-reading-record.md).

*This case is the project's proposal and is not yet in the book.*
