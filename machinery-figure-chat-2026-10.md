# The machinery figure: what the chat of 18 to 30 October 2026 did

A description of one chat's work, written on 2026-10-30 as the chat closed, for the book. The chat drew
the figure on the pitch page of the public repository (`construction-procurement-protocols`, folder
`pitch\`) that shows the project's machines and what each makes for the next. The figure is a candidate
illustration for Part II and for Appendix A; the one-line descriptions under the machines are candidate
captions.

- **Whose words:** Andre's directions are quoted; everything else here is Claude's.
- **Where the work is:** the source is the `machinery` block of `pitch\pitch.yaml`, the drawing is
  `machinery_html` in `pitch\build_pitch.py`, and the page is `pitch\index.html`, rebuilt by the script.
  The hand-over note for whoever takes the figure up next is the last section of `pitch\OPEN.md`. The
  discarded layouts are in `pitch\drafts-2026-10\`, with a README. The council material is in
  `bot-council\briefs\thicket-descriptions.md` and `bot-council\transcripts\` (19 and 20 October).

## 1. What the figure shows

Seven machines, each a clump in a thicket, grown from a common soil of standards, contracts and AI:

- what exists today: the procurement system, BIM, robotic construction;
- what this project built: the estimator;
- what it proposes: bot procurement;
- what others' funded research holds: bot monitoring (cameras and drones checking the built work against
  the model);
- others' machines whose output this project's work improves: BIM for bots, robots from the model.

Each product is a vine from the machine that makes it to the machine that takes it, named along the stem:
bid tabulations, pricing, an evaluator for changes, a testing scaffold, a bot prototype, bot-first
documentation, reference bots, the model, departures, robot standards. What goes back into the
procurement system comes in as dashed vines, marked as Claude's reading. Each machine grows its built work
on its rim, in Andre's scheme: grass on the procurement system, mushrooms on the estimator with threads
under it, ferns on bot procurement, flowers on BIM for bots, a shrub on bot monitoring, a tree on robots
from the model. Two soft grounds mark ours (procurement) and theirs (funded research in BIM, monitoring
and robots). A key names every mark.

## 2. The line under each machine

Each clump carries one plain line, the tension the machine manages. They are Claude's, drawn from the case
study's headings, the positions file and the Machine Cards, then put to the Bot Council (local models and
the outside bots that answered) and, by hand, to the Protocol Institute's PIBot in three turns, and taken
with their corrections. No source states them; they are the project's own claims.

| Machine | Line |
|---|---|
| The procurement system | The lowest bid wins, mistakes and all. |
| BIM | The 3D model is richer; the drawings bind. |
| Robotic construction | The plan is tidy; the site isn't. |
| The estimator | The owner's estimate against what bidders charge. |
| Bot procurement | Who pays to find the drawings' errors? |
| BIM for bots | People certify the model; bidding software reads it. |
| Bot monitoring | Is it built as modelled? Cameras check. |
| Robots from the model | If a robot builds the error, who answers? |

PIBot's caution is worth keeping for the book: the risk in these lines is not Institute jargon but
ambiguous nouns ("model", "machines", "our"). The page's third question stands over the figure: when
errors get cheap to find, who gains?

## 3. How it was arrived at

In order, each at Andre's word:

1. A column of tiles with the common ingredients in a band: legible but "hard to read" with many colours.
2. Sketches after the World Machines site and the Prime Radiant (life bars, a horizontal timeline), kept in
   the Institute's page style.
3. A tech tree, "something that looks more like a tech tree in a video game. More graphics and less
   linear. BIM and Robots are already independent machines. What our project will be doing will improve
   their outputs." Committed on 19 October.
4. The thicket: "Since the PI is working to bring about New Nature, perhaps we could rearrange the machines
   into a Thicket?" After Aneesh Sathe's image, with the look borrowed and not the claim, since a thicket
   in his sense declines to be legible and this figure names what every machine makes. Rounds on line
   weights by kind, bigger fonts, fewer crossings, upright names.
5. Bot monitoring added as a research clump, with the two grounds as "visual clues that our project is
   focusing on procurement". The robot icon given a smile.
6. The sprouts in place of a canopy of built work: "A simple grass for the current procurement system. Some
   mushrooms for the estimator, this step does not directly affect implementation so mycelium would
   contrast with the rest. Ferns for Bot Procurement. Flowering plants for BIM for Bots. Shrubs for Bot
   Monitoring. Trees for Robot Construction." Then the shrub and the tree enlarged.

Every name's place on its vine was found by measurement in the app's browser pane, not by eye: a script
read each label's glyph boxes against every vine, clump and other label, and a search walked each vine for
a spot touching nothing. The final page measures clean. Two local models read the page after each build
as a reader with no prior knowledge and answered thirteen questions; the final page scored 12 of 12 on
both.

## 4. What is open

- Andre's idea for after: "There may be a need to transform this into more of a ecosystems map with the
  links acting as rivers." Not started.
- The names and lines of the two improved machines and of bot monitoring are Claude's and wait on his
  words (`pitch\OPEN.md`).
- The council transcripts hold the bots' answers as received; whether their quoted passages are cut to
  titles before anything is shared is Andre's to rule.

## 5. For the book

The figure can be redrawn from its source at any size; the generator is plain Python writing SVG, with no
dependency beyond the YAML reader. For print, the vines' names would need to be checked again at the
print scale, by the same measurement. The eight lines above are the shortest statement the project has of
its tensions and could open the chapters that treat each machine.
