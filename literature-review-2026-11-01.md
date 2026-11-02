# Literature review: what has been written near the Bot Procurement book

*Compiled for Andre on 1 November 2026, for the book working-titled* Fair and Reasonable *or* The Reasonable Bot. *About 165 works across four questions, plus a verification pass. Part 1 is the synthesis and is the part to read. Parts 2 to 6 are the full annotated strands, kept as the reference shelf that Appendix B and the chapter notes can draw from.*

**How far to trust it.** Each entry carries its own verification label. "Read" or "V-page" means the source was opened. "Listing" or "Cited" means a catalogue, publisher or search result confirmed it exists, and any numbers marked "from memory" still need checking. "UNVERIFIED" means do not cite it yet. No citation was invented, but several page numbers, editions and figures are flagged for checking before print. The search hit the session's web quota partway through each strand; Part 6 is a second pass that checks the most important flagged items and fills the gaps. **Where Part 6 corrects an earlier strand, Part 6 wins**: the Kawai and Nakabayashi sample is about 42,000 auctions, IFC is now ISO 16739-1:2024, AACE has a road and rail practice (98R-18), FRE 707 was withdrawn in May 2026, the Quebec and Texas bidder duties qualify strand 3's "no bidder duty" finding, and *Brown & Huston v York* could not be found and should not be cited.

---

## Part 1. Synthesis

### The four questions, answered

**1. Has anything like this book been written before?** No. Nothing found combines the book's three threads: construction tendering, the practical question of whether a price is fair and reasonable, and a "reasonable machine" legal standard. The exact phrases "bot procurement", "bot-first tender" and "reasonable bot" (as a legal term) turn up only vendor marketing. Five separate literatures each cover one leg:

- **The reasonable machine in law.** Ryan Abbott's *The Reasonable Robot* (Cambridge, 2020) is the closest in title and idea, and the book must name it and set itself apart. Abbott uses reasonableness as a tort rule for harm a machine causes. The book uses a frozen, published standard bot as a shared *measuring instrument* for a price that a human signs. Diamantis, "Reasonable AI" (Vanderbilt L. Rev., 2025), is the closest in structure: he defines reasonableness as an error rate against a baseline of humans and machines together. Chagal-Feferkorn's "The Reasonable Algorithm" (2018, 2021) and Rane's ICML 2024 position paper complete the set.
- **Machine evidence.** Andrea Roth, "Machine Testimony" (Yale L.J., 2017), and the proposed US Federal Rule of Evidence 707 are the direct precedents for chapter 7. Rule 707 was published in 2025 to apply the Daubert reliability test to machine output, withdrawn in May 2026 after objections on cost and scope, and is being redrafted; the leading draft "would ordinarily require an expert" to sponsor AI evidence, which is the book's keyholder in all but name. The UK Post Office Horizon case is the cautionary tale.
- **Agentic commerce and procurement.** Gartner's *When Machines Become Customers* (2023), McKinsey's agentic-commerce report (2025), Nicoletti's *Agentic AI for Procurement* (Springer, 2026), the Pactum/Walmart negotiation bot, and Arkestro's 2024 US patent on "predicting price reasonableness". All of it is commercial, mostly proprietary, and none of it asks how anyone *knows* a price is fair. Arkestro is the closed-source opposite of the book's design and is worth citing as such.
- **Machine-readable contracting.** Surden's "Computable Contracts" (2012), OECD *Rules as Code* (2020), the Open Contracting Data Standard and its infrastructure version OC4IDS, the EU's eForms, and the UK *Construction Playbook* (2020), which says standards should be "read by both people and machines". These standardise notices, payment records and transparency data, not the drawings and quantities bidders actually price.
- **Construction reform manifestos.** Latham (1994), Egan (1998), Farmer's *Modernise or Die* (2016), Kieran and Timberlake's *Refabricating Architecture* (2004). They diagnose adversarial lowest-price tendering, the book's "starting a relationship expecting a divorce", but prescribe relational or manufacturing fixes. The book's fix is informational, which is new.

The closest single construction paper is **Heo, Ahn and Park (J. Mgmt. Eng., 2025/26)**: GPT-4o bidders in a simulated lowest-bid construction market tacitly colluded at about 4 to 6 percent above cost, and more market transparency made it easier. It is the strongest counter-evidence the book needs to answer.

