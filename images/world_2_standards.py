"""Chapter 11 figure: World 2, the Standard, an overworld map of the nearest existing standards.

Each level is a standard that already exists, with the change the book would ask of it.
The road runs from World 1 through field building, the documents (OCDS, IFC and IDS, the
method of measurement), the tender rules (CCDC 23, ISO 10845-3) and the bot itself (AACE's
estimate classes, IEEE 3119) to the castle, a new part of ISO 10845 for the reasonable bot.
Past the castle is the courthouse, where the first case will test it.
The drawing helpers come from second_opinion.py (chapter 1's Bot Procurement World), so
the two worlds share one style. All proposals on the map are Claude's draft for Andre.

    python images/world_2_standards.py images/world-2-standards
    node images/project_hex_map_render.js "$PWD/images/world-2-standards.html" images/world-2-standards.png 1800 1160
"""
import pathlib, random, sys

# Reuse chapter 9's drawing helpers (everything before its drawing code).
_src = (pathlib.Path(__file__).parent / "second_opinion.py").read_text().split("\no = [")[0]
exec(_src)
random.seed(11)


def note(x, y, lines, w=284):
    """A dark sign above a level: the change the book would ask for."""
    p = [f'<rect x="{x-w/2}" y="{y}" width="{w}" height="{16 + 26*len(lines)}" rx="8" fill="{LEAD}" opacity=".86"/>']
    for i, s in enumerate(lines):
        p.append(t(x, y + 30 + 26*i, s, "labs2", "#ffffff"))
    return p


def courthouse(x, y, s=1.0):
    body = mix(C["ink2"], "#ffffff", .55)
    p = [f'<rect x="{x-110*s}" y="{y-14*s}" width="{220*s}" height="{14*s}" fill="{body}" stroke="{LEAD}" stroke-width="4"/>',
         f'<rect x="{x-96*s}" y="{y-26*s}" width="{192*s}" height="{12*s}" fill="{body}" stroke="{LEAD}" stroke-width="4"/>']
    for k in range(5):
        cx = x - 76*s + k*38*s
        p.append(f'<rect x="{cx-9*s}" y="{y-120*s}" width="{18*s}" height="{94*s}" fill="#ffffff" stroke="{LEAD}" stroke-width="4"/>')
    p.append(f'<rect x="{x-100*s}" y="{y-136*s}" width="{200*s}" height="{16*s}" fill="{body}" stroke="{LEAD}" stroke-width="4"/>')
    p.append(f'<path d="M{x-108*s} {y-136*s} L{x} {y-190*s} L{x+108*s} {y-136*s} Z" fill="{body}" stroke="{LEAD}" stroke-width="4" stroke-linejoin="round"/>')
    # scales of justice in the pediment
    p.append(f'<line x1="{x}" y1="{y-178*s}" x2="{x}" y2="{y-146*s}" stroke="{LEAD}" stroke-width="3"/>')
    p.append(f'<line x1="{x-22*s}" y1="{y-170*s}" x2="{x+22*s}" y2="{y-170*s}" stroke="{LEAD}" stroke-width="3"/>')
    for sx in (-22, 22):
        p.append(f'<path d="M{x+(sx-8)*s} {y-158*s} Q{x+sx*s} {y-150*s} {x+(sx+8)*s} {y-158*s}" fill="none" stroke="{LEAD}" stroke-width="3"/>')
    return p


def namebox(x, y, name, cls="pxxs", k=11.2):
    bw = len(name) * k + 28
    return [f'<rect x="{x-bw/2}" y="{y}" width="{bw}" height="30" rx="6" fill="#ffffff" stroke="{LEAD}" stroke-width="3"/>',
            t(x, y + 21, name, cls, LEAD)]


o = [f'<rect width="{W}" height="{H}" fill="{LEAD}"/>']
o.append(t(70, 76, "THE STANDARD", "pxt", "#ffffff", "start"))
o.append(t(70, 116, "Chapter 11 · The nearest standards, and what each would need to change", "dek", "#d9d6cf", "start"))
o.append(t(1730, 76, "WORLD 2", "pxt2", C["sec"], "end"))

X0, Y0, X1, Y1 = 40, 150, 1760, 1060
o += glass(X0, Y0, X1, Y1, C["sec_d"], spread=(.08, .16, .24))
for hx, hy, s in ((110, 1040, .7), (545, 1046, .7), (1700, 1040, .8), (1690, 560, .7), (90, 470, .7), (1110, 1046, .6)):
    o += hill(hx, hy, s)
