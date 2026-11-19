# The zombie garden: what AI gets right

Chapter 8 ended on the words and the accidents, the places where the standard bot has work to do. This chapter asks what a bot is good for once it is put to that work.

Chapter 1 left the PDF zombies shambling inside their walled garden. A protocol owes its users two things: safety, the promise that nothing bad will happen, and liveness, the promise that something good eventually will, so that the system keeps growing and changing. The PDF has safety in abundance and no liveness at all. That is what makes it undead, and it is what a bot could bring back into the garden.

The strengths of AI are the other half of the story chapter 8 told. A model that predicts from probabilities is fast and broad, and it is never exactly right. The drunken sailor and the useful bot are the same machine, and what it does well and what it does badly are one property seen from two sides.

![Board-game illustration in dark green moonlight. A walled courtyard is crowded with construction documents drawn as shambling paper zombies with red eyes, each labelled: drawings, specifications, four addenda, an RFI and an RFI response, the bid bond, bid form, unit price form, bill of quantities, instructions to bidders, geotech report, permit, contract, change order, shop drawing, submittal, schedule, Q&A log, site photos, insurance certificate and a revised drawing. In the middle stand two small rooms, the designer's (a figure in glasses with a roll of plans) and the buyer's (a figure in a tie with a briefcase). Bidders in hi-vis vests stand all around the outside of the wall. Hidden in the crowd is one living document, a glowing blue bot-first spec, and in one corner a PDF lies slain under a cross, earning experience points. A side panel reads "Level up! Zombie slain. Choose your treasure" and offers four: Freed Time (hand the take-offs to the bots and spend the hours on creation), Sealed Alternates (propose a better build; the standard bot gives the review certainty), BIM Vision (the model becomes the tender, not a secondary reference) and Robot Command (robots program themselves from the documents you priced).](../images/zombie-garden.png)

The garden may be slow and inefficient, but it moves the information between buyers and bidders in a reliable fashion. The courts have resolved most of the issues, so why go into the courtyard of the undead when there are entire worlds to explore and conquer?

There may be no glory in the work, but it has to be done, and if the bots are going to take it on, they will need strange new rules to do it.

Since wandering among the undead involves risk, this chapter starts with what the bots are good at, and then lays out the treasure, the danger, and the campaign.

## What the bots are good at

A bot does three things well in a tender. It finds averages, it works fast, and it reads.

An estimator prices new work from what similar work has cost before. A person carries a few dozen jobs in their head: the ones they bid, the ones that went wrong, the one from last spring. A model can draw on every past price for similar work in the record, and an average over thousands of prices is steadier than a memory of a few. Chapter 10 puts numbers on how much steadier.

A reading that takes an office days takes a bot minutes, and that changes what a buyer can afford to check. Chapter 1 warned that a flooded buyer ends up reading a sample, and the award becomes a lottery with better prose. A check that runs in minutes can run on every bid and on every change after award, not only on the few that someone had time for.

The third strength is the newest, and it is the one this project is betting on. General assistants can already read a messy bid summary and fill a standard table from it. Decades of old tenders sit in archives as PDFs that a person can read and a machine mostly cannot. A bot that reads them well enough can turn them into the forest floor of chapter 1, the market's record of what the work has cost, with a person checking each file it converts. The same skill does the harder reading too. Where a contract is priced as a few lump sums, pricing a change means finding past work that looks like it and combining those prices, and that is reading, not arithmetic.

None of the three seems to need a specialized tool. The one head-to-head test the project has found comes from legal research, where a general model scored level with the specialists, and chapter 7e drew the lesson that the data was the advantage and the writing was not. If the same holds in construction, a general model with open bid data could price as well as a specialized estimating tool. The record matters more than the bot that reads it, which is why the project wants a public test that any tool can take.

## Why the error never reaches zero

Chapter 3 put the limit plainly. Bringing a pricing bot's error to zero would lose the prediction model that drives its usefulness, because its strength lies in discovering averages and reaching solutions at superhuman speeds. A bot that predicts from probabilities will always leave tails, the few prices it misses badly.

