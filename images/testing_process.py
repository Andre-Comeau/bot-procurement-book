"""Chapter 1 figure: how the estimator is checked, drawn as a level inside the Estimator's hut.

Same overworld-map style as chapter 1's Bot Procurement World (second_opinion.py) and
chapter 11's World 2 (world_2_standards.py), whose drawing helpers it reuses.
The road runs from older contracts to newer ones: level 1 (learn, Texas contracts let
before May 2026), level 2 (rehearse, Texas contracts let from May 2026) and, behind a locked
gate, the castle (the final test, on newer bid results piling up online). A side road
loops back from the rehearsal: improve the estimator, then rehearse again.
The researchers' terms (training, validation, test data) are given on each sign.
All wording on the map is Claude's draft for Andre.

    python images/testing_process.py images/testing-process
    node images/project_hex_map_render.js "$PWD/images/testing-process.html" images/testing-process.png 1800 1010
"""
import pathlib, random, sys

# Reuse chapter 1's drawing helpers (everything before its drawing code).
_src = (pathlib.Path(__file__).parent / "second_opinion.py").read_text().split("\no = [")[0]
exec(_src)
W, H = 1800, 1010
random.seed(11)

GOLD, SOFT = "#ffd27a", "#d9d6cf"


def sign(x, bottom, rows, w):
    """A dark sign centred on x whose lower edge sits at `bottom`; rows are (text, class, fill)."""
    h = 20 + 26 * len(rows)
    y = bottom - h
    p = [f'<rect x="{x-w/2}" y="{y}" width="{w}" height="{h}" rx="8" fill="{LEAD}" opacity=".88"/>']
    for i, (s, cls, fill) in enumerate(rows):
        p.append(t(x, y + 31 + 26 * i, s, cls, fill))
    return p


def namebox(x, y, name, cls="pxxs", k=11.2):
    bw = len(name) * k + 28
    return [f'<rect x="{x-bw/2}" y="{y}" width="{bw}" height="30" rx="6" fill="#ffffff" stroke="{LEAD}" stroke-width="3"/>',
            t(x, y + 21, name, cls, LEAD)]


def locked_gate(x, y):
    """A wooden gate across the road, with a padlock."""
    wood = "#b98b54"
    p = [f'<rect x="{x-16}" y="{y-52}" width="32" height="104" rx="4" fill="{wood}" stroke="{LEAD}" stroke-width="5"/>']
    for k in range(1, 4):
        p.append(f'<line x1="{x-16}" y1="{y-52+k*26}" x2="{x+16}" y2="{y-52+k*26}" stroke="{LEAD}" stroke-width="3"/>')
    p.append(f'<path d="M{x-9} {y-6} L{x-9} {y-16} Q{x-9} {y-30} {x} {y-30} Q{x+9} {y-30} {x+9} {y-16} L{x+9} {y-6}" fill="none" stroke="{LEAD}" stroke-width="6"/>')
    p.append(f'<rect x="{x-15}" y="{y-8}" width="30" height="26" rx="4" fill="{GOLD}" stroke="{LEAD}" stroke-width="4"/>')
    p.append(f'<circle cx="{x}" cy="{y+4}" r="4" fill="{LEAD}"/><rect x="{x-2}" y="{y+4}" width="4" height="9" fill="{LEAD}"/>')
    return p


o = [f'<rect width="{W}" height="{H}" fill="{LEAD}"/>']
o.append(t(70, 76, "HOW THE ESTIMATOR IS CHECKED", "pxt", "#ffffff", "start"))
o.append(t(70, 116, "Chapter 1 · Inside the Estimator's hut, on the map of the change process", "dek", SOFT, "start"))
o.append(t(1730, 76, "WORLD 1", "pxt2", C["acc"], "end"))

X0, Y0, X1, Y1 = 40, 150, 1760, 900
o += glass(X0, Y0, X1, Y1, C["sec_d"], spread=(.08, .16, .24))
for hx, hy, s in ((100, 330, .8), (1725, 620, .7), (120, 800, .7), (1010, 820, .6), (1350, 800, .7)):
    o += hill(hx, hy, s)

R = 560                                  # the road
L1, L2, GX, CX = 400, 900, 1190, 1480    # level 1, level 2, the locked gate, the castle
LOOP_OUT, LOOP_IN, LOOP_Y = 1090, 270, R + 190

road([(135, R), (CX - 80, R)])
road([(LOOP_OUT, R), (LOOP_OUT, LOOP_Y), (LOOP_IN, LOOP_Y), (LOOP_IN, R)], w=14)
o += draw_roads(ROADS); ROADS.clear()

