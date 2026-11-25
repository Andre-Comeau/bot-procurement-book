---
id: bp-liability-gap
title: "Who is liable when an AI construction price is wrong"
type: problem
status: draft
summary: >
  Today the person or firm that relied on a bot's price carries the loss: construction software vendors'
  terms cap their liability and make checking the user's job, insurers are adding exclusions for
  generative AI, and the bot holds no assets. Without a measure of what a reasonable bot would have read,
  courts and insurers have nothing to compare a bot's reading with.
updated: 2026-11-19
audience: [lawyers, buyers, bidders, insurers, vendors]
questions:
  - Who is liable when an AI estimate for a construction bid is wrong?
  - Do construction software vendors accept liability for AI errors?
  - Does insurance cover AI pricing errors in construction?
  - Can a bidder rely on tender documents prepared by the buyer's engineer?
related:
  - {id: bp-overview, relation: part-of}
  - {id: bp-reference-bot, relation: answers}
  - {id: bp-buyer-as-insurer, relation: answers}
  - {id: bp-stakeholder-lawyers, relation: see-also}
  - {id: bp-stakeholder-vendors, relation: see-also}
  - {id: bp-stakeholder-insurers, relation: see-also}
  - {id: bp-trax-case, relation: see-also}
  - {id: bp-sign-off, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 11, 'The vendors: players, not referees'", url: "https://books.andrecomeau.xyz/bot-procurement/working/02d-the-vendors/"}
  - {title: "Insurance Business, 'ISO's generative AI exclusion is already on thousands of CGL policies', 16 September 2026", url: "https://www.insurancebusinessmag.com/us/news/professional-liability/isos-generative-ai-exclusion-is-already-on-thousands-of-cgl-policies-589971.aspx"}
  - {title: "Ryan v Victoria (City), [1999] 1 SCR 201, headnote", url: "https://ca.vlex.com/vid/ryan-v-victoria-680588037"}
  - {title: "Legal 500, 'Focus on construction: liability of consultants in tendering process' (quoting Cardinal Construction v Brockville, 1984)", url: "https://www.legal500.com/intelligence/canada/real-estate-and-construction/focus-on-construction-liability-of-consultants-in-tendering-process"}
book: [02d-the-vendors.md, 06e-the-underwriters-chapter.md, 06b-the-bot-in-the-witness-box.md, 06c-the-blessing-of-the-legal-department.md]
terms: [Reasonable bot, Patent and latent errors]
allow_words: [certified]
---

# Who is liable when an AI construction price is wrong

> Today, almost always the person or firm that relied on it. Nothing here is legal advice; each statement names its jurisdiction and source.

## In short

- **The vendor:** contract terms for construction software's AI features cap liability (one major vendor at a year's fees or US$1,000), call the outputs recommendations, and make checking them the user's job. "Today the user pays, and the vendor sells the shovel."
- **The insurer:** Verisk's ISO form CG 40 47 (edition 01 26, available from January 2026) lets insurers exclude injury and damage arising from generative AI from general liability policies. General liability never covered a pure pricing loss, so the exclusion shows the direction of travel. The project found no insurer offering cover for a bot's construction pricing errors.
- **The bot:** holds no assets and cannot be sued in any useful sense.
- **The bidder:** answers for its own reading of the tender, including the reading its bot made.
- **The buyer and designer:** answer for the documents they issued (in Canada, an engineering firm that prepares tender documents can owe a duty of care to bidders known to rely on them).
- **What is missing:** a measure of what a reasonable bot would have read, so that "the bot got it wrong" can be told apart from "the bidder priced it badly" or "the documents were wrong".

## Party by party

### Software vendors

The project read the AI terms of the major construction software platforms in November 2026. One caps liability at a year's fees or US$1,000 and excludes defects in output; one calls AI output "recommendations only"; others put verification on the user. One platform requires its own AI suppliers to indemnify it, which is the same rule facing the other way. So the deep pockets a user might sue are, by contract, empty for exactly this loss: a number the bot got wrong and the user relied on.

### Insurers

Verisk's CG 40 47 excludes bodily injury, property damage and personal and advertising injury arising from generative AI; CG 40 48 and CG 35 08 are narrower variants. A pricing loss is a pure economic loss, which general liability policies never covered, so the gap for a bot's price was always there; the exclusions show insurers moving away from AI risk rather than toward it. Specialist AI cover exists for some products (for example performance guarantees underwritten one product at a time), but each needs its own validation.

### Bidders

In common-law tendering, a bidder answers for its reading of the documents. A bot does not change that: the bidder that bids on its bot's number answers for the number. A bidder's bot that sees an error in the tender raises a second question, whether to tell the buyer; the book gives the case for and against ([worked case: the quantity everyone saw](bp-cases.md#the-quantity-everyone-saw)).

### Buyers and designers (Canada)

The Supreme Court of Canada held in *Edgeworth Construction v N.D. Lea & Associates* ([1993] 3 SCR 206) that the engineering firm that prepared tender documents could be liable to a bidder who relied on them. An Ontario court put it as: a bidder "is entitled and expected to rely on the tender documents as conveying the best information the engineer can give" (*Cardinal Construction v Brockville*, 1984). The law also separates errors a careful bidder should have seen (patent) from those it could not reasonably find (latent).

### Following a standard (Canada)

Meeting a published standard is evidence of reasonable care, not automatically a complete defence: the Supreme Court held in *Ryan v Victoria (City)* ([1999] 1 SCR 201) that compliance with a statutory standard does not displace the common-law duty, though in some circumstances it fully satisfies it. A standard alone does not limit liability; contracts, insurance or legislation do.

## Why this blocks the productivity gain

If the user carries every loss, the rational user checks every number the bot produced, and the time saved by the bot is spent again on checking it. The book's opening question is how the gains from automating the administrative side of procurement can be realised if humans must always review the work of bots. Its answer is a shared measure of reasonable reading ([the reference bot](bp-reference-bot.md)) and an agreed party to stand behind it ([the buyer as its own insurer](bp-buyer-as-insurer.md)).

## Aside: the reasonable person, and why bots lack one

Common-law systems resolve most disputes about conduct by asking what a reasonable person would have done. The fiction works because everyone has a rough idea of a reasonable person. Nobody has an idea of a reasonable bot: two models given the same tender can read it differently, and the same model can read it differently twice. The project's proposal is to give the fiction a concrete, rerunnable form, so a judge can ask what the reference bot read and compare.

## Aside: the court record has already started

In *TRAX International v United States* (2026), the first court challenge the project found over an agency's AI-assisted evaluation, the protest was denied, but the court ordered the AI evaluations into the record ([the Trax case](bp-trax-case.md)). The first precedents on bots in tenders are likely to come from disputes like this, before any standard exists.