So the useful questions are not whether the bot is right. They are how big its usual miss is, who reads the prices that fall outside it, and who carries the cost when a tail is expensive. The first is a number the project intends to publish for every version of its estimator. The second is a named person. The third is the insurable event of chapter 3, and in the base case the buyer carries it by standing behind its own number.

## What the strengths do not cover

Speed and breadth do not make a reading accountable. A bot cannot sign a memo, and a court will want to know what a person considered and what the tool did. The losing bidder on the US Army contract in chapter 1 could not trace an error to the evaluators' tool, and the court still ordered the tool's output added to the record. The bot can draft, but someone has to answer for the draft.

That is why the project's design will keep a named person on every decision and treat the bot's price as a second opinion. The bot brings the averages, the speed and the reading. The person brings the signature.

## The treasure

The treasure is improved productivity in construction, lowering costs and expanding the options. The greatest part of it is the release of human capital from the cognitive serfdom of documentation and administration: the take-offs counted by hand, the quantities retyped from one document into another, the hunt through three addenda for the one that changed a detail. Freed from it, people can turn to exploration, creation, and community building.

The practical treasure begins with sealed alternates. Standardized documents read by a standard bot would bring certainty to the review of a bidder's alternate, and that certainty would unleash the untapped capacity of the bidders to improve the product, with the benefits shared with the buyers. Then there is the industry's transition to digital tools. BIM modelling has existed for long enough that its absence from the tender and the contract, if not from the design office, should be considered structural, and standards for bots could grow to encompass it as well. Finally, programming construction robots currently requires translating data between formats. The checks on each translation ensure a high degree of accuracy, but better base documentation could remove the translation altogether and accelerate adoption. On a standardized, digital-first stack, a tradesperson could set up and teach a robot for the task at hand from the same documents the bidders priced, the jigbot of chapter 7c, and automated bidding could carry a project from conception to completion.

## The danger

The danger is anachronistic technology crushing innovation, as maintaining the system becomes a rent-seeking enterprise. The impulse to innovate becomes buried under the desire to slow the velocity and raise the margins. Meanwhile, the waste goes on in plain sight. Every bidder reads the same drawings, takes off the same quantities and prices the same work, and on a job with six bidders, five of them do it for nothing. Their effort does not vanish: it comes back as overhead in the next bid, and the buyers pay for it in the end.

## The campaign

The operational plan? To prepare an expedition to the heart of the procurement process, the documentation of requirements, to slay the PDF zombies and free the villagers from their evil reign.

As bad as the zombies may be, they are providing an essential service. All the villagers have structured their lives around their existence, so their death would also collapse the system.

To kill the PDF, we will need a revised documentation system, built bot-first: specifications that cannot be misread by machines, and that adjust to the display, whether a phone, a computer or a robot's instructions. That specification would be the first living document in the garden. The technology already exists, but reasonable fears of liability will keep designers from adopting it unless standards can be used to determine the appropriate techniques and standards of care. Under that fear sits the question this book keeps returning to: when a bot causes harm, who is liable?

Once dead, the PDF will need to stay dead, and the documentation standards only start the process. A standard bot will be needed to validate the documentation for AI consumption, so that designers can verify that AI is correctly interpreting their documents. When the designers sign off on its outputs, a baseline is established, and custom bots can be supplied to the market to meet the bidding strategies of the different bidders.

The advent of AI creates both the demand and the means for these tools, and the machine itself is the easy part. Throw enough magic tokens at the problem, and a suitable program will be conjured into existence. There is work to do, but it takes place at the workbench.

The real challenge will come from the community building. Adventurers have passed through the village before: tech entrepreneurs who ride in to disrupt the system, slay a monster, carry off whatever treasure they can find and ride on. A garden cleared that way soon fills up again. What lasts is the work of the villagers, the stakeholders in construction procurement: buyers, consultants, bidders, the legal system, politicians, researchers, and the standards agency. The standards are the strange new rules, and only the villagers can approve them. The campaign ends with them moving into the town square they build together over the old zombie garden.

The settlement of the new domain will de-wild the current graveyard. It will also create new spaces for thickets to form, places where wildness flows from human imagination, bringing new liveness into the world.

The first tool for that campaign is being built at the workbench now. Chapter 10 follows what it will do, from the tender to the change order.
