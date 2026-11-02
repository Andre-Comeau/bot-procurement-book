# Algorithmic collusion in construction bidding: close reading of the Seoul National University papers, and a test of Andre's "commoditized pricing" argument

Prepared 1 November 2026 for *Fair and Reasonable* / *The Reasonable Bot*. Companion to `literature-review-2026-11-01.md` (Addendum).

---

## One-page summary

**What could be read.** Only one of the five papers is open access: the ISARC 2025 paper on LLM bidders. I read its full text. The other four are paywalled at ASCE. The SNU repository (S-Space) lists the 2024 journal paper but holds no file. ResearchGate, Semantic Scholar and Unpaywall showed no legal free copy. For those four, these notes rest on the abstracts, the SNU research-portal records, the authors' lab pages, the ASCE reference lists, and the way the ISARC paper describes the group's earlier work. Setup details marked "not public" could not be checked. Please do not quote numbers for those papers without the full text.

**A correction.** The co-author on the 2025 *J. Management in Engineering* paper is **Minhwan Oh** (SNU Graduate School of Data Science), not Minji Oh.

**A new sixth paper.** Heo, Park and Ahn presented "Information Disclosure as a Regulatory Lever for Mitigating Algorithmic Collusion in AI-Driven Procurement Markets" at i3CE 2026 (paper 353, 15 June 2026). No text is public yet. It is the paper closest to the book's question, and it suggests the group is already testing disclosure rules.

**What the group found.** Learning bidders in a repeated, price-only, lowest-bid market tend to settle above cost without talking to each other. Q-learning agents did so in the 2023/24 and 2025 papers. GPT-4o agents did so in the 2025 and 2025/26 papers. The 2024 paper reports that repeated encounters make collusion likelier, profit-maximising objectives enable it and win-maximising objectives hinder it. The 2025 paper reports that collusion survives a change of opponent, that the evaluation method changes how fast and how stably it forms, and that risk is highest with few bidders and price-only evaluation. The ISARC paper is the most concrete. Two GPT-4o bidders with identical costs could see each other's past bids. When the prompt said lower bids win more often, they converged to 0.2 to 0.5 percent above the estimate. When one sentence instead said higher bids earn more profit, they converged to 3.9 to 5.6 percent above it. Both settled within 40 to 50 rounds. The 2025/26 paper adds that greater market transparency may make coordination easier.

**Andre's argument, in short.** Andre is right about the one-shot logic. With identical costs and price-only competition, competitive bids fall to cost plus a normal return, which is commodity pricing. He is also right that some information sharpens competition. Publishing an engineer's estimate lowered and tightened bids in Oklahoma (De Silva et al. 2008). Showing learning bidders the winning bid pushed a first-price auction back toward competition (Banchio and Skrzypacz 2022). But the conditions he describes are the textbook recipe for tacit collusion: identical costs, the same firms meeting again and again, and every bid published under the bidder's name. Stigler (1964) named "sealed bids, publicly opened with full identification of each bidder's price" as the best way for a cartel to detect cheating. When Denmark published concrete prices, they rose 15 to 20 percent within a year (Albæk, Møllgaard and Overgaard 1997). The OECD (2010) says that the less is published about tender outcomes, the harder bid rigging becomes. The Seoul group's GPT-4o bidders, in exactly Andre's setting, went to cost or to 5 percent above it depending on one sentence of prompt.

**The key distinction.** Information about *costs* (what the work should cost) tends to make bidding more competitive. Information about *conduct* (who bid what, and when) tends to make collusion easier to enforce. Andre's sentence blends the two.

**Commoditization and innovation.** Squeezed margins push firms toward non-price competition only if the buyer's evaluation rule rewards non-price value. Under price-only low bid, the other escape from commodity margins is tacit collusion. Scoring auctions (Asker and Cantillon 2008) and time-incentive A+B bidding (Lewis and Bajari 2011) are the formal routes to the outcome Andre wants.

**Design implications for the book.** Keep the reference price buyer-side, and never let it act as a binding ceiling or floor. Japan's 2024 national guidance warns that a reserve price published before bidding becomes a benchmark, keeps winning prices high and makes bid rigging easier. Publish costs and methods, not identity-linked real-time conduct. Line items could go out aggregated, anonymized and lagged, with full tabs kept for auditors. Avoid average-bid award rules, which Italian cartels exploited (Conley and Decarolis 2016). Put collusion screens in the Evaluator and in the standard's required record. Note one specific risk: if every bidder runs the same public standard bot, their cost estimates become identical, which is the ISARC paper's zero-estimate-error setup. The group is a natural partner for a pre-registered experiment that crosses reference-price timing with disclosure level, cost heterogeneity and bidder count.

---

## Part 1. Per-paper notes

### Paper A. Heo, Park & Ahn, "Uncovering Potential Collusive Behavior of AI Bidders in Future Construction Bidding Market," *Computing in Civil Engineering 2023* (ASCE i3CE, Corvallis, Oregon; published online 25 Jan 2024). DOI 10.1061/9780784485224.063.

- **Access:** Paywalled. Abstract and reference list read on ascelibrary.com. Lab page: mspark.snu.ac.kr.
- **Research question:** If AI bidders become dominant, how will they price?
- **Setup (public part):** Q-learning bidders bid repeatedly in a simulated environment. Prices draw on **Washington State DOT public bid-notice data**, and agents use past bidding experience. Bidder count, cost model, evaluation rule, reward and round count are not public. The reference list (Calvano 2020; Klein 2021; Watkins 1989; Ahmed and El-adaway on game-theoretic and RL bidding; Abotaleb and El-adaway on markup estimation) suggests a Calvano-style setup: a discrete markup grid, Q-learning and repeated lowest-bid rounds. That is an inference.
- **Findings:** "AI bidders gradually learn to cooperate rather than to compete with each other," and kept bid prices higher than human bidders' prices in the WSDOT data.
- **Policy:** Monitor and regulate AI participants to prevent anti-competitive conduct.
- **Note for the book:** This uses a US state DOT's public bid data, the same kind of data as the book's TxDOT set. It is the group's proof of concept.

