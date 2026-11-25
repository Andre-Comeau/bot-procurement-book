# The insurable event

When a bot causes financial harm, someone carries the loss. Lawyers will answer who is liable later in this book, with the legal department and the witness box. Underwriters put a price on harm before it happens, and this turned out to be more useful for the project. To underwrite a risk, an insurer needs to measure a risk. Insurers already measure AI products one at a time, but each evaluation needs its own custom validation, which makes it hard for a vendor to shop around for the best price. A reference standard would provide a baseline for measuring the deviation of AI-powered estimating products. The project thinks the insurable event is a shortfall in margin, measured across a broad spectrum of tenders rather than on one job. The bidder declares its costs on bid day, and the insurer keeps a right to audit the books as bonding companies already do. This is a proposal to test with underwriters, and the rest of this opening explains why.

There are issues involving perverse incentives since the bidder ultimately controls costs and could make every line pay out. A clever bot may also suggest a low bid on purpose when the company's particular situation still allows a profit. A low bid is then a strategy and not an error, so it cannot be judged on bid day. Insuring the low bid itself would not work either. Every low bid that wins makes the bidder's finances worse, and tenders come too slowly for the data to arrive before several losses.

It may be possible to insure against insufficient margins instead. Lost margin is where an estimating bot's failure would hurt a bidder most, so it is the risk a bidder would want covered before relying on an outside AI. Anyone can bid low to get the job; the trick is still making money afterwards. The bot would be instructed to design a bid that meets a target margin while understanding the bidder's internal costs. The bidder declares those costs in the estimate file on bid day, such as owned equipment, crew rates or a nearby yard, and the margin is measured against a cost model built from them. Costs on site never enter the claim, so inflating them gains nothing. A false declaration voids the policy, and the insurer keeps a right to audit the books as bonding companies already do. The bidder also carries a share of any shortfall. The software would be deemed in default when its margins keep falling short across a broad spectrum of tenders, not when one job loses money. Character can still play a role, as it does with bid bonds, in the size of the coverage the insurer is willing to provide. It is not a finished product, and no insurer offers it today as far as the project has found.

![Schematic, not data, titled "One losing job is not a claim". Each mug is a completed job, filled to the margin it made against the costs declared on bid day. Two lines run across the mugs: the target margin and, a little lower, the trigger. Top row, a normal year: eight mugs, six full and steaming and two short. Poured together into one large mug, the average sits above the trigger, so there is no payment, and the losses on single jobs stay with the bidder. Bottom row, a bad year: seven of the eight mugs fall short and only one is full. The average sinks below the trigger, and the policy pays: in the large mug, the gap below the trigger is filled in blue for the insurer's share, with a thin grey band for the bidder's own share. The policy only looks at the average across a broad spectrum of tenders.](../images/one-losing-job.png)

## The buyer stands behind its number

Margin insurance is the bidder's cover, and it needs an insurer that does not exist yet. The base case needs no insurer at all. The buyer runs the standard bot, publishes its number, and stands behind it. If the number was wrong, the buyer carries the loss, not the bidder.

That sounds generous, but it is arithmetic. A buyer who lets many tenders a year sees what a reverse auction does to a reliable reference. The bids gather closer to the number, and the cheaper bids across the year outweigh the occasional payout when the bot missed. The buyer already controls its own cost through the auction, so it is the party best placed to carry the error of the tool it chose. Buyers already carry this kind of risk on their own quantities: when the real quantity strays far enough from the estimate, many contracts reset the price, and differing site condition clauses do the same for the ground. Standing behind a price is a step further, and it is the step this book proposes.

The promise starts a new argument. After every loss, someone has to decide whether the number was wrong or the work was done badly, and each side has a reason to tell it differently. The bidder will be tempted to bid low on the strength of the number and claim high when the job goes wrong. Only the record can settle it, which is why the standard keeps one, and why the rule for deciding is something to fix before the bids open, not after. The witness box in chapter 17 is where that argument ends up.

Self-insurance only works for a buyer with enough tenders to average out a bad year. A small town that lets two jobs a year cannot carry the promise alone, so it insures it. Third-party cover also matters for marginal bidders, the thin firms a self-insuring buyer would rather not sponsor but cannot shut out of an open competition. The insurer sits beside the buyer for them, and above the buyer for the rare year when every bot misses together. The rest of this chapter is about what that insurer would need to measure.

## Who answers for the reading

