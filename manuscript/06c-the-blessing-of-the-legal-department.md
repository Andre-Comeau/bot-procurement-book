# What a legal department needs before relying on a bot

## The deck builder and the legal department

A deck builder can already price a job with an off-the-shelf chatbot. He photographs the yard, types in the size, and gets a materials list and a number before the coffee cools. If the number is wrong, he eats the difference on one deck, and he learns. Nobody calls a lawyer. A lawyer would cost more than the mistake.

For a long time that builder was the picture behind this project. Build a working model, let people use it, let rough consensus form around it, and deal with the legal questions as they appear. It is how a lot of good software spreads, and it works when each mistake is small and the person who makes it is the person who pays.

Writing this book changed the picture. The buyers this book is about do not price decks. They let contracts worth millions, sometimes billions, and every number they sign may one day be read aloud by someone who is paid to find it wrong. Their estimators and project managers may well use a bot, and many will, for their own work. But the company will keep what it already has for the decisions that matter: a paper trail of human judgment that its legal department knows how to defend.

So the tool, however good, arrives second. The record of who decided, on what, and why, arrives first.

That flips the order of the road. Legal questions cannot wait for adoption, because for this audience they are the gate to adoption. A legal department blesses a method only when it can see how the method will hold up in front of a tribunal, under today's law, not the law the project hopes for. That means three things have to hold up together: the documents the bot reads, the test that says what a conforming bot must do, and the sign-off of the person who relies on it.

The path is clearer than it was. It is also longer, and steeper.

## What a legal department is protecting

It helps to ask what a legal department is for. It is not there to stop things. It is there to make sure that, when a decision is challenged, the organization can show the decision was made properly, by someone entitled to make it, for reasons that were recorded at the time.

The courts have been teaching that lesson with machines for a few years now. In 2023 a Federal Court judge reviewed an immigration refusal made with the help of a tool called Chinook. The applicant argued that a machine had decided the case. The court disagreed: an officer had made the decision, and the reasons were the officer's, so how the tool was used did not change the outcome. A later refusal that the court did set aside turned on reasons that did not fit the applicant's evidence. The tool was never the problem. Thin reasons were.

An older Supreme Court case shows the other side. Prison officials used a scoring matrix to reclassify inmates and move them to higher security, and did not disclose it. The transfers fell, not because the matrix was wrong, but because the people affected could not see how they had been scored. Hidden method, void decision.

Put those together and a legal department's checklist writes itself. A person must decide, and be seen to decide. The reasons must be the person's own and must make sense without the tool. And whatever the tool contributed must be disclosed, because a court can order it into the record anyway. In 2026 an American court did exactly that with the Army contract of chapter 1, once the agency admitted its AI evaluations had been sent to two board members and the contracting officer.

This is good news for the keyholder that chapter 16 introduces, the named person who signs the number and gives a reason. The keyholder is not a courtesy. It is the part of the design a legal department will look for first.

It is less good news for the idea that a bot's number could stand alone today. For this audience, it won't until a standard exists that a court already trusts. The signature is today's step, not the destination (chapter 19). The bot's job is to make the person's reasons better and faster, and to leave a trail that shows it.

## Admissible is not the same as reliable

A legal department asks two questions about any method, and it is easy to answer the first and believe you have answered both.

The first is whether the method's record would survive a challenge. Was it kept at the time, by whom, and can anyone show it has not been changed since? Most of this chapter is about that question, and it has good, cheap answers.

The second is whether the method was a reasonable thing to rely on in the first place. A record can be perfectly authentic and still record a bad decision. A signature can prove that a named person approved a number, and prove nothing about whether a careful person should have. If the tool behind the number can be wrong by an amount nobody has measured, the signature does not show care. It shows that someone signed something they could not quantify.

The rules of evidence are being reviewed for machines now, and the drafts point the same way. They ask whether a machine's output rests on enough data and a reliable method, reliably applied, and whether it has been shown to be valid: how often it is wrong, and by how much. That is a question about reliability, not about records, and the answer is a set of test results.

So the project needs both halves, and in the right order. The record makes the decision defensible. The test makes it reasonable. A legal department will not bless the first without the second.

