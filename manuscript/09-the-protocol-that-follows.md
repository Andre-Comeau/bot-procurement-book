# The protocol that follows

The last chapter ended at a door, and behind it was the standard, World 2 on the map. For most of this project, the plan for getting through that door was a kind of mumble. Build a model that is good enough, publish it, and the field would gather around it on its own: the owners would adopt it, the courts would find it, and one day a standards body would write down what it already did. The estimator would be the seed and the rest would grow.

That is not how standards get made, and the people who have made them say so plainly.

## Standards make the world

David Lang came to standards the way many builders do, by needing one. He co-founded OpenROV, a cheap, open-source underwater robot, in 2011, and watched its team turn from prototype builders into protocol designers once they found that the bottleneck in ocean technology was the connector, not the robot. His essay for the Protocol Institute's Summer of Protocols, "Standards Make the World", is the history of standards-making he went looking for along the way.

It is easy to remember the title as *Standards Rule the World*, and the difference between the two verbs is the whole of this chapter. A standard that rules is handed down from somewhere. A standard that makes the world had to be made first, by somebody. Lang's answer to who that somebody is: standards "are made and remade by (usually small) groups of people", and "standards-making is something that anyone can engage in, even though almost no one thinks to do it."

He describes two paths. The first is the formal one, with numbered steps. In Canada it runs through the Standards Council: a proposal goes to ISO, experts draft the text, national bodies and the public comment, the experts revise, the members vote, and the standard is published and reviewed in turn. The second is the path the Internet took, summed up in David Clark's line about the IETF, "rough consensus and running code". Build something that works, get people using it, and give it formal governance afterwards. MIDI, USB and the CubeSat each began with a small group saying, in Lang's words, "we're doing this—are you coming?" Nearly all of them ended up in a consortium or a standards body. The disruptive path does not skip the committee. It arrives at the committee with something already running.

Construction procurement has walked both paths before. In 2005 Ron Watermeyer made the case for an international procurement standard built on South Africa's national ones, which already worked; ISO 10845 followed in 2010, and he chaired the ISO subcommittee set up in 2015 to maintain it. The Open Contracting Data Standard went the other way round: a small team, backed by the World Bank and the Omidyar Network, wrote a data format for publishing public contracts, released version 1.0 in 2015, and let governments pick it up one at a time. Ukraine's ProZorro publishes in it, and an infrastructure version, OC4IDS, followed in 2019. Neither standard computes anything. ISO 10845 fixes the procedure and OCDS fixes the record, and both stop at the edge of the question this book asks.

## What the standard is for

Lang's first question for anyone starting a standard is what it is for. The historians he draws on sort standards by purpose: safety, like the rules for steam boilers; interoperability, like screw threads; and performance, like the grades of steel rail. He adds a fourth kind, the contractual standard, a form that everyone agrees to sign so that nobody has to negotiate it again.

The book's answer comes from its central question. When a bot causes harm, someone has to decide what a reasonable bot would have read in the tender, and the standard is there to say which reading binds. Better models will not remove that need, because a better reader is still only one reader. The law already asks what a reasonable bidder would have understood; the standard gives that question an answer that anyone can rerun. Seen this way, the standard bot is a legal instrument before it is a technical one. Nobody is asked to trust the bot; they are given a reasonable reader they can cite in court. That also moves the project out of the innovation bucket, where public buyers are wary, and into the standards bucket, where they already know how to take part.

So the standard is two kinds at once. The bot-first documents are an interoperability standard, the screw thread that lets any bot read any tender. The standard bot is a performance standard with a contractual purpose: a public, versioned test set, a tolerance, and a required record, which any bot can be measured against. The standard specifies the test, not the model. The author's estimator is only the first bot that passes it, which is why the standard can be free while the bots that conform to it compete. And once the base bid can be checked by anyone, the base price becomes a commodity, and the competition on ideas moves to the paid alternates, as chapter 9 argues.

## Starting and sticking

Lang borrows his best line on failure from Carl Cargill, a veteran of technology standards work: most standards efforts do not fail in the committee. They fail before it, when nobody launches them or no sponsor turns up, or after it, when the finished standard finds no one who wants it. In Lang's words, "the danger zone for standards is sometimes in the starting but always in the sticking."

The mumble was about sticking. It assumed that a good model would stick because it was good, which is the one thing Cargill's history says is not enough.