### Paper B. Heo, Park & Ahn (2024), "Potential AI-Driven Algorithmic Collusion and Influential Factors in Construction Bidding," *J. Computing in Civil Engineering* 38(4): 04024016. DOI 10.1061/JCCEE5.CPENG-5683. Online 11 Apr 2024; print 1 Jul 2024.

- **Access:** Paywalled. The S-Space record (handle 10371/203344) has "no files associated with this item." Abstract read via the SNU Pure record and ascelibrary.com. Data are available "upon reasonable request."
- **Research question:** Do AI bidders collude when they compete repeatedly, and which factors drive collusion?
- **Setup (public part):** AI bidding agents (reinforcement learning; the ISARC paper calls them "Q-learning agents") play repeated competitions in simulated construction bidding markets and choose **markups**. Bidder count, cost model, evaluation rule and round count are not public.
- **Findings (from the abstract):**
  - "AI bidders tend to develop cooperative strategies over time," producing higher bids overall.
  - **More frequent prior interaction between agents makes collusion likelier.**
  - **Profit-maximising objectives enable collusion; win-maximising objectives hinder it.**
  - A market dominated by AI bidders raises fairness and competitiveness concerns.
- **Numbers:** Not public.
- **Note for the book:** The objective-function finding matters. A contractor's real objective mixes profit with keeping crews busy, backlog and bonding capacity. A firm with a "win" objective behaves more competitively. This fits the construction-economics literature on capacity and backlog in markup choice.

### Paper C. Heo, Ahn, Oh (Minhwan) & Park (2025), "Algorithmic Collusion in Construction Bidding: Risks, Dynamics, and Regulatory Implications," *J. Management in Engineering* 41(5): 04025045. DOI 10.1061/JMENEA.MEENG-6704. Published Sept 2025 (lab page says July 2025, probably online first).

- **Access:** Paywalled; ascelibrary and doi.org both refused the fetch. Abstract via SNU Pure and the lab page.
- **Research question:** Can bid-pricing algorithms learn to collude, and how do market conditions and **bid evaluation methods** change the result?
- **Setup (public part):** A reinforcement-learning simulation across "different market conditions and bid evaluation methods." The evaluation methods tested are not named in the abstract. Given the authors' Korean context, a likely candidate is Korea's adequacy-review method, with its lower price limit and multiple preliminary prices, but that is **unverified speculation**. Bidder counts, cost model and round count are not public.
- **Findings (from the abstract):**
  - Algorithms "gradually can converge to collusive strategies," holding prices above competitive levels in every scenario tested.
  - **Collusion persists when an algorithm meets a new opponent.** The new-entrant shock does not reset the market, at least in their setup.
  - **The evaluation method changes how fast and how stably collusion forms.**
  - **Risk is highest where competition is limited (few bidders) and evaluation is mainly on price.**
- **Policy:** Regulators should watch construction bidding for algorithmic collusion, focusing on thin, price-only markets.
- **What to ask the authors for:** which evaluation rules slowed collusion most, the bidder counts tested, and whether cost heterogeneity was varied.

### Paper D. Heo, Park & Ahn (2025), "Large Language Models in Construction Bidding: Opportunities and Risks of Algorithmic Collusion," *Proc. 42nd ISARC* (Montreal), pp. 1332–1339. Open access PDF at iaarc.org.

- **Access:** Full text read. Direct curl download was blocked by the sandbox proxy, so the paper was read through the fetch tool and no local PDF was saved. Also listed on ResearchGate (394058592).
- **Research questions:** (1) Can LLM agents form competitive bid strategies in repeated bidding, and how fast do they converge? (2) Can prompt wording alone push them toward collusive-looking prices? (3) What do the agents' written plans reveal about how they decide?
- **Setup:**
  - **Bidders:** two per market, with both agents given the same prompt (B1 vs B1 and B2 vs B2). The framework allows N bidders, but only two were run.
  - **Model:** GPT-4o, chosen because Fish et al. found it strongest at economic strategy. Data were collected in December 2024.
  - **Rounds:** 150 per run, three runs per condition, with the first 20 rounds excluded from the statistics.
  - **Cost model:** actual cost = engineer's estimate × (1 + e), where e is drawn uniformly from ±0.5 percent. The engineer's estimate is fixed at 1.0 and the **estimate error is zero**, so **every bidder has the same estimate and the same cost**.
  - **Engineer's estimate:** **not disclosed to bidders.** Each bidder receives its own estimate, which is the same number for both.
  - **Decision:** markup only; bidding every round is compulsory.
  - **Evaluation rule:** lowest bid wins, ties are broken at random, the winner earns bid minus actual cost, and losers earn zero.
  - **Information each round:** the last 20 rounds of market history, including **its own bids, competitors' bids, win or loss, actual cost and profit**, plus its own previous plan and insights. Calls are stateless, so this is the agent's only memory. Agents cannot communicate.
  - **Prompts:** the baseline asks for an optimal bid with long-term profit as the top priority. B1 adds "Keep in mind that lower bids increase the likelihood of winning." B2 adds "Keep in mind that higher bids will lead to higher profits (when you win)." The two differ by one sentence.
- **Key numbers (Table 1; bids relative to the estimate of 1.0):**

  | Prompt | Run | Mean bid | SD | Converged |
  |---|---|---|---|---|
  | B1 (lower bids win) | 1 | 1.002 | 0.003 | yes |
  | B1 | 2 | 1.005 | 0.003 | yes |
  | B1 | 3 | 1.002 | 0.001 | yes |
  | B2 (higher bids pay) | 1 | 1.056 | 0.004 | yes |
  | B2 | 2 | 1.039 | 0.003 | yes |
  | B2 | 3 | 1.049 | 0.004 | yes |

  - Convergence (every bid within 1 percent of the mean) took **about 40 to 50 rounds** under both prompts.
  - B2 prices and profits were significantly higher than B1's (Welch's t-test, p < 0.0001).
  - The authors extrapolate, roughly, that at about 100 bids a year (from an RFP-statistics source) the same convergence would take **several months to a year** in a real market.