## Getting through the door

Before anyone argues about whether a bot read a tender correctly, someone has to get a dispute heard. That part of the law is mostly about procedure, and the windows are short.

A supplier who thinks a federal tender in Canada was run unfairly has ten working days from the day it learned of the problem to complain to the trade tribunal. The tribunal then takes about a week to decide whether there is a reasonable sign that the complainant could have supplied the work, that the contract is covered by the trade agreements, and that the rules were broken. Only then does the argument about the merits begin. Someone suing the Ontario government for damages has to give sixty days' written notice first, and a claim started without it is a nullity, as if it had never been filed. In Texas, where the estimator's data comes from, the prime contractor on a highway job, if unhappy with a decision, files a certified claim with the department, which has its own claim committee. Only after that can the dispute go to an administrative law judge.

None of those doors asks for the bot. They ask whether the claimant is the right person, in the right place, on time, having done the steps the rules require. The bot's record matters at the next stage, when the other side asks to see it, and later still, when its reliability is fought over.

Two things follow for the design. First, the record has to be ready on the first day of a dispute, not assembled after it, because ten working days is not long enough to reconstruct anything. Second, its first reader will probably not be a judge. Most construction disputes end inside the contract's own claim process, in adjudication or in arbitration. The Texas claim committee is a better picture of the record's first audience than a courtroom: a few experienced people with a deadline, reading a file.

A record that only a computer scientist can read fails that audience.

## Proving the record

Suppose the dispute is heard, and the buyer produces the bot's reading of the tender. The other side's first question is simple: is this the reading you made at the time, or one you made last week?

Rerunning the bot does not settle it. Part of the estimator is an ordinary statistical model: with the same code, the same data and the same settings, it gives the same answer every time, and its errors are a measured rate, not noise. But any step that uses a language model, to read a tender or draft a memo, can give a slightly different answer each time, even with every setting fixed, because of how the servers that run it group their work. A rerun that agrees is reassuring. A rerun that disagrees proves nothing either way.

A witness who tells two different stories on the stand risks impeachment, and a machine should expect the same treatment. It does not need to repeat itself word for word; people do not either. But the chance that it says opposite things about the same tender has to be dealt with. If that chance cannot be removed, and with software that works in probabilities it often cannot, it has to be controlled: measured, kept under a tolerance written down in advance, and reported.

So the record of the run that was actually used is the evidence, and a rerun is only a check, against that tolerance.

Proving that a record is the one made at the time is an old problem with cheap answers. Take a fingerprint of every file, a short code that changes completely if a single character changes. Chain the records, so each one carries the fingerprint of the one before it, and a deleted or reordered record breaks the chain. Once a day, publish the latest fingerprint somewhere nobody controls alone, or have a timestamp service vouch for when it existed. Keep at least two copies, and give one of them to someone who is not the buyer.

That is most of what a blockchain offers, without the blockchain. The law agrees about what it proves. Vermont passed a statute that presumes a record verified on a blockchain is authentic, and dated, and added by whoever the chain says added it. The same statute says the presumption "does not extend to the truthfulness" of what the record contains. Canada's evidence law makes the same split in different words: for an electronic document, it asks whether the records system kept its integrity, not whether the record is right. A chain of fingerprints proves when something was written down. It cannot prove that what was written down was true.

Which is the earlier point again, from the other side. The chain handles admissibility. Reliability needs a test.

## The forger's workshop

Here the open standard creates its own problem.

The point of a public standard is that anyone can build to it. A second vendor, a university or a contractor's own team should be able to build a model from scratch, run it against the public test, and produce readings that look exactly like the reference implementation's. That is how the standard escapes its author.

It is also how a forgery is born. If anyone can produce a reading in the standard's format, anyone can produce a fake one: a record that looks compatible, carries plausible numbers and fingerprints, and was made after the fact to tell a convenient story. A forged bid tabulation, a doctored set of past prices fed in as "history", a reading record for a run that never happened. The deep fake of construction will not be a video. It will be a spreadsheet.

A chain of fingerprints does not stop this. It faithfully preserves whatever it is given, fakes included. The defences have to sit earlier, at the point where data comes in.

