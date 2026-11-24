---
id: bp-procurement-machines
title: "Procurement machines: systems that already screen tenders, and what they teach"
type: history
status: draft
summary: >
  Governments already run machines that read public tenders and flag suspicious ones, such as Brazil's
  Alice (from 2015) and Korea's bid-rigging screen (from 2006). Their lesson for Bot Procurement is
  about flags: a flag is worth something only when it is rare enough to read and someone is obliged to
  act on it. The project keeps a card for each machine on its Procurement Machines site.
updated: 2026-11-19
audience: [buyers, auditors, researchers, standard writers]
questions:
  - Do governments already use AI to screen public tenders?
  - What is Brazil's Alice?
  - What did Korea learn from its bid-rigging screening system?
  - Why do AI flags get ignored?
  - Did Brazil's Alice fall out of use?
related:
  - {id: bp-evaluator, relation: see-also}
  - {id: bp-existing-standards, relation: see-also}
  - {id: bp-cases, relation: see-also}
sources:
  - {title: "Rocha, Rezende and Oliveira, 'Alice: desafios, resultados e perspectivas...', Revista da CGU 14(26), 2022", url: "https://revista.cgu.gov.br/Revista_da_CGU/article/download/530/357"}
  - {title: "Etoday, 19 October 2017 (Korean; KFTC screening figures released in the National Assembly)", url: "https://www.etoday.co.kr/news/view/1551080"}
  - {title: "OECD, DAF/COMP/WP3/WD(2022)31, note by Korea", url: "https://one.oecd.org/document/DAF/COMP/WP3/WD(2022)31/en/pdf"}
  - {title: "OECD OPSI, Robot Alice: bid, contract and notice analyser", url: "https://oecd-opsi.org/innovations/robot-alice-bid-contract-and-notice-analyser"}
  - {title: "Procurement Machines cards", url: "https://machines.andrecomeau.xyz/"}
  - {title: "Open Contracting Partnership, 'AI in public procurement: between experimentation and impact', 9 July 2026", url: "https://www.open-contracting.org/2026/07/09/ai-in-public-procurement-between-experimentation-and-impact/"}
book: [07-building-an-estimator-in-public.md, app-a-the-cards.md]
terms: [Flag]
---

# Procurement machines: systems that already screen tenders, and what they teach

> A flag without an owner is a flag nobody reads. (The author's position.)

## In short

- **Brazil, Alice:** built at the federal comptroller (CGU) in 2015, shared with the federal audit court (TCU) in 2016, improvements taken back in 2018. Collects tender data daily, applies about 40 risk typologies, and sends alerts to more than 500 auditors, prosecutors and comptrollers; since 2021 it also alerts managers during procurement planning.
- **Korea, the bid-rigging screen:** launched by the competition authority in January 2006, succeeding a manual system from 1997. Each bid gets a collusion score from parameters tailored to its type; high scores are analysed further and an officer decides whether to investigate. The OECD's record shows a repair after 2018 that was mainly fewer, better flags: 1,227 in 2017 down to 297 in 2021, with officers' case selection still not standardised in 2022.
- **The lesson:** a flag is useful only if it is rare enough to read and someone's job is to act on it. Too many flags and the pile goes unread; no owner and nobody answers for missing one.

## Did these machines fall out of use?

Yes, for a time, though for different reasons.

- **Brazil:** use of Alice was left optional for each audit area in 2015, and in 2018 the comptroller's own staff found it "em desuso" (in disuse) at the CGU. Their diagnosis was that "the technological part was adequate, but there was no formalised and standardised process". It was revived by redesigning the process: AI classification of alerts, a standing commission, and integration with the audit system so that critical alerts must be analysed (Rocha, Rezende and Oliveira, *Revista da CGU* 14(26), 2022).
- **Korea:** about 10,036 tenders scored as high-risk between 2007 and 2017, and the competition authority investigated 7 of them (figures released by a member of the National Assembly, reported by Etoday, 19 October 2017). The country's audit board criticised the non-use in 2012. The OECD's record puts the causes mainly in the data and parameters, and a rebuild finished in January 2018 followed a 2015 parliamentary audit.

So the book's line that the machines sat unused until acting on the flags became somebody's job fits Brazil closely. For Korea the documented fix was mostly technical.

## How the evaluator applies it

The project's [evaluator](bp-evaluator.md) sends every flag to a named reviewer who must decide and sign, and flags only lines outside its usual error, so that flags stay few.

## Aside: the Procurement Machines cards

The project keeps an illustrated card for each procurement system it studies, from historic public letting systems to current screening machines, at machines.andrecomeau.xyz. One card type, the event card, marks a "whorl in the grain" where several machines meet; the only event card so far is the [Trax case](bp-trax-case.md).
