---
id: bp-stakeholder-lawyers
title: "Stakeholders: what legal departments need before they bless a bot"
type: stakeholder
status: draft
summary: >
  For buyers who let contracts worth millions, legal questions are the gate to adopting AI, not an
  afterthought. A legal department blesses a method only when it can see how the method will hold up
  before a tribunal: a person must decide and be seen to decide, the reasons must stand without the
  tool, and what the tool contributed must be disclosed. Bot Procurement, a proposal, is built around
  that.
updated: 2026-11-19
audience: [lawyers, buyers, public owners]
questions:
  - What does a legal department need before approving AI in procurement?
  - Can a bot's number stand alone in a public procurement decision?
  - Is an authentic AI record enough to show a decision was reasonable?
related:
  - {id: bp-liability-gap, relation: see-also}
  - {id: bp-reading-record, relation: see-also}
  - {id: bp-trax-case, relation: see-also}
  - {id: bp-reference-bot, relation: see-also}
  - {id: bp-stakeholder-buyers, relation: see-also}
  - {id: bp-sign-off, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 12, 'The blessing of the legal department'", url: "https://books.andrecomeau.xyz/bot-procurement/working/06c-the-blessing-of-the-legal-department/"}
  - {title: "May v Ferndale Institution, 2005 SCC 82"}
book: [06c-the-blessing-of-the-legal-department.md]
terms: [Keyholder]
allow_words: [conforming]
---
# Stakeholders: what legal departments need before they bless a bot

> The tool, however good, arrives second. The record of who decided, on what, and why, arrives first. Nothing here is legal advice.

## In short

- A deck builder can price a job with a chatbot and eat the difference if it is wrong; nobody calls a lawyer. Buyers who let contracts worth millions cannot.
- A legal department is not there to stop things. It is there to make sure that, when a decision is challenged, the organisation can show it was made properly, by someone entitled to make it, for reasons recorded at the time.
- **Its checklist:** a person must decide and be seen to decide; the reasons must be the person's own and make sense without the tool; whatever the tool contributed must be disclosed, because a court can order it into the record anyway.
- So the model, the standard that says what a conforming model must do, and the document standard that says what the model reads all have to hold up together, under today's law.

## What the courts have taught so far (Canada and the US)

- **A person decided, so the tool did not matter:** in 2023 a Federal Court judge reviewing an immigration refusal made with a software tool held that an officer had decided and the reasons were the officer's. A later refusal was set aside because its reasons conflicted with the applicant's evidence, not because of the tool. The tool was never the problem; thin reasons were.
- **Hidden method, void decision:** the Supreme Court of Canada set aside prison transfers made after a reclassification with an undisclosed scoring matrix, because those affected could not see how they were scored (*May v Ferndale Institution*, 2005 SCC 82).
- **AI output goes on the record:** in 2026 a US court ordered an agency's AI evaluations into the record of an army contract protest because officials had looked at them ([the Trax case](bp-trax-case.md)).

## Admissible is not the same as reliable

A legal department asks two questions. First, would the record survive a challenge: kept at the time, by whom, unchanged since? That has good, cheap answers ([the reading record](bp-reading-record.md)). Second, was the method reasonable to rely on at all? An authentic signature proves a named person approved a number, not that a careful person should have. If the tool can be wrong by an amount nobody has measured, the signature shows that someone signed something they could not quantify. That is why the project insists on a stated error.

## What this means for the design

The keyholder, the named person who signs with a reason, is the part a legal department will look for first. A bot's number will not stand alone for this audience until a standard exists that a court already trusts. The bot's job is to make the person's reasons better and faster and leave a trail.