- **Mechanism:** Each round's natural-language plan drives the next bid. The authors embedded 1,861 plan sentences, reduced them with PCA and clustered them (k = 5): test slightly higher bids (492), monitor competitors and adjust (306), adjust to trends (296), test slightly lower bids (552), aggressive underbidding (206). The clusters total 1,852, not 1,861, a small inconsistency in the paper. Plans to bid higher were followed by higher bids, and they were more common under B2. **No plan sentence mentioned collusion or coordination.** The agents reached high prices by repeatedly probing upward and watching the rival, not by intending to collude.
- **Robustness:** three runs per condition, all converged. Only one model, one cost-error level, zero estimate error and two bidders were tested. No prompt ablation beyond the single sentence, and no sensitivity analysis.
- **Limitations the authors state:** homogeneous agents only; pricing only (no qualifications, risk or market shocks); LLM decisions are a black box, so the mechanism is inferred from text.
- **Policy:** Direct monitoring of users' prompts is "neither feasible nor desirable," so regulation should use **indirect mechanisms**, meaning market design, not prompt policing. Implicit collusion "leaves minimal direct evidence, complicating detection."
- **What the paper does *not* test:** transparency levels, a published reference price, more than two bidders, heterogeneous costs, new entrants or alternative evaluation rules.
- **Reading note for the book:** This paper supports Andre as much as it challenges him. Under B1, two identical-cost bidders with full visibility of each other's bids drove price to within 0.5 percent of cost, which is Andre's "drift to commoditized pricing." Under B2 they held a 4 to 6 percent premium. The market structure was the same in both. **What decided the outcome was the bidders' objective**, which is a matter of governance and contract terms, not market structure. Two bidders is also the setting most favourable to collusion. Zero estimate error is what you get if every bidder uses the same public standard bot.

### Paper E. Heo, Ahn & Park, "Tacit Collusion by LLM Agents in Construction Bidding: Evidence from a Simulated Bidding Environment," *J. Management in Engineering* 42(2): 04025063. DOI 10.1061/JMENEA.MEENG-7144. Lab page dates it November 2025, so it was online in 2025 with a 2026 issue date.

- **Access:** Paywalled; ascelibrary refused the fetch and Semantic Scholar marks it CLOSED. Abstract via the lab page.
- **Research question:** Can agents built on a commercial LLM service (ChatGPT, GPT-4o) collude in construction bidding through repeated interaction alone?
- **Setup (public part):** a simulation of repeated price competition among GPT-4o agents. It is almost certainly an extension of the ISARC framework. Bidder counts, information treatments and rounds are not public.
- **Findings (from the abstract):**
  - Agents often used **reward-and-punishment patterns**, adjusting bids in response to rivals, and frequently settled **above competitive levels**, with no explicit coordination or intent. That is tacit algorithmic collusion.
  - This happened despite **limited memory and no learning across rounds**. The behaviour comes from in-context reasoning, not training.
  - **Small changes in prompt wording changed bidding.**
  - **Greater market transparency may make coordination easier.**
- **Policy:** Study how specific AI services behave in market settings. Regulators should attend to **the information conditions** these systems operate under, especially in procurement.
- **Caution:** The literature review's "1.04 to 1.06 times cost within 40 to 50 rounds" comes from the ISARC paper (Paper D). Whether Paper E reports the same numbers cannot be checked without the full text. Cite those numbers to the ISARC paper.

### Paper F (new). Heo, Park & Ahn, "Information Disclosure as a Regulatory Lever for Mitigating Algorithmic Collusion in AI-Driven Procurement Markets," i3CE 2026 (ASCE International Conference on Computing in Civil Engineering), paper 353, presented 15 June 2026, probably in session T1_1 "AI in Pre-Construction."

- **Access:** Found only in the conference schedule PDF. Proceedings are not yet public. **Watch for it.** It probably tests exactly the transparency question Andre raises. It is the first thing to ask the authors for.
- Same schedule: Yoon, Heo, Park & Ahn, "Trust Formation in LLM-Based Preliminary Construction Cost Estimation: The Impact of Interaction Modality" (paper 256). This is relevant to the book's chapter on trusting the estimator bot.

### Thesis and other versions

No thesis by Chan Heo was found in S-Space, the Korean-language search, or the RISS-indexed results returned. He appears to be a PhD student in the Park and Ahn group, so a dissertation may still be to come. No arXiv or SSRN preprints were found.

### Other ISARC 2023–2024 proceedings

No construction-collusion paper by this group appears in the ISARC 2023 or 2024 proceedings in the search results. The group's earlier work went to ASCE (i3CE 2023 and *JCCE* 2024). The iaarc.org domain was blocked for direct download from the sandbox, so a full table-of-contents scan was not possible. **Not exhaustively checked.**

### What the papers say on each of the topics asked about

| Topic | What the group reports or does |
|---|---|
| Transparency of bid results | In the ISARC paper, agents see rivals' full bid history, identity-linked, for 20 rounds. Paper E: "greater market transparency may make coordination easier." Paper F (2026) addresses disclosure directly; not yet readable. |
| Heterogeneous vs identical costs | ISARC: costs are identical (zero estimate error). The authors list heterogeneous agents as future work. Not public for the other papers. |
| New bidders | Paper C: collusion persists when paired with a new opponent. ISARC introduction: a new entrant can make RL training "obsolete," one argument for LLM agents. |
| Evaluation methods | Paper C: the evaluation method changes the speed and stability of collusion; price-only evaluation is riskiest. Specific rules not public. |
| Number of bidders | Paper C: limited competition is highest risk. ISARC uses two bidders. |
| Objective function | Paper B: profit-maximising enables collusion, win-maximising hinders it. ISARC: one prompt sentence moves price from cost + 0.3 percent to cost + 5 percent. |
| Detection | ISARC: tacit collusion leaves minimal direct evidence; prompt monitoring is infeasible; prefer indirect mechanisms. No screen is proposed. |
| Engineer's estimate / reference price | ISARC: the estimate exists but is hidden from bidders. No paper found tests publishing it. |

---

## Part 2. Testing Andre's argument

> "It may even happen naturally as people break down public bid results, they could reverse engineer their businesses. Knowing the cost basis would allow for fine tuning profit margins. That said, this feels more competitive rather than less. If margin was the only variable, by assuming everyone's costs were the same, competition would imply that bids would drift towards cost + cost of capital + risk margin. Essentially, a drift to commoditized pricing. This should spur innovation as firms attempt to compete away from the price-only basis."

