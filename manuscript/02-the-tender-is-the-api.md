# The tender is the API

<!--
Part I. The question
Target: 1,000 words, redraft
Brief: Design, tender, compilation; the Amazon API mandate applied to a design consultant and a builder; limited test scaffolding and bug-free drawings as a mythical beast.
Sources: the case study's "Procurement redescribed as software development" and "A note on PDFs"; position 14 (the model is the specification).
Literature (`literature-review-2026-11-01.md`, Part 1): Yegge's platform rant (the source for the Amazon mandate); Pahlka 2023; Alon Levy (IFP 2026) on publishing unit costs; AECV-Bench and DrawingVQA; OCDS, eForms, IFC; the UK Construction Playbook.
Paths are relative to construction-procurement-protocols unless they start with C:\.
-->

## Source passages (to cut and rewrite)

*Laid out by Claude on 2026-11-02. Every quoted passage is Andre's, copied unchanged from the file named under it; the source repository records these as his words, lightly edited from conversation. Notes in italics are Claude's. Delete this section as the chapter is written. The one-shotted design and the long compile are quoted in chapter 1; use them here or there, not both.*

### Design, tender, compilation

> Perhaps the procurement process for construction should be redescribed in terms of software development. There are three main components:
>
> 1. Design
> 2. Tender, which is the API
> 3. Compilation, which is construction itself
>
> The Design and the Compilation negotiate through the API of the Tender process. The builder agrees to provide all the resources needed to compile the Design during an auction-styled event. Readers of the SIG's adoption guide will recognize the 2002 API Mandate at Amazon, applied to an industry where the teams are a design consultant and a construction firm and the API contract is a tender package.

(`case-studies/andre-comeau/README.md`, "Procurement redescribed as software development")

*The literature review's note: the source for the mandate is Steve Yegge's platform rant, not an Amazon document; cite it that way.*

### Limited test scaffolding

> **Limited test scaffolding.** BIM modelling, AI review and licensed professionals help screen for errors, but bug-free drawings are still a mythical beast.

(`case-studies/andre-comeau/README.md`, "Procurement redescribed as software development")

### A note on PDFs

> Bot-based procurement assumes that PDFs will be phased out. They are an archaic artifact from the world of paper. The file sizes are enormous and they are not reliably read by machines. They also lack well-formatted metadata for rapid search and bot instruction. They also display poorly on a screen, especially on the cell phones used by frontline workers.

(`case-studies/andre-comeau/README.md`, "A note on PDFs")

*The prologue already makes this point in one aside ("no one really liked looking at paper sheets on a screen anyhow"); the chapter can carry the full argument and the prologue keep the joke.*

### The model is the specification

> Sufficiently complex building models equal specifications. A BIM model with all the product information encoded in the code used to generate the model would be a potential source for bot procurement. We have been focusing on the raw documentation (.md, .json) that would be used to build the rendering of the model. In bot procurement, the model would render for humans, but the bots would probably prefer the files.

(positions §14, recorded 2026-10-09)

> Generating a building model should be considered as part of public-sector tenders. A model would be far more machine-readable than the current 2D drawings. The challenges are significantly higher costs and a higher risk to the designer: paper can be reviewed by eye far more easily than the code used to generate a high-rise.

> An industry-wide, full-depth adoption of BIM would be a massive gain for bot-based procurement and for AI-guided implementation. The technology already exists. I am assuming there are no design-side efficiencies, because the architects and engineers have to verify even more data than before, and there is likely a shortage of licensed professionals who are both capable of and willing to do this tedious work. It is much simpler to review a technologist's output when it is on paper.

(`context-bank/background-notes.md`, "Priority topic", recorded 2026-10-01)

*Claude's note from positions §14: the question becomes "which file is authoritative when a model, its generating code and the drawings disagree". Singapore's answer so far is the IFC model submitted to the regulator; no standard was found for exchanging the generating code as the contract document. Standard contracts still treat the drawing, not the model, as what binds. The machinery figure's line for BIM says the same: "The 3D model is richer; the drawings bind."*

### Decomposing the project

> Decomposing a project into requirements for one bid may be the equivalent of using PDFs in the age of scrolling.

(positions §15, recorded 2026-10-09; the rest of the passage, on one trade first, is in chapter 11)

### The question the chapter leaves open

*The case study lists it among its open questions (the wording may be Claude's, since Claude wrote the case study's connecting passages): "Whether redescribing procurement as software development holds up as more than a useful metaphor is the deepest open question, and the one this write-up tests the least." Worth one honest paragraph at the chapter's end.*