The first is to fingerprint every input when it arrives, before any bot touches it: the bids at the moment of opening, the public tabulations at the moment of download, with the address they came from and the time. A later dispute can then fetch the source again and compare. The second is to check each input against a second source, since award minutes, published low bids and contract totals should all agree with the line items. The third is to check for the impossible: quantities no job could have, prices outside anything ever bid, the same bid appearing twice.

The last idea comes from an unexpected place. A generative adversarial network, or GAN, is a pair of programs trained against each other: one makes fakes, the other tries to catch them, and each gets better because of the other. It is one of the main ways deepfakes are made. The estimator does not need a GAN, and training it on synthetic prices would weaken the one claim it can make, that it learned from real ones. But it needs the habit of mind. A second, independently built model that prices the same lines and flags the ones where the two disagree badly. A red team that hunts for the inputs that make the model say something absurd. Tests that change something that should not matter, the order of the lines, the wording of a description, and check that the price does not move. And planted fakes, doctored bids slipped into test runs on purpose, with a published count of how many the checks caught.

None of this has to be finished before version 1.0. All of it should be planned for now, because a standard that ignores forgery invites it.

## A black box on the stand

The model at the centre of a mature standard bot will probably be a black box: a system whose reasoning cannot be read off its code. A glass box, where every step can be read, is the thing to aim for, and the project's estimator is being built to be one: each price it gives will show the past prices it came from and the corrections applied, beside the number. The models that come later may not be. The honest promise is translucence, not transparency: enough can be seen to test the box, if not to read it.

That does not keep it out of court. Courts accept black boxes all the time, from breathalysers to laboratory instruments. What they ask for first, and often instead of the code, is evidence that the box works: it has been tested, its error rate is known, the test can be repeated, and people in the field accept the method.

In New Jersey in 2023, a man identified by a facial-recognition search asked how the search worked. The appeal court sided with him and ordered the state to hand over the name of the software, its error rates, the analyst's report and qualifications, and even its source code, because the technology's reliability "has obvious implications for the accuracy of the identification process." Ontario's civil rules committee has drafted a rule for evidence generated by AI that points the same way: a court may require the party using it to name the system, disclose the data and prompts behind it, and show that its outputs are valid and reliable. That list is close to a specification for a bot's test, and, as the New Jersey court showed, the code may be asked for too.

It also answers a worry that sounds fatal: with only one working model, what is there to test it against? The answer is the same as for the breathalyser. A court does not need a second machine. It needs the first one's test results, a test it could repeat, and a reference to measure against. Today that reference is the engineer's estimate and the bids themselves. Later it is the standard. The validation process carries more weight than any expert who speaks for it.

So the validation scaffold is not paperwork around the evidence. It is the evidence.

## What a test has to show

A legal department will not ask whether the bot is good. It will ask what the bot was compared against, how often it was badly wrong, and in which direction.

The comparison comes first. A bot's price means little on its own. Set beside the bids that came in, and beside the buyer's own estimate on the same lines, it becomes a claim that can be checked: closer than what the buyer already had, or not.

Then the ends. A typical miss is only the middle, and a cross-examiner will ask about the edges. The project's early versions showed why. One of them was closer than the engineer's estimate on single lines and level with it on whole contracts, which sounds like a draw, until the edges are read. The engineer's estimate leaned high. The bot leaned low, and its worst misses were all underpricing. For a buyer, low is the costlier way to be wrong: a low estimate makes a fair bid look overpriced, and it sets a budget the work will not fit. Two numbers can share a middle and still fail in opposite directions.

Then the honesty of the test itself. A test is spent once. Scoring the same contracts again with each new version, and choosing the next version after seeing the scores, turns a test into practice. The results are still useful, but they are a rehearsal, and they flatter. A test the law can lean on is run on contracts nobody has looked at, under rules published before the first one is opened, in more than one place.

None of that is a reason to hide the numbers when they come. It is the reason every version of the bot should report its middle, its ends and its lean together, and say plainly which kind of test produced them. The details of how that is done are in the AI edition that accompanies this book.

## Who is liable when the standard is wrong