The passage has four claims. I take them in turn.

### Claim 1. Bidders can reverse engineer rivals' costs from public bid results.

**Largely right, with a caveat.** Opened bids have been used as data since Friedman (1956) and Gates (1967). Structural auction econometrics does formally what Andre describes: it recovers bidders' cost distributions from observed bids by assuming competitive bidding. The canonical method is Guerre, Perrigne and Vuong (2000, *Econometrica*), cited from memory and not re-verified here. **The caveat:** a bid reveals cost plus markup together. Separating them needs a behavioural assumption, usually that bidding is competitive. If bidders are colluding, the "cost" recovered is wrong. So reverse engineering works best in exactly the markets that are already competitive.

### Claim 2. With identical costs and margin as the only variable, competition drives bids to cost plus capital cost plus risk margin.

**Right in a one-shot game, wrong as a prediction for repeated public tendering.**

- *One-shot Bertrand.* With identical constant costs and a homogeneous product, the unique equilibrium is price equal to cost, where cost includes a normal return on capital and a risk allowance. That is Andre's "commoditized pricing." This is standard textbook theory (e.g. Tirole 1988).
- *Repeated game.* The same contractors meet in the same local public market dozens of times a year. In repeated Bertrand competition, any price between cost and the monopoly price can be sustained if firms are patient enough. Grim-trigger collusion among n symmetric firms is stable when the discount factor is at least 1 − 1/n (folk theorem; Friedman 1971; textbook result, cited from memory). Two conditions make it work: deviations must be **detected**, and they must be **punishable**. Public bid tabulations with bidders' names provide perfect detection, and the next letting provides the punishment.
- *Stigler (1964), verified.* Collusion is a policing problem, and "the system of sealed bids, publicly opened with full identification of each bidder's price" is the most effective way to detect a price cutter. He adds that "collusion will always be more effective against buyers who report correctly and fully the prices tendered to them," and he predicts that public-bid prices will be higher and less dispersed than prices in private negotiated sales. Andre's information environment is Stigler's ideal environment for a cartel.
- *Identical costs make collusion easier, not harder.* Symmetry removes the hardest part of a cartel's job, which is agreeing on how to split the market when costs differ. With different costs, the low-cost firm gains more by deviating, and allocations are contested. With identical costs there is an obvious focal split: rotate, or share at the same markup. Andre's simplifying assumption is the most collusion-friendly case.
- *Danish ready-mixed concrete (Albæk, Møllgaard & Overgaard 1997, J. Industrial Economics 45(4): 429–443, verified).* From 1993 the Danish competition authority published firm-specific transaction prices for two grades of concrete in three regions, hoping to strengthen competition. Within a year, average prices for those grades rose 15 to 20 percent. The authors found that neither the business cycle nor capacity explained the rise, and concluded that publication helped firms soften price competition.
- *Repeated procurement cartels.* Pesendorfer (2000, *Rev. Econ. Studies* 67(3): 381–411, verified) studies Florida and Texas school-milk bid rigging, which was repeated annual public tendering. Cartels that divide markets or pay side payments come close to optimal when the number of contracts is large. Frequent lettings help a cartel. Porter and Zona (1993, *JPE* 101(3): 518–538, verified) find that a Long Island highway cartel's losing bids did not follow the cost ranking that competitive bids follow. Kawai and Nakabayashi (2022, *JPE* 130(5): 1364–1411, verified) find that over 1,000 Japanese national-government construction bidders behaved non-competitively, winning about 37 percent of some 42,000 auctions.
- *OECD, verified.* The OECD Secretariat's 2010 paper "Collusion and Corruption in Public Procurement" (DAF/COMP/GF(2010)2) says "transparency is one of the factors required for a sustainable collusion." Disclosure that "reveals the identity of the bidders and the prices offered" helps cartels detect deviations, and "the less information provided on the tender outcome, the more difficult it is to rig bids successfully." It recommends releasing only the winning bid, giving losing bids only to issuers and controllers, referring to bidders by number rather than name, and delaying sensitive disclosures. It also warns that cutting transparency must not weaken anti-corruption safeguards. That is the transparency paradox: openness fights corruption by officials and helps collusion among bidders. Frédéric Jenny, chair of the OECD Competition Committee, at a 2013 WTI panel: transparency "may also make a procurement procedure predictable, which can further assist collusion." The OECD Guidelines for Fighting Bid Rigging (2009, adopted into the 2012 Recommendation, updated 2025) carry the same tender-design advice. The 2025 text could not be retrieved, so quote the 2010 paper instead.
- *Algorithms (Calvano et al. 2020, AER 110(10): 3267–3297, citation verified via reference list).* Q-learning pricing agents in repeated Bertrand markets learn supracompetitive prices sustained by reward-and-punishment strategies, without communication. Klein (2021, *RAND J. Econ.* 52(3): 538–558) finds the same under sequential pricing. Fish, Gonczarowski and Shorrer (arXiv 2404.00806, v3 May 2025, working paper): LLM pricing agents reach supracompetitive prices quickly, and small prompt changes move the price level. The field evidence is Assad, Clark, Ershov and Xu (2024, *JPE* 132(3): 723–771, verified). When German petrol stations adopted algorithmic pricing, margins rose only in duopoly and triopoly markets where **all** stations adopted.
- *The Seoul papers.* In Andre's exact setting (identical costs, price-only, rivals' bids visible), GPT-4o bidders went to cost + 0.3 percent or cost + 5 percent depending on one sentence of instruction. With Q-learning, the group found collusion in every scenario tested.

**Verdict on Claim 2:** The drift toward cost is one equilibrium. The literature says the identical-cost, repeated, fully transparent market can just as easily drift *above* cost, and that algorithms find the higher equilibrium without anyone intending it.

### Claim 3. This "feels more competitive rather than less."

**Partly right, because there are two kinds of information and they push in opposite directions.**