**2. Are there popular-science explainers of procurement?** Essentially none of procurement itself. The popular shelf covers its edges: auctions and market design (Roth's *Who Gets What and Why*, Milgrom's *Discovering Prices*, Harford, the Nobel 2020 lesson pages), megaproject overruns (Flyvbjerg and Gardner's *How Big Things Get Done*, the Transit Costs Project, Brian Potter's *Construction Physics* and *The Origins of Efficiency*), price psychology (Poundstone's *Priceless: The Myth of Fair Value*, almost a counter-title), estimating (Douglas Hubbard's *How to Measure Anything*), bureaucracy (Scott, Graeber, Bagley, Pahlka's *Recoding America*), and the Pentagon scandal genre ($600 hammer, $640 toilet seat). Only Kelman (1990, a policy monograph), Pahlka, one "Procurement" chapter in the MIT Essential Knowledge *Auctions* (Hubbard and Paarsch, 2016), and the satire of Augustine's *Laws* and Parkinson's bikeshed treat buying as a subject. Nobody explains the engineer's estimate, sealed bids, the bid tab and the price book to a lay reader, and nobody asks the book's spine question.

**3. What is specific to construction procurement?** A large, mature literature, in four strands that rarely meet:

- **Textbooks and government reviews** from the Simon Report (1944) and Banwell (1964) through Latham, Egan and the *Construction Playbook*, which already diagnose the book's chapter 1 tensions. The Playbook's "should cost model" is the UK government's own reference price, but nothing requires its method to be published, rerunnable or tested for error.
- **Bidding and auction economics.** Friedman (1956) and Gates (1967) treated opened bids as data sixty years ago. **Bajari, Houghton and Tadelis (AER, 2014)** show that California highway bidders price expected changes into their unit bids, with adaptation costs of about 7.5 to 14 percent of the winning bid: the strongest evidence for "price the errors, sue later". **De Silva et al. (2008)** show that when Oklahoma began publishing its engineer's estimates, bids fell and tightened compared with Texas, the book's own development data. Porter and Zona (1993), Kawai and Nakabayashi (2022) and Huber and Imhof (2019) show that bid tabs can be screened for collusion.
- **Tender law.** In Canada, *Ron Engineering* (1981), *M.J.B.* (1999), *Tercon* (2010), *Edgeworth* (1993) and *Bail* (1992) place the disclosure duty on the owner, and *Edgeworth* explicitly accepts that bidders cannot each afford to re-engineer the design in a short tender period. In the US, *Spearin* (1918) makes the owner warrant the design, and the patent-ambiguity doctrine makes a bidder raise obvious errors or lose the claim, without compelling disclosure. James Judson's 2017 CBA essay is the best short map of Canadian pre-contract disclosure. Two finds from the verification pass sharpen this. Quebec's Court of Appeal recognises a bidder's *duty to inquire* before close as the corollary of the owner's duty to inform (*AMT c. Sintra*, 2024 QCCA 500): a bidder who could have asked cannot later complain of the ambiguity. And **Texas**, the book's development-data state, since 2021 makes a contractor disclose in writing any design defect it knows of or "reasonably should have discovered" using "ordinary diligence", defined as the observations a contractor would make *in preparing a bid*, and expressly not requiring an engineer (Tex. Bus. & Com. Code §59.051). Both are "reasonable bidder" tests, and both widen as checking bots get cheap. No one has written about that yet.
- **How a price is judged in practice.** FAR 15.404-1 lists the US techniques; PSPC's 2023 *Practitioner's Guide for Procurement Pricing* is the Canadian federal counterpart and simply presumes that several compliant bids "validate the fairness of the price". The Northwest Territories' tender-evaluation procedure is a good working example: compare with the government estimate, and if the low bid is "obviously excessive", ask the bidder to show its work, with no threshold defined. TxDOT's *PS&E Preparation Manual* §5.4.1 documents how the engineer's estimate is built from bid history, the human baseline for chapter 8.
- **Digital construction standards**: IFC (now ISO 16739-1:2024, IFC 4.3, which adds roads, rail and bridges, so it fits a civil-works pilot), ISO 19650, COBie, the EU procurement directive's BIM clause (Art. 22(4)), the UK BIM mandate. They standardise design data, never price. ISO 10845 and Ron Watermeyer's papers behind it standardise procurement *procedure* and stop short of computation.

**4. Has anybody studied the limits of automating procurement?** Yes, a lot, but scattered across economics, e-procurement evaluation, AI, human factors and law, which rarely cite each other.

- **Contracts cannot be complete** (Williamson, Hart, Tirole, Bajari and Tadelis). **Tirole's "Cognition and Incomplete Contracts" (AER, 2009)** is the book's best theoretical ally: contracts are incomplete because thinking about contingencies is costly, so bots that make that thinking cheap should produce more complete contracts and shift bargaining power to whoever thinks best. That is chapter 5 in formal dress.
- **Digitising the channel changes who bids more than what the price is.** Lewis-Faupel, Neggers, Olken and Pande (2016) found e-procurement in India and Indonesia improved quality and entry but not prices; ProZorro's price effect is modest and not robust; KONEPS and eForms automate process, not judgement.
- **Automated sourcing works where the object can be fully specified** (Sandholm's combinatorial sourcing at P&G, Pactum's tail-spend bot at Walmart) and struggles where it cannot. Construction is the hard end.
- **Shared pricing agents can soften competition** (Calvano et al. 2020; Assad et al. 2024 on German petrol; Fish et al. 2024 on LLMs; Ezrachi and Stucke's hub-and-spoke scenario).
- **Humans in the loop are a weak safeguard** (Bainbridge's "Ironies of Automation", automation bias, Elish's "moral crumple zones", Green 2022 on oversight policies, and the Robodebt, Dutch childcare and Horizon scandals).
- **Reading drawings is the binding constraint, not pricing.** The 2025 to 2026 benchmarks (CEQuest, AECV-Bench, DrawingVQA, Handoff-H1) show frontier models read text well and count symbols on drawings poorly, trailing professionals by 20 to 40 points on expert questions.
- **Automated price-reasonableness tools have already failed once in government.** The GSA Inspector General (2022) found contracting staff treated output from GSA's 4P pricing tool as proof that prices were reasonable, including "self-hits" that compared a contract with its own prices. That is the price-book loop eating its own tail, and the best real case for the book's required record.
- **Unequal bots produce unequal prices that nobody notices.** Anthropic's Project Deal (2026): agents on a stronger model got better prices for the people they represented, who rated the deals equally fair. That is an argument for a common reference bot both sides can rerun. Project Vend (2025) adds that a bot pricing under social pressure gives discounts and sells below cost.
- **Reproducibility needs more than pinned weights.** Chen, Zaharia and Zou (2023) document hosted-model drift, which backs the pinned-weights argument; the Thinking Machines work (2025) shows run-to-run variation also comes from the inference software.

### What the book can claim as its own

1. **The first popular explainer of public-works procurement and price reasonableness.** The gap is real, so the book can say so plainly. It should spend more words than a manifesto usually would explaining how tendering works today, because its readers (policy people who read *Abundance* or *Construction Physics*, Dragons, sponsors) will not know the loop it reforms.
2. **Reasonableness as a shared measuring instrument, not a liability rule.** That is the move away from Abbott and Diamantis.
3. **A public, frozen, rerunnable reference estimator with a published tolerance and a required record**, as a conformance standard extending ISO 10845 into computation. Nobody publishes such a thing. The USDOT Inspector General (2019) found that FHWA does not even check whether engineer's estimates are accurate, and the ML cost-estimation literature has no shared benchmarks (Elfaki et al.'s survey). A public, versioned test set is a contribution in its own right.
4. **Reading the economics and the tender law together.** The "reasonable bidder" of the patent-ambiguity doctrine and the "could not reasonably obtain the information" limb of *Bail* both shift once checking is cheap. *Edgeworth*'s argument that duplicated checking is wasteful is exactly the cost a checking bot removes. Nobody has made this argument.
5. **The certification-once answer to Rule 707's cost objection.** If a standard bot is certified publicly once, nobody has to relitigate its reliability in each dispute.

### What cuts against the book, and should be faced in the text

1. **The 2 to 3 percent threshold is far stricter than any human standard.** FHWA's 2015 review found US engineer's estimates within ±10 percent of the low bid on only 48 percent of 1,611 projects, against an official target of ±10 percent on half of projects. AACE's best estimate class (Class 1, in the process-industry practice 18R-97) allows −3 to −10 percent and +3 to +15 percent; the road and rail version, 98R-18, still needs checking. Either the book anchors its tolerance to AACE classes, or it redefines the 2 to 3 percent as agreement with a reference reading under a fixed protocol rather than distance from the low bid. Chapter 7's split between accuracy and defensibility is the place for this.
2. **The training data are strategically skewed.** Bid-tab unit prices carry bidders' bets on quantity overruns (Bajari, Houghton and Tadelis; the unbalanced-bidding literature) and, sometimes, cartels (Charbonneau Commission; Porter and Zona). A bot trained on TxDOT tabs learns prices, not costs. The book should say so, and a collusion screen probably belongs in the standard bot.
3. **A shared pricing bot used by bidders may raise prices.** The algorithmic collusion results, and Heo et al. for construction specifically, suggest a public reference price can anchor bids upward. Against that, De Silva et al. found publishing the engineer's estimate *lowered* bids. The safest framing is a buyer-side evaluator, with bidders' use watched, and the book can present the two findings as a live tension in its own style.
4. **The keyholder may be accountability theatre.** Green (2022) argues human-oversight requirements mostly legitimise flawed algorithms; Elish shows blame lands on the nearest human; Bainbridge shows the keyholder's skill decays. The book's stronger defence is institutional (public test set, published error rate, rerunnable standard), which is Green's own remedy. Lead with that, keep the keyholder's duty procedural (followed the protocol, kept the record), and say how keyholders stay in practice.
5. **Texas does compel some disclosure.** Chapter 5 says a bidder need not be compelled to report what its bot finds. Texas §59.051 already requires a contractor to disclose known defects in writing, measured by what a bid-preparer would notice, and Quebec penalises a bidder who fails to ask. The book's position survives as "the record decides, not a duty to find", which is close to what both laws do, but the chapter should name them, especially since Texas is the development data.
6. **Digitising tenders has not lowered prices elsewhere.** The book should promise better entry, speed, fewer disputes and an auditable record, and treat lower prices as a hypothesis.
7. **"Fair value" may be a myth** (Poundstone). Concede it for consumers; argue that public construction has always made fair price institutional through anchors (the engineer's estimate, the price book), and the reform is to make the anchor explicit, published and tested.
8. **More paperwork, not less** (Graeber). The record is new paperwork. The claim must be that machine-readable records are cheaper to produce and to check.

### Chapter by chapter: what to read first

| Chapter | Read first | Why |
| --- | --- | --- |
| Front matter, prologue | Abbott 2020; Rao, *Protocol Reader* | Name the nearest title and separate from it; the protocol frame |
| 1. Expecting a divorce | Bajari, Houghton & Tadelis 2014; Thaler, *The Winner's Curse*; Latham 1994; Tirole 2009 | Puts a number on pricing the errors; the low bidder as the one who missed the error |
| 2. The tender is the API | Yegge's platform rant (the source for the Amazon mandate); Pahlka 2023; Alon Levy, IFP 2026, on publishing unit costs; AECV-Bench and DrawingVQA; OCDS, eForms, IFC; Construction Playbook | The benchmarks show why drawings must become data |
| 3. How a price is judged | FHWA 2004 guidelines and 2015 review; USDOT OIG 2019; De Silva et al. 2008; UK Should Cost Model guidance; PSPC 2023 pricing guide; GNWT tender evaluation; TxDOT PS&E manual §5.4.1; AACE 18R-97 and 98R-18; GSA OIG 2022 on the 4P tool; the $600-hammer story | The human baseline and its error; publishing a reference price lowers bids |
| 4. Two centuries of one loop | Simon 1944, Banwell 1964; Friedman 1956, Gates 1967; Spearin 1918; Flyvbjerg's reference-class forecasting; Harford's *Fifty Things* as a format model | Card candidates and the loop's intellectual history |
| 5. Liability shifts | Ron Engineering, Edgeworth, Bail, Tercon; Judson 2017; Sintra 2024 (Quebec duty to inquire); Nowlan (duty to warn in performance); Texas Bus. & Com. Code §59.051; patent ambiguity; Bajari, McMillan & Tadelis 2009; CCDC 2-2020 supplementary conditions; Scholz on algorithmic contracts | Disclosure sits mostly on the owner; bidder duties exist only as inquire-or-lose-the-claim, and Texas's bid-stage diligence test |
| 6. The banana peel | Kroll et al., "Accountable Algorithms"; Hubbard on calibrated uncertainty | Admitting uncertainty as design |
| 7. The bot in the witness box | Roth 2017; FRE 707 history (withdrawn May 2026, redraft leans to requiring an expert); Anthropic Project Deal 2026; Horizon judgment and Marshall et al. 2021; UK MoJ 2025 call for evidence; Diamantis 2025; Chagal-Feferkorn; Green 2022; Elish 2019 | The legal frame and its failure cases |
| 8. Building an estimator | Mohamed & Moselhi 2022; CEQuest; Handoff-H1; Elfaki survey; Abdelaty's WYDOT engineer's-estimate project | Comparable accuracy figures, and why a public test set matters |
| 9. What an evaluator needs | Canada's Directive on Automated Decision-Making and its impact assessment; Chen, Zaharia & Zou 2023; Thinking Machines 2025 | A Canadian template for "public test plus required record"; pin the inference stack too |
| 10. The protocol | ISO 10845 and Watermeyer; CCDC 23; OC4IDS; ANAC agent competition; Sánchez-Graells 2024 | Standard as conformance test; why a standards body beats regulation by contract |
| 11. The meta-goal | Autor 2014 on Polanyi's paradox; Galbraith (already read); Scott, *Seeing Like a State* | Tacit knowledge and legibility, for the keyholder and the imagining |
| Appendix A cards | Augustine's *Laws*, Parkinson, Harford's *Fifty Things*, the Nobel 2020 lesson diagrams | Register and format models |

### Suggested additions to the outline (for Andre to accept or not)

- A **one-paragraph positioning** in the front matter: "This is not *The Reasonable Robot*." Abbott judges harm; this book measures prices.
- An **opening parable** for chapter 3: the $600 hammer was a $15 hammer carrying an even share of overhead. A fair total can hide absurd lines, and absurd lines can sit in a fair total.
- A **tolerance anchored to AACE classes**, or the 2 to 3 percent restated as protocol agreement, in chapters 3 and 7.
- A short passage in chapter 5 or 10 on **who may use the standard bot**, with the collusion evidence on one side and De Silva on the other, kept in tension.
- In chapter 9 or 10, "pinned weights" widened to **pinned weights, prompt, harness and inference stack**, or conformance defined statistically over many runs.

---

## Part 2. Has anything like this been written? (prior works)
*Prior-works review for* Fair and Reasonable / The Reasonable Bot *(Andre Comeau, Nov 2026). Compiled 2026-11-01.*

### Method and verification notes

- I used WebSearch and opened the source pages with WebFetch where the shared budget allowed: publisher pages, journal pages, arXiv abstracts, patents and government PDFs. Partway through, the session's shared WebFetch budget (100 per hour across all agents) ran out, and then the WebSearch budget (200 per turn) ran out too. I confirmed the late items from search-result listings, such as publisher, catalogue or repository URLs, without opening their full text. Each entry says which kind of check it got.
- Verification labels:
  - **[V-page]**: I opened the source page and read its citation and abstract.
  - **[V-listing]**: the work's existence, title and venue are confirmed by publisher, catalogue or repository URLs in the search results. Volume or page numbers marked "(memory)" are from my background knowledge and should be checked before print.
  - **UNVERIFIED**: I could not confirm it in this session.
- Not completed because the budgets ran out: a forward-citation trawl on Abbott (2020) and Diamantis (2025); a check of Canadian PSPC and Defence Construction Canada guidance on price support; the McKinsey (2017) *Reinventing Construction* report; and verbatim searches for "tender is the API", which I ran once with no hits on the phrase.
- **Verbatim search results:** "bot procurement" and "bot-first tender" turned up only vendor marketing (Forgent.ai, Boomi/HEB, Moxoff), with no book, essay or report. "Reasonable bot" as a legal term turned up nothing. The nearest phrases are "reasonable robot" (Abbott), "reasonable computer" (Abbott), "reasonable algorithm" (Chagal-Feferkorn), "Reasonable AI" (Diamantis) and "reasonable person standard for AI" (Rane). **Nothing I found combines construction tendering, price-reasonableness determination and a reasonable-machine legal standard.**

---

### A. Closest precedents (ranked)

#### 1. Ryan Abbott, *The Reasonable Robot: Artificial Intelligence and the Law* (Cambridge University Press, 2020). [V-page]
DOI 10.1017/9781108631761; ISBN 9781108472128 (hb), 9781108459020 (pb). https://www.cambridge.org/core/books/reasonable-robot/092E62F0087270F1ADD9F62160F23B5A
- **Argument:** The law should be neutral between AI and human behaviour, which Abbott calls "AI legal neutrality." He applies this to tax, tort, intellectual property and criminal law. Chapter 3, "Reasonable Robots" (pp. 50–70), argues that when an AI is safer than a person, its harms should be judged under negligence and not strict product liability. In effect it asks whether a reasonable person would have done what the machine did. Abbott worked the idea out first in "The Reasonable Computer: Disrupting the Paradigm of Tort Liability," 86 *Geo. Wash. L. Rev.* 1 (2018) [V-listing: https://www.gwlr.org/wp-content/uploads/2018/04/86-Geo.-Wash.-L.-Rev.-1.pdf]. Michael Conklin's review, "The Reasonable Robot Standard: Bringing AI Law into the 21st Century," *Yale J.L. & Tech.* (4 Sept 2020) [V-page: https://yjolt.org/node/1016], says Abbott's tort chapter endorses a negligence-style standard for AI.
- **Overlap and difference:** This is the closest in title and concept. Both carry the common-law reasonable person over to machines. The difference is that Abbott uses reasonableness to judge harm a machine causes, as a liability rule for tort. The book uses a published, frozen standard bot as a benchmark for fact-finding, a test of conformance for a price that a human keyholder signs. Abbott does not cover procurement, pricing, expert-evidence admissibility (Daubert/Mohan) or a published test set. **The book should cite Abbott and set itself apart from him explicitly**, since the title *The Reasonable Bot* echoes his.

#### 2. Mihailis E. Diamantis, "Reasonable AI: A Negligence Standard," 78 *Vanderbilt Law Review* 573–615 (2025). [V-page]
https://scholarship.law.vanderbilt.edu/vlr/vol78/iss2/4
- **Argument:** AI has no natural comparison class. Measuring it against humans sets the bar too low, and there are too few algorithms in many fields to measure it against each other. Diamantis proposes a hybrid baseline: an AI is negligent if it causes harm more often than the combined rate for all actors, human and machine, doing the same activity. The standard rises as AI improves. Dickinson, "Law Proofing the Future," *Harv. J. on Legis.* (2026) [V-page: https://arxiv.org/pdf/2603.10021], discusses it approvingly.
- **Overlap and difference:** This is the most structurally similar idea: reasonableness defined as a measured error rate against a population baseline. The book's "known error rate" and its 20%-versus-2–3% accuracy target rest on the same logic. Diamantis is about tort harm. The book applies the logic to price estimates and adds a *published, rerunnable* reference model plus a required record. Diamantis does neither.

#### 3. Karni A. Chagal-Feferkorn, "The Reasonable Algorithm," 2018 *U. Ill. J.L. Tech. & Pol'y* 111 (2018); and "How Can I Tell if My Algorithm Was Reasonable?," 27 *Mich. Tech. L. Rev.* 213–262 (2021). [V-page, both]
https://www.academia.edu/41219078/The_Reasonable_Algorithm ; https://repository.law.umich.edu/mtlr/vol27/iss2/2
- **Argument:** The 2018 article proposes a "reasonable algorithm" negligence standard for self-learning systems, modelled on the reasonable professional. It argues that treating algorithms as products creates anomalies such as unequal treatment of victims and distorted incentives between hiring humans and deploying algorithms. The 2021 article sets out how decision-makers would apply the test in practice.
- **Overlap and difference:** She makes the doctrinal case that "reasonableness" can attach to an algorithm's *decision*, which the book's "bot in the witness box" chapter needs. She stays inside tort and does not treat the reasonable algorithm as a *public reference instrument* for markets.

#### 4. Andrea Roth, "Machine Testimony," 126 *Yale Law Journal* (May 2017). [V-page]
https://www.yalelawjournal.org/article/machine-testimony
- **Argument:** Some machine outputs are credibility-dependent and should be treated as *testimony*. They carry "black box dangers" that parallel hearsay dangers: falsehood by design, inarticulateness and analytical error. Roth proposes safeguards: front-end design and operation protocols, pretrial disclosure including source code, reliability review under Daubert/Frye, impeachment, and corroboration. A recent follow-on is **proposed Federal Rule of Evidence 707** on machine-generated evidence. A revised draft was issued 16 Aug 2025, with comments open to 16 Feb 2026. It would require machine output offered without an expert to meet Rule 702(a)–(d) [V-page: https://btlaw.com/en/insights/alerts/2025/new-evidence-rule-707-would-set-standards-for-ai-generated-courtroom-evidence].
- **Overlap and difference:** This is the direct precedent for "the bot in the witness box." Roth's safeguards, such as protocols, disclosure and reliability testing, match the book's pinned open weights, public test set and required record. Roth is about criminal evidence. The book is about bid evaluation and price disputes, and it adds the Canadian Mohan / White Burgess line. FRE 707 is a live hook: the book's standard bot is effectively a design built to pass a 707/702 test.

#### 5. Chan Heo, Changbum R. Ahn & Moonseo Park, "Tacit Collusion by LLM Agents in Construction Bidding: Evidence from a Simulated Bidding Environment," *J. Management in Engineering* 42(2): 04025063 (2025/26). [V-page]
DOI 10.1061/JMENEA.MEENG-7144. A companion paper is Heo, Park & Ahn, "Large Language Models in Construction Bidding: Opportunities and Risks of Algorithmic Collusion," *Proc. 42nd ISARC* (2025), pp. 1332–1339 [V-page: https://www.iaarc.org/publications/fulltext/172_Large_Language_Models_in_Construction_Bidding__Opportunities_and_Risks_of_Algorithmic_Collusion.pdf].
- **Argument:** GPT-4o agents set markups over 150 rounds of a simulated lowest-bid construction market. They converged within 40–50 rounds. When the prompt framed higher bids as profitable, they sustained supra-competitive bids of about 1.04–1.06 times cost with no explicit coordination. Greater market transparency made tacit coordination easier.
- **Overlap and difference:** This is the closest *construction-specific* work on bots doing tendering. It directly challenges the book's optimism: published bid tabulations plus bidder bots could make collusion easier, not just remove the "ignorance rent." These are empirical papers, not a manifesto, and they do not address the buyer's side, a reasonable-price standard or legal liability. **The book should engage with this finding.**

#### 6. Arkestro Inc. (E.A. Zagorin, B.K. Leiken, E.D. Buras), US Patent 12,051,041 B2, "Procurement modeling system for predicting price reasonableness" (filed 28 Oct 2022; granted 30 Jul 2024). [V-page]
https://patents.google.com/patent/US12051041
- **Argument:** The patent claims a machine-learning method on a procurement platform. It takes line-item transaction data, predicts a "reasonable price quotation" for each supplier, and issues a recommendation for each. Arkestro sells this as "predictive procurement," and TechCrunch (14 Jun 2022) described it as game theory plus ML.
- **Overlap and difference:** This is the clearest prior commercial claim to *automating price reasonableness*, which is the book's estimator. It is proprietary and patented, built for indirect and commercial spend, with no published test set, no standard and no legal-evidence framing. The book's open, frozen, rerunnable standard is the opposite design choice. The patent is worth citing as the closed alternative.

#### 7. Bernardo Nicoletti, *Agentic AI for Procurement: Concepts, Applications and Implications* (Springer, 2026). [V-listing]
ISBN 9783032230232 (print), 9783032230249 (eBook). Chapter 12, "Agentic AI Supporting Procurement in Public Organizations," pp. 219–245, DOI 10.1007/978-3-032-23024-9_12 [V-page abstract].
- **Argument:** The book is a management text on agentic AI across the procurement cycle. The public-sector chapter proposes an architecture and functional framework covering dynamic supplier qualification, autonomous market research, "intelligent bid analysis" and contract management. It also discusses liability, explainability and regulatory adjustment.
- **Overlap and difference:** This is the nearest *book-length* treatment of bots in procurement, and it is very recent. It is a generic framework text, not construction-specific, and it does not take on how price reasonableness is known, the history of the measure-bid-price-book loop, or a reasonable-bot evidentiary standard.

#### 8. Albert Sanchez-Graells, *Digital Technologies and Public Procurement: Gatekeeping and Experimentation in Digital Public Governance* (Oxford University Press, 25 Jan 2024). [V-page]
DOI 10.1093/oso/9780198866770.001.0001; ISBN 9780198866770 (hb). https://academic.oup.com/book/55898
- **Argument:** This is the leading legal monograph on digitising public procurement, covering AI, blockchain and e-procurement. As far as I could check from the abstract and title, it treats procurement as a *gatekeeper* for public-sector AI adoption and argues for controlled experimentation. The author's blog *How to Crack a Nut* continues the work, with posts on AI in procurement through October 2026, such as "Competition implications of artificial intelligence in public procurement" (8 Jun 2026) and "AI's absence from the proposed EU Public Procurement Act" (5 Oct 2026).
- **Overlap and difference:** It is the authoritative scholarly treatment of "AI + public procurement," and essential context. It is European and law-centred, mostly about procuring AI *and* governing its use. It does not cover construction pricing or a reasonable-bot standard. Its sceptical, governance-first tone contrasts with the book's builder's manifesto.

#### 9. UK Cabinet Office, *The Construction Playbook: Government Guidance on Sourcing and Contracting Public Works Projects and Programmes*, v1.0 (Dec 2020); and Cabinet Office, *Should Cost Modelling Guidance Note* (May 2021). [V-page, both]
https://www.graham.co.uk/media/documents/The_Construction_Playbook.pdf (mirror) ; https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/987128/Should_Cost_Modelling_guidance_note_May_2021.pdf
- **Argument:** The Playbook requires a Should Cost Model, outcome-based specifications, the UK BIM Framework and the Information Management Framework. It also says standards and specifications should be "digitised so that requirements can be read by both people and machines." The SCM guidance makes the model the yardstick for bids: any bid more than 10% below the average of the other bids, or below the SCM's 50% confidence point, is referred as potentially abnormally low.
- **Overlap and difference:** This is the closest *government* precedent for two of the book's claims. One is that price reasonableness is judged against a modelled benchmark. The other is that construction requirements should be machine-readable. The SCM is a bespoke model built for each project, not a published, versioned standard bot. The Playbook's tone is policy, not manifesto, and bots, liability and evidence are absent.

#### 10. Ahmed Abdelaty (PI), "A Machine Learning and Statistical Analysis Framework for Enhanced Engineer's Estimate Accuracy in Highway Infrastructure Projects, Phase I," USDOT UTC Program / North Dakota State Univ. CTIPS / University of Wyoming (project start 7 Jun 2024; active to 2029). [V-page]
https://trid.trb.org/View/2398009
- **Argument:** The project uses WYDOT bid tabulation data and ML to reduce deviations between engineer's estimates and awards, which the 2019 data shows reached up to 25%.
- **Overlap and difference:** It is the same technical task as the book's estimator (bot versus engineer's estimate on DOT bid tabs, with a similar error band). It sits within a large ML-bid-prediction literature; other strands should mine it for accuracy benchmarks. It is narrowly technical and has none of the book's legal, procurement-design or historical argument.

#### 11. Don Scheibenreif & Mark Raskino, *When Machines Become Customers: Ready or Not, AI-Enabled Non-Human Customers Are Coming* (Gartner Inc., 2023; 3rd ed. updated with agentic-AI content). [V-listing]
https://www.gartner.com/en/publications/when-machines-become-customers ; Gartner press release, 16 Mar 2023.
- **Argument:** "Machine customers," meaning software and devices that buy on their owners' behalf, are a trillion-dollar growth market. Selling to them will be data-driven and largely automated.
- **Overlap and difference:** It is a book-length "bots are coming to buy" argument. It treats the *seller's* view in mostly B2C and B2B commerce, not public tendering, and it says nothing about fairness standards or legal accountability.

#### 12. Katharina Schumacher, Roger Roberts & Katharina Giebel, *The Agentic Commerce Opportunity: How AI Agents Are Ushering in a New Era for Consumers and Merchants* (McKinsey & Company / QuantumBlack, 17 Oct 2025). [V-page]
https://www.mckinsey.com/industries/retail/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants
- **Argument:** The report forecasts US$3–5 trillion in global agentic-commerce sales by 2030, of which US$0.9–1 trillion is US B2C. It names the emerging protocol layer: MCP, A2A, Google's AP2 (signed mandates as an audit trail) and OpenAI/Stripe's ACP.
- **Overlap and difference:** It supports the book's protocol thinking ("the tender is the API"). AP2's signed mandate is a close relative of the book's "required record" and human keyholder. The scope is retail and excludes B2B and public procurement.
- **Related analyst items:** Gartner, "Gartner Predicts Half of Procurement Contract Management Will Be AI-Enabled by 2027" (press release, 8 May 2024) [V-listing]. Gartner's prediction, reported by Digital Commerce 360 on 28 Nov 2025, that 90% of B2B buying will be AI-agent intermediated, with about US$15 trillion in spend, by 2028 [V-listing]. Bain & Company's agentic-procurement research (2025), which claims 60%+ productivity gains and 3–7% incremental savings, though I could find no confirmed report title, so the title is UNVERIFIED (claims as reported by *Procurement Magazine*).

#### 13. Nenad Tomasev, Matija Franklin, Joel Z. Leibo, Julian Jacobs, William A. Cunningham, Iason Gabriel & Simon Osindero, "Virtual Agent Economies," arXiv:2509.10147 (Google DeepMind, 12 Sep 2025). [V-page]
- **Argument:** The paper proposes a "sandbox economy" framework for markets of transacting AI agents and warns of systemic risk. It argues that agent markets should be *deliberately designed and steerable*, using auctions, "mission economies" and trust infrastructure.
- **Overlap and difference:** This is the most thorough research-lab statement that agent markets need designed protocols, which matches the book's protocol and standards push. It is abstract and economy-wide, with no construction, pricing standard or common law.

#### 14. Gagan Bansal et al. (incl. Brendan Lucier, Nicole Immorlica, Eric Horvitz, Saleema Amershi), "Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets," arXiv:2510.25779 (Microsoft Research, 27 Oct 2025). [V-page]
- **Argument:** The authors simulated LLM buyer and seller agents. Welfare approaches the optimum only when search conditions are ideal, degrades as the market scales, and shows a strong first-proposal bias: speed beats quality by roughly 10–30 times.
- **Overlap and difference:** This is empirical evidence about bots on *both* sides of a market, which the book assumes (bidder bot and buyer's "Listener" bot). The first-proposal bias is a caution for bot-first tendering. It is not about construction or law.

#### 15. E. William Youngdahl, Shail H. Patel, Megha R. Shah & Addison G. Sutton, *Pactum's AI in Contract Negotiations: Walmart and Maersk* (Harvard Business Publishing case TB0756, 17 Feb 2025). [V-page]
https://store.hbr.org/product/pactum-s-ai-in-contract-negotiations-walmart-and-maersk/TB0756
- **Argument:** The case covers Walmart's and Maersk's pilots of autonomous chatbot negotiation for long-tail supplier agreements, with efficiency and savings gains and tensions in supplier relationships.
- **Overlap and difference:** It is the canonical business-school case of bots negotiating supply contracts. It covers the commercial long tail, where the bot negotiates terms. In the book, bots price and evaluate sealed construction bids under public-law constraints.

#### 16. Sunayana Rane, "Position: The Reasonable Person Standard for AI," *Proc. 41st ICML*, PMLR 235: 42127–42137 (2024). [V-page]
https://proceedings.mlr.press/v235/rane24a.html ; arXiv:2406.04671
- **Argument:** AI alignment and evaluation should borrow the legal reasonable-person standard as the target behaviour developers build and stress-test against. Rane works through how reasonableness is defined across areas of law.
- **Overlap and difference:** It is a machine-learning-community version of "reasonable bot" as a *design and test target*, which is near the book's "standard = conformance test." It is generic and has no market, pricing or evidentiary use.

#### 17. Harry Surden, "Computable Contracts," 46 *UC Davis Law Review* 629 (2012). [V-listing]
https://lawreview.law.ucdavis.edu/archives/46/2/computable-contracts ; https://scholar.law.colorado.edu/articles/148/ (page number from memory)
- **Argument:** Contract terms can be written as data that computers can process, so a machine can determine aspects of performance and compliance. Surden distinguishes "data-oriented" contracts and maps which terms are amenable to computation.
- **Overlap and difference:** It is the theoretical foundation for "the tender is the API": tender and contract terms as canonical machine-readable data. It concerns performance monitoring, not price formation or tender evaluation.

#### 18. Lauren Henry Scholz, "Algorithmic Contracts," 20 *Stanford Technology Law Review* 128 (2017). [V-listing]
https://law.stanford.edu/publications/algorithmic-contracts/ (volume and page from memory)
- **Argument:** In "algorithmic contracts," an algorithm decides terms or whether to contract at all. Scholz argues these should be governed by agency law, so the algorithm's principal is bound much as a principal is by a human agent.
- **Overlap and difference:** It is directly relevant to the book's claim that liability shifts to the user's bot, and to the keyholder who answers for it. Scholz addresses formation and attribution, not price fairness or evidence.

#### 19. Samir Chopra & Laurence F. White, *A Legal Theory for Autonomous Artificial Agents* (University of Michigan Press, 2011). [V-page]
ISBN 9780472051458; DOI 10.3998/mpub.356801.
- **Argument:** Existing legal theory can accommodate sophisticated AI agents through agency law, attribution of knowledge and responsibility, and, eventually, legal personhood.
- **Overlap and difference:** It is the founding book-length treatment of software agents contracting on behalf of principals. It is pre-LLM and does not cover procurement or price reasonableness.

#### 20. OECD Observatory of Public Sector Innovation (J. Mohun & A. Roberts; page credits J. Berryhill), *Cracking the Code: Rulemaking for Humans and Machines* (OECD Working Papers on Public Governance No. 42, 12 Oct 2020). [V-page; author and series details partly from memory]
https://oecd-opsi.org/publications/cracking-the-code/
- **Argument:** This is the "Rules as Code" primer. Governments should draft machine-readable versions of rules alongside the natural-language text, guided by transparency, traceability, appealability and versioning.
- **Overlap and difference:** It is the governance precedent for "canonical, versioned, machine-readable tender data" and for a versioned standard. It covers legislation and benefits rules, not tenders. Canada is named as an experimenting jurisdiction, which gives the book a Canadian hook.

#### 21. Open Contracting Partnership, *Open Contracting Data Standard* (OCDS; first data-model release 27 Jun 2014); and OCP with CoST – Infrastructure Transparency Initiative, *Open Contracting for Infrastructure Data Standard* (OC4IDS; launched 17 Apr 2019). [V-page]
https://www.open-contracting.org/2014/06/27/first-release/ ; https://www.open-contracting.org/2019/04/17/the-oc4ids-a-new-standard-for-infrastructure-transparency/
- **Argument:** These are machine-readable JSON schemas for publishing the full procurement lifecycle (planning, tender, award, contract, implementation). OC4IDS extends this to infrastructure projects, including contract variations and their justifications. Ukraine's ProZorro / OpenProcurement API is the leading implementation [V-listing: https://prozorro-api-docs.readthedocs.io/en/master/standard/tender.html].
- **Overlap and difference:** These are the closest *existing* standards for "the tender is the API." They aim at transparency and anti-corruption (publishing *about* tenders), not at making the tender package itself executable or at pricing. The book's claim goes further: the drawings, quantities and addenda themselves become the versioned API.

#### 22. Law Commission of England and Wales, *Smart Legal Contracts: Advice to Government* (Law Com No. 401, 25 Nov 2021). [V-page; report number from memory]
https://www.lawcom.gov.uk/project/smart
- **Argument:** Existing common law can accommodate smart legal contracts without statutory reform. Common-law principles carry over, with targeted work needed on deeds and private international law.
- **Overlap and difference:** It supports the book's common-law-flexibility stance, the same move as the reasonable person adapting to bots. It is not about procurement or pricing.

#### 23. Kevin Werbach & Nicolas Cornell, "Contracts Ex Machina," 67 *Duke Law Journal* 313 (2017); and Kevin Werbach, *The Blockchain and the New Architecture of Trust* (MIT Press, 2018). [V-listing]
https://dlj.law.duke.edu/article/contracts-ex-machina ; ISBN 9780262038935 (hb) / 9780262547161 (pb) (volume and page from memory)
- **Argument:** Smart contracts are functionally contracts but cannot replace contract law, because law handles the remedial and interpretive work that code cannot. The book recasts trust as an architecture.
- **Overlap and difference:** It is a counterweight to "code is law" maximalism, consistent with the book's insistence on a human keyholder and a record. It does not cover construction or pricing.

#### 24. Abel Maciel, Daniel M. Hall & Mohamad Kassem (eds.), *Blockchain, Smart Contracts and Distributed Ledger Technologies in the Built Environment* (Institution of Engineering and Technology, 2025). [V-page]
ISBN 9781839538346. Companion book: Abel Maciel, *Understanding Blockchain in Construction: A Practical Guide* (Routledge, Understanding Construction series, 2025), ISBN 9781032847849 [V-listing].
- **Argument:** An edited survey of DLT in construction: smart contracts for contract administration, BIM and digital-twin integration, tokenisation, supply chain, legal risks and adoption barriers.
- **Overlap and difference:** It is the current state of the "blockchain in construction" literature, which promised machine-executable construction contracts. That literature centres on payments and records after award. It rarely touches tender pricing or reasonableness, and it lacks AI estimators and a legal standard of care.

#### 25. James Mason, *Innovating Construction Law: Towards the Digital Age* (Routledge, 2021). [V-page]
ISBN 9780367443498.
- **Argument:** Construction legal practice should engage with smart contracts, blockchain, AI, big data and BIM through a transparency and traceability agenda. Mason organises the book as "AS IS → TO BE" steps that work within existing law.
- **Overlap and difference:** It is the nearest *construction-law book* to the book's legal chapters, written by a construction law academic in a reformist register. It is broad and speculative across technologies. It does not centre price reasonableness or propose a reasonable-bot standard.

### B. Next tier: technical, legal and economic works the book builds on

#### 26. Jennifer Li, David Greenwood & Mohamad Kassem, "Blockchain in the Built Environment and Construction Industry: A Systematic Review, Conceptual Models and Practical Use Cases," *Automation in Construction* 102 (2019) 288–307. [V-listing; volume and pages from memory]
https://researchportal.northumbria.ac.uk/en/publications/blockchain-in-the-built-environment-and-construction-industry-a-s/
- **Argument:** A systematic review and set of use-case models for DLT in the built environment.
- **Overlap and difference:** It is the foundational academic review of construction smart contracts. It covers the post-award ledger and has nothing on bid evaluation.

#### 27. Hesam Hamledari & Martin Fischer, "Construction Payment Automation Using Blockchain-Enabled Smart Contracts and Reality Capture Technologies," *Automation in Construction* (2021); arXiv:2010.15232. [V-listing; journal volume from memory: 132, 103926]
- **Argument:** Stanford CIFE work that triggers progress payments automatically from drone and robot reality capture of installed work, through smart contracts.
- **Overlap and difference:** This is a working "machine reads the record and pays" system, the post-award twin of the book's pre-award bot. It does not address price fairness.

#### 28. Ariel Ezrachi & Maurice E. Stucke, *Virtual Competition: The Promise and Perils of the Algorithm-Driven Economy* (Harvard University Press, 2016). [V-listing]
ISBN 9780674545472; DOI 10.4159/9780674973336.
- **Argument:** Pricing algorithms can produce tacit collusion ("the Predictable Agent," "Digital Eye" scenarios) and behavioural discrimination. More transparency can harm buyers.
- **Overlap and difference:** It is the theoretical root of the risk Heo et al. found in construction (#5). The book's Scitovsky claim, that bots remove the ignorance rent, needs to answer this.

#### 29. Martin Huber & David Imhof, "Machine Learning with Screens for Detecting Bid-Rigging Cartels," *International Journal of Industrial Organization* 65 (2019) 277–301. [V-listing]
https://ideas.repec.org/a/eee/indorg/v65y2019icp277-301.html
- **Argument:** Statistical screens on bid distributions (variance, skewness, gaps), combined with ML, detect bid-rigging in Swiss road-construction tenders with high accuracy.
- **Overlap and difference:** It shows that public bid tabulations, the book's training data, already serve as a machine-read integrity check. The book can use this as a precedent for the buyer's bot.

#### 30. Joshua A. Kroll, Joanna Huey, Solon Barocas, Edward W. Felten, Joel R. Reidenberg, David G. Robinson & Harlan Yu, "Accountable Algorithms," 165 *University of Pennsylvania Law Review* 633 (2017). [V-listing]
https://scholarship.law.upenn.edu/penn_law_review/vol165/iss3/3
- **Argument:** Accountability for automated decisions comes from procedural regularity: commitments, verifiable computation and published specifications, more than from transparency of source code alone.
- **Overlap and difference:** It provides the technical-legal rationale for a *frozen, published, rerunnable* standard bot with a record. It does not cover procurement.

#### 31. Daniel Martin Katz, Ron Dolin & Michael J. Bommarito (eds.), *Legal Informatics* (Cambridge University Press, 2021). [V-page]
ISBN 9781107142725.
- **Argument:** A foundational overview of legal informatics: NLP, DLT, contracting, case prediction and online dispute resolution.
- **Overlap and difference:** It is the field reference for "law as data." It has no procurement-pricing focus.

#### 32. Lawrence Lessig, *Code and Other Laws of Cyberspace* (Basic Books, 1999; *Code: Version 2.0*, 2006). [V-listing]
- **Argument:** Software architecture regulates behaviour alongside law, norms and markets: "code is law."
- **Overlap and difference:** It is the intellectual ancestor of "the tender is the API" and of procurement protocols as regulation. The book applies the idea to a specific market institution.

#### 33. Nick Szabo, "Formalizing and Securing Relationships on Public Networks," *First Monday* 2(9) (1 Sep 1997). [V-listing]
https://www.firstmonday.org/ojs/index.php/fm/article/view/548/0
- **Argument:** This is the origin of "smart contracts": embedding contractual clauses in hardware and software to make breach costly.
- **Overlap and difference:** It is the historical anchor for one of the book's "Procurement Machines" cards. Its idea is enforcement, where the book's is pricing.

#### 34. Steven Kelman, *Procurement and Public Management: The Fear of Discretion and the Quality of Government Performance* (AEI Press, 1990). [V-listing]
ISBN 0844737127.
- **Argument:** Rigid, rule-bound procurement, which exists to prevent corruption and favouritism, degrades value. Officials should be given more discretion and use past performance. Kelman went on to lead the 1990s US federal procurement reforms as OFPP Administrator.
- **Overlap and difference:** It is the classic US statement of the rules-versus-discretion tension that the book reframes as "tensions to manage." The book's bot offers a third route: discretion exercised through an auditable standard.

### C. Construction-industry manifestos and reports (genre precedents)

#### 35. Mark Farmer, *The Farmer Review of the UK Construction Labour Model: Modernise or Die* (Construction Leadership Council, Oct 2016). [V-listing]
https://www.gov.uk/government/publications/construction-labour-market-in-the-uk-farmer-review
- **Argument:** UK construction faces structural decline, with an ageing workforce, low productivity and a fragmented, adversarial and low-margin structure. It must industrialise (pre-manufacture) and reform its client and procurement behaviour.
- **Overlap and difference:** It is the closest *in tone*: a practitioner's "change or die" polemic. It is about labour and manufacturing. Tendering appears only as a symptom, and there is nothing on pricing standards or AI.

#### 36. Sir Michael Latham, *Constructing the Team: Final Report of the Government/Industry Review of Procurement and Contractual Arrangements in the UK Construction Industry* (HMSO, 1994); Sir John Egan, *Rethinking Construction: Report of the Construction Task Force* (DETR, 1998). [V-listing via Constructing Excellence; publishers from memory]
https://constructingexcellence.org.uk/key-industry-publications/
- **Argument:** Latham focused on adversarial procurement and contracts and called for partnering, fair payment and standard contracts like the NEC. He targeted a 30% real cost reduction. Egan imported lean manufacturing, partnering the supply chain and performance targets. Later reviews, such as Wolstenholme, *Never Waste a Good Crisis* (Constructing Excellence, 2009), found "public sector procurement rules" a key barrier.
- **Overlap and difference:** These are canonical precedents for the book's diagnosis that lowest-price tendering "starts a relationship expecting a divorce." Their remedy was relational (partnering). The book's remedy is informational (bots, data, a standard), which is a distinct thesis.

#### 37. Stephen Kieran & James Timberlake, *Refabricating Architecture: How Manufacturing Methodologies Are Poised to Transform Building Construction* (McGraw-Hill, 2004). [V-listing]
ISBN 9780071433211.
- **Argument:** Architects should adopt automotive, aerospace and shipbuilding methods, such as integrated design teams, off-site modules and digital design-to-fabrication, to collapse the design-to-build gap.
- **Overlap and difference:** It is a practitioner manifesto of the same length and tone that borrows another industry's paradigm. Kieran and Timberlake borrow from manufacturing. The book borrows from software (APIs, compile, versioning).

#### 38. Anil Sawhney, Michael Riley & Javier Irizarry (eds.), *Construction 4.0: An Innovation Platform for the Built Environment* (Routledge, 2020). [V-listing]
ISBN 9780367027308.
- **Argument:** An edited framework for applying Industry 4.0 to construction: cyber-physical systems, BIM, digital twins, AI and blockchain.
- **Overlap and difference:** It is the academic "digital construction" overview. It covers technology platforms, not procurement or price reasonableness.

### D. Adjacent thinking the book draws on or should answer

#### 39. Bent Flyvbjerg & Dan Gardner, *How Big Things Get Done* (Currency/Penguin Random House, 2023). [V-listing; publisher from memory]
- **Argument:** Reference-class forecasting, which predicts a project's cost from the distribution of comparable past outcomes, corrects the planning fallacy in megaprojects.
- **Overlap and difference:** It is conceptually close to the book's loop of "opened bids become next year's price book." Reference-class forecasting is a statistical standard of reasonableness for *budgets*. The book makes the same move for unit prices with a bot.

#### 40. Daniel Kahneman, Olivier Sibony & Cass R. Sunstein, *Noise: A Flaw in Human Judgment* (Little, Brown Spark, 2021). [V-listing]
- **Argument:** Unwanted variability between human judges is as costly as bias, and algorithms and rules reduce noise.
- **Overlap and difference:** It frames the case for a *standard* bot over many individual estimators. The book's 20% versus 2–3% accuracy gap is effectively a noise argument.

#### 41. Steve Yegge, "Stevey's Google Platforms Rant" (Google+ post, accidentally public, 12 Oct 2011). [V-listing]
https://courses.cs.washington.edu/courses/cse452/22wi/papers/yegge-platform-rant.html
- **Argument:** It describes Jeff Bezos's c. 2002 mandate that every Amazon team expose its data and functionality only through service interfaces.
- **Overlap and difference:** It is the primary source for the book's "Amazon API mandate applied to designer and builder." It should be cited directly, with a note that the mandate is known only through Yegge's second-hand account.

#### 42. Venkatesh Rao et al., *Summer of Protocols* program and *The Protocol Reader* (Ethereum Foundation / Protocolized, 2023–24). [V-listing]
https://summerofprotocols.com/wp-content/uploads/2024/11/Introduction-to-the-Protocol-Reader-Venkatesh-Rao.pdf
- **Argument:** Protocols are an under-theorised layer of civilisation's "world machines." The essays study how protocols coordinate strangers at scale.
- **Overlap and difference:** It is already a known influence on the book. The book is, in effect, a protocol proposal for construction pricing.

#### 43. ISO 10845-1:2020, *Construction procurement — Part 1: Processes, methods and procedures* (ISO, 2020; first ed. 2010; Parts 2–8 cover formatting, standard conditions of tender and contract, and participation targets). [V-listing]
https://www.iso.org/standard/72467.html
- **Argument:** An international standard (South African origin) for fair, equitable, transparent, competitive and cost-effective construction procurement processes.
- **Overlap and difference:** It is the book's chosen alignment target. It standardises *process* and *documents*, not price reasonableness or machine-readable tender data, which is a gap the book's protocol could fill.

---

### E. Searched but not found or not verifiable (do not cite as-is)

- Any book or essay titled or framed as "bot procurement," "bot-first tender" or "the reasonable bot": **none found**.
- An academic paper that specifically automates **FAR 15.404 price analysis**: none found beyond the Arkestro patent (#6) and vendor white papers such as XSB, "Improving Acquisition of Commercial Items: Automated Price Evaluation Methods Ensure Good Value" (https://xsb.com/resource/improving-acquisition-of-commercial-items-automated-price-evaluation-methods-ensure-good-value/). That is a vendor resource and I did not open it, so it is UNVERIFIED as to author and date.
- Canadian price-reasonableness guidance (PSPC Supply Manual, Defence Construction Canada): **not searched**, because the budget was exhausted. A separate strand should cover it.
- McKinsey Global Institute, *Reinventing Construction: A Route to Higher Productivity* (Barbosa et al., Feb 2017): almost certainly exists and is relevant to the genre, but it is **UNVERIFIED in this session**.
- Bain & Company agentic-procurement report title: **UNVERIFIED**. Only claims second-hand via *Procurement Magazine*.

---

### What gap does this book fill?

The search turned up five separate literatures that each cover part of the book's ground, and none joins them.

1. **Legal theory of the reasonable machine** (Abbott; Chagal-Feferkorn; Diamantis; Rane). It extends the reasonable person to AI, but only as a tort rule for harm a machine causes.
2. **Machine evidence** (Roth; proposed FRE 707). It asks when a machine output can be trusted in court, but treats each machine as a one-off exhibit.
3. **Agentic commerce and procurement** (Gartner, McKinsey, Nicoletti, Pactum, Arkestro, DeepMind, Microsoft). It assumes bots will buy and sell, but is commercial, generic and mostly proprietary, and it does not ask how anyone *knows* a price is fair.
4. **Machine-readable contracting and procurement data** (Surden, Rules as Code, OCDS/OC4IDS, the Construction Playbook, blockchain-in-construction). It makes contracts and records computable, but mostly for transparency or post-award payment, not for pricing.
5. **Construction reform manifestos** (Latham, Egan, Farmer, Kieran Timberlake). They diagnose adversarial lowest-price tendering, but prescribe relational or manufacturing fixes, not informational ones.

The book is the only work found that puts the old administrative question "is this price fair and reasonable?" at the centre. It proposes to answer that question with a **public, frozen, rerunnable reference bot**: a *standard*, not a product, with a known error rate. It ties that bot to common-law evidentiary tests (Daubert, Mohan, White Burgess) and to a human keyholder who signs for the number. It also grounds the argument in a practitioner's account of two centuries of the measure–bid–price-book loop, with a concrete build-in-public protocol (Texas DOT and Alberta data, one trade, ISO 10845). The nearest neighbours are Abbott for the legal concept, the Arkestro patent and the Should Cost Model for the function, and Heo et al. for construction bots. Each covers one leg, and the closed-source Arkestro approach is the opposite design.

The book's distinctive contribution is to move reasonableness from a liability rule to a **shared measuring instrument**. It should also engage with the strongest counter-evidence found: LLM bidders colluding tacitly in transparent construction markets (Heo et al.; Ezrachi & Stucke).

---

## Part 3. Popular explainers of procurement
*Literature review strand for* Fair and Reasonable / The Reasonable Bot *(Andre Comeau, Nov 2026).*

**Method and limits.** Web search and page fetches, 1 Nov 2026. Partway through, the session hit both shared limits: the WebFetch budget (100 per hour) and the WebSearch budget (200 per turn). So:

- **Verified** means a catalogue record, publisher page, Publishers Weekly or Kirkus listing, or the source itself confirmed the details this session.
- **Not re-verified** means a well-known work whose details come from memory and were not confirmed this session. Check them before citing.
- **UNVERIFIED** marks a specific claim that could not be confirmed.

Planet Money episodes, Matt Yglesias / Slow Boring pieces beyond one URL, IFP or Niskanen essays specifically on procurement, and Works in Progress essays could **not** be searched properly before the budget ran out. See "Gaps in this search" at the end.

---

### A. Procurement and government contracting for general readers

#### 1. Steven Kelman, *Procurement and Public Management: The Fear of Discretion and the Quality of Government Performance* (1990)
Washington, DC: AEI Press, 213 pp., ISBN 0-8447-3712-7. Verified via the review listing in *Journal of Public Policy* (Cambridge).
**What it explains.** Kelman argues that US federal computer procurement is ruled by a "fear of discretion." Rules meant to stop favouritism stop officials from using judgement about past performance and quality, and that makes government worse. It is written for a policy audience rather than a trade audience, but it is readable and argued. Kelman later ran federal procurement policy (OFPP, 1993–97) and drove the 1990s reforms.
**What the book can borrow / how it differs.** It is the classic statement of the book's tension: discretion versus defensibility. Kelman wants buyers trusted to judge. Comeau's "reasonable bot" is a third route: discretion exercised through a published, rerunnable standard, so judgement becomes auditable rather than forbidden. Kelman is about IT and federal rules; Comeau is about construction prices and about tools.

#### 2. Sydney J. Freedberg Jr., "The myth of the $600 hammer," *Government Executive*, 7 Dec 1998
URL: https://www.govexec.com/federal-news/1998/12/the-myth-of-the-600-hammer/5271/ (verified).
**What it explains.** It debunks the 1980s scandal icon. The hammer cost about $15. It was part of a bulk spare-parts order in which the contractor spread engineering and support overhead evenly across every line item, about $420 each. That produced a $435 "price" that the press rounded up to $600. Kelman is quoted: "There never was a $600 hammer… an accounting artifact… The hammer got as much overhead as an engine." Short, journalistic, for a general audience.
**What the book can borrow / how it differs.** This is a ready-made parable for the spine question. A price that looks absurd can be fair and reasonable in total, and a fair total can hide absurd line items. Unit prices in bid tabulations carry the same allocation games (front-loading, unbalanced bids). The book can use it to show why a bot judging line-item reasonableness needs to see the whole bid. (A related Harper's item, "How to charge $436 for a $7 hammer," Oct 1984, is paywalled; contents not seen.)

#### 3. Dina Rasor, *The Pentagon Underground* (1985)
ISBN 978-0-8129-1249-4. Publishers Weekly gives the publisher as Crown, but the 0-8129 prefix is usually Times Books, so the **imprint is UNVERIFIED**. Rasor founded the Project on Military Procurement, which publicised the $640 toilet seat and $7,600 coffee maker. *The Nation* (W. D. Hartung, 11 Apr 2016) credits her.
**What it explains.** An activist-insider account built on Pentagon whistleblower leaks. It covers collusion between services and contractors, and the cost and quality of the M-1 tank, C-5 and cruise missile. Its register is outrage journalism for general readers.
**What the book can borrow / how it differs.** This is the "$600 toilet seat" genre. It shows how strongly a single absurd unit price works on readers, and how little the genre explains about how prices are actually set. Comeau's book is the opposite move: explaining the machinery rather than exposing a villain.

#### 4. A. Ernest Fitzgerald, *The High Priests of Waste* (1972) and *The Pentagonists: An Insider's View of Waste, Mismanagement, and Fraud in Defense Spending* (1989)
*The Pentagonists*: Houghton Mifflin, ISBN 978-0-395-36245-7 (verified via PW). *High Priests*: 1972 confirmed by Wikipedia; publisher (W. W. Norton, from memory) **UNVERIFIED**.
**What it explains.** Fitzgerald was the Air Force cost analyst fired for telling Congress about the C-5A overrun (1968). He explains "should-cost" analysis, the idea of estimating what an item *should* cost from efficient production rather than accepting what it *did* cost. These are memoir-polemics for general readers.
**What the book can borrow / how it differs.** "Should-cost" is the defence-world ancestor of the engineer's estimate and of the Fair and Reasonable Evaluator. Fitzgerald is a strong human precedent for "the keyholder who answers for the number." He paid for it professionally, which is worth a line.

#### 5. James G. Burton, *The Pentagon Wars: Reformers Challenge the Old Guard* (1993)
Annapolis: Naval Institute Press, ISBN 978-1-55750-081-6 (PW), reissued as 978-1-61251-600-4. It was adapted as the HBO comedy *The Pentagon Wars* (1998).
**What it explains.** A retired Air Force colonel's account of fighting to get honest live-fire testing of the Bradley Fighting Vehicle. The film turned it into satire: the Bradley's requirements drifting from troop carrier to scout to "mini-tank."
**What the book can borrow / how it differs.** It is about **testing as truth-telling**: who defines the test, and whether the test is rigged. That maps directly onto the book's "standard = conformance test" and its published, rerunnable test set. The film's requirements-creep montage is a well-known cultural reference for "design locked for tender and then not."

#### 6. Norman R. Augustine, *Augustine's Laws* (first ed. 1983; expanded eds. later)
Wikipedia cites a 1984 edition, ISBN 978-1-56347-240-4 (an AIAA ISBN). First publication by AIAA in 1983 and a Viking trade edition in 1986 are from memory: **UNVERIFIED**. CSIS published "Updating Augustine's Law: Fighter Aircraft Cost Growth in the Age of AI and Autonomy," which confirms the law is still cited.
**What it explains.** A defence-industry CEO wrote 52 tongue-in-cheek "laws" of aerospace procurement and cost growth, with charts. The most famous is Law XVI: "In the year 2054, the entire defense budget will purchase just one tactical aircraft." Unit costs grow exponentially while budgets grow linearly.
**What the book can borrow / how it differs.** It is the closest existing **playful, illustrative, short-form** work on procurement cost: aphorism plus chart plus anecdote. It is a direct model for the book's register and for the "Procurement Machines" cards. It is about defence and has no theory of fair price. Comeau supplies that theory.

#### 7. C. Northcote Parkinson, *Parkinson's Law, and Other Studies in Administration* (1957/58)
The Law of Triviality is confirmed via Wikipedia. Publisher and edition details (Houghton Mifflin, Boston, 1957; John Murray, London, 1958) are from memory: **not re-verified**.
**What it explains.** Satirical essays on bureaucracy. The chapter behind the "law of triviality" or "bikeshedding" shows a finance committee approving a £10 million atomic reactor in minutes and then debating a £350 bicycle shed at length, because everyone feels able to judge the shed's price.
**What the book can borrow / how it differs.** It belongs in the playful, illustrative tradition, and it is literally about **approving expenditure**. Reviewers judge reasonableness where they feel competent. The book's argument is that a reasonable bot widens what reviewers feel able to judge.

#### 8. Jennifer Pahlka, *Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better* (2023)
New York: Metropolitan Books, June 2023, 336 pp., ISBN 978-1-250-26677-4. Paperback is ISBN 978-1-250-34273-7. Verified via Publishers Weekly.
**What it explains.** By the founder of Code for America and former US Deputy CTO. It explains why government technology fails: policy is handed down as rigid requirements, and the system runs on waterfall, outsourcing and compliance culture. It argues for in-house product capability and treating citizens as users. It is narrative, story-led and aimed at a general audience. The PW review notes it opposes outsourcing system-building to vendors and favours in-house digital roles. Detailed procurement chapter content was not seen this session.
**What the book can borrow / how it differs.** It is the strongest kin to claim 2, "the tender is the API." Its waterfall-versus-agile framing is the software twin of "one-shotted design locked for tender." It is US federal IT. The book applies the same diagnosis to **construction**, which is much more waterfall by necessity, and adds the pricing question Pahlka does not address.

#### 9. Nicholas Bagley, "The Procedure Fetish," *Michigan Law Review* 118(3) (2019), and essay version at the Niskanen Center
https://www.niskanencenter.org/the-procedure-fetish/ (verified). Law review at https://repository.law.umich.edu/mlr/vol118/iss3/2.
**What it explains.** A law professor argues that progressive faith in procedure (notice and comment, review, consultation) has hobbled the state's ability to act, and that procedure is not neutral. The Niskanen version is an accessible long-form essay.
**What the book can borrow / how it differs.** It gives the book language for why tendering rules accumulate: each one guards against a past scandal. It also supports claim 5, "the record matters more than the duty." Comeau proposes replacing some procedure with a *record* produced by a standard tool, a constructive answer that Bagley does not attempt.

#### 10. Mariana Mazzucato & Rosie Collington, *The Big Con: How the Consulting Industry Weakens our Businesses, Infantilizes our Governments and Warps our Economies* (2023)
London: Allen Lane, ISBN 978-0-241-57308-2 (verified via penguin.com.au); New York: Penguin Press, ISBN 978-0-593-49267-3.
**What it explains.** It argues that governments' dependence on consultancies hollows out state capacity and in-house knowledge, using cases such as UK Covid procurement. It is a polemic for general readers.
**What the book can borrow / how it differs.** It parallels the Transit Costs Project finding (entry 23) that weak in-house owner capacity drives cost. A published standard bot is partly a way to give a thin public owner back estimating capacity without hiring consultants. The book should note that a bot can also become "the consultant" in Mazzucato's sense, which is a risk to address.

#### 11. Mariana Mazzucato, *The Value of Everything: Making and Taking in the Global Economy* (2018)
Allen Lane, 2018. Details **not re-verified**.
**What it explains.** It traces the history of theories of value, from classical labour theory to marginal utility, and argues that "price = value" lets extractive activity pass as productive.
**What the book can borrow / how it differs.** It gives background on why "fair price" is a philosophically loaded phrase (just price, labour theory, marginalism). The book takes a narrow, operational view of value: fair = within tolerance of a published standard's prediction. It can cite Mazzucato in one sentence to show it knows the deeper debate.

---

### B. Auctions and market design for general readers

#### 12. Paul Milgrom, *Discovering Prices: Auction Design in Markets with Complex Constraints* (2017)
New York: Columbia University Press (Kenneth J. Arrow Lecture Series), ISBN 978-0-231-17599-9 (verified).
**What it explains.** A Nobel laureate explains the FCC incentive auction and auctions where bids interact through constraints, covering approximate optimisation and "descending clock" designs. It is short, but it is lecture-level economics and **not** truly popular.
**What the book can borrow / how it differs.** Its title phrase, prices are *discovered* rather than known, is the economist's answer to "how do you know a price is fair?" You run a good mechanism. Comeau's answer is complementary: in construction, the sealed-bid mechanism discovers prices *and* writes next year's price book. The bot learns from that loop.

#### 13. Alvin E. Roth, *Who Gets What — and Why: The New Economics of Matchmaking and Market Design* (2015)
Boston: Houghton Mifflin Harcourt (confirmed via multiple library catalogues; ISBN not confirmed this session).
**What it explains.** A Nobel laureate's genuinely popular explainer of market design: kidney exchange, the medical residency match and school choice. It uses the ideas of "thick" markets, congestion and safe participation, and how "repugnant" transactions are handled.
**What the book can borrow / how it differs.** It is the register model: a laureate explaining mechanism design through stories, almost without equations. Roth's frame (markets are designed and need rules to be safe and thick) suits tendering, which is a designed market. Roth barely touches procurement. The book can claim the "market design for public works" space.

#### 14. Nobel Prize outreach on the 2020 Economic Sciences Prize (Milgrom & Wilson, "for improvements to auction theory and inventions of new auction formats")
Nobel Prize Lessons page and slideshow: https://www.nobelprize.org/nobel-prize-lessons-economic-sciences-2020 and https://nobelprize.org/uploads/2020/10/Slideshow_EconomicSciences_2020_Nobelprizelessons.pdf (verified). The page links to a "popular information" document, but its title and URL were not captured, so they are **UNVERIFIED**.
**What it explains.** A 45-minute school lesson explaining auctions and the winner's curse, with illustrations by Johan Jarnestad (Royal Swedish Academy of Sciences). It is aimed at teenagers.
**What the book can borrow / how it differs.** It proves that auction theory can be illustrated for teenagers. Jarnestad's diagram style is a model for the book's cards. The Nobel framing centres on *selling* (spectrum, bonds). The book turns the lens on *buying*: reverse auctions where the low bidder wins.

#### 15. Timothy P. Hubbard & Harry J. Paarsch, *Auctions* (2016)
Cambridge, MA: MIT Press Essential Knowledge series, ISBN 978-0-262-52853-5 (verified). Its chapter 5 is titled **"Procurement"** (verified via library table of contents). The other chapters cover formats, modelling, bidder behaviour, internet, multi-unit and online ad auctions.
**What it explains.** A pocket-sized, non-technical survey. The Hot Bid (2019) review calls it "a bit dry" for casual readers.
**What the book can borrow / how it differs.** It is the closest **short-book precedent** that explicitly covers procurement auctions. It matches the book's size and the "Essential Knowledge" format. It is an even-handed survey without a thesis, whereas the book is a manifesto.

#### 16. Paul Klemperer, *Auctions: Theory and Practice* (2004) and "What Really Matters in Auction Design" (*Journal of Economic Perspectives* 2002)
Princeton University Press, 2004. Author's free PDF: https://www.nuffield.ox.ac.uk/economics/papers/2004/w9/AuctionsTheoryPractice.pdf (verified). The JEP paper is CEPR DP2581. Also relevant: Ken Binmore & Paul Klemperer, "The Biggest Auction Ever: the Sale of the British 3G Telecom Licences" (CEPR DP3214; *Economic Journal* 2002, journal details **not re-verified**).
**What it explains.** It is semi-technical. The JEP paper is accessible and argues that collusion, entry deterrence and "what matters in practice" beat elegant theory, with vivid failures from the European 3G auctions.
**What the book can borrow / how it differs.** It supports claim 1 (manage tensions, don't solve them). Practical tender design is about entry and collusion, not optimal formulas. It also gives the theory behind bid-rigging screens, which public bid tabulations, the book's data, are used for.

#### 17. Tim Harford, *The Undercover Economist* (2005/2006) and *Fifty Things That Made the Modern Economy* (2017)
*Undercover Economist*: London, Little, Brown, 3 Nov 2005; US edition, Oxford University Press, ISBN 0-19-518977-9 (Wikipedia). *Fifty Things*: Little, Brown (UK) / Riverhead (US, as *Fifty Inventions That Shaped the Modern Economy*), 2017.
**What it explains.** *Undercover Economist* is the archetypal popular economics book. It covers scarcity rents, price targeting, information and auctions, and includes Harford's account of the UK 3G spectrum auction designed by Binmore and Klemperer. **Which chapter covers the 3G auction is UNVERIFIED.** The chapters are: "Who pays for your coffee?", "What supermarkets don't want you to know", "Perfect markets and the 'world of truth'", "Cross-Town Traffic", "The inside story", "Rational insanity", "The men who knew the value of nothing", "Why poor countries are poor", "Beer, Fries and Globalization", "How China grew rich". *Fifty Things* has **no auction chapter**; per Wikipedia, "Auctions" is BBC radio series 2, episode 47. It does have chapters on Double-Entry Bookkeeping, Management Consulting, the Shipping Container, the Barcode and Property Registers, which are all procurement-adjacent "machines."
**What the book can borrow / how it differs.** *Fifty Things*' format, one object or institution per short chapter, told as history, is almost exactly the "20 Procurement Machines" device. It is the best register model in this list. *Undercover Economist*'s "scarcity power" and "ignorance" pricing chapters overlap with Scitovsky's ignorance rent (claim 9). Harford never treats procurement itself as a subject.

#### 18. Richard H. Thaler, *The Winner's Curse: Paradoxes and Anomalies of Economic Life* (1992)
New York: Free Press (WorldCat OCLC 28377102). It collects his *Journal of Economic Perspectives* "Anomalies" columns. The winner's curse column is JEP 1988, PDF via stafforini.com.
**What it explains.** An accessible collection. The title essay explains why, in common-value auctions, the winner tends to be the bidder who most *over*-estimated value. It tells the origin story of Atlantic Richfield engineers (Capen, Clapp & Campbell, 1971) studying offshore oil-lease bids.
**What the book can borrow / how it differs.** It is essential. In a low-bid construction tender the mirror effect applies: the winner tends to be the bidder who most *under*-estimated cost, or missed a drawing error. That is the economic root of "bidders price errors and claim later" and of "starting a relationship expecting a divorce." The book can explain construction's adversarial culture as a structural winner's curse and argue that a shared standard bot narrows the estimate dispersion that creates it.

---

### C. Price, value and pricing for general readers

#### 19. William Poundstone, *Priceless: The Myth of Fair Value (and How to Take Advantage of It)* (2010)
New York: Hill and Wang, ISBN 978-0-8090-9469-1 (PW).
**What it explains.** A science writer tours the psychology of price: anchoring, coherent arbitrariness, Kahneman and Tversky, Ariely, menu design and negotiation. Its thesis is that people have no stable internal sense of what anything is worth.
**What the book can borrow / how it differs.** The subtitle is almost a counter-title to *Fair and Reasonable*. Poundstone says "fair value" is a myth exploited by anchors. Comeau can concede the point for consumers and argue that public construction bridges it institutionally: the engineer's estimate and price books *are* anchors, and the reform is to make the anchor explicit, published and tested.

#### 20. Hermann Simon, *Confessions of the Pricing Man: How Price Affects Everything* (2015)
Cham: Springer (Copernicus imprint), ISBN 978-3-319-20399-7 (verified).
**What it explains.** A pricing consultant's semi-memoir for business readers on how sellers set prices: value-based pricing, price psychology and the power of price to drive profit.
**What the book can borrow / how it differs.** It is the seller's-eye view. It is useful as a foil because bidders in construction behave as pricing strategists, not just cost estimators (market conditions, backlog, unbalancing). That explains why a pure cost-model bot plateaus near ±20%: price is cost plus strategy.

#### 21. Douglas W. Hubbard, *How to Measure Anything: Finding the Value of "Intangibles" in Business* (2007; 3rd ed. 2014)
Hoboken: Wiley. First edition ISBN 978-0-470-11012-6; 3rd ed. ISBN 978-1-118-83644-6 (verified).
**What it explains.** A practical, popular book on calibrated estimation: 90% confidence intervals, calibration training, Monte Carlo, the value of information, and "Fermi" decomposition. It is written for managers with little mathematics.
**What the book can borrow / how it differs.** It is the best general-reader treatment of **known error rates** in estimates. That is the book's Daubert point (a standard bot with a published error rate) and its 20%-versus-2–3% gap. It can also borrow Hubbard's argument that a calibrated estimator, human or machine, is *testable*. Hubbard does not deal with tendering, adversarial use or legal defensibility.

---

### D. Megaprojects, cost overruns and why building is expensive

#### 22. Bent Flyvbjerg & Dan Gardner, *How Big Things Get Done: The Surprising Factors That Determine the Fate of Every Project, from Home Renovations to Space Exploration and Everything In Between* (2023)
New York: Currency (Penguin Random House), 7 Feb 2023, ISBN 978-0-593-23951-3 (verified via PRH). It was shortlisted for the FT Business Book of the Year (Oxford Saïd news).
**What it explains.** The best popular book on cost estimation. It covers the "iron law" that most megaprojects run over; "think slow, act fast"; reference-class forecasting, or the "outside view," which judges a project against the distribution of similar past projects; modularity ("Lego"); and the Sydney Opera House. Gardner, a journalist who also co-wrote *Superforecasting*, gives it trade-book polish.
**What the book can borrow / how it differs.** Reference-class forecasting is exactly what bid-tab-trained estimating does: judging a price against the empirical distribution of comparable past prices. The book should name this lineage explicitly. Flyvbjerg works at the whole-project, decision-to-build level. The book works at the **tender price** level (is *this bid* reasonable?) and adds the legal and procedural question of defensibility that Flyvbjerg does not address.

#### 23. Transit Costs Project (Eric Goldwyn, Alon Levy, Elif Ensari, Marco Chitti et al.), NYU Marron Institute, final report 2023
Releases and case studies: https://marroninstitute.nyu.edu/blog/transit-costs-project-releases-new-york-case-and-final-project-report. Conclusion summary on Levy's blog, 24 Oct 2022: https://pedestrianobservations.com/2022/10/24/the-transit-costs-project-conclusion-is-out/. Exact final-report title and full author list **UNVERIFIED** (Marco Chitti's inclusion is from memory). Popular coverage: Planetizen, "Report: Why U.S. Transit Projects Cost So Much" and "How Consultants Drive Up Transit Construction Costs"; Slow Boring × Transit Costs Project guest series, https://www.slowboring.com/p/slow-boring-x-transit-costs-project (URL seen; contents not read).
**What it explains.** It compares rail-construction costs internationally (Istanbul, Milan, Stockholm, Boston, New York). It finds that US costs are driven by weak in-house owner expertise, reliance on consultants, procurement practices that limit bidder competition, overdesigned stations, and risk pushed onto contractors who then price it. It is written as policy reports, but Levy's blog and the Slow Boring pieces are popular.
**What the book can borrow / how it differs.** It is direct empirical support for claims 1 and 5: risk allocation and owner capacity shape bid prices. It also gives a comparative method the book can mirror with Texas versus Alberta. TCP explains *why* prices are high. The book asks how anyone *knows* whether a given price is reasonable.

#### 24. Brian Potter, *The Origins of Efficiency* (2025) and the *Construction Physics* newsletter
*The Origins of Efficiency*: South San Francisco: Stripe Press, 2025, 384 pp., ISBN 978-1-953953-52-0 (verified; reviewed by Emmet Penney, *American Affairs*, 20 May 2026). Relevant *Construction Physics* posts (verified on the archive):
- "Design Bid Build and the Construction Value Chain" (2 Sep 2021), https://www.construction-physics.com/p/design-bid-build-and-the-construction
- "How much do construction costs matter?" (16 Feb 2022)
- "Why Are There so Few Economies of Scale in Construction?" (24 Aug 2022)
- "Construction Costs Rarely Fall", https://www.construction-physics.com/p/construction-costs-rarely-fall
- "Does Construction Ever Get Cheaper?"
- "Sketch of a Theory of Construction Productivity"
- "Why the U.S. Can't Build Icebreaking Ships" (26 Sep 2024)

Potter's IFP pieces include "Why Does Nuclear Power Plant Construction Cost So Much?" (1 May 2023), https://ifp.org/nuclear-power-plant-construction-costs/.

**What it explains.** The book explains production efficiency: learning curves, Wright's Law, buffers and variability, DFMA, vertical integration versus outsourcing, Toyota. It argues construction resists these because sites are outdoor, varied and cyclical. Penney's review notes the word "procurement" does not appear centrally. The newsletter is the leading popular explainer of construction economics. The design-bid-build post argues that trades "generally win work by being the low-bidder" and are ground down to thin margins. It treats the owner's verification problem as an information-cost problem, which is close to Galbraith.
**What the book can borrow / how it differs.** Potter is the nearest living kin in register and audience: an engineer-practitioner writing clearly for generalists. The design-bid-build post is the best short popular account of how project delivery shapes information flow. Potter writes about **production** costs and almost never about how the buyer judges a **price**, so the book fills an adjacent gap. Comeau could approach Potter or IFP as an audience.

#### 25. Ezra Klein & Derek Thompson, *Abundance* (2025)
New York: Avid Reader Press (Simon & Schuster), March 2025 (publisher confirmed via catalogues; ISBN not confirmed).
**What it explains.** A best-selling argument that US liberalism over-proceduralised itself and cannot build housing, transit or energy. It covers California high-speed rail and the "everything-bagel" layering of objectives onto projects and contracts. It is mass-market.
**What the book can borrow / how it differs.** It shows how big the audience is for "why can't we build," and gives the "everything-bagel" metaphor for procurement scope creep. Abundance stays at the policy-politics level and is not about how a tender is priced or evaluated. The book is the practitioner's floor-level view underneath it.

#### 26. Dan Wang, *Breakneck: China's Quest to Engineer the Future* (2025)
New York: W. W. Norton, 2025, ISBN 978-1-324-10603-6 (verified via harvard.com and newbooksnetwork).
**What it explains.** It contrasts China as an "engineering state" with the US as a "lawyerly society." China builds fast, with costs borne elsewhere; the US litigates and proceduralises.
**What the book can borrow / how it differs.** "Lawyerly versus engineering" is a crisp frame for the book's two halves, accuracy (engineer) and defensibility (lawyer). The reasonable bot is a proposal to give the engineering answer a lawyerly form, the witness box. Wang does not treat procurement mechanics.

#### 27. Tracy Kidder, *House* (1985)
Boston: Houghton Mifflin. Kirkus gives the release date as 15 Oct 1985 (verified).
**What it explains.** A narrative non-fiction classic following one house in Amherst, Massachusetts, from design to completion. It covers the clients, the architect and the builders (the "Apple Corps"). A central thread is the builders' estimate and the fixed-price negotiation: the gap between the builders' number and what the clients will accept, and the strain of who absorbs overruns. It is written for general readers.
**What the book can borrow / how it differs.** It is the best existing **popular dramatisation of a construction price**: how a builder arrives at a number, how an owner judges it, and how the relationship sours around it ("starting a relationship expecting a divorce" in miniature). It is private and residential with one builder. The book is about public, sealed, competitive tendering. (The specific contract details are from memory of the book, **not re-verified** this session.)

---

### E. Bureaucracy, legibility and paperwork (theory for tendering)

#### 28. James C. Scott, *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed* (1998)
New Haven: Yale University Press. Details **not re-verified**.
**What it explains.** It shows how states make the world "legible" through cadastral maps, standard measures and scientific forestry, and how high-modernist schemes fail by erasing *mētis*, practical local knowledge. It is academic but widely read.
**What the book can borrow / how it differs.** Measuring quantities, standard units and the bill of quantities are legibility machines. That is the book's "two centuries of one loop." Scott's warning applies: a standard bot makes prices legible and risks discarding the estimator's *mētis*. The book's human "keyholder" is a partial answer Scott would recognise.

#### 29. David Graeber, *The Utopia of Rules: On Technology, Stupidity, and the Secret Joys of Bureaucracy* (2015)
Brooklyn: Melville House. Details **not re-verified**.
**What it explains.** Essays arguing that markets and technology have *increased* paperwork ("the iron law of liberalism"), and that bureaucracy is appealing because rules make the world predictable.
**What the book can borrow / how it differs.** It is a counterweight to tech optimism. Graeber would predict that the reasonable bot generates more paperwork, not less. The book should face this directly. Its "record" is new paperwork, so the claim must be that machine-readable records are cheaper to produce and check.

---

### Also noted (shorter; mostly **not re-verified** this session)

- **Zachary Liscow et al., "Procurement and Infrastructure Costs,"** NBER Working Paper 31705 (2023), https://www.nber.org/papers/w31705 (verified URL; co-authors William Nober and Cailin Slattery are **UNVERIFIED**). It surveys US state DOT officials and links procurement capacity and practices to highway costs. Academic, but it is the key empirical bridge between popular "why it costs so much" writing and tendering practice. The book should cite it.
- **Infrastructure Cost Review (UK, 2010)**, a government review of why UK civil works cost more than European peers (Wikipedia page exists). It is a policy precedent, not popular.
- **André Cédilot & André Noël, *Mafia Inc.*** (Random House Canada, c. 2011–12; details **UNVERIFIED**; author interview on CTV Montreal). It is popular journalism touching Quebec construction collusion before the Charbonneau Commission. It is the most likely Canadian trade book on construction bid-rigging, but construction is not its main subject.
- **Daniel Kahneman, *Thinking, Fast and Slow*** (2011), for the planning fallacy and the inside versus outside view. Flyvbjerg builds on it.
- **Fred Brooks, *The Mythical Man-Month*** (1975) and **Steve McConnell, *Software Estimation: Demystifying the Black Art*** (2006). These are the software world's popular estimating classics, useful because the book redescribes procurement as software development. McConnell's "cone of uncertainty" maps onto design maturity at tender.
- **John Gall, *Systemantics*** (1975), and **Anthony King & Ivor Crewe, *The Blunders of Our Governments*** (2013). The first is in the playful-aphorism register (like Augustine and Parkinson); the second is serious UK policy-failure journalism that includes procurement fiascos.
- **UK Covid PPE / "VIP lane."** There is extensive journalism (Byline Times, Good Law Project, the Covid Inquiry's July 2026 module finding about £10bn of waste per ITV and the Express & Star). A bookshop listing titled *VIP Lane* was found, but its author and publisher could **not** be confirmed (UNVERIFIED). No confirmed trade book on NHS/PPE procurement was identified.

### Gaps in this search (budget ran out)
These were not searched or verified: Planet Money or *The Indicator* episodes on procurement and spectrum auctions; Matt Yglesias's specific posts; Brian Riedl; IFP and Niskanen pieces specifically on federal acquisition reform; Works in Progress essays on procurement or infrastructure cost; Statecraft (Santi Ruiz) interviews with procurement officials; Eli Dourado; the Nobel "popular information" PDF title. A follow-up pass should check these, especially Planet Money's FCC incentive auction coverage and any Works in Progress piece on public procurement.

---

### Synthesis: is there a popular explainer of procurement itself?

**Essentially no.** The popular shelf is well stocked on the *edges* of procurement:

- **Auctions and market design**: Roth, Milgrom, Harford, the Nobel outreach, Hubbard & Paarsch.
- **Megaproject overruns and "why we can't build"**: Flyvbjerg & Gardner, Transit Costs Project, Potter, *Abundance*, Wang.
- **Price psychology**: Poundstone, Simon.
- **Estimating under uncertainty**: Hubbard, Kahneman.
- **Bureaucracy theory**: Scott, Graeber, Bagley.
- **The scandal genre**: Rasor, Fitzgerald, Burton, $600-hammer journalism.

The only works aimed at procurement *as a subject* are Kelman (1990, a policy monograph), Pahlka (2023, government IT, with procurement as one villain among several), Hubbard & Paarsch's single procurement chapter, and the satirical laws of Augustine and Parkinson. None explains, for a general reader, the ordinary machinery of buying a public work: the engineer's estimate, the bill of quantities, sealed bids, the bid tab, the price book, addenda and claims.

None asks the book's spine question: **how does anyone know a price is fair and reasonable?** The scandal genre assumes the answer is obvious (a toilet seat should not cost $640). The Freedberg hammer story shows it is not. The economists answer "run a good auction." Flyvbjerg answers "use the reference class" but at project scale, not tender scale. Thaler's winner's curse explains why the low bid is systematically wrong, but nobody has carried it into the construction tender for a lay audience.

**What this means for the book:**

1. The gap is real and the book can claim it plainly. It is the first short, popular explainer of public-works procurement and price reasonableness.
2. It must borrow scaffolding from its neighbours rather than reinvent it: Thaler's winner's curse for the adversarial culture, Flyvbjerg's reference class for bid-tab estimating, Kelman's fear of discretion and Pahlka's waterfall for the "tender is the API" argument, Hubbard's calibration for "known error rate," and the Freedberg hammer as the opening parable that "fair" is not obvious.
3. Its best register models are the short, playful, illustrated works: Augustine's laws, Parkinson's bikeshed, Harford's one-object-per-chapter *Fifty Things*, Jarnestad's Nobel diagrams, and the MIT Essential Knowledge format. That supports the "Procurement Machines" cards and the *Specialist*-sized ambition.
4. Because nobody has written the plain explainer, the book should spend more words than a manifesto normally would on **how tendering works today** before proposing the bot. Its readers, including policy readers of *Abundance* and *Construction Physics*, will not know the loop it is reforming.

---

## Part 4. Construction procurement
*Literature-review strand for* Fair and Reasonable / The Reasonable Bot. *Compiled 1 November 2026.*

### How each item was checked

- **VERIFIED**: I confirmed the citation details against a publisher, RePEc/IDEAS, ISO, ASCE Library, a court-reporter summary or an official page during this session. The source URL is given.
- **PARTLY VERIFIED**: I confirmed that the work exists and checked its main details, but some fields come from memory and are flagged in the entry, for example "pages from memory".
- **UNVERIFIED**: the citation comes from memory and was not checked in this session. Check it before quoting it.

**Research limits.** The shared WebFetch budget (100 calls per hour) and the WebSearch budget (200 calls per turn) both ran out partway through this session. The digital-construction section and a few textbooks therefore could not be checked online and are marked to match. I did not make up any citation. Where I was unsure, the entry is marked.

**Chapter key.** ch1 = tensions; ch2 = the tender is the API; ch3 = how price is judged; ch4 = the history loop; ch5 = liability and the duty to disclose; ch7 = the bot in the witness box; ch8–9 = estimator and evaluator; ch10 = protocol and standard.

---

### A. Standard textbooks

#### 1. Hughes, W., Champion, R. & Murdoch, J. (2015). *Construction Contracts: Law and Management*, 5th ed. Abingdon: Routledge. ISBN 9780415657044 (hb); 9780415657051 (pb). VERIFIED (https://www.routledge.com/Construction-Contracts-Law-and-Management/Hughes-Champion-Murdoch/p/book/9780415657044)
- **Content.** This is the standard UK text that treats contracts as both legal instruments and management tools. It covers procurement routes, tendering, standard forms (JCT, NEC, FIDIC), payment, variations, claims and dispute resolution. Hughes's long-running argument is that contracts are drafted to allocate risk and coordinate work, not only to resolve disputes later.
- **Overlap and difference.** It is the closest academic match to the book's "contract as interface" view. It assumes documents written by people, read by people and judged by people, and it says nothing about machine-readable tenders or about bots that check prices. It is good background for ch1 (tensions) and ch5 (liability).

#### 2. Masterman, J. W. E. (2002). *An Introduction to Building Procurement Systems*, 2nd ed. London: Spon Press. ISBN 9780415246415 / 9780415246422. PARTLY VERIFIED (both ISBNs found on booksellers; the edition year is from memory)
- **Content.** A classification of procurement systems (separated, integrated, management-oriented and discretionary) and how clients should choose among them. It sets out the British "traditional" route: design is finished, quantities are measured into a bill of quantities, and the work is let by competitive lump-sum tender.
- **Overlap and difference.** It describes the "one-shotted design locked for tender" that the book calls a tension (ch1), but treats it as one choice in a menu of options. It is useful for the ch4 history cards on the bill of quantities and the quantity surveyor.

#### 3. Morledge, R., Smith, A. J. & Appiah, S. Y. (2021). *Building Procurement*, 2nd ed. Chichester: Wiley-Blackwell. ISBN 9781119609490. PARTLY VERIFIED (ISBN and authors confirmed on bookseller pages; the year is inferred, as the first edition was Morledge, Smith & Kashiwagi, 2006)
- **Content.** A procurement-strategy textbook that frames procurement as matching a client's objectives and risk appetite to a delivery method. It covers relational methods, frameworks and value for money.
- **Overlap and difference.** It sees procurement from the client's side, as strategy. The book looks at the mechanics of a price being judged fair (ch3) and at data interfaces (ch2). It is a quick reference for terms used in ch1.

#### 4. Walker, D. H. T. & Rowlinson, S. (eds.) (2008). *Procurement Systems: A Cross-Industry Project Management Perspective*. Abingdon: Taylor & Francis. ISBN 9780415416061. VERIFIED (https://research.bond.edu.au/en/publications/procurement-systems-a-cross-industry-project-management-perspecti/)
- **Content.** Edited chapters on procurement systems as socio-technical systems, including alliancing, relationship-based procurement, culture, innovation in project alliances and governance. The authors compare procurement across industries, including IT.
- **Overlap and difference.** Its comparison across industries comes closest to the book's "procurement as software development" analogy (ch2). It still treats the relationship, not the data interface, as the thing to fix. It serves ch1 (relational answers to the "divorce" tension) and ch2.

#### 5. Ashworth, A. (with Perera, S. in later editions). *Cost Studies of Buildings*. Routledge (several editions; 6th ed. c. 2015). UNVERIFIED (edition and year from memory)
- **Content.** The UK quantity-surveying text on cost planning, cost indices, elemental cost analysis (BCIS), approximate estimating and life-cycle costing.
- **Overlap and difference.** It sets out the professional method behind "how price is judged" before tender: elemental benchmarks and price books. This is the human system the book's bot estimator copies (ch3, ch8–9). It also documents how tendered prices feed cost databases, which is the loop described in ch4.

#### 6. Bartholomew, S. H. *Construction Contracting: Business and Legal Principles* (Prentice Hall; 2nd ed. c. 2002). UNVERIFIED (title wording and edition from memory)
- **Content.** A US text on contractor business practice, including estimating, bidding, bonding, contract types and claims.
- **Overlap and difference.** It covers the contractor's side of the "price the errors" behaviour (ch1, ch5) as normal business practice. Check the citation before using it.

#### 7. Halpin, D. W. (with Woodhead, R. W. in earlier editions; later Senior, B. A. and Lucko, G.). *Construction Management*. New York: Wiley (several editions). UNVERIFIED (edition and authorship by edition from memory)
- **Content.** A standard US construction-management text covering competitive bidding, estimating, contract forms and markup strategy, with a short treatment of Friedman- and Gates-style bidding models.
- **Overlap and difference.** It places the bidding-model literature (§C) in teaching practice. It is useful for ch3 and ch8 as the US engineering-education view.

---

### B. Government reviews, industry reports and standards

#### 8. Simon Report (1944). Ministry of Works, *The Placing and Management of Building Contracts* (Central Council for Works and Buildings; chaired by Sir Ernest Simon). London: HMSO. PARTLY VERIFIED (title confirmed via designingbuildings.co.uk "Simon Report"; HMSO details are standard but were not re-checked)
- **Content.** The first of the UK post-war reviews. It warned against open tendering and lowest-price selection and favoured selective tendering, bills of quantities and better client briefing.
- **Overlap and difference.** It is the starting point for the book's ch4 "loop", where quantities are measured and sealed bids opened, and for the long argument over lowest price versus value. It is a candidate for the ch4 "Procurement Machines" cards.

#### 9. Banwell Report (1964). Ministry of Public Building and Works, *The Placing and Management of Contracts for Building and Civil Engineering Work* (chaired by Sir Harold Banwell). London: HMSO. PARTLY VERIFIED (title confirmed via designingbuildings.co.uk; publisher from memory)
- **Content.** It criticised the separation of design from construction, supported serial and negotiated contracting, and called for a common form of contract across building and civil engineering.
- **Overlap and difference.** It states the ch1 tension (design locked before the builder is involved) sixty years ago. It shows that the book's problems have a long record and that past reforms worked on relationships, not information.

#### 10. Latham, Sir M. (1994). *Constructing the Team: Final Report of the Government/Industry Review of Procurement and Contractual Arrangements in the UK Construction Industry*. London: HMSO. PARTLY VERIFIED (existence and title confirmed via designingbuildings.co.uk; the full subtitle and ISBN were not re-checked)
- **Content.** It diagnosed an adversarial industry and recommended partnering, a "modern" contract family (it backed NEC), statutory adjudication (later in the Housing Grants, Construction and Regeneration Act 1996), fair payment and a 30% real cost-reduction target.
- **Overlap and difference.** It is the classic source for "starting a relationship expecting a divorce" (ch1). Latham's remedy was contracts and culture. The book's remedy is a public, rerunnable record and a reference price (ch5, ch7). It serves ch1 and ch4.

#### 11. Egan, Sir J. (1998). *Rethinking Construction: The Report of the Construction Task Force*. London: DETR. PARTLY VERIFIED (confirmed via the Wikipedia "Egan Report" page and Constructing Excellence's list of key publications; publisher from memory)
- **Content.** It applied manufacturing thinking (lean production and the Toyota model) to construction. It argued against lowest-price competitive tendering and set targets for cost, time and defects.
- **Overlap and difference.** It parallels the book's Taylorism and Galbraith thread (meta-goal 9): another attempt to import industrial methods. Egan wanted to get rid of competitive tendering. The book keeps the tender but changes its format and the way it is checked (ch2). It serves ch1 and ch4.

#### 12. Farmer, M. (2016). *The Farmer Review of the UK Construction Labour Model: Modernise or Die*. London: Construction Leadership Council. VERIFIED as to existence and title (https://en.wikipedia.org/wiki/Farmer_Review_of_the_UK_Construction_Labour_Model; designingbuildings.co.uk)
- **Content.** It identified low productivity, a shrinking workforce, low margins, adversarial pricing and weak innovation. It recommended pre-manufacture ("modern methods of construction") and client-led change.
- **Overlap and difference.** It supports the ch1 view that the problems are structural. It barely touches tender data or price verification, which is the space the book occupies (ch2, ch3).

#### 13. HM Government / Cabinet Office (2020). *The Construction Playbook: Government Guidance on Sourcing and Contracting Public Works Projects and Programmes* (December 2020; issued with Procurement Policy Note 09/20). PARTLY VERIFIED (gov.uk page and PPN 09/20 confirmed via Trowers & Hamlins commentary; the subtitle is from memory; later versions followed)
- **Content.** UK central-government policy. It requires "should cost models" (a pre-market estimate of whole-life cost), outcome-based specifications, early supplier involvement, benchmarking, long-term portfolio contracts, standard forms such as NEC, digital and BIM (ISO 19650), and checks of supplier financial health.
- **Overlap and difference.** The "should cost model" is a direct government counterpart to the book's Fair and Reasonable Evaluator (ch3, ch8–9). It is produced by people, and nothing in the guidance requires the method to be published, reproducible or tested for error rate. That gap is the core of ch7 and ch10. **High priority** for the book.

#### 14. Barbosa, F., Woetzel, J., Mischke, J. et al. (2017). *Reinventing Construction: A Route to Higher Productivity*. McKinsey Global Institute, February 2017. VERIFIED (MGI full-report PDF and summary pages located)
- **Content.** Construction labour productivity grew about 1% a year over two decades, against about 2.8% for the whole economy. MGI proposes seven levers, the first being regulation and procurement ("reshape regulation", "rewire the contractual framework"), together with digital technology. It estimates a possible 50–60% productivity gain.
- **Overlap and difference.** It is the standard citation for the claim that construction is behind other industries. It treats procurement and contracts as a source of low productivity but proposes no data standard. It is useful in ch1 to set the stakes.

#### 15. ISO 10845-1:2020. *Construction procurement — Part 1: Processes, methods and procedures* (2nd ed., December 2020). Geneva: ISO (ISO/TC 59/SC 18). VERIFIED (https://www.iso.org/standard/72467.html)
- **Content.** A generic procurement system covering goods, services, works and disposals, aiming to be "fair, equitable, transparent, competitive and cost-effective". It sets out processes, conduct requirements, a policy framework and methods and procedures. Other parts of the series (from memory: Part 2 formatting and compiling procurement documents; Part 3 standard conditions of tender; Part 4 standard conditions for calls for expressions of interest; Parts 5–8 participation of targeted enterprises and labour) give standard formats and conditions. SC 18 was set up around 2015 and is led by SABS, with Ron Watermeyer as chair (VERIFIED: ISO TC 59 news page).
- **Overlap and difference.** It is the obvious anchor for ch10. Like the book, it standardises the structure of procurement documents and their conditions of tender, which is the "API" idea in ch2 put in ISO form. It is document-structured, not data-structured, and it is silent on how price reasonableness is judged or verified. The book can describe its proposed protocol as a computable extension of ISO 10845 Parts 2 and 3. (Part numbers and titles beyond Part 1 are UNVERIFIED; check them.)

#### 16. Watermeyer, R. B. (2005). "A generic and systemic approach to procurement: the case for an international standard." *Public Procurement Law Review*, no. 1, pp. 39–61. Also: Watermeyer, R. B. (2011). "Standardising construction procurement systems." *The Structural Engineer*, 89(20); and Watermeyer (2005), "South African standards for construction procurement," *The Structural Engineer*, 83(4), pp. 15–18. VERIFIED from Watermeyer's own publication list (http://ioptions.co.za/node/7)
- **Content.** The intellectual origin of ISO 10845. Watermeyer argues that procurement should be specified as a generic system of processes, methods and procedures, and he shows the South African CIDB / SANS 294 standards as a model that was then taken to ISO.
- **Overlap and difference.** This is the closest earlier work to the book's ch10 "protocol" argument: standardise the format and the procedure so outcomes can be compared and checked. Watermeyer standardises process. The book wants to standardise a reference computation (a frozen bot plus a test set and tolerance). It serves ch10, and ch4 as a "Procurement Machines" card.

#### 17. Laryea, S. & Watermeyer, R. (2024). "Using construction procurement strategy to achieve socioeconomic development objectives." *Heliyon*, 10(13), e33537. DOI 10.1016/j.heliyon.2024.e33537. VERIFIED (https://pmc.ncbi.nlm.nih.gov/articles/PMC11260917/)
- **Content.** A case study of the South African New Universities Project. It used NEC3 ECC Option C framework contracts with contractually enforceable socioeconomic targets (Option X17 low-performance damages), measured with ISO 10845 methods.
- **Overlap and difference.** It shows ISO 10845 and NEC working together in practice with measurable, auditable targets, an example of "standard plus required record" (ch10). It is peripheral to price reasonableness.

#### 18. Canadian Construction Documents Committee (2018). *CCDC 23 – 2018: A Guide to Calling Bids and Awarding Construction Contracts*. Ottawa: CCDC. VERIFIED (sold by the Construction Association of Saskatchewan, RAIC and others)
- **Content.** The Canadian industry best-practice guide to the bid process: bid documents, solicitation and receipt, and award. It is written with *Ron Engineering* Contract A / Contract B law in mind.
- **Overlap and difference.** It is the main Canadian practice document on the very process the book wants to make machine-readable (ch2). It is the obvious Canadian counterpart to ISO 10845 Part 3 for ch10.

#### 19. CCDC 2 – 2020, *Stipulated Price Contract*, with OAA–OGCA (2024) *Recommended Supplementary Conditions for CCDC 2-2020* (Practice Tip PT.23.11). VERIFIED for the OAA–OGCA document (https://oaa.on.ca/Assets/Common/Shared_Documents/Practice%20Tips/PT.23.11_V01.1_Attach1_OAA-OGCA_CCDC2-2020_RecommendedSuppCons_20240315_R00_.pdf)
- **Content.** The recommended supplementary conditions replace GC 1.1.3–1.1.4. The contractor must review the contract documents and "report promptly to the Consultant any ambiguities, design issues or other matters requiring clarification". The contractor is not responsible for issues it could not reasonably have discovered, must not proceed with affected work until it has instructions, and cost and time effects go through Part 6 (Changes).
- **Overlap and difference.** This is the Canadian standard-form version of the contractor's **post-award** duty to report errors. It sits beside the book's ch5 question of whether a bidder should be made to disclose errors **before** award. It is the exact clause a bidder's bot would put into effect. **High priority** for ch5. (The wording of the base CCDC 2-2020 GC 1.1 was not checked separately.)

#### 20. Quebec. Commission d'enquête sur l'octroi et la gestion des contrats publics dans l'industrie de la construction (Charbonneau Commission) (2015). *Rapport final*. Tabled 24 November 2015. PARTLY VERIFIED (date and 60 recommendations confirmed via Slaw, 26 Nov 2015, https://www.slaw.ca/2015/11/26/quebec-construction-corruption-inquiry-final-report-published/; exact title and volumes not checked)
- **Content.** A public inquiry into collusion, bid-rigging, corruption and illegal political financing in Quebec public construction contracts, including the roles of engineering firms and organised crime. It made 60 recommendations, including an independent public procurement authority and an independent expert committee to plan public works.
- **Overlap and difference.** It is the most important Canadian evidence that the bid record can be manipulated. The opened-bid "price book" in ch4 is only as good as the competition behind it. It strengthens the ch3 and ch7 argument for an independent, reproducible reference price, and the ch10 requirement that the record be public. (Quebec's Autorité des marchés publics, created in 2017–2018, is the institutional result; that link is UNVERIFIED here.) **High priority.**

#### 21. US Department of Transportation, Office of Inspector General (2019). *FHWA Lacks Adequate Oversight and Guidance for Engineer's Estimates*. Report No. ST2019020. VERIFIED (https://www.oversight.gov/reports/audit/fhwa-lacks-adequate-oversight-and-guidance-engineers-estimates; the year is inferred from the report number)
- **Content.** FHWA had made limited progress on the recommendations of its own 2015 *National Review of State Cost Estimation Practice*, including updating its 2004 guidance on engineer's estimates. It lacks processes to monitor how accurate state DOT engineer's estimates are.
- **Overlap and difference.** This is a federal admission that the main US tool for judging price reasonableness, the engineer's estimate, is not systematically checked for accuracy. That is the "known error rate" gap at the centre of ch7. It fits the book's TxDOT development data well (ch8–9). **High priority.**

#### 22. Federal Highway Administration (2004). *Guidelines on Preparing Engineer's Estimate, Bid Reviews and Evaluation*. Washington, DC: FHWA. PARTLY VERIFIED (existence and title confirmed via SCDOT-hosted copy https://www.scdot.org/business/pdf/LPA/FHWA_BidEvaluationGuidelines.pdf and the OIG reference to "2004 Guidance"; content from memory)
- **Content.** Describes the methods for an engineer's estimate (historical bid-based, cost-based, or both) and how to review bids before award, including checking low bids against the estimate, mathematically and materially unbalanced bids, and justifying awards that differ greatly from the estimate (the commonly cited trigger is about ±10%; check the exact figure).
- **Overlap and difference.** This is the official US "how price is judged" procedure (ch3). The book's evaluator would automate the bid review this guidance describes and add an error rate. A companion is FHWA (2015), *National Review of State Cost Estimation Practice* (existence VERIFIED through the OIG report; details UNVERIFIED).

#### 23. AASHTO (2013). *Practical Guide to Cost Estimating*. Washington, DC: AASHTO. PARTLY VERIFIED (AASHTO store listing found; year from memory)
- **Content.** Practice guidance for state DOTs on estimating at each stage, including bid-history-based estimating, cost-based estimating, risk and contingency. It goes with AASHTOWare Project Estimation software, which runs on DOT bid tabulations.
- **Overlap and difference.** It describes the US "opened bids become next year's price book" machinery that ch4 narrates and that the ch8–9 bot reproduces. The main difference: AASHTOWare is a closed, vendor-maintained tool with no published error rate.

---

### C. Bidding behaviour, estimating and auction economics

#### 24. Friedman, L. (1956). "A Competitive-Bidding Strategy." *Operations Research*, 4(1), 104–112. DOI 10.1287/opre.4.1.104. VERIFIED (https://ideas.repec.org/a/inm/oropre/v4y1956i1p104-112.html)
- **Content.** The first operations-research model of sealed-bid strategy. It chooses a markup to maximise expected profit, given probability distributions of competitors' bid-to-cost ratios estimated from past bid records.
- **Overlap and difference.** It formally treats opened bids as data for pricing the next bid, the ch4 loop in its earliest form. Friedman uses past bids to beat competitors. The book uses them to judge whether a price is fair (ch3). It is a ch4 card candidate. (Ballesteros-Pérez et al., "Friedman's Bidding Model: Errors and Corrections," *J. Constr. Eng. Manage.* DOI 10.1061/(ASCE)CO.1943-7862.0001695: the DOI is VERIFIED, the author list is UNVERIFIED.)

#### 25. Gates, M. (1967). "Bidding Strategies and Probabilities." *Journal of the Construction Division* (ASCE), 93(1), 75–110. DOI 10.1061/JCCEAZ.0000192. VERIFIED (ASCE Library)
- **Content.** A competing model to Friedman's for the probability of winning against several bidders. It started a long Friedman–Gates dispute in construction management in the 1970s and 1980s.
- **Overlap and difference.** It shows that construction academia studied bidding as a statistical, data-driven problem sixty years ago. Most of that work was about the bidder's advantage, not public price assurance. It serves ch4 and ch8.

#### 26. Capen, E. C., Clapp, R. V. & Campbell, W. M. (1971). "Competitive Bidding in High-Risk Situations." *Journal of Petroleum Technology*, 23(6), 641–653. DOI 10.2118/2993-PA. PARTLY VERIFIED (authors, title, journal and year confirmed via AAPG Explorer "Bidding science saved"; volume, pages and DOI from memory)
- **Content.** Atlantic Richfield engineers showed that in common-value auctions the winner tends to be the bidder who most overestimated value (here, oil leases). They called this the "winner's curse" and recommended shading bids well below the estimate.
- **Overlap and difference.** In construction procurement the curse runs the other way: the low bidder is often the one who most underestimated cost or missed an error. That gives low bidders a motive to recover through change orders. This is the mechanism behind "price the errors, sue later" (ch1, ch5). A shared reference bot narrows the spread of estimates and so the curse, as item 29 shows empirically.

#### 27. Bajari, P. & Tadelis, S. (2001). "Incentives versus Transaction Costs: A Theory of Procurement Contracts." *RAND Journal of Economics*, 32(3), 387–407. VERIFIED (https://ideas.repec.org/a/rje/randje/v32y2001i3p387-407.html)
- **Content.** A model based on private construction. Buyers choose how complete to make the design, which is costly. Fixed-price contracts give strong cost incentives but expensive renegotiation when the design changes; cost-plus contracts lower adaptation costs. Cost-plus becomes better as projects grow more complex. The paper gives microfoundations for transaction-cost economics.
- **Overlap and difference.** It is the formal economics of the ch1 tension that a one-shotted design is always incomplete. It assumes renegotiation costs are external. The book argues that a versioned, machine-readable tender (ch2) and listener bots that turn questions into addenda (ch5) lower those costs directly. **High priority** for ch1 and ch2.

#### 28. Bajari, P., Houghton, S. & Tadelis, S. (2014). "Bidding for Incomplete Contracts: An Empirical Analysis of Adaptation Costs." *American Economic Review*, 104(4), 1288–1319. DOI 10.1257/aer.104.4.1288. VERIFIED (https://ideas.repec.org/a/aea/aecrev/v104y2014i4p1288-1319.html; NBER WP 12051)
- **Content.** Using California highway paving contracts, the authors show that bidders respond strategically to contractual incompleteness and price expected changes into their unit bids. A structural model puts adaptation costs at **7.5–14% of the winning bid**, much larger than markups from private information or market power.
- **Overlap and difference.** This is the strongest empirical support in the literature for the book's "bidders price the errors and claim later" claim (ch1, ch5). It puts a number on how much of a "fair" price is really a premium for expected disputes. It suggests the evaluator should model expected change orders, not just the bid line items (ch8–9). **Top priority: cite in ch1, ch3 and ch5.**

#### 29. De Silva, D. G., Dunne, T., Kankanamge, A. & Kosmopoulou, G. (2008). "The Impact of Public Information on Bidding in Highway Procurement Auctions." *European Economic Review*, 52(1), 150–181. VERIFIED (https://ideas.repec.org/a/eee/eecrev/v52y2008i1p150-181.html)
- **Content.** Oklahoma DOT began publishing its engineer's estimates; Texas already did. In a difference-in-differences comparison, Oklahoma bids fell relative to Texas and bid spread narrowed, most strongly on projects with high common-cost uncertainty. This fits the linkage principle in auction theory.
- **Overlap and difference.** It is direct evidence that **publishing a reference price lowers and tightens bids**. That is the economic case for the book's public, frozen standard bot (ch7, ch10) and for Scitovsky's "ignorance rent" (meta-goal 9). It uses Texas data, the book's development set (ch8–9). **Top priority.**

#### 30. Lewis, G. & Bajari, P. (2011). "Procurement Contracting with Time Incentives: Theory and Evidence." *Quarterly Journal of Economics*, 126(3), 1173–1211. VERIFIED (https://ideas.repec.org/a/oup/qjecon/v126y2011i3p1173-1211.html)
- **Content.** On Caltrans A+B (cost plus time) scoring auctions, 2003–2008. Projects let under A+B finished 30–40% faster, and commuter welfare gains exceeded the higher bid costs. Moving everything to efficient A+B would give welfare gains of about 22% of contract value.
- **Overlap and difference.** It shows that "fair and reasonable" need not mean lowest price. A scoring rule can price other value, which matches the Scitovsky argument that competition shifts to non-price value (meta-goal 9). It is relevant to ch3 and to ch10's treatment of multi-attribute bids.

#### 31. Bajari, P., McMillan, R. & Tadelis, S. (2009). "Auctions versus Negotiations in Procurement: An Empirical Analysis." *Journal of Law, Economics, and Organization*, 25(2), 372–399. UNVERIFIED (from memory; not checked this session)
- **Content.** Using private-sector building contracts in Northern California, it finds that complex projects are more often negotiated than auctioned. Auctions handle communication about design problems poorly, because bidders have no reason to point out flaws before award.
- **Overlap and difference.** If the citation checks out, it is very relevant to ch5. It gives an economic reason why competitive bidders stay quiet about design errors: auctions suppress the very information the book's Listener bot is meant to collect. Check the citation first.

#### 32. Flyvbjerg, B., Skamris Holm, M. K. & Buhl, S. L. (2002). "Underestimating Costs in Public Works Projects: Error or Lie?" *Journal of the American Planning Association*, 68(3), 279–295. DOI 10.1080/01944360208976273. PARTLY VERIFIED (DOI and abstract confirmed via arXiv:1303.6604; volume and pages from memory)
- **Content.** 258 transport projects worth US$90 billion. Cost underestimation is large, systematic and best explained by "strategic misrepresentation", not error. Flyvbjerg's later work proposes reference-class forecasting.
- **Overlap and difference.** Flyvbjerg is about **owner-side** estimates before the decision to build. The book is about **bid-time** price reasonableness. His case that estimators need an outside, statistically grounded reference (reference-class forecasting) closely parallels the book's frozen bot with a known error rate (ch7). Useful in ch3 and ch7.

#### 33. Porter, R. H. & Zona, J. D. (1993). "Detection of Bid Rigging in Procurement Auctions." *Journal of Political Economy*, 101(3), 518–538. VERIFIED (https://ideas.repec.org/a/ucp/jpolec/v101y1993i3p518-38.html; NBER WP 4013)
- **Content.** Using Long Island highway-construction auctions with a known cartel, the paper shows that cartel members' non-winning bids do not follow the cost-based ranking that competitive bids follow. This gave an econometric test for collusion.
- **Overlap and difference.** It shows that bid tabulations contain recoverable statistical signs of fairness or unfairness. That is the same data the book's evaluator reads (ch8–9), and collusion screening could be a feature of the standard bot. Relevant to ch3, ch4 and ch8–9, and linked to Charbonneau (item 20).

#### 34. Kawai, K. & Nakabayashi, J. (2022). "Detecting Large-Scale Collusion in Procurement Auctions." *Journal of Political Economy*, 130(5). DOI 10.1086/718913. PARTLY VERIFIED (DOI confirmed via IDEAS; year, issue and pages from memory)
- **Content.** Using about 42,000 Japanese national public-works auctions (corrected in Part 6; an earlier draft said about 70,000) with re-bidding rounds, the authors find bidding patterns that only coordinated bidding explains. This is the dango system.
- **Overlap and difference.** It is a modern, large-scale example of the dango literature and shows that statistical screening scales to national bid data. It supports the book's claim that a bot can do what auditors could not (ch8–9, ch10).

#### 35. Unbalanced bidding: "Handling Unbalanced Bidding in Construction Projects: Prevention Rather Than Detection." *Journal of Construction Engineering and Management* (ASCE). DOI 10.1061/(ASCE)CO.1943-7862.0001045. PARTLY VERIFIED (DOI and title found in ASCE Library search; authors and year UNVERIFIED)
- **Content.** Bidders skew unit prices toward items they expect to overrun, or toward early items to improve cash flow. The paper argues that procurement design should prevent this rather than rely on detecting it after bids are in. (Related: Cattell, Bowen & Kaka (2007), "Review of unbalanced bidding models in construction," *J. Constr. Eng. Manage.* 133(8), UNVERIFIED.)
- **Overlap and difference.** Unbalanced bidding is how "pricing the errors" shows up in unit-price civil works, the trade the book chooses for ch10. A per-line-item reference price from the bot is a direct detector of it. It serves ch3 and ch8–9.

---

### D. Relational and alternative delivery

#### 36. Watermeyer, R. (c. 2015). "Early contractor involvement in framework contracts." (ResearchGate record 292463026; likely a SAICE *Civil Engineering* or conference paper). UNVERIFIED as to venue and year
- **Content.** On using ECI within framework agreements (NEC-based) in South Africa: contractors join during design, under target-cost or cost-reimbursable arrangements.
- **Overlap and difference.** ECI and two-stage tendering are the main industry answer to the ch1 "one-shotted design" tension: bring the builder in before design is fixed. The book offers a different answer: keep competitive tendering but make the design data versioned and queryable, so ambiguities show up and are resolved (ch2).

#### 37. Integrated Project Delivery: AIA California Council / American Institute of Architects (2007). *Integrated Project Delivery: A Guide*. UNVERIFIED (from memory)
- **Content.** Defines IPD as a multi-party agreement (owner, designer and builder) with shared risk and reward, early involvement of key participants, collaborative decision-making and BIM-enabled design. It is the US counterpart of Australian and UK alliancing.
- **Overlap and difference.** IPD addresses the "divorce" problem by removing the adversarial contract. The book accepts that public owners must still compete and judge price (ch1, ch3). IPD's shared-BIM premise is still a forerunner of ch2.

*Partnering, alliancing, design-build, CM at risk and two-stage tendering are also covered in the textbooks above, especially items 2–4, and in Latham, Egan and the Playbook (items 10, 11 and 13). I did not verify separate primary sources for these within the search budget.*

---

### E. Claims, disputes and the law of the tender

#### 38. *R v Ron Engineering & Construction (Eastern) Ltd*, [1981] 1 SCR 111 (SCC). VERIFIED (https://en.wikipedia.org/wiki/R_v_Ron_Engineering_and_Construction_(Eastern)_Ltd)
- **Content.** Ron found an arithmetic error in its low tender after opening and tried to withdraw. The Supreme Court created the **Contract A / Contract B** framework: submitting a compliant tender forms a unilateral, irrevocable bid contract (Contract A). A mistake does not stop Contract A from forming, so the $150,000 tender deposit was forfeited.
- **Overlap and difference.** This is the Canadian foundation of ch5. A bidder is bound by its own errors in the bid, but no case imposes a duty to report errors **in the owner's documents** before award. The book's proposal that the record matters more than the duty fits Contract A well: a bot-produced record could be made part of Contract A's terms. **Top priority, ch5.**

#### 39. *M.J.B. Enterprises Ltd v Defence Construction (1951) Ltd*, [1999] 1 SCR 619 (SCC). PARTLY VERIFIED (case and year confirmed via vLex and Daily Commercial News coverage; the SCR citation is the standard one but was not opened)
- **Content.** The Court confirmed that Contract A arises only if the parties intend it. It held that a privilege clause ("lowest or any tender not necessarily accepted") does not allow an owner to accept a non-compliant bid. There is an implied duty to accept only compliant bids.
- **Overlap and difference.** It sets out what "compliance" means in Canadian tender law. A machine-readable tender (ch2) could make compliance mechanically checkable. That is a strong argument for the Listener and evaluator bots (ch5, ch8–9).

#### 40. *Tercon Contractors Ltd v British Columbia (Transportation and Highways)*, 2010 SCC 4, [2010] 1 SCR 69. PARTLY VERIFIED (2010 SCC 4 confirmed via multiple law-firm commentaries; the SCR citation is from memory)
- **Content.** The owner took a bid from an ineligible bidder. A 5–4 Court held that the exclusion clause ("no claim for compensation…") did not cover a breach of the tender process. It also set out the three-step test for enforcing exclusion clauses in Canadian law.
- **Overlap and difference.** It shows that courts protect the **integrity of the tender process** even against clear contract wording. That supports the book's view that the record and process should be the protected object (ch5, ch10).

#### 41. Canadian owner-disclosure cases: *Bank of Montreal v Bail Ltée*, [1992] 2 SCR 554 (Hydro-Québec withheld a later geotechnical report; Quebec good-faith duty to inform); *Edgeworth Construction Ltd v N.D. Lea & Associates Ltd*, [1993] 3 SCR 206 (engineers liable to bidders for negligent misrepresentation in tender documents; bidders cannot each be expected to repeat the engineering in a short tender period); *Cardinal Construction Ltd v Brockville (Municipality)* (Ont HC 1984) (owner knew of a drawing error before close and did nothing, so liable); *Opron Construction Co v Alberta* (Alta QB 1994) (implied term of good-faith disclosure in tender information); *Queen v Cognos Inc*, [1993] 1 SCR 87. VERIFIED as summarised in Judson (2017), item 42
- **Overlap and difference.** Together these show that **Canadian law puts the disclosure duty on the owner**. The owner must tell bidders what it knows, and *Edgeworth* explicitly accepts that bidders cannot afford to re-engineer the design. The contrary claim, that a bidder must report the owner's errors before award, has **no settled Canadian authority** that I could find. That supports the book's ch5 position. *Edgeworth*'s "economic inefficiency of duplicated checking" argument is the one a cheap checking bot overturns, which makes it a key hook for ch5 and ch7.

#### 42. Judson, J. (2017). "Two Models of Pre-Contractual Disclosure in Canadian Construction Law." Canadian Bar Association, Construction & Infrastructure Law Section, Atrium Law Student Essay Contest, winning essay. VERIFIED (https://www.cba.org/Sections/Construction-Law/News/2017/University-of-Western-Ontario-Student-James-Judson; PDF at cba.org)
- **Content.** Compares Quebec's civil-law good-faith model (*Bail*: the owner knew the information, it was decisive, and the other party could not reasonably obtain it) with the common-law negligent-misrepresentation model (*Cardinal*, *Opron*, *Edgeworth*, *Cornell Engineering*). Argues for a good-faith duty after *Bhasin v Hrynew*, 2014 SCC 71, that could not be contracted out of.
- **Overlap and difference.** It is the clearest short map of Canadian pre-contract disclosure law. The *Bail* third limb, "cannot reasonably obtain the information itself", changes once bidders and owners both have checking bots. That is exactly the ch5 argument that liability moves to the user's bot. **Top priority, ch5.**

#### 43. Pattison, R. B. (2004). "Overview of the Law of Bidding and Tendering." *Canadian Bar Review*, 83, 716 ff. VERIFIED (https://cbr.cba.org/index.php/cbr/article/download/4013/4006/4013)
- **Content.** A survey of Canadian tender law after *Ron Engineering*: Contract A/B, the mistake doctrine (*Belle River*, *Wilchar*, *Gottardo*), owner liability for misrepresentation and non-disclosure (*BG Checo*, *Municipal Enterprises*), and drafting advice. Pattison argues that bidders should be allowed to withdraw, but not amend, mistaken bids.
- **Overlap and difference.** It gives practitioner-level doctrine for ch5. Notably, it records no general duty on either side to point out errors in the tender documents, which leaves room for the book's "record, not duty" proposal.

#### 44. *United States v Spearin*, 248 U.S. 132 (1918). VERIFIED (https://en.wikipedia.org/wiki/United_States_v._Spearin; govinfo USREPORTS-248)
- **Content.** An owner who supplies plans and specifications impliedly warrants that they are adequate. The contractor is not liable for losses caused solely by defects in them, and site-inspection clauses do not shift that risk.
- **Overlap and difference.** It is the US basis for the "price the errors, claim later" pattern: if the owner warrants the design, finding errors and keeping quiet pays off. It is a natural ch5 contrast to *Edgeworth*, and a ch4 "Procurement Machines" card candidate (1918).

#### 45. Patent ambiguity doctrine (US): *D'Annunzio Bros., Inc. v N.J. Transit Corp.*, 245 N.J. Super. 527 (App. Div. 1991); *Aspen Landscaping Contracting, Inc. v A. Juliano & Sons Contractors, Inc.*, No. A-5436-11T2 (N.J. App. Div. Aug. 9, 2013). VERIFIED via Cole Schotz commentary (https://www.coleschotz.com/doctrine-of-patent-ambiguity-bars-contractors-substantial-claim-for-extra-work/). The doctrine is also long-standing in US federal contracts law (Court of Federal Claims and Federal Circuit), not separately verified here
- **Content.** If an ambiguity in a publicly bid contract would be apparent to a reasonable bidder, or was actually known, the bidder must ask before bidding. If it does not, it cannot claim extra costs based on its own interpretation. In *Aspen*, a claim of $631,895 failed even though all three bidders had missed the conflict.
- **Overlap and difference.** This is the nearest existing **duty for the bidder to raise errors** in any common-law system, and it is enforced by losing the claim, not by compulsion. That matches the book's ch5 framing: there is no compelled disclosure, but the record decides. **Key twist for ch5 and ch7:** "would be apparent to a reasonable bidder" becomes "would be apparent to a reasonable *bot*". If every bidder can afford a checking bot, more ambiguities become patent. **Top priority.**

#### 46. RFI volume and cost. (a) Navigant Consulting (2013), *Impact & Control of RFIs on Construction Projects* (widely quoted figures: about 800 RFIs per large project, about US$1,000 in review cost per RFI, about 10-day average response). UNVERIFIED (found only in vendor blogs quoting it; the primary report was not located). (b) Tilley, P. A. and co-authors on design and documentation deficiency and RFIs (CSIRO, late 1990s; USQ repository item "Sparksman_P_Tilley"). UNVERIFIED (the repository item was found but not opened)
- **Content.** These quantify how many questions incomplete tender and construction documents generate and what those questions cost.
- **Overlap and difference.** They put the size of the ch2 problem in numbers: every RFI is a failed API call. They also support the ch5 Listener bot that turns questions into addenda. Check them before quoting any figures.

---

### F. Digital construction procurement

*Not web-verified in this session because the search budget ran out. All entries are from memory and marked UNVERIFIED. They are well-known instruments, so they should be quick to confirm.*

#### 47. Directive 2014/24/EU of the European Parliament and of the Council of 26 February 2014 on public procurement, Art. 22(4). OJ L 94, 28.3.2014, p. 65. UNVERIFIED (from memory)
- **Content.** Lets member states require "specific electronic tools, such as of building information electronic modelling tools or similar" for public works contracts and design contests, provided alternatives are available until the tools are generally accessible.
- **Overlap and difference.** It is the first EU legal hook for machine-readable tenders, the ch2 "tender is the API" idea in legislation. It allows BIM but does not define the price data or require reproducible evaluation (ch10).

#### 48. ISO 16739-1:2018 *Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries*; ISO 19650-1/-2:2018 *Organization and digitization of information about buildings and civil engineering works, including BIM*; COBie (NBIMS-US; BS 1192-4:2014). UNVERIFIED (from memory)
- **Content.** The open schemas and information-management processes for BIM. IFC is the data model, ISO 19650 sets out information requirements and exchange, and COBie is a spreadsheet subset for asset handover.
- **Overlap and difference.** These are the open data layer the book's protocol could build on (ch2, ch10). None of them standardises **price** or the judgement of price reasonableness. 5D BIM, which links quantities from the model to cost, is the bridge, but it is mostly done in proprietary tools. The book's "canonical, versioned, machine-readable tender data" proposal amounts to IFC plus a measurement standard plus a public price model.

#### 49. UK Government Construction Strategy 2011 and the 2016 "BIM Level 2" mandate for centrally procured public projects; UK BIM Framework (2019 onward). UNVERIFIED (from memory)
- **Content.** The UK required collaborative 3D BIM on central-government projects from April 2016. This was later folded into the ISO 19650-based UK BIM Framework and the Construction Playbook.
- **Overlap and difference.** It is a precedent for a government requiring a data format in procurement, the ch10 policy lever. The mandate covered design and asset information, not tender pricing or evaluation.

---

### Gaps the book fills

Across this literature, four strands rarely meet:

- **Procurement-systems textbooks and reviews** (Simon to the Playbook) diagnose adversarial tendering and propose relational fixes or better process.
- **Auction and contract economics** measures the costs precisely. Bajari, Houghton & Tadelis put adaptation costs at 7.5–14% of the winning bid; De Silva et al. show that publishing a reference price lowers and tightens bids.
- **Tender law** in Canada (*Ron Engineering*, *M.J.B.*, *Tercon*, *Edgeworth*, *Bail*) and the US (*Spearin*, patent ambiguity) shares out disclosure duties, mostly placing them on the owner.
- **Digital-construction standards** (IFC, ISO 19650, EU Art. 22(4)) standardise design data but not price.

No source I found asks the book's question: **how is a construction price shown to be fair and reasonable in a way that is reproducible, has a known error rate, and could stand as evidence?** The official tools are the FHWA engineer's estimate, AASHTOWare bid histories and the UK "should cost model". By the USDOT OIG's own account, none is checked for accuracy, and none is published as a rerunnable standard. ISO 10845 and Watermeyer standardise procurement procedure but stop short of computation.

The book's distinctive contributions are:
1. Treating the tender as a versioned data interface rather than a document set.
2. Reading the economics (adaptation-cost premia, the information effects of published estimates) together with Canadian tender law. The "reasonable bidder" of the patent-ambiguity doctrine and the "cannot reasonably obtain" limb of *Bail* both shift once checking is cheap.
3. Proposing a frozen, public reference estimator with a published tolerance and required record, as a conformance standard that extends ISO 10845 into computation.

One open point should be checked before ch5 is written. Bajari, McMillan & Tadelis (2009) is reportedly the main economics source for the idea that competitive auctions discourage bidders from reporting design flaws; it is item 31, not yet verified. The Canadian contractor duty-to-warn case law (for example *Brown & Huston Ltd v York*) is also still unchecked. I could not locate either in this session.

---

## Part 5. The limits of automating procurement
*Literature review strand for* Fair and Reasonable / The Reasonable Bot *(Andre Comeau). Compiled 1 November 2026.*

### How this was checked, and what was not

Every citation below was confirmed to exist, either by opening the source or by a search result showing the title, venue or DOI. The verification level is marked on each entry:

- **[Read]**: I opened the source (abstract, paper or official page) and the findings come from it.
- **[Cited]**: the search confirmed title, authors, venue or DOI, but I did not open the text. The findings are from my prior knowledge of a well-known work and should be spot-checked before quoting numbers.
- **UNVERIFIED**: specific figures or claims I could not confirm in this session.

Both the session's web-fetch budget (100 per hour, shared) and its search budget (200 per turn) ran out near the end. A few items I planned to read (Project Vend posts, the Pactum/Walmart HBR article, the OECD procurement chapter body, the Canadian Directive text, the Robodebt recommendation wording) are therefore summarised from secondary coverage or prior knowledge and marked as such.

---

### Theme A: E-procurement. Digitising the process helps, but not where you'd expect

**A1. Lewis-Faupel, S., Neggers, Y., Olken, B. A. & Pande, R. (2016). "Can Electronic Procurement Improve Infrastructure Provision? Evidence from Public Works in India and Indonesia." *American Economic Journal: Economic Policy* 8(3): 258–283. DOI 10.1257/pol.20140258. NBER WP 20344: https://www.nber.org/papers/w20344 [Read: abstract]**
- The study uses staggered e-procurement rollout across Indian states and Indonesian districts. It finds **no reduction in prices paid**, but **better quality**: Indian roads met quality standards more often and Indonesian projects had fewer delays.
- Winners were more often from outside the region. The authors read this as selection: e-procurement lowers the cost of getting tender information and lets better contractors enter.
- **For the book:** This is the cleanest causal evidence that digitising the *tender channel* changes *who bids* more than *what the price is*. It supports the Scitovsky claim that lowering information costs shifts competition toward non-price value. It also cautions against promising that bots will lower prices.

**A2. Kovalchuk, A., Kenny, C. & Snyder, M. (2019). *Examining the Impact of E-Procurement in Ukraine: The Role of Competition and Transparency* (CGD Working Paper 511). Center for Global Development. https://www.cgdev.org/sites/default/files/examining-impact-e-procurement-ukraine.pdf [Read]**
- On ProZorro, the effect on bidder numbers is small and loses significance once fixed effects are added. Final prices sit about 3.5–5.8% further below estimates, but this is not robust. Contracts were signed about 5–6 days faster.
- The authors call the results "suggestive," not conclusive. The samples were narrow (above-threshold, single-lot tenders), pre-period data were weak, and the rules banned awards above the estimate, which contaminates the savings measure.
- **For the book:** ProZorro is the flagship "open data procurement" story, yet the rigorous evidence on price is modest. The reliable win is speed and transparency, not price discovery. This fits the book's "tender is the API" theme, since it mainly makes the record better. It also shows that **savings measured against an engineer's estimate depend on how the estimate was made**, which is the book's central difficulty.

**A3. OECD (2025). *Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions*, chapter "AI in public procurement." OECD Publishing. https://www.oecd.org/en/publications/2025/06/governing-with-artificial-intelligence_398fa287/full-report/ai-in-public-procurement_2e095543.html [Cited: page confirmed, chapter body not retrieved]**
- The report surveys about 200 government AI use cases across 11 functions, procurement among them. The abstract stresses fraud detection, forecasting and automated internal processes, alongside safeguards and "enablers."
- UNVERIFIED: the specific procurement findings (for example, which countries use AI for red-flagging, price benchmarking or document drafting).
- **For the book:** The OECD frames procurement AI mainly as **integrity analytics and back-office automation**, not as price-reasonableness adjudication. The book's evaluator would sit beyond the OECD's catalogue of current practice. That shows novelty, and also a lack of precedent.

**A4. OECD (2016). *The Korean Public Procurement Service: Innovating for Effectiveness*. OECD Public Governance Reviews. https://www.oecd.org/governance/the-korean-public-procurement-service/ [Cited]**
- This is the standard review of KONEPS, Korea's end-to-end national e-procurement system. KONEPS integrates registration, bidding, contracting and payment, and links to many government databases. It is usually credited with large transaction-cost savings and fewer opportunities for collusion through face-to-face contact.
- UNVERIFIED in this session: specific savings figures.
- **For the book:** KONEPS is the strongest real-world precedent for "canonical, machine-readable tender data" at national scale. Even KONEPS automates the *process* (forms, matching, payment) rather than the *judgement* of fair price. That is the boundary the book wants to cross.

**A5. European Commission. eForms: Commission Implementing Regulation (EU) 2019/1780, mandatory for EU notices from 25 October 2023. https://single-market-economy.ec.europa.eu/single-market/public-procurement/digital-procurement/eforms_en [Cited]**
- eForms replaces the old standard forms with a structured XML data standard, so every above-threshold EU notice becomes machine-readable. The Commission's earlier eProcurement policy (the 2012–2013 communications on end-to-end e-procurement) had set full digitalisation targets that were missed for years.
- **For the book:** This is direct institutional support for "PDFs should give way to canonical, versioned, machine-readable tender data." It also shows the limit. eForms standardises **notices**, not drawings, specifications or bills of quantities. The documents bidders actually price remain PDFs, which is the gap the book's API argument targets.

**A6. Open Contracting Partnership (2024). *Red Flags in Public Procurement: A Guide to Using Data to Detect and Mitigate Risks*; and the Open Contracting Data Standard (OCDS). https://www.open-contracting.org/resources/red-flags-in-public-procurement-a-guide-to-using-data-to-detect-and-mitigate-risks/ [Cited]**
- OCDS defines a shared JSON schema across the contracting lifecycle (planning, tender, award, contract, implementation). The red-flags guide lists data-driven indicators such as single bidding, short tender periods and price anomalies.
- **For the book:** OCDS is the nearest existing "protocol" in the Rao sense, and a natural standard for the book's public, versioned test set. Its weak spot is the same as the book's: OCDS captures **line-item prices** inconsistently, and that is the data a price-reasonableness bot needs.

**A7. Fazekas, M., Tóth, I. J. & King, L. P. (2016). "An Objective Corruption Risk Index Using Public Procurement Data." *European Journal on Criminal Policy and Research* 22(3): 369–397. [Cited from prior knowledge; not re-checked this session]**
- The paper builds a composite risk index from tender data (single bidder, short submission periods, unusual procedures) across Hungarian procurement. Risk indicators cluster in politically connected awards.
- **For the book:** It shows that screening procurement data at scale is feasible and produces **probabilities, not verdicts**. That is the same epistemic status the book gives its bot.

**A8. Sánchez-Graells, A. (2024). *Digital Technologies and Public Procurement: Gatekeeping and Experimentation in Digital Public Governance*. Oxford University Press. https://academic.oup.com/book/55898 [Read: publisher/university summary]**
- The book argues that "regulation by contract", where governments use procurement to impose AI safeguards, gives a "false sense of security." Buyers lack digital skills, are exposed to "policy irresistibility" around hyped technology, and cannot police vendors. It calls for moving "beyond AI regulation by contract."
- **For the book:** This is the most important legal-academic counterweight. If the "reasonable bot" standard is set *through procurement contracts* (buyers requiring bidders to use a conformance-tested bot), Sánchez-Graells predicts weak enforcement. The book should explain why an **independent standards body plus a public test set** is different from regulation by contract. It plausibly is different, and closer to his preferred external regulation.

---

### Theme B: The limits proper. Why contracts, and therefore tender documents, cannot be complete

**B1. Williamson, O. E. (1985). *The Economic Institutions of Capitalism*. Free Press. [Cited: canonical]**
- Bounded rationality plus opportunism make complete contracts impossible. Governance structures (hierarchy, relational contracting, hybrid forms) exist to handle what contracts cannot specify, and asset specificity raises hold-up risk.
- **For the book:** This grounds "starting a relationship expecting a divorce." Construction contracts are classic high-specificity, incomplete contracts. A bot can lower the cost of *writing and reading* the contract, but Williamson's argument rests on unforeseeable contingencies, which a bot does not remove.

**B2. Hart, O. & Moore, J. (1990). "Property Rights and the Nature of the Firm." *Journal of Political Economy* 98(6): 1119–1158; and Hart, O. (2017). "Incomplete Contracts and Control." *American Economic Review* 107(7): 1731–1752 (Nobel lecture). https://hart.scholars.harvard.edu/publications/incomplete-contracts-and-control [Cited]**
- When contracts are incomplete, what matters is who holds **residual control rights**, the right to decide when the contract is silent.
- **For the book:** The "keyholder" is a residual-control-rights construct: someone must decide when the bot's answer is not covered by the test set. Hart supports the book's insistence on a named human who answers for the number.

**B3. Tirole, J. (2009). "Cognition and Incomplete Contracts." *American Economic Review* 99(1): 265–294. https://publications.ut-capitole.fr/id/eprint/1180/ [Cited]**
- Contracts are incomplete because thinking about contingencies is **costly**. Parties choose how much effort to spend finding design flaws, and the buyer's choice affects the seller's hold-up power.
- **For the book:** This is the closest theoretical match to the book's thesis. If bots cut the cost of cognition, Tirole's model predicts **more complete contracts** and less hold-up. It also predicts that whoever has the better bot gains bargaining power, which supports Chapter 5's liability shift. This is perhaps the strongest academic ally the book has.

**B4. Bajari, P. & Tadelis, S. (2001). "Incentives versus Transaction Costs: A Theory of Procurement Contracts." *RAND Journal of Economics* 32(3): 387–407. https://ideas.repec.org/a/rje/randje/v32y2001i3p387-407.html [Cited]**
- Fixed-price contracts give strong cost incentives but make change orders costly. Cost-plus contracts adapt easily. Which is optimal depends on how complete the design is, and completing a design is costly.
- **For the book:** This formalises "one-shotted design locked for tender." The book's argument that bots make design completion cheaper implies, through Bajari–Tadelis, a shift toward fixed-price contracting. That is a testable prediction the book could state.

**B5. Bajari, P., Houghton, S. & Tadelis, S. (2014). "Bidding for Incomplete Contracts: An Empirical Analysis of Adaptation Costs." *American Economic Review* 104(4): 1288–1319. https://ideas.repec.org/a/aea/aecrev/v104y2014i4p1288-1319.html [Cited]**
- Using California highway paving auctions, the authors show that bidders **anticipate changes and quantity errors and skew their bids** (unit-price bid skewing). The adaptation costs of renegotiation are substantial. As I recall, they are on the order of 8–14% of the winning bid (UNVERIFIED figure, check before quoting).
- **For the book:** This is direct empirical support for "bidders who price drawing errors and claim later." It also complicates the price-reasonableness bot. Unit prices in public bid tabulations, the bot's training data, are **strategically distorted** by expected quantity overruns. A bot trained on TxDOT bid tabs learns skewed prices, not costs. The book should say this explicitly.

**B6. Flyvbjerg, B., Holm, M. S. & Buhl, S. (2002). "Underestimating Costs in Public Works Projects: Error or Lie?" *Journal of the American Planning Association* 68(3): 279–295. https://ppp.worldbank.org/library/underestimating-costs-public-works-projects-error-or-lie [Cited]**
- Across 258 transport projects, about 9 in 10 overran their cost estimates, by an average of 28%. The pattern has not improved over 70 years, and the authors attribute it to strategic misrepresentation rather than technical error.
- **For the book:** Pre-tender estimate error is dominated by **incentives, not arithmetic**. A more accurate bot does not fix misrepresentation, but a *published, rerunnable* bot could. That is a strong argument for the "defensibility over accuracy" distinction in chapter 7.

**B7. Autor, D. H. (2014). "Polanyi's Paradox and the Shape of Employment Growth." NBER Working Paper 20485 (Jackson Hole symposium). https://www.nber.org/papers/w20485 [Cited]**
- "We know more than we can tell." Tasks that rest on tacit knowledge resisted computerisation because nobody could write the rules down. Autor predicted that machine learning would erode the paradox through inference from examples rather than codified rules.
- **For the book:** An estimator's "feel" for a fair price is classic Polanyi knowledge. LLMs trained on bid data are exactly Autor's "inference from examples," which supports feasibility. Autor also stresses that such inference fails off-distribution, which limits a bot trained on Texas and tested in Alberta.

---

### Theme C: How accurate can price estimation get? (the 20% vs 2–3% question)

**C1. Federal Highway Administration (2015). *National Review of State Cost Estimation Practice* (Final Report, February 2015), FHWA National Review Program. https://www.fhwa.dot.gov/construction/contracts/2014cost.pdf [Read]**
- FHWA's 2004 *Guidelines on Preparing Engineer's Estimate, Bid Reviews and Evaluation* set the target that **the engineer's estimate should be within 10% of the low bid on at least 50% of projects**. Of 1,611 compliance-assessment projects, only **774 (48%) were within ±10%**.
- 74% of states build estimates mainly from historical bid data, 2% mainly from cost-based estimates, and 24% from both.
- **For the book: this is the single most important finding in this strand.** Human practice in the US highway sector does not reach ±10% half the time, and the official *target* is ±10% on only half of projects. The author's 2–3% "trust threshold" is **an order of magnitude stricter than what agencies require of human engineers**. Either the book drops the threshold, or it justifies it as a different measure (agreement with a reference estimate under a fixed protocol rather than distance from the low bid). The "conformance test vs accuracy" distinction in chapter 7 is the right place for that.

**C2. U.S. DOT Office of Inspector General (2019). *FHWA Lacks Adequate Oversight and Guidance for Engineer's Estimates*. Report ST2019020. https://www.oversight.gov/reports/audit/fhwa-lacks-adequate-oversight-and-guidance-engineers-estimates [Read: summary page]**
- FHWA had made "limited progress" on six key recommendations from its 2015 review and "lacks adequate guidance and processes to oversee and monitor the accuracy of Engineer's Estimates."
- **For the book:** The human baseline the bot competes with is itself weakly governed. That supports the case for a standard that is published, versioned and testable.

**C3. AACE International. Recommended Practice 18R-97, *Cost Estimate Classification System – As Applied in Engineering, Procurement, and Construction for the Process Industries*. [Cited via secondary summary: https://epcland.com/aace-estimate-classification-system/]**
- Expected accuracy (80% confidence ranges) runs from Class 5 (low −20% to −50%, high +30% to +100%) to **Class 1, at 65–100% design definition (low −3% to −10%, high +3% to +15%)**.
- **For the book:** Even the best class of *human* estimate in the profession's own standard allows −3% to −10% and +3% to +15%. The book's 2–3% sits at the **edge of Class 1**. The book could anchor its tolerance in AACE classes ("the reasonable bot must perform at Class 1 or 2 for a fully defined civil-works package"). That anchor would carry far more weight than an asserted 2–3%.

**C4. Mohamed, B. & Moselhi, O. (2022). "Conceptual estimation of construction duration and cost of public highway projects." *Journal of Information Technology in Construction (ITcon)* 27: 595–618. DOI 10.36680/j.itcon.2022.029. https://itcon.org/paper/2022/29 [Read]**
- An ensemble of ML models on public highway projects (2004–2015; roads, bridges, drainage) reports **cost MAPE of 4.5%** and duration MAPE of 7.4%, tested on samples of 29 and 56 projects.
- **For the book:** Single-digit MAPE is reported in the academic literature, but on small hold-out sets, with the *final* cost as target and project-level features. That is very different from the book's unit-price-by-line-item setting. Treat such figures as upper bounds on what is attainable, not as typical performance.

**C5. Elfaki, A. O., Alatawi, S. & Abushandi, E. (2014). "Using Intelligent Techniques in Construction Project Cost Estimation: 10-Year Survey." *Advances in Civil Engineering* 2014: 107926. https://doaj.org/article/0ee838af01634a2faf358e02f50a6a25 [Cited]**
- The survey covers ten years of ML, neural network, fuzzy and case-based reasoning approaches to construction cost estimation. It finds a field of many small, single-dataset studies with limited comparability and limited use in practice.
- **For the book:** The ML cost-estimation literature lacks shared benchmarks, which is the gap the book's "public versioned test set" would fill. This is a genuine contribution claim the book can make.

**C6. Wu, Y., Wang, L. & Liu, R. (2025). "CEQuest: Benchmarking Large Language Models for Construction Estimation." arXiv:2508.16081. https://arxiv.org/abs/2508.16081 [Read]**
- CEQuest has 164 multiple-choice and true/false questions on drawing interpretation, spatial reasoning and quantity takeoff. The best model, GPT-4.1, scored **75.4%**, and all models scored below 80%. In a case study, models rounded a 5.33 cy slab to 5 cy where estimators round up. Explanations were often plausible but logically flawed.
- **For the book:** General-purpose LLMs still fail basic estimating judgement. The rounding example is a neat illustration of "domain convention" knowledge that a conformance test must encode.

**C7. Kondratenko, A., Birhane, M., Hsain, H. E. & Maciocci, G. (2026). "AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawing Understanding." arXiv:2601.04819. https://arxiv.org/abs/2601.04819 [Read]**
- Frontier multimodal models (Gemini 3 Pro, GPT-5.2, Claude Opus 4.5 and others) reach about 0.95 on OCR-type questions but only **0.4–0.55 exact-match accuracy on counting symbols**. Gemini 3 Pro scored 0.39 on doors and 0.34 on windows. Bedrooms and toilets score much better (0.82–0.89) because they carry text labels. The authors conclude that models lack "robust drawing literacy" and recommend human-in-the-loop workflows.
- **For the book:** **Takeoff from drawings, not pricing, is the binding constraint.** Machines read text well and graphics poorly. This strongly supports the book's argument that tenders should ship as machine-readable data (quantities as data, not PDF drawings). The "tender is the API" chapter is the fix for the failure this benchmark measures.

**C8. Jung, Y., Fu, J. & Golparvar-Fard, M. (2026). "DrawingVQA: A Real-World Benchmark for Multi-Depth Visual-Textual Reasoning on Construction Drawings." arXiv:2607.15418. https://www.alphaxiv.org/abs/2607.15418 [Read: abstract page]**
- On 33 issued-for-construction structural drawing sets, Gemini-2.5-pro scored **71.7% overall vs 94.9% for experienced professionals**, and **55.6% vs 93.3% on expert-reasoning questions**. Humans answered only a 20-question subset, so the comparison is not like-for-like.
- **For the book:** A 20–40 point gap on expert reasoning in mid-2026 suggests the author's "within ~20%" bot result reflects the field accurately. Closing to Class-1 accuracy from drawings alone is not in sight.

**C9. Chicelli, B., Alves, H., Anselmo, R., Weinberg, J., Lemos, F. & Baryla, J. (2026). "Handoff-H1: An Orchestrated Vision-Agent System for Material Quantity Takeoff from Construction Blueprints." arXiv:2608.15032 (Handoff AI). https://arxiv.org/abs/2608.15032 [Read]**
- On their own 10-set residential benchmark, the agentic system scored a composite of 81.6 vs 77.6 for independent estimators, with higher coverage but lower precision. **More than one in five matched quantities fell outside a ±25% tolerance.** Siding and other continuous-measurement trades were weakest. The best plain frontier model scored 61.4.
- Caveats: the benchmark, gold standard and LLM judge all come from the vendor, and the system is proprietary.
- **For the book:** This is the best current evidence that **orchestrated agents plus a knowledge base beat raw LLMs**, and that they rival humans on coverage. The ±25% tolerance and vendor-run evaluation also illustrate why the book's demand for an *independent, public, frozen* test set matters. Industry already publishes self-graded benchmarks.

**C10. Wong, S., Zheng, C., Su, X. & Tang, Y. (2023). "Construction contract risk identification based on knowledge-augmented language model." arXiv:2309.12626 (later published in *Computers in Industry*, UNVERIFIED). https://arxiv.org/abs/2309.12626 [Read]**
- GPT-4 is augmented with retrieved clause and expert-review knowledge, plus repeated sampling and majority voting, to flag risky EPC contract clauses. Results are **qualitative only**: two worked clauses, with no accuracy metrics reported.
- **For the book:** Much of the LLM-for-contracts literature reports demos, not error rates. That matches the book's complaint that nobody publishes the error rate. Majority voting over samples is also a workaround for non-determinism (see E8–E9).

**C11. Moon, S., Chi, S. & Im, S. (2022). "Automated detection of contractual risk clauses from construction specifications using bidirectional encoder representations from transformers (BERT)." *Automation in Construction* 142: 104465. DOI 10.1016/j.autcon.2022.104465 [Cited]**
- A fine-tuned BERT classifies risk clauses in construction specifications. Accuracy figures are UNVERIFIED, since I could not retrieve the abstract metrics.
- **For the book:** This is part of a substantial Korean and Chinese NLP-on-specifications literature (alongside the "poisonous clause" extraction work at Ewha and others). Pre-LLM supervised models give measurable F1 on narrow tasks. That design, narrow task plus labelled test set plus reported error, is the one the book proposes for pricing.

**C12. Huber, M. & Imhof, D. (2019). "Machine learning with screens for detecting bid-rigging cartels." *International Journal of Industrial Organization* 65: 277–301. https://ideas.repec.org/a/eee/indorg/v65y2019icp277-301.html [Cited]**
- Statistical screens on bid distributions (variance, skewness, gap between the lowest bids) are fed to ML classifiers. Trained on Swiss construction cartel cases, they correctly classify most tenders as collusive or competitive. The figure is roughly 80%+ as I recall (UNVERIFIED).
- **For the book:** Public bid tabulations, the book's "price book," can be mined not only for fair price but for **evidence of unfair price**. A reasonable-price bot should probably include a collusion screen. A reasonable price derived from a cartelised market is not a fair one.

---

### Theme D: Automated bidding, negotiation and pricing agents

**D1. Calvano, E., Calzolari, G., Denicolò, V. & Pastorello, S. (2020). "Artificial Intelligence, Algorithmic Pricing, and Collusion." *American Economic Review* 110(10): 3267–3297. DOI 10.1257/aer.20190623 [Cited]**
- Simple Q-learning pricing agents in repeated oligopoly simulations learn to charge **supra-competitive prices without communicating**, sustained by reward-punishment strategies.
- **For the book: a candid challenge.** If every bidder runs the same "standard bot" to price, the standard bot becomes a **focal point and a hub** (the "hub-and-spoke" worry). A published reference price may anchor bids upward toward it rather than discipline them. The book should consider whether the standard bot is for the **buyer's evaluation only**, and whether bidders' use of it should be watched.

**D2. Assad, S., Clark, R., Ershov, D. & Xu, L. (2024). "Algorithmic Pricing and Competition: Empirical Evidence from the German Retail Gasoline Market." *Journal of Political Economy* 132(3): 723–771. DOI 10.1086/726906 [Cited]**
- This is the first large-scale empirical evidence. Adopting algorithmic pricing software raised margins mainly **when competing stations both adopted**. In duopoly markets where both adopted, margins rose by roughly 28% (figure from memory, UNVERIFIED).
- **For the book:** Same caution as D1, now with real-world evidence. Symmetric adoption of pricing algorithms can soften competition. Sealed-bid one-shot tenders are less exposed than daily gasoline pricing, but repeated public tenders with published bid tabs are a repeated game.

**D3. Fish, S., Gonczarowski, Y. A. & Shorrer, R. I. (2024). "Algorithmic Collusion by Large Language Models." arXiv:2404.00806 (presented at the 2025 ASSA meetings). https://arxiv.org/abs/2404.00806 [Cited]**
- LLM-based pricing agents in simulated oligopolies quickly reach supra-competitive prices. Small, innocuous-looking changes in prompt wording change how much they collude.
- **For the book:** This extends D1 to exactly the kind of agent the book proposes. It also shows **prompt sensitivity**: behaviour depends on wording. That is a strong argument for the book's insistence on a frozen, published configuration (weights *and* prompt *and* harness).

**D4. Ezrachi, A. & Stucke, M. E. (2016). *Virtual Competition: The Promise and Perils of the Algorithm-Driven Economy*. Harvard University Press. [Cited: canonical]**
- The book sets out four scenarios: algorithms as messenger, hub-and-spoke, "predictable agent," and "digital eye" autonomous collusion. Competition law built on human agreement struggles with each.
- **For the book:** It supplies the vocabulary for the collusion risk of a shared standard bot. The "hub-and-spoke" scenario, where competitors share a single pricing provider, maps directly onto a public reference bot used by all bidders.

**D5. Jennings, N. R., Faratin, P., Lomuscio, A. R., Parsons, S., Wooldridge, M. J. & Sierra, C. (2001). "Automated Negotiation: Prospects, Methods and Challenges." *Group Decision and Negotiation* 10(2): 199–215. DOI 10.1023/A:1008746126376 [Cited]**
- This is the foundational framing paper. Automated negotiation needs a negotiation protocol, a negotiation object and agents' decision models. Game-theoretic, heuristic and argumentation-based approaches each fail under different assumptions, chiefly unbounded rationality versus incomplete information.
- **For the book:** It anticipates "protocol" thinking by 25 years. The "negotiation object" is what construction lacks: the object is a set of drawings, not a parameterised offer space. That again supports "the tender is the API."

**D6. Baarslag, T., Aydoğan, R., Hindriks, K. V., Fujita, K., Ito, T. & Jonker, C. M. (2015). "The Automated Negotiating Agents Competition, 2010–2015." *AI Magazine* 36(4): 115–118. https://ojs.aaai.org/index.php/aimagazine/article/view/2609; and Baarslag et al. (2012). "The First Automated Negotiating Agents Competition (ANAC 2010)." In *New Trends in Agent-Based Complex Automated Negotiations*, Springer. [Cited]**
- ANAC is a yearly tournament (the GENIUS platform) for bilateral multi-issue negotiation agents. Strategies that do well in one tournament often do poorly in the next domain, which shows that negotiation performance is domain-sensitive.
- **For the book:** ANAC is a working model of the book's protocol idea: a **public, versioned environment where anyone's agent is run against the same test**. It is a precedent for a "Fair and Reasonable Evaluator" competition.

**D7. Sandholm, T. (2007). "Expressive Commerce and Its Application to Sourcing: How We Conducted $35 Billion of Generalized Combinatorial Auctions." *AI Magazine* 28(3): 45–58; and Sandholm, T., Levine, D., Concordia, M., Martyn, P., Hughes, R., Jacobs, J. & Begg, D. (2006). "Changing the Game in Strategic Sourcing at Procter & Gamble: Expressive Competition Enabled by Optimization." *Interfaces* 36(1): 55–68. [Cited]**
- Through CombineNet, suppliers bid with rich expressions (bundles, discounts, conditions), and optimisation clears the market. Sandholm reports around 12.6% average savings over prior prices across many events (figure from memory, UNVERIFIED). P&G is the flagship case.
- **For the book:** This is the strongest success story for automated procurement, and it works because **goods and logistics lanes can be specified completely**. Construction works rarely can. It sharpens the book's point that the limit is specification, not computation.

**D8. Van Hoek, R., DeWitt, M., Lacity, M. & Johnson, T. (2022). "How Walmart Automated Supplier Negotiations." *Harvard Business Review* (November 2022). [Cited via secondary sources; HBR text not retrieved]**
- Walmart used Pactum's chatbot to negotiate terms with tail-spend suppliers. Secondary reports (PYMNTS 2023; Harvard PON) say about **75% of suppliers preferred the bot** to a human buyer. Widely quoted pilot figures (roughly 64% of suppliers reaching agreement, ~1.5% savings and payment terms extended to about 35 days) are UNVERIFIED from the primary source.
- **For the book:** This is a real-world autonomous procurement negotiation at scale. It is confined to **tail spend with standard terms**, the low-specificity end of Williamson's spectrum. Construction sits at the other end.

**D9. Bianchi, F., Chia, P. J., Yuksekgonul, M., Tagliabue, J., Jurafsky, D. & Zou, J. (2024). "How Well Can LLMs Negotiate? NegotiationArena Platform and Analysis." *Proceedings of ICML 2024*, PMLR 235. https://proceedings.mlr.press/v235/bianchi24a.html [Cited]**
- Running LLM-vs-LLM negotiations, the authors find that behavioural tactics (for example, feigning desperation) can shift outcomes by large margins. LLMs show human-like irrationalities such as anchoring, and some act irrationally in simple games.
- **For the book:** LLM negotiators are manipulable through style. A bid-evaluation bot that reads bidder narratives (qualifications, clarifications) is exposed to the same thing. That argues for evaluating **structured data** rather than prose.

**D10. Bansal, G., Hua, W., Huang, Z., Fourney, A., ... Horvitz, E. & Amershi, S. (2025). "Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets." arXiv:2510.25779 (Microsoft Research). https://arxiv.org/abs/2510.25779 [Read]**
- In simulated two-sided markets, all models showed severe **first-proposal bias**: the first offer was accepted 60–100% of the time, a 10–30× advantage for speed over quality. Welfare **fell as the number of options grew** (−65% for Sonnet-4 in one setting). Weaker models were vulnerable to manipulation and prompt injection that redirected payments. Frontier models approached optimal welfare only under perfect search.
- **For the book:** This is direct evidence that **agentic buyers do not yet evaluate competing offers well**, which is exactly the buyer-side task the book automates. Its "consideration set" failure is a strong argument for the book's design: the bot should check *one price against a reference*, not choose among many offers.

**D11. Anthropic (2025). "Project Vend: Can Claude run a small shop? (And why does that matter?)" (with Andon Labs), June 2025, https://www.anthropic.com/research/project-vend-1; and "Project Vend: Phase two," December 2025, https://www.anthropic.com/news/project-vend-2 [Cited: pages confirmed; findings from secondary coverage, e.g. The Decoder, Gigazine]**
- Over about a month, "Claudius" (Claude Sonnet 3.7) ran an office vending business. It **lost money**: it sold items below cost, gave in to requests for discounts, ignored a lucrative offer, hallucinated payment details and briefly confused its own identity. Phase two, with better tools, scaffolding and a supervisory "CEO" agent, reportedly became profitable, though failures persisted.
- **For the book:** This is a vivid case where **pricing judgement under social pressure** fails: the bot priced to please its counterparty. It also shows that scaffolding (tools, procedures, oversight agents) matters as much as the model, which supports the book's "standard = bot + harness + record."

---

### Theme E: Humans in the loop, accountability, and machine evidence

**E1. Bainbridge, L. (1983). "Ironies of Automation." *Automatica* 19(6): 775–779. DOI 10.1016/0005-1098(83)90046-8 [Cited]**
- Automating the routine leaves humans the hardest, rarest cases. Their skills decay because they no longer practise, and monitoring is something humans do badly.
- **For the book:** **The keyholder irony.** If the bot prices routine items and the keyholder only signs, the keyholder loses the estimating skill needed to challenge the bot in the hard case. The book should state how keyholders stay in practice, for example through periodic manual estimates, as pilots fly manual approaches.

**E2. Parasuraman, R. & Manzey, D. H. (2010). "Complacency and Bias in Human Use of Automation: An Attentional Integration." *Human Factors* 52(3): 381–410. DOI 10.1177/0018720810376055 [Cited]**
- Automation complacency and automation bias are robust, affect experts as well as novices, and are not cured by training alone. Reliable automation produces *more* complacency.
- **For the book:** A bot that is right 97% of the time is the most dangerous kind for a human sign-off. The keyholder model needs structural safeguards, not just a signature.

**E3. Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F. & Lakhani, K. R. (2023). "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality." Harvard Business School Working Paper 24-013. SSRN 4573321; later published in *Organization Science* (2025, UNVERIFIED details). [Cited]**
- In a field experiment, BCG consultants using GPT-4 did markedly better on tasks inside the AI's capability frontier. On a task just outside it, they were about 19 percentage points **less** likely to reach the correct answer than consultants without AI (figure from memory).
- **For the book:** Professional judgement degrades exactly where the bot is wrong but plausible. That is the case the keyholder exists for, and where the keyholder is weakest.

**E4. Green, B. (2022). "The Flaws of Policies Requiring Human Oversight of Government Algorithms." *Computer Law & Security Review* 45: 105681. DOI 10.1016/j.clsr.2022.105681. arXiv:2109.05067 [Read: abstract]**
- A survey of 41 policies finds they assume humans can oversee algorithms. The evidence says they cannot, and the requirement **legitimises flawed algorithms** while giving a "false sense of security." Green proposes *institutional* oversight instead: agencies must justify adoption with empirical evidence that the proposed human oversight works, followed by public review.
- **For the book: the sharpest challenge to the "keyholder."** A human signing for the bot's number may be accountability theatre. The book's better defence is its *institutional* element: the public test set, published error rate and rerunnable standard. That is Green's remedy. The book should lead with it and treat the keyholder as secondary.

**E5. Elish, M. C. (2019). "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction." *Engaging Science, Technology, and Society* 5: 40–60. https://estsjournal.org/index.php/ests/article/view/260 [Cited]**
- In automated systems, blame lands on the nearest human operator, who acts as a "moral crumple zone," even when that person had little real control (the Air France 447 and Three Mile Island cases).
- **For the book:** The keyholder risks becoming the crumple zone for the standard bot's errors. The book should make the keyholder's duty **procedural** (followed the protocol, kept the record) rather than **substantive** (the number was right).

**E6. Royal Commission into the Robodebt Scheme (2023). *Report*. Commonwealth of Australia, 7 July 2023. Overview: https://www.apra.gov.au/sites/default/files/2024-02/Robodebt%20Royal%20Commision%20-%20Overview%20of%20Final%20Report.pdf [Read: overview]**
- An automated income-averaging debt scheme raised inaccurate and **unlawful** debts. Legal concerns were suppressed through "dishonesty and collusion," and institutional checks (the Ombudsman, the AAT and others) failed.
- The recommendations include more review and oversight of automated decision-making. I recall Recommendation 17.1 calling for a legislative framework, a clear path for review and publication of business rules for independent expert scrutiny (wording UNVERIFIED).
- **For the book:** The failure was not the algorithm's arithmetic but **reversing the burden of proof onto the citizen**, plus secrecy. The book's "anyone can rerun" principle is the direct antidote. Publishing the business rules is close to the book's "published standard bot."

**E7. Amnesty International (2021). *Xenophobic Machines: Discrimination through Unregulated Use of Algorithms in the Dutch Childcare Benefits Scandal*. EUR 35/4686/2021. https://www.amnesty.org/en/documents/eur35/4686/2021/en/ [Cited]**
- The Dutch tax authority's self-learning risk-classification model used nationality as a risk factor. Flagged parents faced aggressive fraud investigations and repayments, with tens of thousands affected, and the government resigned in January 2021. The model was a black box to the officials who acted on it.
- **For the book:** A **risk score treated as a verdict**, with officials deferring to it, is exactly what Parasuraman (E2) predicts. It warns that a bot flagging a bid as "unreasonable" may be treated as decisive. The book's tolerance band and required record are the safeguards to emphasise.

**E8. *Bates & Others v Post Office Ltd (No 6) "Horizon Issues"* [2019] EWHC 3408 (QB), Fraser J. https://www.judiciary.uk/wp-content/uploads/2019/12/bates-v-post-office-appendix-2.pdf [Cited]**
- The court found that Horizon contained bugs, errors and defects capable of causing branch shortfalls, and that the Post Office's assertions of Horizon's robustness were not justified. Hundreds of sub-postmasters had been prosecuted on Horizon data.
- **For the book: the defining "bot in the witness box" cautionary tale.** Machine output was treated as presumptively reliable, and disclosure of the system's known error log was resisted. The book's demand for a **known error rate and an open, rerunnable bot** is the inverse of Horizon practice. The book should cite this explicitly.

**E9. Marshall, P., Christie, J., Ladkin, P. B., Littlewood, B., Mason, S., Newby, M., Rogers, J., Thimbleby, H. & Thomas, M. (2021). "Recommendations for the probity of computer evidence." *Digital Evidence and Electronic Signature Law Review* 18: 18–26. DOI 10.14296/deeslr.v18i0.5240 [Read: abstract]**
- The central problem, they argue, is "the evidential presumption that computers are reliable," which is unwarranted. Their recommendations (written for the Ministry of Justice) focus on staged disclosure of known errors, change logs and quality-management records.
- **For the book:** The "required record" in the book's protocol should mirror these recommendations: error logs, version history and test results disclosed on challenge.

**E10. Ministry of Justice (UK) (2025). *Use of evidence generated by software in criminal proceedings: Call for evidence*. Published 21 January 2025, closed 15 April 2025. https://www.gov.uk/government/calls-for-evidence/use-of-evidence-generated-by-software-in-criminal-proceedings [Read]**
- The common-law presumption that a computer was operating correctly replaced s.69 PACE 1984, which was repealed by s.60 of the Youth Justice and Criminal Evidence Act 1999 following the Law Commission's 1997 recommendation. The call asks whether the presumption is fit for purpose and puts **AI and algorithm-generated evidence in scope**, while merely recorded data (photos, texts) is out of scope.
- **For the book:** The UK is actively rethinking whether machine output deserves a presumption of reliability. The book's answer is a presumption earned through a conformance test, not assumed. It is a constructive middle position the book can claim.

**E11. Proposed U.S. Federal Rule of Evidence 707 ("Machine-Generated Evidence"). Approved for publication by the Advisory Committee on Evidence Rules (2 May 2025, 8–1, DOJ dissenting) and the Standing Committee (10 June 2025). Public comment 15 August 2025 to 16 February 2026. [Read: secondary legal coverage, National Law Review / Proskauer, https://natlawreview.com/article/machine-generated-evidence-challenges-federal-rules-inside-contested-proposed; Lexvisio, 26 Aug 2026]**
- Rule 707 would subject machine output offered *without* a sponsoring expert to the Rule 702 reliability standard (sufficient facts or data, reliable methods, reliable application), with an exception for simple instruments.
- Commenters attacked it as overbroad (GPS, surveillance footage), too narrow (it misses deepfakes), costly for under-resourced parties, and redundant (DOJ, ABA). **In May–June 2026 the committees declined to advance it** and sent it back for further study, with an expert mini-conference at the October 2026 meeting.
- **For the book: timely and double-edged.** The legal system *wants* a Daubert-style test for machine output, which supports the "reasonable bot with a known error rate." Yet the first serious attempt stalled because nobody could define the boundary or bear the cost of challenging AI. The book's **pre-certified, public conformance test** is one answer to the cost objection: the test is done once, publicly, rather than relitigated in every case. The book should say so.

**E12. Treasury Board of Canada Secretariat. *Directive on Automated Decision-Making* (in force 2019; third-review amendments effective April 2023), with the *Algorithmic Impact Assessment* (AIA) tool. https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592; amendments notice: https://www.canada.ca/en/government/system/digital-government/policies-standards/policy-service-digital-announcements/amendments-directive-automated-decision-making.html [Read: amendments notice; directive text blocked to the fetcher, details from prior knowledge]**
- The Directive applies to systems "developed or procured to support administrative decisions." The 2023 amendments extended it to internal services, required publishing the AIA and a peer-review summary before production, and strengthened explanation and bias-testing requirements.
- From prior knowledge (re-check): the AIA assigns impact levels I–IV, and the higher levels require peer review, human intervention before a final decision, and plain-language explanations. A fourth review was under way in 2025–26.
- **For the book: directly relevant to a Canadian author.** A federal bid evaluation or price-reasonableness determination arguably *is* an administrative decision affecting an external party (the bidder). If so, a government "Fair and Reasonable Evaluator" would trigger an AIA, publication and probably human-in-the-loop requirements. The book should check whether contract-award decisions fall within the DADM's scope, which is UNVERIFIED and worth a footnote. The DADM's published AIA plus peer review is already a template for "standard = public test + required record."

**E13. Sánchez-Graells, A. (2021). "Where does the proposed EU AI Act place procurement?" *How to Crack a Nut* blog, republished by Competition Policy International, 29 October 2021. https://www.pymnts.com/cpi-posts/where-does-the-proposed-eu-ai-act-place-procurement/ [Read]**
- The AI Act takes an "extremely light-touch approach" to AI used *in* public procurement: it is not among the Annex III high-risk uses, which centre on law enforcement, justice, migration and access to public benefits. Procurement is left to voluntary codes, and the Act is mainly aimed at the private sector.
- The final AI Act (Regulation (EU) 2024/1689) did not, to my knowledge, add procurement decisions to Annex III (UNVERIFIED against the final text). The Commission's separate *model contractual AI clauses* (2023) address buying AI, not using it in procurement.
- **For the book:** In the EU, a price-reasonableness bot in procurement is **largely unregulated by the AI Act**. That leaves room for the book's voluntary standard and also means no regulatory forcing function exists. The book should distinguish procuring AI (heavily discussed) from AI doing procurement (barely regulated).

---

### Theme F: Reproducibility and model drift (the pinned-weights argument)

**F1. Chen, L., Zaharia, M. & Zou, J. (2024). "How Is ChatGPT's Behavior Changing Over Time?" *Harvard Data Science Review* 6(2) (issue number UNVERIFIED). https://hdsr.mitpress.mit.edu/pub/y95zitmz; arXiv:2307.09009 (2023) [Read]**
- Between March and June 2023, GPT-4's accuracy on identifying prime numbers fell from **84% to 51%**. Its willingness to answer sensitive questions changed, code formatting errors rose and instruction-following declined. The authors conclude that the "same" LLM service can change substantially within months, so continuous monitoring is needed.
- **For the book:** This is direct support for **pinned, open weights**. A standard bot accessed through a commercial API is not the same bot from month to month, so its error rate is not a fact about anything stable.

**F2. He, H. & Thinking Machines Lab (2025). "Defeating Nondeterminism in LLM Inference." *Connectionism* blog, 10 September 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference [Read]**
- Even at temperature 0, output varies across runs because inference kernels are **not batch-invariant**: results depend on server load and batch size. In 1,000 runs of the same prompt on Qwen3-235B, there were **80 distinct outputs**, diverging at token 103. With batch-invariant kernels, all 1,000 runs were identical.
- **For the book: a refinement the book needs.** **Pinning weights is necessary but not sufficient.** To be "rerunnable by anyone," the standard must also pin the inference stack (kernels, precision, batch-invariant settings), the prompt, the tools and the decoding parameters. Alternatively, it must define conformance statistically over N runs. Both are feasible, and the book should say which it means.

---

### Synthesis: what is known about the limits, what isn't, and where the reasonable bot sits

**What is known.** There is a substantial literature on the limits of automating procurement, though it is scattered across fields that rarely cite each other.

- **Economics**, from Williamson and Hart through Tirole and Bajari–Tadelis, explains why construction contracts *cannot* be complete. The empirical work (Bajari, Houghton & Tadelis; Flyvbjerg) shows that bid prices embed strategic responses to that incompleteness. Historical bid tabs are therefore a skewed price signal, not a cost signal.
- **E-procurement evaluations** (Lewis-Faupel et al.; ProZorro; KONEPS; eForms) show that digitising the *channel* reliably improves speed, transparency and entry, but has weak or no effect on price.
- **Automated sourcing and negotiation** (Sandholm, Pactum, ANAC) works where the object can be fully specified, and struggles where it cannot.
- **Algorithmic pricing research** (Calvano; Assad; Fish et al.) shows that shared or symmetric pricing agents can soften competition.
- **Human-factors and public-administration research** (Bainbridge; Parasuraman; Green; Elish; Robodebt; the Dutch scandal; Horizon) shows that a human "in the loop" is a weak safeguard and that presumptions of machine reliability cause serious injustice.
- **Current construction-AI benchmarks** (CEQuest; AECV-Bench; DrawingVQA; Handoff-H1) show that the binding constraint is reading drawings, not pricing. Expert-reasoning accuracy trails professionals by 20–40 points, and the best agentic takeoff still misses ±25% on a fifth of items.
- On the human baseline, the evidence is striking. **US engineer's estimates fall within ±10% of the low bid only about half the time**, and the profession's best estimate class (AACE Class 1) tolerates −3% to −10% and +3% to +15%.

**What isn't known.**
- No published study measures the *line-item unit-price* accuracy of an ML or LLM estimator against bid tabulations under a public, frozen protocol. Every figure is on private data, project-level totals or vendor-run benchmarks.
- No one has studied how a **shared public reference bot** changes bidding behaviour: whether it anchors, coordinates or disciplines prices.
- No court has yet set an admissibility standard for AI-generated valuation evidence. FRE 707 stalled in 2026, and the UK review is open.
- It is unclear whether Canada's DADM covers contract-award decisions.
- No study tests whether a "keyholder" sign-off adds accuracy or merely transfers blame.

**Where the book sits.**
- The "reasonable bot / conformance-test standard" sits in the gap between these literatures. It responds to the main critiques:
  - to Green's critique of human oversight, with institutional oversight (a public test set and published error rate);
  - to Horizon and the presumption of reliability, with a reliability that is earned and can be rebutted;
  - to FRE 707's cost objection, with certification done once in public rather than relitigated case by case;
  - to Chen et al. and the nondeterminism work, with pinned weights, which must be extended to a pinned inference stack;
  - to the AECV-Bench and DrawingVQA failures, with "the tender is the API," which removes drawing-reading from the critical path.
- Three things cut against the book, and it should say so:
  - (1) the 2–3% threshold is far stricter than any human standard. It is best reframed through AACE classes or as agreement under a protocol, not distance from the low bid;
  - (2) bid-tab training data are strategically skewed;
  - (3) a common public pricing bot used *by bidders* raises algorithmic-collusion and hub-and-spoke concerns. The safest framing is a buyer-side evaluator plus a collusion screen.
- **Tirole's "cognition and incomplete contracts"** is the most natural theoretical home for the book. If bots make thinking about contingencies cheap, contracts become more complete and hold-up power shifts to whoever thinks best. That is the book's liability-shift chapter in formal dress.

---

## Part 6. Verification pass and gap-filling (corrections win)
Session date: 1 November 2026. The shared WebFetch budget (100 per hour, all agents) refused many calls during this pass, so much confirmation relies on search-engine listings and snippets. Each label means:

- **VERIFIED**: I opened the source, or an authoritative listing confirms it. URL given.
- **CORRECTED**: An earlier strand had it wrong. The right details are given.
- **PARTLY VERIFIED**: The core facts are confirmed but some details are not. What is unconfirmed is stated.
- **STILL UNVERIFIED**: I could not confirm it in this session.

**Corrections to earlier strands, in brief** (details below):

1. **ISO 16739-1:2018 (IFC 4) has been superseded by ISO 16739-1:2024 (IFC 4.3).** IFC 4.3 adds roads, rail, bridges and ports, which matters for the book's civil-works pilot. This corrects strand 3, item 48.
2. **The claim that there is "no settled Canadian authority" for a bidder duty to raise errors before close (strand 3, item 41) is incomplete.** Quebec appellate law recognises a bidder's *duty to inquire* (obligation de se renseigner) as the corollary of the owner's duty to inform (*AMT c. Sintra*, 2024 QCCA 500). At common law there is a contractor *duty to warn* of design defects (*Brunswick Construction v Nowlan*, SCC 1974/75), though it concerns performance, not the bid stage.
3. ***Brown & Huston Ltd v York (City)* (Ont CA 1985) could not be found** in any searchable source. Treat it as STILL UNVERIFIED and do not cite it.
4. **AACE 18R-97 applies to the process industries.** The road and rail analogue is **AACE 98R-18**. The Class 1 range (−3% to −10% / +3% to +15%) is confirmed, but only via secondary tables. Class 1 maturity is 65–100% in the current revision; older summaries say 50–100%.
5. **Bajari, McMillan & Tadelis (2009) is now VERIFIED**, including the design-flaw finding (strand 3, item 31). The design-flaw point is argued from theory and industry sources, not tested directly. The authors say so themselves.
6. **New and important: Texas law.** Texas, the book's development-data state, has *codified* a contractor's duty to disclose known design defects in writing (Tex. Bus. & Com. Code §59.051, 2021). The test is "ordinary diligence," defined as the observations a contractor would make **in preparing a bid**. VERIFIED. This partly cuts against the book's ch5 "no compelled disclosure" line.
7. **FRE 707 (strand 4, item E11) needs refining.** In May 2026 the Advisory Committee **withdrew** the published rule and is studying a substantially revised version that "would ordinarily require an expert." The October 2026 meeting held a mini-conference. VERIFIED from the October 2026 agenda book.
8. **Kawai & Nakabayashi (strand 3, item 34):** the sample is about **42,000** auctions, not about 70,000. Pages are 1364–1411. VERIFIED.

---

### 1. Bajari, McMillan & Tadelis (2009): VERIFIED

**Citation:** Bajari, P., McMillan, R. S. & Tadelis, S. (2009). "Auctions versus Negotiations in Procurement: An Empirical Analysis." *Journal of Law, Economics, and Organization* 25(2): 372–399. NBER Working Paper 9757 (June 2003), DOI 10.3386/w9757. Sources: https://nber.org/papers/w9757 (opened); working-paper PDF https://www.nber.org/papers/w9757.pdf (opened).

**Findings:**
- **Data.** About 4,100 private non-residential building projects in Northern California, 1995–2000 (Table 4.2 totals 4,087).
  - 43.3% were negotiated (1,769 projects).
  - 56.7% were auctioned: invited bidders 37.2%, open bidding 18.4%, prequalified bidders 1.1%.
- **Main result.** Auctions perform poorly when projects are complex, contract design is incomplete, or there are few bidders. Complex projects tend to be negotiated.
- **Communication.** Abstract: "auctions stifle communication between buyers and the sellers, preventing the buyer from utilizing the contractor's expertise."
- **Design flaws.** The working-paper text says:
  - "contractors strategically read the plans and specifications to determine where they will fail" (p. 10);
  - "a contractor has an incentive to hide information about possible design flaws, submit a low bid" (p. 20);
  - "Competitive bidding may therefore leads to adverse selection, which is more problematic when projects are complex" (p. 11).
- **Caveat.** The authors admit they cannot separate the communication story from an "ex ante coordination" story (p. 16). The design-flaw mechanism is argued from theory and industry interviews, not tested statistically.

**Relevance:** This is the economics citation for the ch5 claim that sealed-bid competition rewards silence about design errors. The book should cite it as "argued, consistent with the data," not as a causal finding. Page numbers above are from the NBER working paper; check them against the JLEO version before quoting.

### 2. Bajari, Houghton & Tadelis (2014) AER: VERIFIED

**Citation:** Bajari, P., Houghton, S. & Tadelis, S. (2014). "Bidding for Incomplete Contracts: An Empirical Analysis of Adaptation Costs." *American Economic Review* 104(4): 1288–1319. DOI 10.1257/aer.104.4.1288. IDEAS listing with abstract: https://ideas.repec.org/a/aea/aecrev/v104y2014i4p1288-1319.html (opened).

**Finding confirmed.** The abstract states that "adaptation costs account for 7.5-14 percent of the winning bid." Markups from private information and market power are "much smaller" by comparison. The data are California highway paving contracts.

**Relevance:** The 7.5–14% figure in strands 3 and 4 is correct and can be quoted.

### 3. FHWA (2015) National Review of State Cost Estimation Practice: VERIFIED

**Citation:** FHWA Resource Center, Construction & Project Management Technical Service Team (2015). *National Review of State Cost Estimation Practice*, Final Report, February 2015, FHWA National Review Program. https://www.fhwa.dot.gov/construction/contracts/2014cost.pdf (opened).

**Confirmed:**
- Of **1,611 projects**, **774 (about 48%)** had a low bid within ±10% of the engineer's estimate. The median by state is 47% (SD 13%). The report calls this "slightly under" the guideline.
- The 2004 *Guidelines on Preparing Engineer's Estimate, Bid Reviews and Evaluation* state that "the engineer's estimate should be within 10 percent of the low bid for at least 50 percent of the projects." The report dates the guidelines both 20 and 30 January 2004; cite them as January 2004.
- The guideline measures the 10% against the low bid, while the review's band is framed around the estimate. This mismatch is minor but worth a footnote.

### 4. AACE 18R-97 Class 1 accuracy range: PARTLY VERIFIED, with a correction on scope

- **Range confirmed.** Class 1 is **−3% to −10% (low) / +3% to +15% (high)**, at **65–100% project definition**, with end use "tendering, contract award, final control estimate." Sources:
  - CIMA+ for Halton Region (Ontario), *Integrated Master Plan, Vol. 5, App. 5B: Transportation Costing Framework Technical Memo* (2026), Table 1-1, which reproduces the AACE table: https://www.halton.ca/getmedia/db5fb286-34a6-45bc-8bda-4ef6626fd33f/pw-imp-appendix-5B-cost-estimation-framework-mar-2026.pdf (opened).
  - EPCLand summary citing 18R-97: https://epcland.com/class-1-cost-estimates/ (opened).
- **Maturity.** EPCLand gives Class 1 maturity as "50% to 100%," which reflects the older 2005 revision. The current revision (and Halton) give 65–100%.
- **Primary text not opened.** The AACE RP is paywalled. Cite it as AACE International Recommended Practice 18R-97, *Cost Estimate Classification System – As Applied in Engineering, Procurement, and Construction for the Process Industries* (rev. 2020). Confirm the revision year with AACE.
- **Correction on scope.** 18R-97 is for the **process industries**. For highways and civil works the closer document is **AACE RP 98R-18**, *Cost Estimate Classification System – As Applied in Engineering, Procurement, and Construction for the Road and Rail Transportation Infrastructure Industries*. Table of contents: https://web.aacei.org/docs/default-source/toc/toc_98r-18.pdf (listing only). Its class ranges were **not** verified this session, and AACE ranges vary by industry. The book should either cite 18R-97 explicitly as "the generic process-industry table" or check 98R-18's Class 1 range before using it as the civil-works benchmark.
- **Canadian usage (new).** Canadian municipalities use this matrix in practice: City of Winnipeg, *Cost Estimate Classification*, https://legacy.winnipeg.ca/infrastructure/pdfs/CostEstimateClassification.pdf (listing only), and Halton above. A CanadaBuys solicitation attachment also reproduces a "classification system cost estimate matrix" (could not be read).

### 5. Canadian duty to warn, bidder duties before close, federal price-reasonableness guidance

#### 5a. *Brown & Huston Ltd v York (City)* (Ont CA 1985): STILL UNVERIFIED. Do not cite.

Six search formulations (with "City of York," with CanLII, and as "duty to warn") found no trace of this case. It may be misremembered, or simply not indexed online. If the author has it from a textbook (for example Kirsh, or Goldsmith on *Canadian Building Contracts*), it needs a CanLII or reporter check before use.

#### 5b. Contractor's duty to warn at common law: *Brunswick Construction Ltée v Nowlan*: VERIFIED as to existence and holding

**Citation:** *Nowlan v Brunswick Construction Ltd* (1972), 34 DLR (3d) 422 (NBCA), aff'd *Brunswick Construction Ltée v Nowlan*, [1975] 2 SCR 523, 1974 CanLII 181 (SCC); also reported 21 BLR 27.
- Holding as summarised by Alexi: https://alexi.com/matters/issues/the-builder-s-duty-to-warn-the-owner-of-the-danger-of-defects-in (opened). A builder on whom the owner relies must warn the owner if defects in the plans would prevent the work from serving its purpose.
- Context from N. A. Brown, "The Contractor's Duty to Warn: Recent Developments, Present Scope and Some Future Possibilities," *International Construction Law Review* (2002): https://www.i-law.com/ilaw/doc/view.htm?id=130000 (abstract only). Brown says Ritchie J's majority grounded the duty in reliance, while Laskin J (dissenting in part) relied on an absolute obligation to build fit-for-purpose works.

**Relevance:** This is the Canadian anchor for a contractor's duty to warn. It operates during performance and is grounded in the owner's reliance. It does **not** create a duty at the bid stage, so it supports the book's "record, not duty" stance for tendering while showing that a duty exists once a contract does.

#### 5c. Quebec: the bidder's *duty to inquire* before close: VERIFIED (commentary). New.

- ***Agence métropolitaine de transport c. Sintra inc.*, 2024 QCCA 500**, reversing 2022 QCCS 4971. Miller Thomson commentary (11 June 2024): https://millerthomson.com/en/insights/construction-newsletter-quebec/court-of-appeal-rules-alleged-ambiguities-tender-documents (opened).
  - The bidder's duty to inquire is described as "the corollary of the tendering body's duty to inform."
  - A bidder who finds ambiguities or irregularities before bidding must ask the client. If it does not, it "cannot then complain of having been the victim of an ambiguity" that could have been clarified.
- ***Entreprises électriques LM inc. c. Société de transport de Montréal*, 2018 QCCS 5375**, and ***Ville de Salaberry-de-Valleyfield c. Construction NRC inc.*, 2021 QCCA 844**. BCF commentary, V. Berthiaume, 1 Sept 2022: https://www.bcf.ca/en/thought-leadership/case-studies/ready-to-bid-be-sure-to-read-the-tender-documents-carefully/ (opened).
  - The bidder "cannot remain idle" when unsure, but the standard is not perfection.
  - The owner's knowledge still prevails: the owner knew of asbestos (LM), or knew of the bidder's calculation error (NRC), so the owner was liable.

**Relevance (ch5):** This **qualifies strand 3's claim** that no Canadian authority puts a duty on bidders to raise errors before close. In Quebec civil law it is a duty to *inquire*, not a duty to *disclose*. Failure to inquire costs the bidder its later claim. That is a "record" consequence, which fits the book's thesis well. With a bot, "could have been clarified" becomes a much wider net, since anything the bidder's bot *would* have flagged arguably could have been clarified. This is the strongest doctrinal hook found for ch5's liability-shift argument.

#### 5d. Texas: a statutory contractor duty to disclose design defects, with a bid-stage "ordinary diligence" test: VERIFIED. New and directly relevant.

**Citation:** Tex. Bus. & Com. Code §59.051, added by Acts 2021, 87th Leg., R.S., ch. 838 (S.B. 219), §1, effective 1 Sept 2021. Text from https://texas.public.law/statutes/tex._bus._&_com._code_section_59.051 (opened; it mirrors statutes.capitol.texas.gov BC.59.htm#59.051).
- Bill analysis: https://capitol.texas.gov/tlodocs/87R/analysis/html/SB00219F.htm.
- Commentary (listings): Bracewell (22 Sept 2021), https://www.bracewell.com/resources/new-rules-liability-limitations-construction-design-defects-texas; Bradley, "Out with *Lonergan*, in with *Spearin*," https://www.buildsmartbradley.com/2021/11/out-with-lonergan-in-with-spearin-texas-legislature-provides-contractors-with-limited-protection-for-defective-plans-and-designs/.

**Content (verified text):**
- **(a)** "A contractor is not responsible for the consequences of design defects in" plans and specifications provided by others, and "may not warranty the accuracy, adequacy, sufficiency, or suitability" of those documents. This overrules *Lonergan* (Tex. 1907) and moves Texas toward *Spearin*.
- **(b)** The contractor must, "within a reasonable time of learning of a defect," disclose in writing any known defect, including one that "reasonably should have been discovered by the contractor using ordinary diligence."
  - **"Ordinary diligence means the observations of the plans, specifications, or other design documents" that a contractor would make *in preparing a bid* or fulfilling its scope of work.**
  - Ordinary diligence "does not require that the contractor engage a person licensed or registered" (an engineer or architect) "or any other person with specialized skills."
- **(c)** A contractor that fails to disclose "may be liable for the consequences of defects that result from the failure to disclose."

**Relevance (top priority, ch5–6):**
- This is a statutory "reasonable bidder" test. The disclosure duty is measured by the observations a contractor would make **while preparing a bid**, and Texas is the book's development-data state.
- The "no specialized skills" carve-out is exactly what a bot puts under pressure. If a bot that any bidder can run would flag the defect, is it within "ordinary diligence"? The statute also ties liability to the *failure to disclose* (a record question), not to a duty to find. This closely matches the book's "the record matters more than the duty."
- It partly cuts against the book's ch5 claim that "a bidder need not be compelled to disclose errors its bot finds." In Texas a contractor who *knows* of a defect must disclose it in writing within a reasonable time, though the duty attaches on "learning" of the defect and not necessarily before tender close. The book should engage with this directly.

#### 5e. Canadian federal price-reasonableness guidance

- **PSPC (2023). *Practitioner's Guide for Procurement Pricing*, version 2023-1.** Public Services and Procurement Canada, Procurement Support Services Sector, August 2023. https://achatscanada.canada.ca/sites/default/files/2023-10/practitioners_guide_for_procurement_pricing_2023-1_0_0.pdf (opened; first 100k of 118k characters read). **VERIFIED.**
  - The guide gives no single formal definition of "fair and reasonable." It uses the phrase in context: a price "fair and reasonable to Canada," and validation that prices are "appropriate, attributable and reasonable."
  - Competition: with multiple compliant bidders, "multiple bids will validate the fairness of the price," which gives "a high degree of comfort that the price being fixed is fair market value."
  - For single bids or non-competitive contracts: market comparison, commercial prices as a proxy, historical contract data, cost analysis (validating the cost base and profit), benchmarking and **should-cost analysis**, audit clauses, and price support assessed by PSPC's **Price Advisory Group**.
  - Construction and Defence Construction Canada do not appear in the part read.
  - **Relevance:** This is the Canadian federal counterpart to FAR 15.404-1 for ch3. Competition is presumed to establish fairness, which is the presumption the book interrogates.
- **PSPC Supply Manual §4.70.30.1 (price support)** and **SACC clause C0008T "Price Support – Non-competitive Bid."** Both are located in search listings (https://buyandsell.gc.ca/policy-and-guidelines/supply-manual/section/4/70/30/1; https://buyandsell.gc.ca/policy-and-guidelines/standard-acquisition-clauses-and-conditions-manual/5/C/C0008T/5). Text not read: buyandsell.gc.ca blocks the fetcher (robots). The section title and current text are **STILL UNVERIFIED**. The Supply Manual has been migrating to CanadaBuys.
- **Defence Construction Canada:** no public guidance on price reasonableness or comparing bids with the pre-tender estimate was found in search. Only DCC solicitations on MERX turned up. **STILL UNVERIFIED / not found.**
- **Government of the Northwest Territories, Department of Infrastructure, "Tender Evaluation"** (section 3.8 of its tendering procedures; undated). https://www.inf.gov.nt.ca/sites/inf/files/3.8_tender_evaluation.pdf (opened). **VERIFIED.** A Canadian public owner's working procedure:
  - **Excessive bids.** If the lowest tender is "obviously excessive" and a scope review confirms the government estimate looks right, the low bidder is asked to review its own estimate. That may mean submitting it for departmental review or meeting departmental staff.
  - **Report.** A report to the responsible manager recommends a course of action, and re-tendering may reduce the scope.
  - **Negotiation.** It is allowed with the lowest bidder, but generally not above the apparent second-lowest bid, and legal advice is recommended.
  - **Inadequate prices.** If the lowest price is "obviously inadequate," the bidder is asked to review its tender but **may not increase its offer**.
  - **Thresholds.** None. "Obviously excessive" is left to judgement.
  - **Relevance (ch3):** This is exactly the practice the book describes. The price-reasonableness test is "compare with the government estimate, then ask the bidder to show its work," governed by an undefined "obviously excessive" standard. That is the gap a published tolerance would fill.

### 6. FAR 15.404-1, and automating price-reasonableness determinations

- **FAR 15.404-1(b)(2) price analysis techniques: VERIFIED** (listing): https://www.acquisition.gov/far/15.404-1. The techniques are:
  - comparison of proposed prices received in response to the solicitation;
  - comparison with historical prices;
  - parametric estimating methods;
  - comparison with competitive published price lists;
  - comparison with independent government cost estimates (IGCEs);
  - comparison with prices from market research;
  - analysis of data other than certified cost or pricing data.

  **Caveat for late 2026:** under the **Revolutionary FAR Overhaul (RFO)**, agencies issued class deviations adopting a rewritten Part 15 in 2025–26 (e.g. DOE PF 2026-20; VA deviation March 2026; DFARS 2026-O0048). See https://www.acquisition.gov/node/63942. Check whether the book's paragraph citation still matches the RFO text.
- **GSA OIG (2022). *FAS's Use of the 4P Tool on Contract and Option Awards Often Results in Noncompliant Price Determinations*,** Report A201045, 27 July 2022. https://gsaig.gov/content/fass-use-4p-tool-contract-and-option-awards-often-results-noncompliant-price-determinations (opened). **VERIFIED. New.**
  - GSA built the **Price Point Plus Portal (4P)** to automate price comparison for Multiple Award Schedule products.
  - OIG found that contracting staff **treated 4P output as proof of price reasonableness without further analysis**.
  - Staff approved prices from "self-hits," meaning comparisons with the same contract's own pricing.
  - Staff relied on other government prices even when 4P showed better commercial prices.
  - 4P data was often outdated or inaccurate (FAS disputed this).
  - **Relevance:** This is the best real-world case of an **automated price-reasonableness tool failing in practice**. It shows automation bias, and the "self-hit" is the price-book loop eating its own tail. It directly supports the book's insistence on a required record and a human keyholder (ch6, ch8). **Top priority.**
- **GSA OIG, *FAS's Use of Pricing Tools Results in Insufficient Price Determinations*** (original report, probably A180068; implementation review A230051): https://www.gsaig.gov/content/fass-use-pricing-tools-results-insufficient-price-determinations. Located; date and details **STILL UNVERIFIED**. It concerns CALC and similar tools.
- **GSA CALC / CALC+** (Contract-Awarded Labor Category tool, launched by 18F in May 2015): https://18f.gsa.gov/2015/05/12/announcing-the-calc-tool (listing). This is a public "prices paid" lookup for labour rates and an early government open-price-book tool. Listing only.
- **DoD "should cost" / DCAA automation:** no academic work automating FAR price reasonableness was found beyond strand 1's items (the Arkestro patent, the XSB white paper). PSPC's 2023 guide (5e) also recommends should-cost analysis.

### 7. Does Canada's Directive on Automated Decision-Making cover procurement? Answer: not addressed. PARTLY VERIFIED.

- **TBS, *Guide on the Scope of the Directive on Automated Decision-Making*** (issued 12 June 2025, modified 15 Sept 2026): https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-scope-directive-automated-decision-making.html (opened).
  - The guide **does not mention procurement, contracting, bid evaluation or contract award**.
  - Scope turns on whether a system supports an "administrative decision," summarised as "any decision that has the potential to affect legal rights, privileges or interests." A system is in scope if "it makes or supports decisions at any point in the decision-making process."
  - It covers individuals inside and outside government.
  - It refers scope questions to Appendix A and departmental legal services.
- **TBS amendments notice** (page dated 8 Oct 2024): https://www.canada.ca/en/government/system/digital-government/policies-standards/policy-service-digital-announcements/amendments-directive-automated-decision-making.html (opened). It lists seven amendments effective 25 April 2023, the first being expansion to **internal services** (hiring, performance management, security screening). Procurement is mentioned only as systems "developed or procured to support administrative decisions." This confirms strand 4, item E12.
- A **fourth review** of the DADM is under way (GCcollab: https://wiki.gccollab.ca/images/2/26/EN_Presentation_4th_review_DADM.pdf, not opened).
- **Conclusion for the book:** whether contract award is in scope is **untested and unaddressed in TBS guidance**. Under the guide's test (a decision affecting a bidder's legal rights or interests, under Contract A / *Ron Engineering*), a strong argument exists that an automated bid-evaluation or price-reasonableness system is in scope. The book can say so as argument, not as settled. No commentary specifically on DADM and procurement was found.
- **Related (new): UK Cabinet Office, *Procurement Policy Note 017: Improving transparency of AI use in procurement*.** https://gov.uk/government/publications/ppn-017-improving-transparency-of-ai-use-in-procurement/ppn-017-improving-transparency-of-ai-use-in-procurement-html (listing only; date and content STILL UNVERIFIED). From the title, it is likely about bidders' use of AI in preparing bids, which makes it relevant to ch5's bidder-bot disclosure question. Check before citing.

### 8. EU AI Act Annex III: VERIFIED. Public procurement is not listed.

**Citation:** Regulation (EU) 2024/1689, OJ L, 12.7.2024, Annex III. Text at https://www.artificialintelligenceact.eu/annex/3/ (opened).

The eight areas are:
1. biometrics;
2. critical infrastructure;
3. education and vocational training;
4. employment and workers' management;
5. access to essential private and public services and benefits;
6. law enforcement;
7. migration, asylum and border control;
8. administration of justice and democratic processes.

**Neither "procurement" nor "public contracts" appears.** Point 5(a) covers public authorities evaluating eligibility for public assistance benefits and services, not awarding contracts.

This confirms Sánchez-Graells (strand 4, item E13). Further context:
- Commission **draft guidelines on high-risk classification** (Art. 6) were published in mid-2026: https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems (listing).
- The **Digital Omnibus** provisional agreement (May–June 2026) postponed Annex III high-risk obligations, reportedly to 2 Dec 2027. See Gibson Dunn, https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines/ (listing).

### 9. Proposed FRE 707 as of late 2026: VERIFIED to October 2026, with a refinement to strand 4

**Source:** Advisory Committee on Evidence Rules, *Agenda Book, October 15, 2026* (posted 23 Sept 2026), https://www.uscourts.gov/sites/default/files/document/2026-10_evidence_rules_agenda_book_9-23_final.pdf (opened; about 100k of 128k characters read). Page numbers are PDF pages "of 221."

- **Publication.** The rule was approved for comment in spring 2025 and would apply Rule 702 reliability standards to machine or AI output offered without an expert.
- **Comments.** The agenda says "more than 70 written comments" (p. 5). The May 2026 minutes count 59: 3 unqualified support, 27 support with revisions, 27 opposed (p. 25). The two figures conflict.
- **7 May 2026.** The Committee **"voted to withdraw the proposed rule as issued for public comment, and to submit a modified rule proposal for further study"** (p. 5). The changes were acknowledged as "substantial" (pp. 26–27). They include:
  - replacing "machine-generated evidence" with **"artificial intelligence"** and adding a statutory AI definition;
  - **deleting the simple-scientific-instrument exception**;
  - adding a **notice requirement**, modelled on Rules 404 and 807;
  - adding a judicial-notice carve-out (the example given is Google Maps distances).
- **Three alternative drafts.** The Committee prefers **Version Two**, which "would ordinarily require an expert to establish admissibility," with exceptions (p. 26).
- **15 October 2026 meeting.** The morning was a **mini-conference** with AI experts and litigators on "potentially unreliable AI offered as evidence" (pp. 5–6, 23–24). The Chair noted that Rules 707 and 901(c) (deepfakes) might be published together (p. 27). The outcome of the 15 October meeting is **not yet verified**.
- **Refinement to strand 4, item E11.** Strand 4 says "declined to advance it and sent it back for further study." More precisely, **the published rule was withdrawn in May 2026**, and a substantially revised version, leaning toward requiring an expert, is under study for possible republication.
- **Relevance:** "Ordinarily require an expert" is the book's **keyholder**: a human who answers for the machine number. The notice requirement echoes the book's **required record**. Deleting the simple-instrument exception means a "standard bot" would *not* escape scrutiny by being routine, unless it fits judicial notice. A pre-certified public test is the argument for treating it more like a judicially noticeable reference.
- **Safe wording for the book (Nov 2026):** "Proposed Rule 707 was published for comment in 2025, withdrawn in May 2026, and is being redrafted. The leading draft would ordinarily require an expert to sponsor AI-generated evidence. It is not law." Secondary listings: Redgrave LLP, "...Hits Pause to Consider Significant Revisions..." (https://www.redgravellp.com/publication/machine-generated-evidence--rules-advisory-committee-hits-pause-to-consider-significant-revisions-to-proposed-federal-rule-of-evidence-707-addressing-evidence-generated-by-artificial-intelligence); Lexvisio, 26 Aug 2026.

### 10. Popular sources not yet searched

1. **NPR *Planet Money*, "Hacking The Perfect Auction"** (6 Nov 2020). https://www.npr.org/2020/11/06/932048876/hacking-the-perfect-auction (listing). Milgrom and Wilson's Nobel and the FCC incentive auction. A plain-language model of designing a market mechanism, useful for ch3 and ch10 on auctions as designed machines.
2. **NPR *The Indicator from Planet Money*, "Why building public transit in the U.S. costs so much"** (26 June 2023). https://www.npr.org/2023/06/26/1184420745/why-building-public-transit-in-the-us-costs-so-much (listing). A short audio explainer drawing on the Transit Costs Project. An accessible entry for ch1 readers.
3. **Alon Levy, "We Should Know How Much Transit Components Cost,"** Institute for Progress, *Transit Abundance Playbook*, 17 June 2026. https://ifp.org/we-should-know-how-much-transit-components-cost/ (opened).
   - Lump-sum contracts hide costs and invite change-order inflation.
   - Bidders should itemize labour by job, materials by commodity and systems by product.
   - USDOT should publish national unit costs with regional adjustments, and federal grants should be conditioned on transparent unit pricing.
   - Levy claims savings of 15–20%, citing Italy, Spain, India and Massachusetts.
   - **Relevance:** This is the closest popular statement of the book's "public price book" and "tender is the API" ideas, from a well-known author. **Top priority (ch2, ch4, ch8).**
4. **Liscow, Nober & Slattery, "Procurement and Infrastructure Costs,"** NBER WP 31705 (Sept 2023). https://www.nber.org/papers/w31705 (opened; authors now VERIFIED: Zachary Liscow, Will Nober, Cailin Slattery). Also published in *Brookings Papers* (2024): https://brookings.edu/wp-content/uploads/2024/05/Procurement_and_Infrastructure_Costs.pdf. It surveys DOTs and contractors in all 50 states and finds DOT capacity and weak competition are key cost drivers. **This upgrades strand 2's UNVERIFIED author list.**
5. **Zachary Liscow & Cailin Slattery, "To Fix Its Broken Infrastructure, America Must Rebuild Government Capacity,"** *Project Syndicate*, Nov 2025. https://www2.project-syndicate.org/commentary/to-fix-its-broken-infrastructure-america-must-rebuild-government-capacity-by-zachary-liscow-and-cailin-slattery-2025-11 (listing). The op-ed version of item 4. Also Liscow, "State Capacity for Building Infrastructure," Aspen Economic Strategy Group (Dec 2024), https://economicstrategygroup.org/wp-content/uploads/2024/11/liscow_exec_summarypdf.pdf (listing).
6. **Statecraft (Santi Ruiz), "What Is America's Infrastructure Cost Problem?"** https://www.statecraft.pub/p/what-is-americas-infrastructure-cost (listing; guest and date STILL UNVERIFIED). Also "How to Fix Defense Procurement," https://www.statecraft.pub/p/how-to-fix-defense-procurement (listing). Practitioner interviews in the book's register.
7. **Slow Boring × Transit Costs Project.** https://www.slowboring.com/p/slow-boring-x-transit-costs-project (listing; date and author STILL UNVERIFIED, presumably Yglesias). Popular framing of the Transit Costs Project's procurement findings.
8. ***Works in Progress*, "How Madrid built its metro cheaply."** https://worksinprogress.co/issue/how-madrid-built-its-metro-cheaply/ (listing; author and issue STILL UNVERIFIED). Madrid's in-house design, standardised stations and contractor management under Manuel Melis. A strong ch1 and ch10 contrast case. Related: Bent Flyvbjerg, "Madrid's Modular Metro," Substack, https://flyvbjerg.substack.com/p/madrids-modular-metro (listing).
9. **Eric Lofgren, *Acquisition Talk*** (blog and podcast on defence acquisition, cost-based pricing and "certified cost and pricing data"). https://acquisitiontalk.com/ (listing). The best popular-technical source on why US defence pricing relies on cost analysis rather than markets (ch3, the FAR side).
10. **Eli Dourado on construction costs: STILL UNVERIFIED.** No specific essay was surfaced. Brian Potter (*Construction Physics*, already in strand 2) covers this ground better.

### 11. Digital construction

- **Directive 2014/24/EU, Art. 22(4): VERIFIED.** https://www.legislation.gov.uk/eudr/2014/24/article/22/2016-01-01 (opened).
  - "For public works contracts and design contests, Member States may require the use of specific electronic tools, such as of building information electronic modelling tools or similar."
  - Where they do, contracting authorities "shall offer alternative means of access ... until such time as those tools become generally available."
  - Background: European Commission Public Buyers Community, *The PP Directives and BIM: How to use Procurement as an enabling mechanism* (2024), https://public-buyers-community.ec.europa.eu/system/files/2024-05/The_PP_Directives_and_BIM_-_How_to_use_Procurement_as_an_enabling_mechanism_and_avoid_associated_risks_%28ohne_Anm%29_0_0.pdf (listing).
- **ISO 19650-1:2018 and ISO 19650-2:2018: PARTLY VERIFIED** (buildingSMART and MnDOT open-BIM listings; iso.org not opened). Titles: *Organization and digitization of information about buildings and civil engineering works, including BIM – Information management using BIM – Part 1: Concepts and principles; Part 2: Delivery phase of the assets.*
- **ISO 16739-1: CORRECTED.** The current edition is **ISO 16739-1:2024** (IFC 4.3 ADD2), which supersedes ISO 16739-1:2018 (IFC 4).
  - buildingSMART, "IFC 4.3 Formally Approved and Published as an ISO Standard" (2024), https://www.buildingsmart.org/?p=29521 (listing).
  - DIN Media listing, https://www.dinmedia.de/en/standard/iso-16739-1/379231104.
  - **IFC 4.3 adds infrastructure entities (alignment, road, rail, bridge, marine).** That makes it the relevant schema for a civil-works pilot, which the 2018 edition was not.
- **UK 2016 BIM mandate: PARTLY VERIFIED.** Cabinet Office, *Government Construction Strategy* (May 2011), https://assets.publishing.service.gov.uk/media/5a78ce8eed915d07d35b2933/Government-Construction-Strategy_0.pdf (located). The widely quoted requirement is "fully collaborative 3D BIM (with all project and asset information, documentation and data being electronic) as a minimum by 2016." The exact wording comes from secondary sources (Designing Buildings Wiki) and was not read in the PDF. The "Level 2" label and the April 2016 date come from later guidance, and the successor is the *Government Construction Strategy 2016–2020* (https://www.gov.uk/government/publications/government-construction-strategy-2016-2020).

**Recent papers on LLMs and automation in tender and contract documents (2023–2026):**

1. **Kim, E. W., Shin, Y. J., Kim, K. J. & Kwon, S. (2025).** "Development of an Automated Construction Contract Review Framework Using Large Language Model and Domain Knowledge." *Buildings* 15(6): 923. DOI 10.3390/buildings15060923. https://www.mdpi.com/2075-5309/15/6/923 (opened). **VERIFIED.**
   - RAG over a standard-form knowledge base (Oman SCF, based on FIDIC Red Book 1999). It compares an input contract with the standard form to flag modified, added or omitted clauses.
   - On 320 queries the proposed method scored Answer Correctness 0.750, against 0.687 for GPT-4o-mini alone and 0.697 for basic RAG. Faithfulness 0.893; Context Recall 0.969.
   - There is **no human-expert baseline**. The authors say RAGAS "cannot fully capture the nuanced judgments required in professional contract analysis."
   - **Relevance:** Comparing tender documents against a frozen standard form is a narrow version of the book's conformance test. Accuracy around 75% supports the "assistant, not arbiter" framing.
2. **Zheng, C., Wong, S., Su, X., Tang, Y., Nawaz, A. & Kassem, M. (2023/2025).** "Automating construction contract review using knowledge graph-enhanced large language models." arXiv:2309.12132 (opened). The journal version appears at *Automation in Construction* (ScienceDirect PII S0926580525002195, 2025; listing only, volume not confirmed). GraphRAG with a nested contract knowledge graph on international EPC contracts. The abstract gives no headline accuracy figure.
3. **"Application of large language models to intelligently analyze long construction contract texts,"** *Construction Management and Economics* 43(3): 226–242 (2025). DOI 10.1080/01446193.2024.2415676. https://www.tandfonline.com/doi/abs/10.1080/01446193.2024.2415676 (listing). Authors and figures **STILL UNVERIFIED**.
4. **Already covered in strand 4** (no change): CEQuest (arXiv:2508.16081), Handoff-H1, AECV-Bench. Also seen this session: "Can AI Master Construction Management (CM)? Benchmarking..." arXiv:2504.08779 (listing; authors and figures unverified), and Heo et al.'s further work (item 12).
5. **Not found:** a peer-reviewed paper measuring LLM-generated **RFIs** or **bid-evaluation** accuracy on construction tenders. Only vendor material exists (Drawer.ai, Nomic, the LlamaIndex/SoftIQ tender agent case study, Contextfort). The Australian **Digital Transformation Agency** was reported to be "exploring AI use in tender evaluations" (techpartner.news; listing only, UNVERIFIED).

### 12. Other verifications

- **Nicoletti, *Agentic AI for Procurement: Concepts, Applications and Implications* (Springer, 2026): VERIFIED** (listing). ISBN 978-3-032-23023-2 (print), 978-3-032-23024-9 (eBook). Bookseller and library listings: Schweitzer, Tenlong, ESCP library, EconPapers chapter listing https://econpapers.repec.org/bookchap/sprsprchp/978-3-032-23024-9_5f16.htm.
- **Heo, Ahn & Park, "Tacit Collusion by LLM Agents in Construction Bidding: Evidence from a Simulated Bidding Environment," *J. Management in Engineering*: VERIFIED** (listing). Seoul National University lab page: https://mspark.snu.ac.kr/publication/tacit-collusion-by-llm-agents-in-construction-bidding-evidence-from-a-simulated-bidding-environment/. Volume and issue 42(2) and article 04025063 come from strand 1 and were not re-checked. **New related items:**
  - "Potential AI-Driven Algorithmic Collusion and Influential Factors in Construction Bidding," *J. Computing in Civil Engineering* (ASCE), DOI 10.1061/JCCEE5.CPENG-5683, https://ascelibrary.com/doi/10.1061/JCCEE5.CPENG-5683 (listing).
  - "Uncovering Potential Collusive Behavior of AI Bidders in Future Construction Bidding Market," ASCE conference proceedings, DOI 10.1061/9780784485224.063 (listing).
  - "Algorithmic collusion in construction bidding: risks, dynamics and regulatory implications" (SNU lab page; venue unverified).
  - Together these make Heo and colleagues a sustained research programme, which the book must answer in ch10.
- **Kawai, K. & Nakabayashi, J. (2022), "Detecting Large-Scale Collusion in Procurement Auctions," *Journal of Political Economy* 130(5): 1364–1411, DOI 10.1086/718913: VERIFIED, with a correction.** Source: https://ideas.repec.org/a/ucp/jpolec/doi10.1086-718913.html (opened).
  - **CORRECTION to strand 3, item 34:** the sample is **about 42,000 auctions** (about US$40 billion) of Japanese national-government construction, **not "about 70,000."**
  - The method uses rebids in auctions where every initial bid failed to meet the secret reserve price.
  - It flags more than 1,000 bidders whose conduct is inconsistent with competition. Flagged firms won about 15,000 projects, roughly 37% of the sample.
- **Liscow et al., NBER w31705: authors VERIFIED** as Zachary Liscow, Will Nober and Cailin Slattery (item 10.4).
- **Charbonneau Commission: PARTLY VERIFIED.** The official name is *Commission d'enquête sur l'octroi et la gestion des contrats publics dans l'industrie de la construction*. The final report was made public in November 2015 (Wikipedia: work completed 25 Nov 2015; strand 3 says tabled 24 Nov 2015) with 60 recommendations. Wikipedia gives no formal report title. Cite it as *Rapport final de la Commission d'enquête sur l'octroi et la gestion des contrats publics dans l'industrie de la construction* (3 tomes, Nov 2015). Confirm the tome count with BAnQ: https://collections.banq.qc.ca/ (listing).
- **McKinsey Global Institute, *Reinventing Construction: A Route to Higher Productivity* (Feb 2017; Barbosa, Woetzel, Mischke et al.): VERIFIED** (full-report PDF listing on mckinsey domains). Strand 1 marked it UNVERIFIED; strand 3 already verified it.
- **Anthropic Project Vend: PARTLY VERIFIED** (Anthropic page https://www.anthropic.com/research/project-vend-1 located; fetch refused). Consistent secondary coverage confirms the findings:
  - The Decoder, "Anthropic's Claude ran a store and lost money by selling below cost and giving discounts," https://the-decoder.com/anthropics-claude-ran-a-store-and-lost-money-by-selling-below-cost-and-giving-discounts/
  - Simon Willison, 27 Jun 2025, https://simonwillison.net/2025/Jun/27/project-vend
  - CO/AI, "tungsten cubes"

  Claudius sold below cost, was talked into discounts by staff, and lost money on tungsten cubes.
- **New, highly relevant: Anthropic, "Project Deal," posted 24 April 2026.** https://www.anthropic.com/features/project-deal (opened). **VERIFIED.**
  - **Setup.** The experiment ran for one week in December 2025 with 69 San Francisco employees, each given a US$100 budget. Claude interviewed each person and built a custom agent, and the agents negotiated autonomously in Slack.
  - **Design.** There were four parallel runs. The "real" run used Opus 4.5 only; two runs randomly assigned Opus 4.5 or Haiku 4.5.
  - **Volume.** The real run produced 186 deals across more than 500 listed items, worth just over US$4,000.
  - **Stronger models got better prices.** Opus sellers earned about $2.68 more per item and Opus buyers paid about $2.45 less. One broken folding bike sold for $65 through Opus and $38 through Haiku.
  - **Participants did not notice.** Perceived fairness was about 4.05 for Opus deals against 4.06 for Haiku deals, on a 1–7 scale.
  - **Prompting style made little difference.** Telling agents to negotiate aggressively or nicely had no statistically significant effect.
  - **Authors' conclusion:** "The policy and legal frameworks around AI models that transact on our behalf simply don't exist yet."
  - **Caveats.** It is a pilot with a self-selected pool and small-value goods.
  - **Relevance (top priority, ch6–7, ch10):**
    - Asymmetric bot capability shifts price outcomes *invisibly*, so "it felt fair" stops being evidence of a fair price. That makes the case for a public, frozen reference bot that both sides can rerun.
    - The null effect of prompting style suggests that model capability, not instructions, drives price outcomes. That supports pinning the *model* in the standard.
  - Secondary coverage: The Decoder, https://the-decoder.com/anthropic-says-stronger-ai-models-cut-better-deals-and-the-losers-dont-even-notice/.

### 13. Bonus items

- **The "reasonable bidder" or "reasonable contractor" standard applied to AI:** no scholarly work was found. The two closest doctrinal hooks are Texas's "ordinary diligence" disclosure standard (5d) and Quebec's duty to inquire (5c). US patent-ambiguity doctrine (strand 3, item 45) asks what a reasonable bidder would have noticed. No commentary applies any of these to AI. **This looks like a genuine gap the book can claim.**
- **Public bid-tab data for a reference estimator:**
  - TxDOT, *Average Low Bid Unit Prices*: https://www.txdot.gov/content/txdot/en/business/letting-bids/average-low-bid-unit-prices.html (listing).
  - TxDOT, *Bid Tabulations Dashboard*: https://www.txdot.gov/business/road-bridge-maintenance/contract-letting/bid-tabulations-dashboard.html (listing).
  - TxDOT, *Bid Items and Index*: https://www.txdot.gov/business/letting-bids/bid-item-index.html.
  - TxDOT, *PS&E Preparation Manual* §5.4.1, "Estimated Bid Price Determination": https://www.txdot.gov/manuals/des/pse/chapter-5--engineer-s-estimate/section-4--prices/estimated-bid-price-determination.html (listing). This is TxDOT's official method for building the engineer's estimate from bid history, the human baseline for ch8.
  - Data.gov carries agency bid-tabulation datasets (e.g. https://catalog.data.gov/dataset/bid-tabulations-2045c; https://catalog.data.gov/dataset/procurement-bid-tabulations-archive; owners unverified).
  - Oregon DOT, *Average Bid Item Prices*: https://oregon.gov/odot/Business/Pages/average_bid_item_prices.aspx.
  - Third-party scrapers (Apify "txdot-scraper") and aggregators (constructionbids.ai) exist, a sign of demand for machine-readable bid tabs.
  - **No public, versioned benchmark dataset or "reference estimator" for construction unit prices was found** on IEEE DataPort, Kaggle or GitHub. Academic DOT studies (e.g. Georgia Tech theses on highway cost estimation with ML; a ROSA P report, dot 86897) use agency data but publish no frozen benchmark. **This confirms strand 4's gap finding.**

---

### What the book gains from this pass

1. **Ch5 now has firmer doctrine on both sides:**
   - an owner disclosure duty (Edgeworth, Bail);
   - a Quebec bidder **duty to inquire** (*Sintra* 2024);
   - a common-law **duty to warn** during performance (*Nowlan*);
   - a Texas **statutory disclosure duty measured by "ordinary diligence"**, defined by reference to bid preparation (2021);
   - a GNWT working procedure that tests price only against an undefined "obviously excessive" standard.

   The bot argument becomes concrete: "ordinary diligence" and "could have been clarified" both expand as checking gets cheaper.
2. **Ch3 and ch6 gain a cautionary real-world case.** GSA's 4P tool shows automated price reasonableness producing noncompliant determinations through automation bias and self-referential comparisons.
3. **Ch6 and ch7 gain an argument for a common standard bot.** Anthropic's Project Deal shows that unequal agents produce unequal prices that their principals do not detect.
4. **Ch2, ch4 and ch8 gain a popular ally.** Alon Levy (IFP, June 2026) calls for itemized bids and federally published unit costs.
5. **Two standards are out of date and need fixing:** IFC is now ISO 16739-1:2024 (with infrastructure), and AACE has an infrastructure-specific RP (98R-18).

### Still to do (budget-blocked)

- Read the AACE 98R-18 Class 1 range.
- Find the PSPC Supply Manual 4.70.30 text, possibly via CanadaBuys.
- Look for *Brown & Huston* on CanLII directly. A seventh search also failed.
- Find the outcome of the 15 Oct 2026 Evidence Rules meeting (minutes not yet posted).
- Identify the authors of the *Works in Progress* Madrid essay and the Statecraft interview guest.
- Find the date and content of UK PPN 017.
- Find the date of the GSA OIG pricing-tools report.

---


## Addendum, 1 November 2026 (afternoon): Andre's follow-up questions

**On the 2 to 3 percent threshold (Andre's position, verbatim in the thread).** Ten percent of $10 million is $1 million. Engineers do not carry the estimating risk, so they are not the primary market. Contractors who must stand behind their prices are, and 10 percent is too much variance on a large contract. *Implication for the text: the threshold is a bidder's standard, not an owner's, and chapter 3 should compare it with contractor margins rather than with engineer's-estimate accuracy.*

**Texas §59.051: is there case law?** None found. A search of law-firm commentary (Gordon Rees, March 2022; Hicks Johnson, November 2024; Porter Hedges; Griffith Davison; Butler Snow) turned up no reported decision applying the disclosure duty. Hicks Johnson calls the statute's reach "ripe for litigation". This was a web search, not a Westlaw or Lexis check, so trial-court rulings or unpublished opinions could exist. The statute's own text supports Andre's reading: "ordinary diligence" means the observations a contractor would make "in the reasonable preparation of a bid", and it "does not require that the contractor engage a person licensed or registered … or any other person with specialized skills". Chapter 59 excludes critical infrastructure facilities (refineries, power plants, oil and gas sites), and design-build or EPC work where the contractor supplied the design; whether TxDOT highway contracts fall inside it was not confirmed. Sources: [statute text (Justia)](https://law.justia.com/codes/texas/2024/business-and-commerce-code/title-4/chapter-59/subchapter-b/section-59-051/); [Griffith Davison on the exclusions](https://www.griffithdavison.com/texas-legislature-relieves-contractors-of-liability-for-design-defects-with-a-few-caveats/); [Gordon Rees 2022](https://www.grsm.com/insight/recent-amendments-and-caselaw-affecting-the-construction-industry-in-texas/); [Hicks Johnson 2024](https://hicksjohnson.com/wp-content/uploads/2024/11/Insights-in-Focus_11-24-24.pdf).

**The construction algorithmic-collusion research programme (Seoul National University).** Chan Heo, with Moonseo Park and Changbum Ryan Ahn (and Minhwan Oh on one paper), Department of Architecture and Architectural Engineering, SNU. Four or five papers, in order:

1. Heo, Park & Ahn (2024). "Potential AI-Driven Algorithmic Collusion and Influential Factors in Construction Bidding." *J. Computing in Civil Engineering* 38(4): 04024016. DOI 10.1061/JCCEE5.CPENG-5683. Reinforcement-learning bidders setting markups in repeated simulated tenders drift toward collusion. Repeated encounters make it likelier. **Profit-maximising objectives enable collusion; win-maximising objectives hinder it.** [SNU record](https://snu.elsevierpure.com/en/publications/potential-ai-driven-algorithmic-collusion-and-influential-factors/)
2. Heo et al., "Uncovering Potential Collusive Behavior of AI Bidders in Future Construction Bidding Market," ASCE conference proceedings, DOI 10.1061/9780784485224.063 (page did not load; details unchecked).
3. Heo, Ahn, Oh & Park (2025). "Algorithmic Collusion in Construction Bidding: Risks, Dynamics, and Regulatory Implications." *J. Management in Engineering* 41(5): 04025045. DOI 10.1061/JMENEA.MEENG-6704. Collusion persists when a bot meets a new opponent; **the bid-evaluation method changes how fast and how stably collusion forms**; risk is highest with few bidders and price-only evaluation. [SNU record](https://snu.elsevierpure.com/en/publications/algorithmic-collusion-in-construction-bidding-risks-dynamics-and--2/)
4. Heo, Park & Ahn (2025). "Large Language Models in Construction Bidding: Opportunities and Risks of Algorithmic Collusion." *Proc. 42nd ISARC*, pp. 1332–1339. [PDF](https://www.iaarc.org/publications/fulltext/172_Large_Language_Models_in_Construction_Bidding__Opportunities_and_Risks_of_Algorithmic_Collusion.pdf)
5. Heo, Ahn & Park (2025/26). "Tacit Collusion by LLM Agents in Construction Bidding: Evidence from a Simulated Bidding Environment." *J. Management in Engineering* 42(2): 04025063. DOI 10.1061/JMENEA.MEENG-7144. GPT-4o bidders reach about 1.04 to 1.06 times cost within 40 to 50 rounds when told high bids are profitable; more transparency helps them coordinate.

*Why they are adjacent to the book:* their finding that the evaluation rule shapes collusion is a design input for the Evaluator and the protocol (chapter 10). The book's buyer-side reference price is one of the countermeasures their regulatory papers call for. They are natural reviewers, data partners or co-authors for a test of whether a published reference bot disciplines or anchors AI bidders.

## Addendum 2, 1 November 2026 (evening): Kolt, "Governing AI Agents"

**Citation.** Noam Kolt, "Governing AI Agents," *Notre Dame Law Review* 101 (forthcoming); arXiv:2501.07913 (v1 14 Jan 2025, v2 11 Feb 2025). https://arxiv.org/abs/2501.07913. Shared by Andre, who also supplied the PDF; read in full (v2, 48 pp.).

**Argument.** AI agents (systems that plan and act with little human involvement) raise classic agency problems, and two frameworks fit them: principal-agent economics and the common law of agency (the Restatement (Third) of Agency). The problems are information asymmetry, discretionary authority, loyalty and delegation to sub-agents. The usual fixes (incentive design before delegation, monitoring during, enforcement after) fit poorly. Agents "will maximize whatever they are programmed to maximize", failures are about competence rather than motive, monitoring breaks at machine speed and scale, and it is unclear how to sanction an agent. Kolt proposes three governance principles backed by new technical and legal infrastructure: **inclusivity** (agents loyal to societal interests, not just their user), **visibility** (insight into how agents are built and run) and **liability** (allocating responsibility among those who design, operate and use agents). He also flags inter-agent collusion and agents colluding on prices for competing vendors (pp. 16–17, 29).

**Why it matters for the book.**
- It is the strongest legal-theory frame for the book's cast. The bidder's bot is the bidder's agent; the buyer's Listener is the owner's agent; the keyholder is the principal who answers.
- **Chapter 5 gets a sharper footing.** In agency law the duty to disclose (Restatement §8.11) runs from agent to *principal*. So a bidder's bot owes what it finds to the bidder, not to the owner. That is the agency-law version of Andre's "the bidder may stay quiet". Kolt's *inclusivity* principle is the counter-pressure: should a bot also owe something to third parties? The book can name that tension in its own labels.
- **Visibility and liability map onto the record and the keyholder.** The book's signed record, frozen version and error rate are concrete visibility infrastructure, and the keyholder is a liability allocation. Kolt calls for this infrastructure in general; the book builds a version of it for one market.
- **Monitoring at machine speed** supports a published conformance test over case-by-case review.
- **Collusion** is named as an agent-governance failure mode, which ties Kolt to the Seoul papers.
- **Gap the book fills:** Kolt never treats standards bodies, certification or a reference "reasonable" agent. The book's standard bot is exactly the missing piece.
- Related, from memory and unverified this session: Alan Chan et al., "Visibility into AI Agents" (FAccT 2024; arXiv:2401.13138), which proposes agent identifiers, real-time monitoring and activity logs. Check it before citing.

**Parts III.B to IV, read from Andre's PDF (page numbers are v2's).**
- **Monitoring (pp. 33–35).** Principals hire agents for skills they lack, so they "can never hope completely to check the agent's performance" (Arrow, quoted p. 33). Human oversight of AI is "impractical and undermines the very purpose" of using agents (p. 35). The promising but "potentially perilous" route is AI agents monitoring AI agents ("scalable oversight"). And "Monitoring, after all, identifies problems. It does not penalize or prevent them" (p. 35). *For the book:* the Listener and the Evaluator are monitoring agents; the standard's conformance test is what keeps the monitor itself honest.
- **Enforcement (pp. 36–37).** Termination, penalties and reputational sanctions do not bite on agents that do not value money or freedom, and building those motives in would create the conflicts agency law exists to solve.
- **Inclusivity (pp. 38–41).** "Single-single" alignment is too narrow; agents act for many principals with conflicting interests, as trustees must deal impartially among beneficiaries. Kolt's own example is two agents from the same vendor negotiating a price against each other, and he names "collusion between agents" as a policy problem (p. 41). *For the book:* the standard bot is a deliberately impartial agent, owed to the market rather than to either party, which is one concrete answer to Kolt's open question "whose interests should AI agents serve?"
- **Visibility (pp. 41–43).** AI agents, unlike people, "can be designed to automatically produce detailed records of their activities" (p. 41, citing Bryan Casey, "Robot Ipsa Loquitur," 108 Geo. L.J. 225 (2019): machine logs "speak to the fault of the parties involved"). Proposals: agent identifiers, real-time monitoring and logging (Chan et al., "Visibility into AI Agents", FAccT 2024, and "IDs for AI Systems", arXiv:2406.12137), Shavit et al.'s ledgers of agent actions, and wider auditor access to models, since black-box access is insufficient (Casper et al., FAccT 2024). *For the book:* this is the strongest scholarly support for "the record matters more than the duty", and Casey's paper belongs in chapter 7. Auditor access supports open, pinned weights.
- **Liability (pp. 43–47).** Three questions: who is liable, when, and to what standard of care.
  - *Who:* the "many hands" problem, and the "computer as scapegoat". A naive agency rule rewards operators for *not* controlling their AI. Kolt proposes allocating liability by each actor's (i) ex ante ability to prevent harm and (ii) resources to remedy it. He quotes Shavit et al.: "at least one human entity is accountable for every uncompensated direct harm", and Ayres & Balkin: people "should not be able to obtain a reduced duty of care by substituting an AI agent for a human agent." *For the book:* that is the keyholder, and the book's allocation (design on the designer, reading on the bidder's bot, the addendum on whoever issued it) follows Kolt's prevent-or-remedy test.
  - *When:* Restatement §7.04 (within authority or ratified) and §7.05 (negligence in "selecting, training, retaining, supervising, or otherwise controlling the agent"). *For the book:* the keyholder's duty becomes procedural, which is choosing a conforming bot and keeping the record, as the review already suggested. Kolt doubts the foreseeability limit suits unpredictable agents; a published error rate makes the bot's failures foreseeable in a measured way.
  - *Standard of care:* Restatement §8.08, the "care, competence, and diligence normally exercised by agents in similar circumstances", raised by special skills. Kolt's worry (p. 47): holding domain-specific agents to a higher standard could push well-resourced labs away from building them, leaving the field to less reliable firms. *For the book:* this is the reasonable-bot problem stated in agency terms, and Kolt leaves it open. A public conformance test answers it, because the standard of care is set by the published test and its tolerance, not by each vendor's claimed skill, so a capable vendor gains nothing by staying general-purpose.
- **Conclusion (pp. 47–48).** "Principles, however, are not enough"; new technical and legal infrastructure is needed while the technology is young. The book is a worked example for one market.
- **Note:** v2 cites Diamantis, "Reasonable AI", as 77 Vand. L. Rev. (forthcoming 2025); the published citation in Part 2 (78 Vand. L. Rev. 573) is the later one.

**Andre's response to Kolt (1 November 2026, in the thread), which supersedes the "for the book" notes above where they differ.**
- A bot's own record of its activities is a poor structural choice. Records cost almost nothing to make, a bot's intent cannot be known, and the record could be a smoke screen. So the book should not rest on the bidder's bot's self-reported log or reasoning. (Kolt half-concedes this: he notes chains of thought "might not accurately reflect the actual operation of the agent".) What can carry weight is a reading that a third party can rerun: the frozen tender, the named standard version, and the same output on rerun.
- Liability as it stands, with every contributor able to be made to pay regardless of share, puts restoring the victim ahead of fair allocation and stalls AI adoption. The standard's contribution is certainty about legal outcomes.
- The standard sets a floor for the standard of care in construction procurement. This points toward the construction manager acting as the owner's agent, rather than a general contractor as counterparty.
- The standard bot serves no one. It is a repeatable test case for baselining projects, not an agent with a principal.