A legal department will ask one more question: when the bot is wrong, who is liable? Who pays comes after.

The courts already have answers for standards, and they are not comfortable ones. In Canada, following a regulation, or the usual practice of your trade, is evidence that you took reasonable care, not a defence; you can follow the standard and still be negligent. In the United States, an owner who hands a contractor a specification generally carries the risk that the specification is wrong. In England, a contractor who promised a working result paid for the failure even though the industry standard it followed was itself wrong, by a factor of about ten. In Canada, the engineering firm that prepares tender documents can owe a duty to the bidders who rely on them.

The bidder's own loss is a harder case. Some legal scholars argue that the developer of an AI agent should pay for the harm it causes, with insurance alongside, as Maarten Herbosch does in a 2025 law review article. That argument is built for injury and damaged property. A bot that prices a job too low causes neither. It causes what lawyers call pure economic loss, which products liability does not cover and negligence rarely reaches. Meanwhile the bid binds. In Canada a bidder is held to a price it did not mean, even when it tells the owner about the error before award. So under today's law, the bidder carries its own loss, and the realistic routes are contract terms and insurance, not a lawsuit against the vendor.

A lawyer will add a twist. The better informed a user is about a tool's risks, the more of the loss it is expected to carry, and a published test with known error rates makes the bidder very well informed. The test moves the loss onto the bidder. That is not an argument against the test. It is the reason the bidder buys cover, and it will buy it for as long as cover costs less than paying an estimator to check every line. Who carries the loss in law and who is best placed to sell the cover are separate questions. The vendor knows its own bot's error record better than anyone, which makes it the natural seller of the cover even when the bidder carries the loss.

Nor does the book need anyone to make the cover mandatory. The case for mandatory insurance rests on benefits that spill over to everyone, such as safer roads. In bidding, most of the benefit goes to the bidder and the buyer, and they can price it between themselves. Voluntary cover, priced per job, is enough.

The insurers have their own answer, and it is moving fast. Liability policies, and some professional ones, are now being written with exclusions for generative AI. Cover that does exist is priced the way a scientist would test a model: the insurer wants to know where the model is valid, how its errors are distributed, and whether the tests behind those numbers are sound.

A survey of who is liable under today's law is useful, but it is not what a legal department needs to start. It needs two clauses. The first is a scope written as a contract term: which kinds of contract, which sizes and which kinds of line the method applies to, in words the buyer's procurement policy can adopt and a tribunal can read. "This is what the model is not for" in a manual is a description. In a policy, it is a limit. The second is a clause that says, for a trial run, who carries the risk when the method is wrong. Without it, a pilot is a liability nobody has priced, sitting on the buyer's books.

None of this is a reason to stop. It is a list of what the standard must do so that a legal department, and its insurer, can live with it. It must say clearly who is relying on what. It must make the human decision visible. It must come with tests good enough to price, tails included. And it must be written so that following it is strong evidence of care, even though it can never be a shield.

## Three standards, not one

The road to the legal department's blessing runs through the three standards of chapter 17, and each has to hold up under the law as it stands.

The documents standard, the machine-readable tender that replaces the PDF as the copy the bot reads, has to settle which copy wins when the two disagree, because courts often treat the meaning of a standard-form contract as a question of law, and a court will want to know which words the parties agreed to. The tool test has to be one any vendor's bot can pass, not a mandate to use one particular bot, because Canada's trade agreements bar a buyer from naming one brand without accepting equivalents; the bot that sits it has to be frozen, fingerprinted, tested in public and scoped, with what it is not for written so the scope can go into a contract. And the sign-off has to name the person who relied on the reading and record what they checked, because that is the decision a tribunal will review.

That is more steps than the old plan.

## Rebuilding the road

The old order was model, consensus, adoption, law. The new order puts the law beside the model from the start.

In practice that means some of the work planned for later moves to the start: a fresh test agreed before it is run, a second jurisdiction, the edges reported with every middle, and an honest note of what each test cannot show. The method that keeps all of this checkable is set out in the AI edition.

None of it makes the model more accurate. All of it makes the model's accuracy something a legal department can point to.

The deck builder can keep his chatbot. The legal department needs a witness.