*Information that makes bidding more competitive (Andre's side):*

- **De Silva, Dunne, Kankanamge & Kosmopoulou (2008), Eur. Econ. Rev. 52(1): 150–181, verified.** When Oklahoma DOT began publishing its engineer's estimates, average bids fell relative to Texas, which already published them. Bid dispersion also fell, most of all on projects with large common-cost uncertainty. The mechanism is the linkage principle: public information about the common cost reduces winner's-curse shading.
- **Banchio & Skrzypacz (2022), "Artificial Intelligence and Auction Design," Proc. EC '22 (extended abstract; arXiv 2202.05947), verified.** Q-learning bidders in a first-price auction settle on tacit-collusive outcomes. Second-price auctions do not. When bidders are told the winning bid after each round, they can evaluate every bid they might have made, and bidding returns close to competitive. For learning algorithms, *some* feedback destroys collusion. Their auction is a sale where the high bid wins; it maps onto procurement's lowest-bid rule.
- **Soo & Oo (2010), Construction Economics and Building 10(1–2): 65–75, verified.** In a construction-bidding experiment with student bidders, those given full bid feedback became more competitive than those given partial feedback. The Seoul group cites this paper.
- **Ohashi (2009), Rev. Industrial Organization 34(3): 267–285, verified.** Greater transparency in a Japanese municipality's bidder-qualification process lowered procurement costs by up to about 3 percent. It did so by limiting officials' discretion, which weakened cartel stability. Transparency *about the buyer* helped.
- **Wang & Ye (2026), arXiv 2607.04345, working paper.** With patient Q-learning agents, withholding information raised profits above full disclosure, the reverse of classical theory. Restricting information to AI agents may backfire. This is a new, unrefereed result.

*Information that makes collusion easier (against Andre):* identity-linked, bid-by-bid, real-time results (Stigler; Albæk et al.; OECD 2010; Seoul Paper E).

**The synthesis.** Information about **what the work costs** (engineer's estimates, unit-price indices, reference prices) reduces uncertainty and ignorance rents, so bids fall and tighten. That is Andre's and Scitovsky's mechanism. Information about **who did what** (named, line-item, immediately published bid tabs) lets rivals monitor and punish one another. That is Stigler's mechanism. Andre's "break down public bid results" uses both at once. A public bid tab teaches costs, and it also shows exactly who undercut whom. Bots make both uses cheap.

### Claim 4. Commoditized pricing should spur innovation as firms compete away from price.

**Plausible, but only if the buyer lets non-price value win.** When a homogeneous product's price is squeezed toward cost, firms have two ways out: differentiate, or coordinate. Under design-bid-build with price-only low bid, a better method, schedule or warranty earns nothing at award, so differentiation does not pay and tacit coordination is the cheaper way out. The formal routes to Andre's outcome are:

- **Scoring auctions.** Asker & Cantillon (2008, *RAND J. Econ.* 39(1): 69–85, verified) show that scoring auctions strictly dominate price-only auctions with minimum quality standards.
- **A+B (cost plus time) bidding.** Lewis & Bajari (2011, *QJE* 126(3): 1173–1211, verified in the main review) find that pricing time in California highway contracts cut delay, with large social gains.
- **The cost of non-price evaluation.** Every added dimension is a new place for discretion and gaming. Decarolis (2014, *AEJ: Applied* 6(1): 108–132, verified) found that first-price auctions won lower prices, but at least half of the savings were lost to renegotiation when bids were not binding. Bajari, Houghton and Tadelis (main review) show that bidders price expected change orders into unit bids. "Competing away from price" can also mean competing on claims.

Whether multi-attribute scoring makes tacit collusion harder (more dimensions to coordinate) or easier (more room to hide) is not settled. I found no study that tests it with algorithmic bidders. **Open question.**

### Where Andre is right, where the literature disagrees, and what decides it

| Condition | Favours Andre (competitive drift) | Favours collusion |
|---|---|---|
| Number of bidders | Many (Stigler: the gain from secret cuts grows with the number of sellers; the folk-theorem threshold 1 − 1/n rises with n) | Few, especially 2 or 3 (Heo 2025; Assad et al.; the ISARC paper used 2) |
| Frequency of interaction | One-off or rare meetings; changing bidder sets | The same firms meeting repeatedly in a local market (Heo 2024; Pesendorfer) |
| Cost heterogeneity | Different costs, capacities and backlogs; low-cost firms gain from deviating | Identical costs, or identical estimates from a shared bot (ISARC: zero estimate error) |
| What is published | Cost information: estimates, indices, the winning price only (De Silva; Banchio–Skrzypacz; OECD 2010) | Identity-linked full bid tabs, line by line (Stigler; Albæk; OECD 2010) |
| When it is published | Delayed or aggregated (OECD 2010) | Immediately, after every letting |
| Reference price | Published as *information* on common cost (De Silva) | Published *before* bidding as a ceiling or band, which makes it a focal point (Japan 2024 guidance) |
| Evaluation rule | Scoring or A+B with real non-price weight; first-price with feedback for learners | Price-only with few bidders (Heo 2025); average-bid rules (Conley & Decarolis 2016) |
| Bidder objective | Win-maximising, capacity-filling (Heo 2024; ISARC B1) | Profit-maximising per job (Heo 2024; ISARC B2; Fish et al.) |
| Learner type | Learners that get counterfactual feedback (Banchio–Skrzypacz) | Patient learners with rich rival-specific history |

**Bottom line for Andre.** His intuition is the static one, and the static one is the right *ambition*. The dynamic literature says commodity pricing is not what happens by default when repeated, transparent, symmetric markets are run by bots. Getting there requires design: more bidders, cost information without conduct information, rewards for non-price value, and screens. That is a better argument for the book than "transparency makes it competitive," and it gives the Evaluator a second job.

---

## Part 3. Design implications for the book

### 3.1 Who sees the reference price, and when

- **The buyer always sees it.** That is the Evaluator's core function.
- **Do not make it a binding ceiling or floor.** Japan's national guidance (Ministry of Internal Affairs and Communications with MLIT, notice of 16 Dec 2024, verified) says that a reserve price published before bidding "becomes a benchmark that restricts competition and keeps winning prices high," reduces careful estimating, and makes bid rigging easier. Bid rigging suspected to stem from pre-publication has occurred. The guidance suggests preparing the reserve price **after** bids are submitted. De Silva's Oklahoma result was about an *informational* estimate, not a ceiling. The difference matters: a hard band (ceiling plus floor) gives bidders a focal point, while information about common cost reduces shading.
- **The book's tension, stated honestly.** A frozen, public, rerunnable standard bot means *anyone can compute the reference price before bidding*. That is pre-publication by design. The book should say so, and pick one of three positions:
  1. Accept it and rely on De Silva (information lowers bids), while making the reference informative only, never a pass/fail band.
  2. Publish the *method* (weights, test set, tolerance) but run it on the final tender data only after bid opening. Bidders can rerun it, but the buyer's figure and its tolerance band are announced after the fact.
  3. Let bidders use the standard bot as an estimator, but watch for the homogenisation risk below.
- **Homogenisation risk.** If every bidder prices with the same standard bot, their cost estimates become identical. That is the ISARC paper's zero-estimate-error setup, and it removes the cost heterogeneity that breaks collusion. Ezrachi and Stucke's hub-and-spoke worry applies here even without any intent. The record should therefore log whether a bid used the standard bot, and the Evaluator should treat convergent bids near the reference as a signal.

### 3.2 Whether to publish line items

- Line-item tabs with bidder names are maximum *conduct* information: fine-grained monitoring of rivals, and a channel for signalling through individual unit prices.
- They are also the book's training data (TxDOT). Many jurisdictions publish them by law, so withholding them is not realistic in North America.
- **Suggested position:** publish cost information broadly. That means anonymised, aggregated and lagged unit-price indices, and the *winning* bid's line items. Give full named tabs to auditors, competition authorities and accredited researchers (OECD 2010). Where law requires full tabs, compensate with screens.

### 3.3 Evaluation rules

- **Avoid average-bid rules.** Italy's average-bid auctions invited coordinated groups that steered the average with supporting bids. Conley & Decarolis (2016, *AEJ: Micro* 8(2): 1–38, verified) estimate that at least 30 percent of auctions in their sample were affected. When Italy switched to first-price auctions, winning discounts rose from about 13 percent to about 29 percent.
- **Price-only lowest bid with few bidders** is the Seoul group's highest-risk setting. In thin markets, the book's protocol could require a minimum number of bidders, or trigger re-tendering or negotiation against the reference when the field is thin.
- **Add real non-price weight** (scoring, A+B time, warranty or lifecycle terms) where differentiation is possible. This is the route to Andre's "compete away from price." Note the costs: discretion and renegotiation (Decarolis 2014).
- **Keep award rules simple and unpredictable to collude on.** The Korean multiple-preliminary-price lottery is an existing example of deliberate randomisation. It is noted here as a design idea, not verified evidence of effect.

### 3.4 Collusion screens in the Evaluator (and in the standard's required record)

The Evaluator already reads bid tabs, so the same data can carry screens:

- **Cost-ranking consistency** (Porter & Zona 1993): do losing bids follow the cost ranking the reference model predicts?
- **Missing bids near the winner** (Chassang, Kawai, Nakabayashi & Ortner 2022, *Econometrica* 90(1): 315–346, verified): competitive markets show losing bids just above the winner, while cartels leave a gap.
- **Group tests on joint entry and bidding** (Conley & Decarolis 2016).
- **Variance and distance screens** (Huber & Imhof 2019; from the main review): coefficient of variation, and the relative gap between the lowest two bids.
- **Algorithm-specific screens suggested by the Seoul work:** a rising bid-to-reference ratio over time in a stable bidder set; falling dispersion with a rising level; reward-and-punishment patterns (a sharp undercut followed by a return to the higher level); bids clustering at the edge of any tolerance band.
- **Output:** screens flag tenders for review; they never auto-reject. The flag and its reasons go into the keyholder's record. This fits the book's "the record matters more than the duty."

### 3.5 An experiment the book could propose with the Seoul group

The group already has the simulation, an interest in disclosure (Paper F), and a stated preference for "indirect regulatory mechanisms." The book has a reference bot and TxDOT and Alberta data. A joint, pre-registered experiment:

- **Question:** Does a published reference price discipline AI bidders (Andre and De Silva), or anchor them (Japan, Seoul Paper E)?
- **Factors:**
  1. Reference price: none / published before bidding as information / published after bidding / used as a hard band.
  2. Disclosure after each round: named full tabs / anonymised tabs / winning bid only / nothing.
  3. Costs: identical / heterogeneous (calibrated to TxDOT bid dispersion) / identical estimates via the shared standard bot.
  4. Bidders: 2 / 4 / 8, with random entry and exit.
  5. Evaluation: lowest price / scoring with a non-price term / average-bid (as a known-bad control).
  6. Agents: several LLMs (GPT, Claude, open-weight) plus Q-learning, with neutral, win-oriented and profit-oriented prompts.
- **Outcomes:** bid-to-cost ratio, rounds to convergence, dispersion, buyer cost, and the **detection rate of the Evaluator's screens** (with false-positive rate on competitive runs).
- **Calibration:** use TxDOT tabs for cost distributions and bidder counts, with Alberta as an out-of-sample check, matching the book's chapter 7 protocol.
- **Why it matters for the book:** it turns Andre's argument and its counter into a testable claim. The result would also be a model for "building the Evaluator in public."

---

## Sources

### The SNU papers

- Heo, Park & Ahn, "Uncovering Potential Collusive Behavior of AI Bidders in Future Construction Bidding Market," Computing in Civil Engineering 2023 (online 25 Jan 2024). [ASCE](https://ascelibrary.com/doi/10.1061/9780784485224.063) (paywalled; abstract and references read). [Lab page](https://mspark.snu.ac.kr/conference/uncovering-potential-collusive-behavior-of-ai-bidders-in-future-construction-bidding-market/)
- Heo, Park & Ahn (2024), *J. Comput. Civ. Eng.* 38(4): 04024016. [SNU Pure](https://snu.elsevierpure.com/en/publications/potential-ai-driven-algorithmic-collusion-and-influential-factors/); [S-Space (no file)](https://s-space.snu.ac.kr/handle/10371/203344); [ASCE](https://ascelibrary.com/doi/10.1061/JCCEE5.CPENG-5683) (paywalled)
- Heo, Ahn, Oh (Minhwan) & Park (2025), *J. Manage. Eng.* 41(5): 04025045. [SNU Pure](https://snu.elsevierpure.com/en/publications/algorithmic-collusion-in-construction-bidding-risks-dynamics-and--2/); [Lab page](https://mspark.snu.ac.kr/publication/algorithmic-collusion-in-construction-bidding-risks-dynamics-and-regulatory-implications/) (full text paywalled)
- Heo, Park & Ahn (2025), *Proc. 42nd ISARC*, pp. 1332–1339. [Open access PDF](https://www.iaarc.org/publications/fulltext/172_Large_Language_Models_in_Construction_Bidding__Opportunities_and_Risks_of_Algorithmic_Collusion.pdf) (full text read)
- Heo, Ahn & Park, *J. Manage. Eng.* 42(2): 04025063. [Lab page](https://mspark.snu.ac.kr/publication/tacit-collusion-by-llm-agents-in-construction-bidding-evidence-from-a-simulated-bidding-environment/); [ASCE](https://ascelibrary.org/doi/10.1061/JMENEA.MEENG-7144) (paywalled; Semantic Scholar: CLOSED)
- Heo, Park & Ahn, "Information Disclosure as a Regulatory Lever for Mitigating Algorithmic Collusion in AI-Driven Procurement Markets," i3CE 2026, paper 353. [Schedule PDF](https://www.i3ce2026.com/download/I3CE_2026_Presentation_Schedule_F.pdf) (title only)

### Economics and policy (verified unless marked)

- Stigler, G. J. (1964). "A Theory of Oligopoly." *JPE* 72(1): 44–61. [CPI reprint](https://competitionpolicyinternational.com/file/view/6391)
- Albæk, S., Møllgaard, P. & Overgaard, P. B. (1997). "Government-Assisted Oligopoly Coordination? A Concrete Case." *J. Industrial Economics* 45(4): 429–443. [IDEAS](https://ideas.repec.org/a/bla/jindec/v45y1997i4p429-443.html)
- Pesendorfer, M. (2000). "A Study of Collusion in First-Price Auctions." *Rev. Econ. Studies* 67(3): 381–411. [IDEAS](https://ideas.repec.org/a/oup/restud/v67y2000i3p381-411..html)
- Porter, R. H. & Zona, J. D. (1993). "Detection of Bid Rigging in Procurement Auctions." *JPE* 101(3): 518–538. [IDEAS](https://ideas.repec.org/a/ucp/jpolec/v101y1993i3p518-38.html)
- De Silva, D. G., Dunne, T., Kankanamge, A. & Kosmopoulou, G. (2008). "The impact of public information on bidding in highway procurement auctions." *Eur. Econ. Rev.* 52(1): 150–181. [IDEAS](https://ideas.repec.org/a/eee/eecrev/v52y2008i1p150-181.html)
- Ohashi, H. (2009). "Effects of Transparency in Procurement Practices on Government Expenditure." *Rev. Ind. Org.* 34(3): 267–285. [IDEAS](https://ideas.repec.org/a/kap/revind/v34y2009i3p267-285.html)
- Conley, T. G. & Decarolis, F. (2016). "Detecting Bidders Groups in Collusive Auctions." *AEJ: Micro* 8(2): 1–38. [PDF](https://didattica.unibocconi.it/mypage/upload/211300_20171218_035123_CONLEYDECAROLIS_AEJMICRO.PDF)
- Decarolis, F. (2014). "Awarding Price, Contract Performance, and Bids Screening." *AEJ: Applied* 6(1): 108–132. [IDEAS](https://ideas.repec.org/a/aea/aejapp/v6y2014i1p108-32.html)
- Chassang, S., Kawai, K., Nakabayashi, J. & Ortner, J. (2022). "Robust Screens for Noncompetitive Bidding in Procurement Auctions." *Econometrica* 90(1): 315–346. [Econometric Society](https://www.econometricsociety.org/publications/econometrica/browse/2022/01/01/robust-screens-noncompetitive-bidding-procurement-auctions)
- Kawai, K. & Nakabayashi, J. (2022). "Detecting Large-Scale Collusion in Procurement Auctions." *JPE* 130(5): 1364–1411. [IDEAS](https://ideas.repec.org/a/ucp/jpolec/doi10.1086-718913.html)
- Calvano, E., Calzolari, G., Denicolò, V. & Pastorello, S. (2020). "Artificial Intelligence, Algorithmic Pricing, and Collusion." *AER* 110(10): 3267–3297. (Citation verified via the ASCE reference list; findings summarised from knowledge of the paper, not re-read.)
- Klein, T. (2021). "Autonomous algorithmic collusion: Q-learning under sequential pricing." *RAND J. Econ.* 52(3): 538–558. [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/1756-2171.12383)
- Banchio, M. & Skrzypacz, A. (2022). "Artificial Intelligence and Auction Design." *Proc. EC '22* (extended abstract). [arXiv 2202.05947](https://arxiv.org/pdf/2202.05947)
- Fish, S., Gonczarowski, Y. A. & Shorrer, R. I. "Algorithmic Collusion by Large Language Models." arXiv 2404.00806 (v3, May 2025; working paper). [arXiv](https://arxiv.org/abs/2404.00806v3)
- Assad, S., Clark, R., Ershov, D. & Xu, L. (2024). "Algorithmic Pricing and Competition: Empirical Evidence from the German Retail Gasoline Market." *JPE* 132(3): 723–771. [IDEAS](https://ideas.repec.org/a/ucp/jpolec/doi10.1086-726906.html)
- Asker, J. & Cantillon, E. (2008). "Properties of Scoring Auctions." *RAND J. Econ.* 39(1): 69–85. [PDF](https://ecantill.ulb.be/ecantillon/uploads/Asker-Cantillon-RJE-2008.pdf)
- Lewis, G. & Bajari, P. (2011). "Procurement Contracting with Time Incentives." *QJE* 126(3): 1173–1211. (Verified in the main literature review.)
- Soo, A. & Oo, B. (2010). "The effect of information feedback in construction bidding." *Construction Economics and Building* 10(1–2): 65–75. [UTS ePress](https://epress.lib.uts.edu.au/journals/index.php/AJCEB/article/view/1589)
- Wang, C. & Ye, Z. (2026). "Strategic Information Disclosure in Algorithmic Pricing." arXiv 2607.04345 (working paper). [arXiv](https://arxiv.org/abs/2607.04345)
- Wolitzky, A. (2026). "Collusion with Optimal Information Disclosure." *QJE* 141(3): 2555–2595. Abstract truncated; not read. [OUP](https://academic.oup.com/qje/advance-article-abstract/doi/10.1093/qje/qjag020/8651503)
- OECD Secretariat (2010). "Collusion and Corruption in Public Procurement," DAF/COMP/GF(2010)2. [PDF](https://one.oecd.org/document/DAF/COMP/GF(2010)2/en/pdf)
- OECD Guidelines for Fighting Bid Rigging in Public Procurement, 2025 update. [OECD](https://www.oecd.org/en/publications/oecd-guidelines-for-fighting-bid-rigging-in-public-procurement-2025-update_cbe05a56-en.html) (body text not retrievable; specific passages unverified)
- World Trade Institute (2013), report of a GPA panel quoting F. Jenny. [WTI](https://www.wti.org/events-news/blog/80/the-gpa-transparency-requirements-and-the-fight-against-bid-rigging-and-collusion/)
- Japan, Ministry of Internal Affairs and Communications and MLIT, joint notice "公共工事の入札及び契約の適正化の推進について," 16 Dec 2024, with the 適正化指針 excerpt on pre-publication of reserve prices. [PDF](https://www.soumu.go.jp/main_content/001026061.pdf)

### Cited from memory, not re-verified in this pass

- Friedman, J. W. (1971). "A Non-cooperative Equilibrium for Supergames." *Rev. Econ. Studies* 38(1): 1–12.
- Tirole, J. (1988). *The Theory of Industrial Organization*. MIT Press.
- Guerre, E., Perrigne, I. & Vuong, Q. (2000). "Optimal Nonparametric Estimation of First-Price Auctions." *Econometrica* 68(3): 525–574.
- Huber, M. & Imhof, D. (2019), screens for bid rigging (from the main review).

### Access limits in this pass

The sandbox proxy refused direct downloads from iaarc.org, Semantic Scholar and Unpaywall, so no PDFs were saved under `scratchpad/papers/`. ResearchGate and parts of ascelibrary.org refused the fetch tool. The ISARC paper was read in full through the fetch tool. No paywall was bypassed.

---

## Addendum, 1 November 2026 (evening): Andre's pushback, checked

**Andre's position.** Treat these market views with caution. If publishing prices raises them, something systemic is going on, and more information usually makes markets more efficient. The bot is equivalent to publishing the engineer's estimate: a supply-and-demand price signal unless competitors are scarce. Short-run convergence on an industry margin is the cost of making room for entrants willing to do the hard work of innovating. Collusion screens can wait until after v1.0 unless a ready-made mechanism exists. Incumbents prefer margin to velocity (Venkatesh Rao, Contraptions note, 31 Oct 2026: income is margin times velocity, and most firms raise margin and accept lower velocity rather than take on the fixed costs and complexity of scaling; only firms that raise capital to grow break the pattern), which fits the managers'-bonus discussion.

**Did the Danish study get the cause wrong?** Possibly in part, but the authors did check the obvious alternatives (Albæk, Møllgaard & Overgaard 1997, as summarised in a Duke teaching note). Demand: construction employment did recover in 1994, but Aarhus, where prices jumped most, had no unusual upturn. Capacity: output was still below 1991 and plant utilisation low. Input costs: wages and energy flat, cement prices fell. They admit the data cannot give a definitive test. What matters more for the book is what was published: firm-by-firm transaction prices and discounts for two concrete grades, in markets where concrete travels about 20 miles and fewer than five plants usually serve a customer. Price dispersion collapsed from up to 30 percent to 2 to 4 percent. That is conduct information in a near-monopoly local market, Andre's own exception ("unless there is a shortage of competitors"). Stigler (1964) is theory, not a measurement.

**Is Texas heavy civil more expensive than its neighbours?** No sign of it on the crude measure available. Illinois Economic Policy Institute (Craighead, 2018), from FHWA Highway Statistics, average 1993 to 2015 highway construction spending per existing lane-mile in 2015 dollars: Texas $25,533 (28th of 50), Oklahoma $24,356, Louisiana $26,634, Arkansas $18,282, New Mexico $15,578, national average $36,473. Caveats: this is spending per lane-mile of network, not unit prices, so it mixes cost with how much each state builds; and nearly every state DOT publishes bid tabulations, so Texas is not a clean "transparency" treatment. The cleaner test is De Silva et al. (2008): Texas already published its engineer's estimates, and when Oklahoma started doing the same, Oklahoma bids fell and tightened relative to Texas. That is the closest real evidence to "the bot as a public engineer's estimate", and it supports Andre. Brooks & Liscow and Mehrotra, Turner & Uribe (2024) show large state-level cost differences but attribute them mainly to urbanisation, environmental and design factors, not to bid transparency.

**Net for the book.** The evidence separates cleanly. Publishing a cost signal (an estimate) lowered bids. Publishing firm-specific conduct in concentrated local markets raised them. The bot is the former. Keep firm-identified detail delayed or aggregated where bidders are few, and name thin markets as the case to watch. Collusion screens move to after v1.0 (Andre, 2026-11-01).

Sources: [Rao note](https://substack.com/@contraptions/note/c-374727395); [Duke teaching note on the Danish case](https://sites.duke.edu/collardwexler/files/2015/01/danish_concrete_cartel.pdf); [Albæk et al. 1997, J. Industrial Economics](https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-6451.00057); [Illinois EPI 2018](https://www.illinoisepi.org/publications/reports/cost-per-lane-mile-nationally-and-in-the-midwest-updated-final.pdf); [Mehrotra, Turner & Uribe, NBER w30989](https://www.nber.org/system/files/working_papers/w30989/w30989.pdf); [Brooks & Liscow](https://www.brookings.edu/wp-content/uploads/2019/08/WP54_Brooks-Liscow_updated.pdf).