# the way back: an arrow where the loop rejoins the road, and a sign on the loop
o.append(f'<path d="M{LOOP_IN} {R+34} L{LOOP_IN-20} {R+72} L{LOOP_IN+20} {R+72} Z" fill="{C["acc"]}" stroke="{LEAD}" stroke-width="4" stroke-linejoin="round"/>')
o += sign((LOOP_IN + LOOP_OUT) / 2, LOOP_Y + 23, [("improve the estimator, then rehearse again", "lab", "#ffffff")], 470)

# the start
o.append(f'<rect x="60" y="{R-34}" width="150" height="68" rx="34" fill="{C["acc"]}" stroke="{LEAD}" stroke-width="5"/>')
o.append(t(135, R + 7, "START", "pxs", "#ffffff"))

# level 1: learn
o += sign(L1, R - 64, [("Texas contracts let before May 2026", "lab", "#ffffff"),
                       ("The estimator learns its prices from", "labi", SOFT),
                       ("what bidders actually charged.", "labi", SOFT),
                       ("Researchers call this training data", "labi", GOLD)], 430)
o += level(L1, R, "1", C["action"])
o += namebox(L1, R + 54, "LEARN")

# level 2: rehearse
o += sign(L2, R - 64, [("Texas contracts let from May 2026", "lab", "#ffffff"),
                       ("Each version is checked on them,", "labi", SOFT),
                       ("improved, then checked again.", "labi", SOFT),
                       ("Three so far: v0.1, v0.2 and v0.3.", "labi", SOFT),
                       ("Researchers call this validation data", "labi", GOLD)], 450)
o += level(L2, R, "2", C["sec"])
o += namebox(L2, R + 54, "REHEARSE")

# the locked gate: not run yet
o += locked_gate(GX, R)
o.append(f'<rect x="{GX-75}" y="{R+66}" width="150" height="30" rx="6" fill="{C["acc_d"]}" stroke="{LEAD}" stroke-width="3"/>')
o.append(t(GX, R + 87, "NOT RUN YET", "pxxs", "#ffffff"))

# the castle: the final test
CY = R + 30
o += sign(CX, CY - 187 - 18, [("Newer bid results, piling up online", "lab", "#ffffff"),
                              ("Left alone until there is a product", "labi", SOFT),
                              ("and someone who wants the answer.", "labi", SOFT),
                              ("The error bands we quote come only from here.", "labi", SOFT),
                              ("Researchers call this test data", "labi", GOLD)], 470)
o += castle(CX, CY, .75, mix(LEAD, "#ffffff", .18), C["acc"])
o += namebox(CX, CY + 14, "FINAL TEST", "pxs", 15.5)

# the time axis
AY = R + 305
o.append(f'<line x1="120" y1="{AY}" x2="1640" y2="{AY}" stroke="{LEAD}" stroke-width="14" stroke-linecap="round"/>')
o.append(f'<line x1="120" y1="{AY}" x2="1640" y2="{AY}" stroke="#f3e6c8" stroke-width="6" stroke-linecap="round"/>')
o.append(f'<path d="M1630 {AY-20} L1676 {AY} L1630 {AY+20} Z" fill="#f3e6c8" stroke="{LEAD}" stroke-width="5" stroke-linejoin="round"/>')
o.append(t(120, AY - 24, "OLDER CONTRACTS", "pxxs", "#ffffff", "start"))
o.append(t(1676, AY - 24, "NEWER CONTRACTS", "pxxs", "#ffffff", "end"))

o.append(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="none" stroke="#ffffff" stroke-width="6"/>')
o.append(t(70, 962, "The rehearsal marks flatter us a little. The castle is where the numbers we quote come from.", "foot", "#ffffff", "start"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .pxt{{font-family:'Press Start 2P',monospace;font-size:34px;letter-spacing:.04em}}
  .pxt2{{font-family:'Press Start 2P',monospace;font-size:26px}}
  .px{{font-family:'Press Start 2P',monospace;font-size:20px}}
  .pxs{{font-family:'Press Start 2P',monospace;font-size:15px}}
  .pxxs{{font-family:'Press Start 2P',monospace;font-size:11px}}
  .dek{{font-family:Lora,Georgia,serif;font-style:italic;font-size:21px}}
  .lab{{font-family:Lora,Georgia,serif;font-weight:500;font-size:20px}}
  .labi{{font-family:Lora,Georgia,serif;font-style:italic;font-size:18px}}
  .foot{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:28px}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "testing-process"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#2c2c2a}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