# a river under the second row, for scenery
o.append(f'<path d="M40 784 C 400 760, 700 806, 1000 784 S 1500 760, 1760 784" fill="none" stroke="{LEAD}" stroke-width="34"/>')
o.append(f'<path d="M40 784 C 400 760, 700 806, 1000 784 S 1500 760, 1760 784" fill="none" stroke="{C["action"]}" stroke-width="24"/>')

R1, R2, R3 = 960, 660, 420
road([(130, R1), (1560, R1), (1560, R2), (230, R2), (230, R3), (1420, R3)])
o += draw_roads(ROADS); ROADS.clear()
# bridges where the road crosses the river
for bx in (1560, 230):
    o.append(f'<rect x="{bx-26}" y="756" width="52" height="56" fill="#b98b54" stroke="{LEAD}" stroke-width="4"/>')
    for k in range(4):
        o.append(f'<line x1="{bx-26}" y1="{766+k*12}" x2="{bx+26}" y2="{766+k*12}" stroke="{LEAD}" stroke-width="2"/>')

# the gate from World 1
o.append(f'<rect x="60" y="{R1-34}" width="150" height="68" rx="34" fill="{C["acc"]}" stroke="{LEAD}" stroke-width="5"/>')
o.append(t(135, R1 + 4, "FROM", "pxxs", "#ffffff"))
o.append(t(135, R1 + 22, "WORLD 1", "pxxs", "#ffffff"))

LV = [  # number, x, y, colour, name under the level, the ask above it
    ("2-1", 360, R1, C["acc"], "FIELD BUILDING", ["Name it loudly, define it slowly,", "gather a small group"]),
    ("2-2", 660, R1, C["action"], "OCDS + OC4IDS", ["An extension for the tender's", "questions, addenda and readings"]),
    ("2-3", 960, R1, C["action"], "IFC 4.3 + IDS", ["Requirements a bot can check", "before the bid, not after"]),
    ("2-4", 1260, R1, C["action"], "MEASUREMENT", ["One name for each pay item,", "so prices can be compared"]),
    ("2-5", 1300, R2, C["sec"], "CCDC 23", ["A guide note: name the bot", "version the tender was read by"]),
    ("2-6", 900, R2, C["sec"], "ISO 10845-3", ["Conditions of tender: a bot's", "question answered to every bidder"]),
    ("2-7", 500, R2, C["sec"], "AACE CLASSES", ["A conformance class beside", "the five estimate classes"]),
    ("2-8", 520, R3, C["acc"], "IEEE 3119", ["A construction profile: buy bots", "that pass the public test"]),
]
for num, x, y, col, name, ask in LV:
    o += note(x, y - 132, ask)
    o += level(x, y, num, col)
    o += namebox(x, y + 54, name)

# the castle: a new part of ISO 10845
CX, CY = 1000, R3 + 30
o += note(CX, CY - 270, ["The reasonable bot: a public test set,", "a tolerance and a required record"], w=380)
o += castle(CX, CY, .75, mix(LEAD, "#ffffff", .18), C["sec"])
o += namebox(CX, CY + 14, "ISO 10845 · NEW PART", "pxs", 15.5)

# past the castle: the courthouse and the first case
HX, HY = 1500, R3 + 30
o += courthouse(HX, HY, .8)
o += namebox(HX, HY + 14, "THE FIRST CASE", "pxs", 15.5)
o += note(HX, HY - 240, ["Daubert, Mohan, the Rule 707 redraft:", "a method and a known error rate"], w=380)

o.append(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="none" stroke="#ffffff" stroke-width="6"/>')
o.append(t(70, 1112, "Every level is a standard that already exists. The castle is the one that doesn't.", "foot", "#ffffff", "start"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .pxt{{font-family:'Press Start 2P',monospace;font-size:34px;letter-spacing:.04em}}
  .pxt2{{font-family:'Press Start 2P',monospace;font-size:26px}}
  .px{{font-family:'Press Start 2P',monospace;font-size:20px}}
  .pxs{{font-family:'Press Start 2P',monospace;font-size:15px}}
  .pxxs{{font-family:'Press Start 2P',monospace;font-size:11px}}
  .dek{{font-family:Lora,Georgia,serif;font-style:italic;font-size:21px}}
  .lab{{font-family:Lora,Georgia,serif;font-weight:500;font-size:20px}}
  .labs2{{font-family:Lora,Georgia,serif;font-style:italic;font-size:18px}}
  .foot{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:28px}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "world-2-standards"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#2c2c2a}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