Sticking is also a waiting game, in which everyone waits for someone else to move first. The courts will not lean on a standard that does not exist yet, a standards body will not write one without a pilot, and a buyer will not fund a pilot without a return it can count. Each of them is being reasonable, and together they keep the door shut. The way out is a benefit that one of them can capture now, before any standard exists, and that is the evaluator's job.

Starting needs fewer people than it seems to. Lang's advice is to "start with a small group of true believers and gradually work outwards", and the disruptive path does not ask for everyone's agreement up front, only for enough people to get something working.

Sticking needs patience. The CubeSat, the ten-centimetre satellite that now flies by the hundred, took about ten years to take off after its standard was written, and one of its inventors, Jordi Puig-Suari, gave the reason: "People needed to gain some comfort that these standards are going to be around for a while." For a liability standard, that comfort is the whole product. A court can rely on a reading only if the standard existed before the tender went out and still exists, unchanged, when the claim arrives years later. The ten to fifteen years this book has assumed before the standard takes effect is not a delay to apologize for; it is about what the CubeSat took.

## The field-building level

At the Protocol Institute's 2026 Symposium, Lang opened with a talk on field building, the work of turning an idea into a field: something with its own people, money, institutions and arguments. His point, for this book, is that fields do not generate themselves. Someone builds them, often an outsider, and in an earlier essay he calls those people "fire starters". The talk works almost as a checklist for the level that sits in front of World 2's castle.

**Name enthusiastically, define hesitantly.** "Bot procurement" is a name, and it can be used loudly. "The reasonable bot" should stay loosely defined for longer than feels comfortable, because a strict definition in the first year ends conversations and pushes people out. The test set can grow into the definition.

**Make momentum.** Lang's list is small grants, workshops, meetups, and vision papers or artifacts. The estimator is an artifact. So is this book.

**Recruit keystone individuals.** A field gains energy when established people from neighbouring fields join it. Here that means someone who has sat on a standards committee, a construction lawyer who has argued over a reading, and a public owner willing to run a pilot. Inside the owner, the first ally is probably not an executive but whoever has to defend a change-order price in a dispute: that person knows the pain best, and needs no standard to find a reproducible number useful.

**Watch the signals.** A field is mature when it has an industry, an institution, or both. The signals to watch are on the bot-first card: a public owner publishing a tender as data, a dispute over an agency's AI, a Canadian mirror committee for construction procurement.

**Beware capture.** Once a field is worth something, a larger player can take it over and slow it down, or make it, as Lang puts it, "uninteresting". In bot procurement the likely captor is a platform vendor whose own format becomes the de facto standard. That is the strongest reason to keep the standard free and the estimator only its first conforming bot. A free test behind a paid gate would be capture from the inside.

**Find the economic flywheel.** Lang's warning example is area studies, which had money while the Cold War gave it a reason and closed when the reason went, because it "didn't have its own self-sustaining economic flywheel". This is where the mumble was most wrong, and where chapter 9 already holds the answer. The evaluator's savings, the claims never started and the reviews never paid for, are the flywheel the field needs. They pay for the next version whether or not anyone funds a standard.

## A stadium with one player

Nadia Eghbal's *Working in Public* is about open-source software, but it describes the shape this project is about to take. She sorts projects by two things: how fast their users grow and how fast their contributors grow. Toys have few of either. Clubs have contributors but few outside users. Federations, rare and large, grow both. Stadiums grow users quickly and contributors hardly at all: a few people on the field and a crowd in the stands.

The estimator today is a toy. If the book's plan works, it becomes a stadium: owners, consultants and bidders using a reference bot that one person maintains. Eghbal's lesson is that code is cheap to copy and the maintainer's attention is not, and that the lasting cost of software is the upkeep, not the first build. For a liability standard the stadium is the dangerous stage, because the comfort the CubeSat needed depends on someone still being on the field in ten years. The author has already said where that leaves versioning: new versions need funding, and the pace of revisions will follow the value the market places on the standard.

The stadium also has its worst spectators. The bidder who spends compute searching a frozen standard bot for exploits takes the maintainer's work and gives nothing back; Eghbal would call that an extractive use of the commons. A bounty for each exploit reported turns some of those spectators into players, and since one patch protects every tender read against that version, the bounty can be paid for across all of them.

The way out of the stadium is the path Lang describes, the move into a consortium or a standards body, where the people who rely on the standard share the cost of keeping it. Owners can help before that day comes. Kelly Roegies's guide to open protocols for governments suggests procurement criteria that reward suppliers who contribute upstream, and a public owner who buys bots can ask, in its own tenders, which bidders help maintain the test.

## The nearest standards