Liability for what a bot reads will likely sit with the user's bot, not with the bot that supplied the information. That matches how contract law already works. An AI vendor can tell its own customer to use the tool at their own risk. A company whose bot answers strangers cannot so easily, because a bot's answer can bind its owner when someone reasonably relies on it. Drawings and specifications already work this way for human estimators: the buyer answers for the documents, and each bidder answers for its own reading of them.

Two statements are true at once. The bidder's bot's reading of the requirements is the bidder's responsibility, and when the reading is wrong, the bidder eats the cost. The buyer and its designers are still responsible for documents free of errors. Those documents are written for people today, and that is why a move to documents written for bots needs a standard. Until one limits what a designer answers for, few designers will write for machines.

It also explains why the buyer should not run a bot that answers bidders' questions. Bidders would each ask differently, a bot answers from probabilities, and the answers would differ from one bidder to the next. In Canada the buyer has to treat bidders equally, and a bidder who lost could say it relied on what it was told. A shared bot would turn every answer into a liability.

So each bidder brings its own bot, and the bidder decides whether to raise what the bot finds. Compelling it to report would not work, for five reasons. Bidders are not the designers, and a duty to find errors hands them a licensed professional's liability. Nobody pays them for the review, and paying for it invites bidders who bid for the fee. A flood of minor issues would hide the major one and push tenders into the building season. Anyone can be made to ask a question, but nobody can be made to ask a useful one. And designers would have less reason to get the drawings right if the bidders were made to check them.

Critics call this a guild protecting its habits, and the point is fair: the honest bidder who asks can lose to the strategic one who stays quiet. The best reason to raise an error is to stop a rival from exploiting it, and that works for a firm that would rather win on its location, its crew or its capital than on the buyer's mistakes. A bot does not create that motive. It makes acting on it cheap, because a question found and written in minutes can be answered to every bidder at once.

## How often a price runs low

An underwriter's first question about any price is which way it leans, and how far. For human prices the public records give a fair answer: low prices are common, and losses, as far as anyone can see, are rarer.

Start with the buyer's own number. On Texas highway contracts let from 2017 to 2024, the winning bid came in more than 10 percent under the state engineers' estimate on about a third of contracts, and more than 20 percent under on one in eight. In California from 2000 to 2008 the same happened on half of contracts and on nearly a third. Nationally, the Federal Highway Administration found the low bid within 10 percent of the estimate on just under half of projects. Which way the miss runs depends on the market. When work is scarce and many firms bid, the bids fall below the estimate; when bidders are busy, they climb above it.

Then the bidders against each other. In Texas the second-lowest bid was more than 10 percent above the winner's on a third of contracts, and more than 20 percent above on one in eight. Against the middle of the other bids, the winner was more than a fifth lower on more than a quarter of contracts. Ten percent is the spread at which one large bonding company asks its contractor to explain the bid, so on this work the letter would go out on one job in three.

None of this says the low bid lost money. A low price can be a real advantage: a yard nearby, owned equipment, a crew that would otherwise sit idle. Whether it was an error only shows on the contractor's books, and those are rarely public. What is public is softer. In a 2019 survey of 666 American construction firms, 29 percent said they usually make less profit than they estimated. In a smaller Australian survey, almost two in five quantity surveyors and contractors said their last completed project had been underpriced. In laboratory auctions, experienced construction executives fell into the winner's curse, with two winning bids in three below the price at which they would break even. In the field the industry survives the curse anyway, through habits learned on the job and ways back from a bid that went too low.

So the base rate an insurer would start from is not zero, and it is not one number. Human prices run well below the market often, and lose money less often. A bot's error has to be measured against both, which is why every version of the bot will report its lean beside its middle. The prototype's own lean, low by design, is in chapter 16.

## What economists already know

Insurance against a bad price is new. The economics of buying insurance is not, and four old results carry over.

The first is about deductibles. An insurer pays for its staff, its brokers and the capital it holds for a bad year, so a policy always costs more than the losses it expects to pay. In the 1960s the economists Kenneth Arrow and Jan Mossin showed what a sensible buyer does about that: it keeps the small losses and insures only the large ones. A buyer with deep pockets keeps more, and may buy nothing at all. For a bidder, that means a policy that pays only once a miss is large, with the bidder carrying the first part.

