# Liability shifts to the user's bot

<!--
Part II. The machines
Target: 1,500 words, redraft
Brief: The heart of the manifesto. Why a bidder should not be compelled to report what its bot finds, why the record matters more than the duty, silence before the contract, and the construction manager as a fourth party. Both statements true: the bidder may stay quiet, and the system still needs disclosure. Also (bot council, 2026-10-31): the Listener makes editorial choices about what to bring forward; say who answers for what it collated or left out, or the record reads as one nobody is accountable for reading. Why a bidder would raise an error, Andre, 2026-10-31 (verbatim): "The best reason to raise an error would be to prevent another bidder from exploiting it. This assumes that the firms are competing on primarily on price and the bidder revealing the weakness would rather use their competitive advantage -location, productivity, capital structure, personnel, ect... to win the bid over strategic bidding. Bot Procurement does not fix this issue, but it could lower costs for revealing them. Faster plan reviews from potential bidders combined would allow the issues to be reviewed early in the tender process and the changes reviewed with little effort. Encouraging companies that want to compete based on skill to make more Requests for Information (RFI) since they will be easier to process." (The reward side of Galbraith's Star Model; it needs no duty, since an answer goes to every bidder.)
Sources: the case study's "Liability shifts to the user's bot" and "Who bears the cost of validating intent"; positions 1, 2, 7, 9, 16 and 20; the quoted passages under "Tensions to be managed" in `sentences-since-3-october.md`.
Reasons against compelling disclosure (Andre's memo of 2 October 2026; Andre cleared it for the book, 2026-11-02). The public version is positions §2 (`context-bank/positions-liability-disclosure-buyer-bot.md`), so quote from there: §2.1 bidders are not the designers, and a duty assigns them a licensed professional's liability; §2.2 the work is not paid for, and paying for it invites claims or "professional bidders who bid for the fee"; §2.3 issue spamming on open tenders, where a flood of minor issues hides the major one and extends tenders into the construction season; §2.4 questions would be asked badly: "compelling someone to ask a question is fairly trivial; compelling them to make the question useful is impossible"; §2.5 design quality would fall. Andre tested his own remedy against the same objection (the Listener could also tempt designers to lower quality; answer: the designer's service levels). Mechanisms from the bot council that answer "the record, not the duty" (`C:\hex_ai\bot-council\transcripts\2026-10-06-duty-to-report-discussion.md`): publish the checks rather than the standard (an error inside the published checks is patent, outside them latent); an allowance rule under which a silent find on an allowance item is worth nothing; and Andre's malicious-bidder problem (run a thorough bot, submit a thin one). Pair it with the asymmetric record (`2026-10-10-pibot-web-alignment-and-the-record-tension.md`): the buyer's log is a public record, the bidder's is its own.
Literature (`literature-review-2026-11-01.md`, Part 1): Ron Engineering, Edgeworth, Bail, Tercon; Sintra 2024 (Quebec duty to inquire); Texas Bus. & Com. Code §59.051 (bid-stage diligence; both qualify "no compelled disclosure"); Bajari, McMillan & Tadelis 2009; Scholz on algorithmic contracts. Collusion (`collusion-papers-notes-2026-11-01.md`, Part 3.1): who may use the standard bot, with the Seoul group's collusion evidence on one side and De Silva on the other, kept in tension.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Positions §1 to §7 were written before the repository began quoting him: there the meaning is Andre's and much of the wording is Claude's edit, and they are marked "Andre's meaning, edited wording". Notes in italics are Claude's. Delete this section as the chapter is written. This is the longest set; the chapter's 1,500 words will use perhaps a third of it.*

### Liability shifts to the user's bot

> Liability for AI bots will likely shift from the information provider, a company's chatbot, to the user's bot, since this would better match our society's state of contract law. It would be easier for the AI vendor to disclaim all liability for accuracy to its own user (use at your own risk) than to deal with the contract law surrounding estoppel, which would apply to customers relying directly on a company's bot. Specifications and drawings already work like this for review by human estimators.

> The structure for the three parties involved in the procurement API follows from this. The Tender API would be the public-facing documents. The Bidders would supply their own bots to review the data. This bot, or another (the Bidder's choice, really), would then communicate with the Bidder about potential deficiencies. The Bidder could instruct its bots to RFI (Request for Information) the issue or to remain quiet, since compelling this information would create a massive Kafka protocol. There would be a forward-facing bot for the Buyer side of the Tender, but it would only be there as an MCP connection for Bidder questions. On both sides, the inner bot structures would be subject to variability.

(`case-studies/andre-comeau/README.md`, "Liability shifts to the user's bot")

*The "MCP connection" sentence predates the Listener (positions §6); the chapter should describe the Listener instead.*

### Both statements true

*Andre's meaning, edited wording:*

> - The Bidder's bot's interpretation of the project requirements is the Bidder's responsibility.
> - The Buyer and Designers are liable for error-free documentation.
>
> Since error-free documentation is currently written for human users, it is the shift to bot-first procurement that implies the need for official standards. Until Designer liability can be constrained by standards or insurance, there will be limited incentive to move away from human-first communication.

(positions §7, recorded 2026-10-02; decision 23)

*Andre's meaning, edited wording, on why the Designer should not run a bot that answers bidders:*

> The alternative to each party running its own bot would be for the Designer or Owner to provide the Witness and Oracle that Bidders query. That arrangement turns answers into liabilities. Bidders would all ask different questions, and a bot answers from a probabilistic model, so the answers would differ from one query to the next. Even where every answer is technically correct, and even where the differences look immaterial, current construction contract law could allow a claim: a Bidder can say its bid was unsuccessful because it relied on what it was told.

(positions §1, recorded 2026-10-02)

*Claude's note there: in* Edgeworth *the Supreme Court of Canada held that the firm that prepared tender documents could be liable to a bidder who relied on them, and Canadian tender law requires the owner to treat bidders equally, which differing answers would breach. The heading invites a misreading: it is liability for the reading that shifts, not for the design.*

### Why a bidder should not be compelled to report

*Andre's meaning, edited wording. The five reasons are listed in the hidden note above; these are the passages that carry them best.*

> When a human estimator notices an error and says nothing, there is no record, so there is little risk of a claim. When a Bidder's bot finds the error and reports it to the Bidder, and the Bidder decides not to tell the Buyer, that decision could surface in the discovery process of a later lawsuit and create liability.

(positions §2, "Why it matters for bots")

> Designers are paid to produce drawings. Bidders are rarely paid to provide pricing. The rewards of design review go to the design. Compelling Bidders to supply information on deficiencies raises the question of who pays for that service.

(positions §2.2)

> A flood of minor complaints would also hide any major issue. Tenders could be extended to allow every item to be resolved, along with the corrections to the corrections. That would cut into construction schedules, which matters where seasonal weather makes delay costly.

(positions §2.3)

> In short: compelling someone to ask a question is fairly trivial; compelling them to make the question useful is impossible. Since Bidders could ask bad questions easily, by accident or by design, the goals of such a rule, collaborative tenders and few changes after tender, would not be served to the degree expected.

(positions §2.4)

> Shifting responsibility for finding errors to Bidders gives Designers an incentive to produce lower-quality work. To avoid liability they would still comply with standards, but the effort to minimize cost or improve constructability would be left to the Bidders.

(positions §2.5)

*The strongest counter-case, from the bot council of 2026-10-06 (Claude's summary in positions §2.6): vgr_zirp called the five reasons "a guild protection argument dressed up as efficiency reasoning", and argued that a protocol which gives bidders a detector the buyer lacks creates the asymmetry it then refuses to correct, so the honest bidder who asks loses to the strategic one who stays quiet. Reasons 2.4 and 2.5 were not answered. Andre's own reply was a question: assuming the duty were easy to write, how would it be enforced, when bidders would claim their error detection as confidential? Claude's six mechanisms are in positions §2.7; the one that needs no new law is that a bidder who knew, or should have known, of a patent error cannot price it later, and "should have known" moves once a reasonable bidder's bot would have found it. That is chapter 7's question.*

### The tension, not a conflict

> There is no conflict in the duty to report; just a tension and unclarified thinking. The duty to report was rejected as a reliable tool for ensuring that deficiencies in the tender are reported, which would allow resolutions to be included in all bidders' prices and avoid changes during the implementation phase.

> Having bots log their work, and including a mandatory declaration, are systems to discourage non-disclosure.

> This does lead to the conflict the review saw. While the log and the declaration would be effective for bidders acting in good faith, those able and willing to circumvent the rules would win most tenders with their lower prices. This creates a perverse incentive and ultimately returns the system to the current state, with the additional downside of having Buyers believe they are receiving a superior product.

> The two-sided approach of looking at bot-first specifications and standardized bots for baselining the tender may still represent the best distribution of risks based on financial incentives.

(positions §16, recorded 2026-10-10. The banana-peel passages from the same section are in chapter 6.)

### The record, not the duty

> Record keeping would have helped the Army's case: recording what the bot did, and when, and why. Part of the goal is lessening the time needed by a human reviewer, so punting all the reviews to the carbon machine does not help. Perhaps the code for the Buyer-side bot would be public.

(positions §9, recorded 2026-10-07, from the Trax discussion)

*Claude's note: the record here is the one the buyer's own bots keep of their own acts. A log required of bidders was set aside as a topic for discussion, not a goal, by Andre's lean of 2026-10-10 (positions §16). That asymmetry (the buyer's log is public, the bidder's is its own) is the answer to the council's point above that the Listener's editorial choices need someone accountable for them.*

### The Listener

*Andre's meaning, edited wording:*

> Many Bidders are happier to have ambiguity removed from a tender than to find an issue they could exploit, because exploiting it carries the risk of having to make a claim to get paid.

> One limit of the present, human-only process is that Designers and Owners are reluctant to give information or guidance on minor issues. Moving the administrative work of preparing addenda to bots creates an incentive to work toward tenders with fewer unknowns and fewer claims.

> This could tempt Designers to lower quality, since making changes during the tender would become expected. It may be manageable through the service levels negotiated with the Designer. Designers usually work on several projects at once. If low-quality drawings demand excessive effort during one tender at the expense of other projects, that may be enough incentive to provide adequate requirements in the first place.

(positions §3, recorded 2026-10-02; decision 16)

> The Listener's primary role is collating questions from Bidders, whether human or bot. It may communicate the equivalent of a head bow, a shake or a shrug: simple responses that assure the counterparty their request has been heard, with procedural details about next steps.

(positions §6, Andre's meaning, edited wording)

### Who bears the cost of validating intent

> Designers often reduce their liability by including the review and analysis of the public-facing versions of these documents as part of the compiling process. While this does wonders for the Designer's liability and provides more grounds for Owner claims against the successful Bidder, it unfairly, in my opinion, requires the bidder to validate the design despite not receiving compensation unless they win the bid.

> The use of bots would greatly ameliorate this issue by providing low-cost reviews that the specifications meet the intents of the background documents, from the point of view of the potential bidders. The Designers should have already performed this check, so it would be a request to provide comments on how the specifications have accounted for certain items. The Design bots could write up the description and escalate the response for human review and entry into the corpus. The need for liability will require continued use of humans until insurance or legislation provides alternate options.

> The Design and Owner bots could then provide additional commentary, or modify the specs and drawings, in an iterative process until the closing of the questions period, which would lead to bids based on capabilities and capacities instead of the ability to detect errors.

(`case-studies/andre-comeau/README.md`, "Who bears the cost of validating intent". The section's first paragraph, on the two streams of data, is left in the source. Andre's §13 passages on the two routes, bot-readable documents or a standard bot, are in chapter 10.)

### Silence before the contract

> When would this come into effect? During the tender, during contract negotiations after the winner has been selected but the contract has not been signed, after the contract is in place? This rule would definitely apply once the ink has met the paper, but the duty of the bidder to report this beforehand is unclear.

> It would be best practice to bring these issues up before signing the contract, but doing so could jeopardize the bidder's unpaid work during the tender process. Compelling the bidder to reveal information detrimental to their financial interest does not seem like an equitable distribution of risks and rewards. This is a hard problem. Construction management (CM) contracts can often solve them by adding a fourth party to the equation for constructability design. The tension with this approach is variability in skill and motivation.

(positions §20, recorded 2026-10-11)

### The construction manager as a fourth party

> When the CM provides the deeper bench needed for discovering problems earlier in the project, they pay for themselves; when they take a rent-collecting role, then GC is vastly superior. For public sector procurement, the need for open market tenders makes selecting CM vendors based on past performance difficult. Technical rules can be used to remove undesirable vendors, but it would compel the use of untried vendors. Great for discovering new sources of supply and keeping the market competitive; challenging from a relationship-building [standpoint] to create cost savings through trust and cost of training.

(positions §20, recorded 2026-10-11)

### Words that bind

> This legal concept forms a baseline for contractual discussions. Most contracts have "written instructions" requirements to control for changes made through inadvertent comments.

> I don't remember the context when we discussed this for this project, but it feels important since most of the work in creating the tender is preventing claims from inadvertent instructions. Theoretically, estoppel allows a verbal contract to take place anytime, anywhere. By enforcing these micro-contracts, individuals can operate as distributed vendors and buyers, minimizing the cost of centralized supervision.

(positions §20, recorded 2026-10-11)

*The law beside these is `context-bank/legal-assumptions.md`, L14 and L25: words and conduct can displace a written-instructions clause, but by waiver or a pattern of conduct, not by one inadvertent comment.*

### Who benefits when error detection becomes cheap

> I am optimistic about this outcome because, although incumbents would detect the errors more easily and would have more incentive to stay quiet, the usually lower-cost challengers would want to commoditize the bid to align with their competitive advantage. The smaller challengers are often capacity-constrained for administrative tender requests, but AI would provide most of this bureaucratic work.

(`case-studies/andre-comeau/README.md`, "Who benefits when error detection becomes cheap")

*The case study's own caution (perhaps Claude's wording): the deeper moat in construction bidding is usually bonding capacity, surety and prequalification history, none of which AI changes directly. The Seoul group's evidence that AI bidders collude tacitly (`collusion-papers-notes-2026-11-01.md`, Part 3.1) pulls against Andre's optimism; keep them in tension, as the hidden note says.*
