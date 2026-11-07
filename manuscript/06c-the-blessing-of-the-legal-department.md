# The blessing of the legal department

<!--
Draft, not yet placed (2026-11-07). Proposed home: Part III, after the witness box (it would be chapter 11, and the standards and meta-goal chapters would move to 12 and 13), or the first chapter of Part IV, before the standards chapter. Listed in build_site.py's working copy without a number until Andre places it. Andre expects the material may spawn several chapters; a possible split is at the end of this note.
Target: none set. This draft is about 2,800 words of prose.
Brief (Andre, 2026-11-07, verbatim, from the project thread "Answer Grimm talk follow-ups"):
"While the blockchain, or duplicate approach would still be necessary, since the standard would be open, people should be able to build their own models from scratch. They could generate data that should be compatible with the standard. This would be an avenue for deep fakes to be born. We may need some GAN testing as well. This may be an issue for after the v1.0 is completed, but we should not be writing off this possibility."
"The thinking so far was a rush to a working model -> rough consensus -> adoption -> legal issues are addressed as they appear. Our review of the issues post-standard make me think that the legal issues would need to be resolved early for mass adoption. The residential deck builder can already use vanilla AI to estimate projects. His project risk value and the cost of the work to clients make legal consultations prohibitive. I may have had this type of situation in mind when formulating the original long-term thinking. Now, with the book forcing a deeper dive, this is not the target audience. Even if estimators and project managers adopt the tool, this will almost certainly be secondary to the paper trail of human judgement with respect to legal departments. They can use the tool for their own benefit, but the company would keep a low-risk legally defensible system in place when millions -billions come into play."
"On one hand, the path to success is becoming clearer; otoh, it will be longer. To receive blessings from legal departments will require a model + standard + document standard that will hold up to the current jurisprudence. I know less about this than construction procurement, so not only will this require more steps, it will also be on a steeper incline."
"We may also need to restructure significant portions of the model to realign with this approach now instead of leaving things to v2.0 after initial deployment."
Every sentence of the prose below is Claude's, built on those passages and on the research notes listed next. It needs Andre's voice pass. The title is Claude's, from his phrase "receive blessings from legal departments"; alternatives: "Legal goes first", "The paper trail wins", "Asking legal first".
Tone: a little drier than Part I, as TONE.md expects of a legal chapter, but kept to the builder-explaining-to-a-friend voice; about one joke a paragraph at most.
Sources (project research library, 2026-11-07; nothing here is legal advice and the book should say so once):
- Filing gates: CITT Procurement Inquiry Regulations SOR/93-602 ss. 6-7 (10 working days, 30 at most; "reasonable indication" check within 5 working days); Irving Shipbuilding v Canada (AG) 2009 FCA 116; Ontario Crown Liability and Proceedings Act 2019 s. 18 (60 days' notice) and Corrigan v Ontario 2023 ONCA 39 (claim without notice a nullity), via WeirFoulds; TxDOT Construction Contract Administration Manual "Claims" and 43 TAC 9.2 (certified claim, Contract Claim Committee, SOAH contested case). File: research-library/algorithmic-law-crash-course/filing-authentication-validation-2026-11-07.md.
- Authentication: FRE 902(13)/(14) (Foley summary); Canada Evidence Act ss. 31.1-31.5 and CAN/CGSB-72.34; Vermont 12 V.S.A. 1913 ("does not extend to the truthfulness, validity, or legal status of the contents", checked). Thinking Machines 2025 on nondeterministic inference (secondary coverage only).
- Human judgment on the record: Haghshenas v Canada 2023 FC 464; later Chinook cases set aside where reasons failed; May v Ferndale Institution 2005 SCC 82 (undisclosed scoring matrix). File: haghshenas-ai-plus-public-servant-2026-11-07.md. Trax v United States (Fed. Cl. 26-796, Sept 2026): considered AI output goes in the record (crash course 4.1).
- Black boxes: Daubert; Mohan, White Burgess (not yet read at source); R. v. Hughes disclosure orders (manuals, logs, validation reports); Ontario Civil Rules Committee AI proposal (identify software, training data categories, evidence of validity), OBA submission Sept 2025.
- Standards and who pays: Ryan v Victoria 1999 (compliance is evidence, not a defence); Spearin (US 1918); MT Højgaard v E.ON [2017] UKSC 59; Edgeworth v N.D. Lea (SCC 1993); Ledcor 2016 SCC 37 (standard-form interpretation a question of law); CFTA Art. 509 ("or equivalent"). Files: standards-and-law/ and legal-adoption/.
- Insurers: Verisk generative-AI exclusions CG 40 47, CG 40 48, CG 35 08 (Insurance Journal, Aug 2026); Munich Re aiSure underwriting.
- Competition: Cornish-Adebiyi v Caesars (3d Cir. July 2026); Competition Act s. 47.
- Residential: construction-procurement-protocols context-bank/residential-estimating.md (a deck builder's AI pipeline, 2026-10-07).
To check before printing: that the facial-recognition disclosure cases are Ontario's and are R. v. Hughes (from the crash course, not re-read); every (gk) item in the filing note, the Mohan/White Burgess wording, the Daubert factors as stated, and whether the RICS AI standard (mandatory 9 March 2026) should join the insurers' paragraph.
Appendix D: add Vermont 12 V.S.A. 1913, Haghshenas, May v Ferndale, Irving Shipbuilding, Corrigan, Ryan v Victoria, MT Højgaard, Goodfellow et al. 2014 (GANs) once Andre keeps the passages that use them.
Possible split (Claude's suggestion): (1) "The blessing of the legal department": the audience shift and the new order of the road; (2) "Getting heard, proving the record": filing gates, authentication, the black box; (3) "The forger's workshop": open standards, compatible fakes, adversarial testing. Each could grow to chapter length if Andre wants the legal material to carry more of the book.
Paths are relative to the project files folder unless stated.
-->

## The deck builder and the legal department

A deck builder can already price a job with an off-the-shelf chatbot. He photographs the yard, types in the size, and gets a materials list and a number before the coffee cools. If the number is wrong, he eats the difference on one deck, and he learns. Nobody calls a lawyer. A lawyer would cost more than the mistake.

For a long time that builder was the picture behind this project. Build a working model, let people use it, let rough consensus form around it, and deal with the legal questions as they appear. It is how a lot of good software spreads, and it works when each mistake is small and the person who makes it is the person who pays.

Writing this book changed the picture. The buyers this book is about do not price decks. They let contracts worth millions, sometimes billions, and every number they sign may one day be read aloud by someone who is paid to find it wrong. Their estimators and project managers may well use a bot, and many will, for their own work. But the company will keep what it already has for the decisions that matter: a paper trail of human judgment that its legal department knows how to defend.

So the tool, however good, arrives second. The record of who decided, on what, and why, arrives first.

That flips the order of the road. Legal questions cannot wait for adoption, because for this audience they are the gate to adoption. A legal department blesses a method only when it can see how the method will hold up in front of a tribunal, under today's law, not the law the project hopes for. That means three things have to hold up together: the model, the standard that says what a conforming model must do, and the document standard that says what the model reads.

The path is clearer than it was. It is also longer, and steeper.

## What a legal department is protecting

It helps to ask what a legal department is for. It is not there to stop things. It is there to make sure that, when a decision is challenged, the organization can show the decision was made properly, by someone entitled to make it, for reasons that were recorded at the time.

The courts have been teaching that lesson with machines for a few years now. In 2023 a Federal Court judge reviewed an immigration refusal made with the help of a tool called Chinook. The applicant argued that a machine had decided the case. The court disagreed: an officer had made the decision, and the reasons were the officer's, so how the tool was used did not change the outcome. Later cases went the other way only where the officer's reasons could not stand on their own. The tool was never the problem. Thin reasons were.

An older Supreme Court case shows the other side. Prison officials used a scoring matrix to reclassify inmates and did not disclose it. The decisions fell, not because the matrix was wrong, but because the people affected could not see how they had been scored. Hidden method, void decision.

Put those together and a legal department's checklist writes itself. A person must decide, and be seen to decide. The reasons must be the person's own and must make sense without the tool. And whatever the tool contributed must be disclosed, because a court can order it into the record anyway. In 2026 an American court did exactly that with an army contract: it ordered the agency's AI evaluations into the record because officials had looked at them, whether or not anyone had relied on them.

This is good news for the keyholder from chapter 1, the named person who signs the number and gives a reason. The keyholder is not a courtesy. It is the part of the design a legal department will look for first.

It is less good news for the idea that a bot's number could ever stand alone. For this audience, it won't, at least not until a standard exists that a court already trusts. The bot's job is to make the person's reasons better and faster, and to leave a trail that shows it.

## Getting through the door

Before anyone argues about whether a bot read a tender correctly, someone has to get a dispute heard. That part of the law is mostly about procedure, and the windows are short.

A supplier who thinks a federal tender in Canada was run unfairly has ten working days from the day it learned of the problem to complain to the trade tribunal. The tribunal then takes about a week to decide whether there is a reasonable sign that the complainant could have supplied the work, that the contract is covered by the trade agreements, and that the rules were broken. Only then does the argument about the merits begin. Someone suing the Ontario government has to give sixty days' written notice first, and a claim started without it is a nullity, as if it had never been filed. In Texas, where the estimator's data comes from, a contractor unhappy with a decision on a highway job files a certified claim with the department, which has its own claim committee. Only after that can the dispute go to an administrative law judge.

None of those doors asks for the bot. They ask whether the claimant is the right person, in the right place, on time, having done the steps the rules require. The bot's record matters at the next stage, when the other side asks to see it, and later still, when its reliability is fought over.

Two things follow for the design. First, the record has to be ready on the first day of a dispute, not assembled after it, because ten working days is not long enough to reconstruct anything. Second, its first reader will probably not be a judge. Most construction disputes end inside the contract's own claim process, in adjudication or in arbitration. The Texas claim committee is a better picture of the record's first audience than a courtroom: a few experienced people with a deadline, reading a file.

A record that only a computer scientist can read fails that audience.

## Proving the record

Suppose the dispute is heard, and the buyer produces the bot's reading of the tender. The other side's first question is simple: is this the reading you made at the time, or one you made last week?

Rerunning the bot does not settle it. Part of the estimator is an ordinary statistical model: with the same code, the same data and the same settings, it gives the same answer every time, and its errors are a measured rate, not noise. But any step that uses a language model, to read a tender or draft a memo, can give a slightly different answer each time, even with every setting fixed, because of how the servers that run it group their work. A rerun that agrees is reassuring. A rerun that disagrees proves nothing either way.

So the record of the run that was actually used is the evidence, and a rerun is only a check, against a tolerance written down in advance.

Proving that a record is the one made at the time is an old problem with cheap answers. Take a fingerprint of every file, a short code that changes completely if a single character changes. Chain the records, so each one carries the fingerprint of the one before it, and a deleted or reordered record breaks the chain. Once a day, publish the latest fingerprint somewhere nobody controls alone, or have a timestamp service vouch for when it existed. Keep at least two copies, and give one of them to someone who is not the buyer.

That is most of what a blockchain offers, without the blockchain. The law agrees about what it proves. Vermont passed a statute that presumes a record verified on a blockchain is authentic, and dated, and added by whoever the chain says added it. The same statute says the presumption "does not extend to the truthfulness" of what the record contains. Canada's evidence law makes the same split in different words: it asks whether the records system kept its integrity, not whether the records are right. A chain of fingerprints proves when something was written down. It cannot prove that what was written down was true.

## The forger's workshop

Here the open standard creates its own problem.

The point of a public standard is that anyone can build to it. A second vendor, a university or a contractor's own team should be able to build a model from scratch, run it against the public test, and produce readings that look exactly like the reference implementation's. That is how the standard escapes its author.

It is also how a forgery is born. If anyone can produce a reading in the standard's format, anyone can produce a fake one: a record that looks compatible, carries plausible numbers and fingerprints, and was made after the fact to tell a convenient story. A forged bid tabulation, a doctored set of past prices fed in as "history", a reading record for a run that never happened. The deep fake of construction will not be a video. It will be a spreadsheet.

A chain of fingerprints does not stop this. It faithfully preserves whatever it is given, fakes included. The defences have to sit earlier, at the point where data comes in.

The first is to fingerprint every input when it arrives, before any bot touches it: the bids at the moment of opening, the public tabulations at the moment of download, with the address they came from and the time. A later dispute can then fetch the source again and compare. The second is to check each input against a second source, since award minutes, published low bids and contract totals should all agree with the line items. The third is to check for the impossible: quantities no job could have, prices outside anything ever bid, the same bid appearing twice.

The last idea comes from an unexpected place. A generative adversarial network, or GAN, is a pair of programs trained against each other: one makes fakes, the other tries to catch them, and each gets better because of the other. It is one of the main ways deepfakes are made. The estimator does not need a GAN, and training it on synthetic prices would weaken the one claim it can make, that it learned from real ones. But it needs the habit of mind. A second, independently built model that prices the same lines and flags the ones where the two disagree badly. A red team that hunts for the inputs that make the model say something absurd. Tests that change something that should not matter, the order of the lines, the wording of a description, and check that the price does not move. And planted fakes, doctored bids slipped into test runs on purpose, with a published count of how many the checks caught.

None of this has to be finished before version 1.0. All of it should be planned for now, because a standard that ignores forgery invites it.

## A black box on the stand

The model at the centre of a mature standard bot will probably be a black box: a system whose reasoning cannot be read off its code. That does not keep it out of court. Courts accept black boxes all the time, from breathalysers to laboratory instruments. What they ask for instead of the code is evidence that the box works: it has been tested, its error rate is known, the test can be repeated, and people in the field accept the method.

In Ontario, defendants who wanted to challenge facial-recognition evidence did not get the source code. The courts ordered manuals, logs and validation reports. Ontario's rules committee is now consulting on a rule for evidence generated by AI that asks for almost the same list: name the software, describe the kinds of data it was trained on, and show that its outputs are valid and reliable. That list is close to a specification for the reading record and its test.

So the validation scaffold is not paperwork around the evidence. It is the evidence.

Some of it exists. The estimator was trained on Texas contracts let up to the end of 2025 and tested once, on contracts let from May 2026 that it had never seen. It is measured against honest baselines: the state's own engineer's estimate, and the spread between the bidders themselves. Each version's scores are logged. A person signs every number.

What is missing is the part that cannot be added later. The tested model was never frozen and fingerprinted, so today nobody can prove that the model that scored 21 percent is the model that would be used. The rule that the test set is opened once per version is followed, but it is not published with its dates. The scores have no intervals around them, which is the first thing a cross-examiner will ask about. Nobody has written down and checked the ways information from the test period could have leaked into training. And the model has not been tried on a second jurisdiction it was not built on.

The first four are cheap, and every week they wait is a week of results that a court or a reviewer cannot rely on.

## Who pays when the standard is wrong

A legal department will ask one more question, the one this book is named for: when the bot is wrong, who pays?

The courts already have answers for standards, and they are not comfortable ones. In Canada, following a standard is evidence that you took reasonable care, not a defence; you can follow the standard and still be negligent. In the United States, an owner who hands a contractor a specification generally carries the risk that the specification is wrong. In England, a contractor who promised a working result paid for the failure even though the industry standard it followed was itself wrong, by a factor of about ten. In Canada, the engineer who prepares tender documents can owe a duty to the bidders who rely on them.

The insurers have their own answer, and it is moving fast. Policies that once covered a professional's mistakes without asking how they were made are now being written with exclusions for generative AI. Cover that does exist is priced the way a scientist would test a model: the insurer wants to know where the model is valid, how its errors are distributed, and whether the tests behind those numbers are sound.

None of this is a reason to stop. It is a list of what the standard must do so that a legal department, and its insurer, can live with it. It must say clearly who is relying on what. It must make the human decision visible. It must come with tests good enough to price. And it must be written so that following it is strong evidence of care, even though it can never be a shield.

## Three standards, not one

The road to the legal department's blessing runs through three artifacts, and each has to hold up under the law as it stands.

The model has to be frozen, fingerprinted, tested in public, and scoped: this is what it is for, and this is what it is not for. The standard has to be a test any vendor's model can pass, not a mandate to use one particular bot, because Canada's trade agreements require buyers to accept equivalent products, and a buyer cannot write one vendor into a tender. And the document standard, the machine-readable tender that replaces the PDF as the copy the bot reads, has to settle which copy wins when the two disagree, because the interpretation of a standard-form contract is a question of law, and a court will want to know which words the parties agreed to.

That is more steps than the old plan. It is also steeper, because the law is the part of the road the author knows least.

## Rebuilding the road

The old order was model, consensus, adoption, law. The new order puts the law beside the model from the start.

In practice that means some of the work planned for version 2.0 moves into version 1.0. Freeze and fingerprint the tested model. Publish the one-shot rule with its dates. Write down what a reading record contains, field by field. Put intervals on the scores. Check for leakage, and say what was found. Then, before the evaluator touches a live price, add calibration, a second jurisdiction, a test registered before it is run, and the adversarial suite.

None of it makes the model more accurate. All of it makes the model's accuracy something a legal department can point to.

The deck builder can keep his chatbot. The legal department needs a witness.