The cliff after the tool was a missing list of asks. Here is one, drawn as World 2. Every level on the map is a standard that already exists, kept by people who already meet, and each needs one change rather than a new institution. The castle is the only new thing.

![World 2, the Standard: an overworld map from World 1 through eight levels, each an existing standard with the change it would need (field building; OCDS and OC4IDS; IFC 4.3 and IDS; methods of measurement; CCDC 23; ISO 10845-3; AACE's estimate classes; IEEE 3119), to a castle, a new part of ISO 10845 for the reasonable bot, and past it a courthouse for the first case](../images/world-2-standards.png)

**The documents.** The Open Contracting Data Standard lets anyone write an extension: there is a template, and the Open Contracting Partnership keeps a registry. So the first ask needs nobody's permission, only work. An extension would record, for each tender, the questions asked, the addenda issued, and which version of the reference bot read it. On the design side, IFC 4.3 already covers roads, rail and bridges, and buildingSMART's Information Delivery Specification, final since June 2024, lets a designer state requirements that a program can check. The ask there is a use case for the items a bidder prices, so the requirements are checked before the bid instead of argued about after it. The method of measurement, whether a civil engineering method like CESMM4 or a state transportation department's list of pay items, needs one name for each item, so that a price from one tender can be compared with a price from the next. The test set needs a published crosswalk, not a new method.

**The tender rules.** In Canada, CCDC 23 is the guide to calling bids and awarding contracts, written by a committee of industry associations. A guide note could ask every tender to name the version of the reference bot it was read against, the way a contract names the edition of the building code. ISO 10845-3, the standard conditions of tender, could add the Listener's rule: a question raised by any bidder's bot is answered to every bidder, by addendum.

**The bot.** AACE's estimate classes measure how accurate an estimate can be expected to be, given how far the design has come. The ask is a conformance class beside them: agreement with a reference estimate under a fixed protocol, which is where the book's two to three percent belongs, since it measures something different from distance to the low bid. AACE's recommended practices are drafted by members and put out for public review. IEEE 3119, published in 2025, walks a buyer through procuring an AI system, from defining the problem to monitoring the contract. A construction profile would let a buyer require that any estimating bot it buys passes the public test.

**The castle.** The conformance test itself, a public test set, a tolerance and a required record, is the one thing that does not exist. Its natural home is a new part of ISO 10845, whose subcommittee already has a working group for maintaining the series. The way in is through a national standards body, and whether Canada sits on that subcommittee is the first thing to find out. If it does not, a Canadian mirror committee would itself be one of the signals the field is waiting for.

**The courthouse.** Past the castle is not a standard but a court. The tests for expert evidence, Daubert in the United States and Mohan in Canada, ask for a method that can be tested and a known error rate. The proposed federal rule on machine-generated evidence was withdrawn in May 2026 and is being redrafted. The castle is built so that, when the first case arrives, both answers are already on the shelf.

The levels are in the order they can be started. The first two need nobody's permission, the middle ones need a membership and a committee, and the castle needs a national body and years. That order is the pitch: each level gives the next one something already running.

## The campaign for World 2

Put together, the versions in chapter 9 line up with the standards path.

**Version 1.0, momentum.** One trade first, probably civil work, where public bid prices already exist. A public, versioned test set and a published tolerance, on an offline model whose weights do not change. The name in use, the definition kept open, and a small group of true believers. The OCDS extension and the IDS use case, which need nobody's permission. This book is the vision paper.

**Version 2.0, proof of work.** The evaluator in an owner's hands, saving money the owner can count. That saving is the economic flywheel, and the first owners to use it are the keystone individuals the field needs. Workshops follow, where the people who will one day sit on the committee first argue about the test, and the asks that need a committee go in: the AACE practice, the CCDC guide note, the IEEE profile.

**Version 3.0, the working model.** The standard is written backwards from what the test has to catch, not from the estimator's internals, so that a second vendor's bot can pass it too. It then goes looking for its formal home: a consortium, or a national committee proposing a computable extension of ISO 10845, which already fixes the procedure and stops short of the price.

The prediction can be wrong, and it should say how. If by 2035 no public owner anywhere runs a tender whose questions, addenda, bids and evaluation pass through agents on a published data format, the forecast failed. The standard itself is further out, in the ten to fifteen years the CubeSat suggests, and its first court challenge will probably come before it, from a dispute fought under the old rules.

The model was never going to generate the field. The most it can do is give a small group of people something that runs, and something to argue about. That is how a standard starts, and the villagers, as the introduction promised, are the ones who decide whether it sticks.

---
