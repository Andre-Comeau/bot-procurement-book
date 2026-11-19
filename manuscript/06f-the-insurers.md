# The insurers: a pilot, then a standard

<!--
Part IV. What each party stands to gain. Chapter 7g, the insurers' pitch.
Split 2026-11-19 from the underwriters' chapter (06e, now chapter 3, "The insurable event"), at Andre's request. Title from the last section heading ("What we need later: a pilot, then a standard"), following Andre's "retitle using the section headings when possible".
The sections below are unchanged from 06e version 4 (2026-11-11). What is whose there: Claude wrote the standards and players sections, the paragraph on which bidders need this and the wording of the ask; they still need Andre's voice pass. The sources list, figure notes and the source check of 2026-11-18 (which cut AIUC's interviews line and rewrote Munich Re's process; both carried over here at the merge of 2026-11-19) stay in 06e's header.
Claude's sentences added on 2026-11-19, to confirm in Andre's voice: the opening paragraph.
Open for Andre: whether this chapter takes the 7a-7e headings (what they need, what they fear, what a standard does for them); whether Appendix E moves into Appendix A with the insurers' one-page pitch.
-->

Chapter 3 asked what an insurer would need to measure before it could cover an estimating bot: a shortfall in margin across many tenders, against costs declared on bid day. This chapter turns to the insurers themselves. Some are already insuring AI, none is insuring construction prices, and the project has one thing to offer them that their own methods have to rebuild for every client.

## The players on the field

Two organizations are already insuring AI, and both are a few years ahead of this project. Neither is working on construction pricing.

AIUC. The Artificial Intelligence Underwriting Company is a venture-funded firm founded in 2025. It wrote AIUC-1, a standard for AI agents with about fifty requirements across six areas: data, security, safety, reliability, accountability and society. Products are audited against it, certified for a year and retested every quarter, and the firm arranges insurance for certified products. Several of its accountability requirements describe the estimate file almost exactly: a named owner for each change, approval before release, and tamper-evident logs of every input and output.

Its strength is speed, which came from building on existing frameworks instead of starting from scratch. Within about seven months it had a standard built on NIST, the EU AI Act and MITRE, an accredited auditor and a first insured customer. Its weaknesses for this project are just as clear. It was written for chatbots and agents, so much of it, such as prompt injection and jailbreaks, does not apply to a weighted median of past prices. It sets no accuracy threshold and runs no statistical test. One company owns the text, the tests and the certificate, and its terms forbid copying or adapting the standard.

So the project should keep going on its own. AIUC-1 was written for a different kind of risk, such as a chatbot giving a wrong or harmful answer. Few AI products price and bid on someone's behalf, so nothing in it measures whether a price is fair. In this project the price is the product, and its accuracy is what drives adoption. That needs a fair point of comparison and an agreed range around it, which AIUC-1 does not have. Joining would mean writing under terms that rule out an open text, which is the main thing this project offers. The better path is a crosswalk that cites AIUC-1's requirement numbers, so a vendor could hold both certificates without doing the work twice.

Munich Re and Armilla. One of the world's largest reinsurers, Munich Re has insured the performance of AI models since about 2018. It assesses the model and how it has performed in the past, and sets the premium by the model's quality and stability. The guarantee is that the model performs to an agreed level, and when it falls short the policy pays the losses that follow. This is close to what insurance for bot procurement could look like. The agreed error would be the margin the bot promised, and the shortfall would be measured across all of the vendor's clients. The provider locks its predictions and checks them against what happens later, which is close to how this project plans to test its own tools on newer contracts. Armilla, a smaller firm in Toronto that writes policies through Lloyd's, works in a similar way. It assesses a model before insuring it and includes an independent certification with every policy. Its main product covers financial loss that an AI causes to third parties. That is a separate space, since most problems in a tender are between two parties, the buyer and the bidder.

Munich Re's strength is that it already pays claims on performance alone, with no need to prove anyone was negligent. Its method works on any kind of model, and its own material says no model can ever be perfect. The weakness of both firms is that each evaluation is custom. The metric is agreed client by client, the method is public only in outline, and two quotes from two insurers may not measure the same thing. Neither firm knows much about tendering law or the gap between a bid and a cost.

So the project is not a competitor to either firm. It does not sell insurance and has no financial interest in doing so. What it can offer is the common point of comparison that their processes have to rebuild for every client. A public way to measure the misses, a public test, and an agreed range for construction pricing would make each evaluation cheaper and each quote comparable, and it would give any insurer, not only one, something to write a policy against.

Many market issues are still open. There is no loss history yet that links a low bid to real losses. Many bidders using the same standard could all fail at once. The bidders keenest to buy coverage may be the riskiest ones, and an open range can be gamed. The market may also be too small for an insurer to build a product alone. The project is not meant to solve these. It exists to show that the conversation is worth having.

Not every bidder needs this. A small company can hold its whole picture in one or two heads: its equipment, its crews, its costs and how much risk it will take. A vanilla AI or a home-built tool already gives it a bid to review, and paying for software and insurance on top would turn profit into overhead. Medium and large companies are different. Their estimating departments have middle managers and span regions, and they bid on the largest jobs, where a losing bid wastes the most effort. For them, insured bot procurement is a way to standardize estimates and raise productivity while keeping risk under control. These are the bidders a pilot should start with.

## What we need now: the ranges an off-the-shelf policy would require

The project would like input from underwriters on the ranges and variance an off-the-shelf insurance policy for estimating bots would require. How far off may a bot's price be, how often, and how steady must that be before an insurer could sell a standard policy rather than a custom one?

## What we need later: a pilot, then a standard

The ask will change as the tools improve, roughly in three steps.

1. Once the reference Estimator and Model are good enough, the next step is a pilot with a real insurance policy. One insurer would write a small, capped policy on the reference tools, used by a few willing bidders on real tenders. The pilot would produce real claims or near misses, and policy terms that have been tested in practice. A lower-stakes start could be pricing change orders after a contract is awarded, where no bid is at risk. A draft term sheet for such a pilot is in [Appendix E](app-e-pilot-term-sheet.md), for an underwriter to mark up.
2. The pilot then feeds the standard. Large-scale adoption needs firmer limits on liability than any single policy can give, and an industry standard is where those limits get written. The policy terms tested in the pilot would become its first requirements.
3. With the standard in place, insurers could cover any product that passes the same public test. Private companies and programmers could then walk through the door, if they find the market attractive enough. They can build much better estimating software than this project, and the reference tools would stay only as the floor everyone is measured against.

The reference tools do not need to be the best. They need to be good enough to run the pilot, build the standard, and build the market.

What would an insurer gain from the pilot? Not a proprietary product. Whatever the pilot teaches would go into an open standard, and that may cool some appetite for the experiment. What the insurer would gain is first-hand experience with the technology and the standard before anyone else, which is a real first-mover advantage. It would also help build a field that bidders are willing to enter, because they could finally put a value on the insurance. A proprietary product would be worth more to one firm, but a field is far more likely to grow into a market, to the benefit of the first mover, with latecomers trying to keep up.
