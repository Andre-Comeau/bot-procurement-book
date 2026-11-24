---
id: bp-ai-failure-modes
title: "What AI gets wrong in procurement: four failure modes"
type: risk
status: draft
summary: >
  The book sorts how AI (and people) go wrong with two questions: did it go wrong in words or in deeds,
  and did anyone mean it? That gives four failure modes, miscommunication, misadventure, manipulation and
  malice, each with its own remedy. A standard bot helps most against miscommunication, helps against
  misadventure, needs bonds and escrow against manipulation, and has nothing to offer against malice.
updated: 2026-11-19
audience: [everyone, lawyers, researchers, AI vendors, buyers]
questions:
  - What are the risks of using AI in construction procurement?
  - Can a standard stop a malicious AI bidder?
  - What happens when an AI misreads a tender?
  - How should procurement handle AI that makes mistakes?
related:
  - {id: bp-reference-bot, relation: see-also}
  - {id: bp-ai-strengths, relation: contrasts}
  - {id: bp-competition-risk, relation: see-also}
  - {id: bp-cases, relation: see-also}
sources:
  - {title: "Bot Procurement (book in draft), chapter 14, 'What do we do with a drunken sailor?'", url: "https://books.andrecomeau.xyz/bot-procurement/working/03b-what-do-we-do-with-a-drunken-sailor/"}
book: [03b-what-do-we-do-with-a-drunken-sailor.md]
terms: [Reference bot]
---

# What AI gets wrong in procurement: four failure modes

> Words or deeds, meant or not. Each corner has its own remedy, and the standard bot has a part to play in three of them.

## In short

| | Accidental | Malicious |
|---|---|---|
| **Words** | Miscommunication ("Who's on First?"): remedy, a shared reading | Manipulation (the Serpent): remedy, law, bonds and escrow |
| **Deeds** | Misadventure (the drunken sailor): remedy, consequences, guardrails, rollback | Malice (the dragon): remedy, force; not a procurement problem |

The book's images come from Genesis and Revelation, read as the story of a creator and a creation made in its image, with people as the creator and AI as the creation.

## Miscommunication

Two parties agree on every word and understand nothing, as in Abbott and Costello's routine. Perfect communication is beyond people and the bots made in their image; ambiguity at the margins is also where variety comes from. A standard bot starts small, with one frozen text for one trade that everyone reads the same way, and gives a judge a reasonable reading to measure every other reading against. This is where Bot Procurement is strongest ([the reference bot](bp-reference-bot.md)).

## Misadventure

The drunken sailor means no harm; he will do something foolish and the crew will deal with it. This is the problem with the AI that exists today. The tools are familiar from software: better technology, hard guardrails, version control, and rolling back to the last model that worked. A standard sets a floor and makes sure there is a known good version everyone can roll back to.

## Manipulation

The Serpent works with words, promising more than the fruit delivers. AI agents are a new tool for old goals. Law is the old remedy, and a rerunnable standard bot leaves a mark a judge can measure: a bidder that bent the tender left a reading that differs from the reference. The risk grows when a standard bot is trusted to evaluate sealed alternates: a manipulator who knows its strengths and weaknesses could design an alternate that passes the review and does nothing for the buyer. Publishing the bot also shows the manipulator where to aim. So the strength has to come from consequences posted in advance: a bond held against the alternate, or money held in escrow and released only when the promised benefit appears. On a plain lump-sum bid, a manipulator has little room: a bid that is too low still leaves the buyer with the building at that price.

## Malice

When words fail, force follows. AI has neither intent nor a body yet; when it has both, malice may find a home. If a frontier model attacks a tender outright, procurement closes the tender and leaves the fight to the labs and the law. Brute force is not a standard's problem.

## Aside: why the human comparison matters

The chapter opens on a point the project returns to often: public debate worries about misbehaving bots while forgetting misbehaving people. Every failure mode above has a long human history, and procurement already has institutions for each (tender law, bonds, debarment, audit). The question is not whether bots fail, but which existing remedy fits each failure and what is missing, which for misreading is a shared reference.

## Aside: lessons the book keeps from bots

Some material is left out of this edition on purpose. The book's witness-box chapter muses about deterring bots with punishment; the project's own note on it is that a bot that can be deterred is a bot that will resist being switched off. That is the wrong lesson to teach an agent.