The second is about size. In 1982 David Mayers and Clifford Smith found that large, diversified companies gain less from insurance, because they can absorb a loss that would sink a smaller firm. When they buy it, they buy it for other reasons: a lender asks for it, or the insurer handles claims better than they could. A contractor with thirty bids a year can carry its own misses, and a firm with a handful cannot. The cover is most useful to small bidders, and to whoever has the most jobs to spread it over, which is the software vendor.

The third is about prevention. In 1972 Isaac Ehrlich and Gary Becker separated insurance, which moves a loss to someone else, from self-protection, which makes the loss less likely. Self-protection is often worth more. Checking a bot's price against the lowest prices paid in recent years, and against the standard, before the bid goes in, is self-protection. In the project's own model, those checks do more for a bidder than any policy, and they leave a remainder small enough to insure cheaply. An insurer that charges less for checked bids pays the bidder to check.

The fourth is the oldest warning in bidding. In 1971 Ed Capen and two colleagues at Atlantic Richfield worked out why the oil leases their company won kept disappointing. The winning bid tended to be the one whose estimate was most wrong. They called it the winner's curse. Douglas Dyer and John Kagel later showed how construction firms learn to live with it. A bot that errs the same way for every client brings the curse back in a new form, because its mistakes no longer cancel out across the bidders.

None of this is news to an underwriter. It may be news to an estimator.

## Who would buy it

The project's model puts these ideas to work on two Texas highway bidders. The medium bidder sends 31 bids a year on jobs of about $8 million, wins about five, and earns about $2 million a year. The small bidder sends 12 bids a year on jobs of about $1.5 million, wins about two, and earns about $125,000. Both price with a bot that typically misses by 6 percent, both check every price before it goes out, and both keep the first 5 percent of any miss, with the cover paying 80 percent of the rest.

What the cover is worth depends on how much a bad year hurts, which economists call risk tolerance. Picture a coin toss that wins a sum or loses half of it. The largest sum a firm would just about accept is its risk tolerance. The table writes it as a share of a year's profit. A firm with thin capital sits low on that scale, and a firm with deep pockets sits high.

| Bidder | Risk tolerance, as a share of a year's profit | What the cover is worth to the bidder, per job won | Buys it at 0.15 percent, sold on its own? | Buys it at 0.11 percent, through the vendor? |
|---|---|---|---|---|
| Medium | 35 percent | $18,500 on an $8 million job (0.23 percent) | Yes | Yes |
| Medium | 70 percent | $10,700 (0.13 percent) | No | Yes |
| Medium | 140 percent | $8,200 (0.10 percent) | No | Barely |
| Small | 40 percent | $12,000 on a $1.5 million job (0.80 percent) | Yes | Yes |
| Small | 80 percent | $4,250 (0.28 percent) | Yes | Yes |
| Small | 160 percent | $2,300 (0.15 percent) | Barely | Yes |

The two prices in the last columns are the lowest an insurer could charge and still earn a fair return. Sold on its own through a broker, the cover needs about 0.15 percent of the contract. Sold by the software vendor with its bot, with claims handled automatically and a yearly cap on what the insurer pays, it needs about 0.11 percent.

The cover sells to any firm with thin capital, and through the vendor to most firms. It rarely sells on its own to a firm with deep pockets, as Arrow, Mossin, Mayers and Smith would have predicted. These are the model's figures, on assumptions that a real bidder's books would replace.

## Four open questions

Four questions direct this effort, and the project cannot answer them alone:

### 1. Where does the product's normal error end and a defect begin?

As a probabilistic technology, bringing an AI-powered pricing bot's error to zero would lose the prediction model that drives its usefulness. Its strength lies in discovering averages and reaching solutions at superhuman speeds. The tails will always be there with a technology built on probabilities. Insurance can pick up the tails left over after the model tuning. Where would an underwriter draw the line between error that comes with the product and a defect?

### 2. Could insurance speed up adoption?

By picking up the tail risk, insurers will allow for faster iterations. Software developers and their clients could forgo a lengthy trial period and begin using productivity-enhancing tools much earlier in the lifecycle. This is great for the software client receiving the productivity gains, and great for the software developer receiving cash flow to develop the next iteration of the product. What would an insurer need to see before covering a tool that has not finished its trials?

### 3. How should the tails be covered?

With careful measurements and validation, it should be possible to insure a product based on its own characteristics, but the coverage of the tails would be tricky. Should the risk be capped leaving the vendor and their client exposed in the case of a major failure? Should the insurance premium be increased making deals less likely to close?

### 4. Would a shared standard lower insurance premiums?

Both of the questions about the tails are ameliorated through a reference standard. In our case of AI enhanced procurement, a standard AI-powered estimating system would provide a baseline insurers could use to limit payout risks. Since the reference standard would be able to generate estimates with error ranges, commercial products could be measured against this standard. Premiums could be capped by making the deviation a condition of each insurance policy. A bidder who prices below the standard is free to do so, but that bid is not covered. The rule carries more weight than it seems to. The standard is public, so a bidder can run it before the tender closes and see a claim coming. Without the rule, a bidder could bid below the standard on purpose to win the job and leave the insurer to pay for the gap. How much would a shared standard need to tell an insurer before it changes the price of a policy?

There is also the issue of bid inflation. By limiting coverage of bids that may be too low based on the standard, insurers will create incentives for keeping bids closer to the expected outcomes. There will be systematic risk to buyers from this approach. The carrot to counterbalance this risk would be the growth of custom bids. Alternative bids are tricky for people to judge, and they draw complaints from unsuccessful bidders because the selection criteria cannot be written in advance without knowing the nature of the value engineering. A working, open-source estimator would solve this problem, because the method itself becomes the criterion disclosed in the tender. Bidders can model their proposals on their own copy before closing and see the outcomes, and the buyer judges them the same way afterwards. The same file always gets the same price, whoever runs it. A person still needs to review each alternative, since it may conflict with a need the tender never stated. The tender can say up front that alternatives pass or fail on the engineer's technical review, with written reasons, and a back-up lowest-cost bid applies if none of the alternatives is suitable. Life-cycle costs could come into a later version of the standard. Standardized AI could then replace the incentives for bid inflation with the opportunity for contractors to use their expertise to offer solutions unforeseen in the tender.

With these in mind, the aim is to make a probabilistic price insurable inside a bidding system that pretends every price is certain. The courts would not need to move for this to happen. Underwriters would.

## The standards we are following

The project does not need to invent a framework for AI. Several already exist, and an underwriter or a lawyer will look for them first. The plan is to follow their lead and add only what they leave out. None of them says how to check whether a price is right. The project's standard adds three things. The first is an agreed way to measure how far an AI estimate misses. The second is a fair point of comparison, which here is what contractors actually bid. The third is a range around that comparison, wide enough that an honest bid rarely falls outside it, which an insurer can write a policy against.

1. NIST AI Risk Management Framework (United States). This is the backbone. It lists about 72 practices for mapping, measuring and managing the risks of an AI system. Its text is free to quote and adapt anywhere, so the project's standard can be written as a profile under it without anyone buying a copy. Texas already requires its state agencies to adopt AI rules aligned with it.
2. EU AI Act, Article 15. A tender bot is not a high-risk system under the Act, but Article 15 is the only clause in the frameworks we read that asks a provider to declare its accuracy and the metrics behind it. It is the precedent for publishing how far the estimates miss and the range an honest bid should fall within.
3. ISO/IEC 42001. This is a certifiable management system for the organization that runs the AI, not for the AI itself. It is a paid standard, so the project cites its clause numbers rather than its text. Several of its controls match the estimate file.
4. MITRE ATLAS. This is a catalogue of attacks on AI systems. The one that matters most here is poisoned data, such as fake or rigged bid results fed into the price history.
5. RICS professional standard on AI. The Royal Institution of Chartered Surveyors made it mandatory for its members on 9 March 2026. Surveyors must keep a register of the AI they use, and a named surveyor must decide whether an AI output is reliable enough to use. It is the one construction body this project found already setting rules for AI, and lawyers expect courts to read it when judging negligence.

Insurers already work this way with models they did not build. American actuaries follow a written rule, ASOP 56, on how far they may rely on someone else's model. Florida has accepted private hurricane models against published standards since 1995. An AI estimating system could be listed the same way.

Following their lead has three advantages. A reader from insurance, law or IT security sees familiar ground and can check the profile against what they already use. The project can borrow years of consensus instead of building it from scratch. A crosswalk to each framework also lets a commercial product show that it meets the project's standard and theirs at the same time. None of these frameworks sets a number, though, and following them is evidence of care rather than a shield. Deciding who is liable is still left to the policy and the contract.

Who is already insuring AI, and what the project would ask of an insurer, belongs to the insurers themselves. Their pitch is [chapter 13](06f-the-insurers.md), with the other parties who stand to gain.
