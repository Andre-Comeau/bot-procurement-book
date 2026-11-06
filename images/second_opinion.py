"""Chapter 9 figure: Bot Procurement World, a retro overworld map of the bid, award and change process.

World 1 runs Tender, Bid, Contract, RFI, Contemplated change and Quote, then splits
three ways to the Change Order castle: the estimator's hut, the evaluator's hut
(with a secret path between them), and the slow road from consultant to
sub-consultant and back to consultant. The Standard joins the other worlds of
bot construction, each with its own field-building level and castle.
Stained-glass palette (Protocol Institute brand colours with lead outlines, as in
failure_modes_glass.py). An original drawing in the overworld-map genre: no game
characters or sprites. The first version (the book level and the Standard as
World 1's castle) is kept in the project files as bot-procurement-world-v1.

    python images/second_opinion.py images/second-opinion
    node images/project_hex_map_render.js "$PWD/images/second-opinion.html" images/second-opinion.png 1800 1160
"""
import random, sys

C = dict(action="#0064ff", action_p="#004fcc", sec="#0f6e56", sec_d="#085041",
         acc="#d85a30", acc_d="#9e3d18", canvas="#f9f8f5", ink="#2c2c2a", ink2="#5f5e5a")
LEAD = "#2c2c2a"
W, H = 1800, 1160
random.seed(7)


def mix(a, b, f):
    a = [int(a[i:i + 2], 16) for i in (1, 3, 5)]; b = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(int(x + (y - x) * f) for x, y in zip(a, b))


def t(x, y, s, cls, fill=None, anchor="middle"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}"{f} text-anchor="{anchor}">{s}</text>'


def glass(x0, y0, x1, y1, base, cell=40, spread=(.0, .10, .2)):
    """A tiled ground: each square a shade of the base, leaded like glass."""
    p = []
    for gx in range(x0, x1, cell):
        for gy in range(y0, y1, cell):
            f = random.choice(spread)
            p.append(f'<rect x="{gx}" y="{gy}" width="{min(cell, x1-gx)}" height="{min(cell, y1-gy)}" '
                     f'fill="{mix(base, "#ffffff", f)}" stroke="{mix(base, LEAD, .45)}" stroke-width="1.5"/>')
    return p


def road(pts, w=22):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    return [f'<path d="{d}" fill="none" stroke="{LEAD}" stroke-width="{w+8}" stroke-linejoin="round" stroke-linecap="round"/>',
            f'<path d="{d}" fill="none" stroke="#f3e6c8" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>',
            f'<path d="{d}" fill="none" stroke="{C["acc_d"]}" stroke-width="5" stroke-dasharray="2 16" stroke-linecap="round"/>']


def hill(x, y, s=1.0, col=None):
    col = col or C["sec_d"]
    return [f'<path d="M{x-34*s} {y} Q{x-34*s} {y-58*s} {x} {y-58*s} Q{x+34*s} {y-58*s} {x+34*s} {y} Z" '
            f'fill="{col}" stroke="{LEAD}" stroke-width="4"/>',
            f'<circle cx="{x-10*s}" cy="{y-34*s}" r="{4*s}" fill="{LEAD}"/><circle cx="{x+10*s}" cy="{y-34*s}" r="{4*s}" fill="{LEAD}"/>']


def level(x, y, label, fill, sub=None, size=84):
    h = size / 2
    p = [f'<rect x="{x-h+6}" y="{y-h+6}" width="{size}" height="{size}" rx="10" fill="{LEAD}"/>',
         f'<rect x="{x-h}" y="{y-h}" width="{size}" height="{size}" rx="10" fill="{fill}" stroke="{LEAD}" stroke-width="5"/>',
         t(x, y + 9, label, "px", "#ffffff")]
    if sub:
        bw = 26 + 10.5 * len(sub)
        p.append(f'<rect x="{x-bw/2}" y="{y+h+14}" width="{bw}" height="34" rx="6" fill="#ffffff" stroke="{LEAD}" stroke-width="3"/>')
        p.append(t(x, y + h + 38, sub, "lab", LEAD))
    return p


def hut(x, y, roof, name, below=False, small=False):
    return [f'<rect x="{x-42}" y="{y-30}" width="84" height="62" fill="#ffffff" stroke="{LEAD}" stroke-width="5"/>',
            f'<path d="M{x-58} {y-28} L{x} {y-82} L{x+58} {y-28} Z" fill="{roof}" stroke="{LEAD}" stroke-width="5" stroke-linejoin="round"/>',
            f'<rect x="{x-14}" y="{y}" width="28" height="32" fill="{LEAD}"/>',
            f'<rect x="{x-34}" y="{y-16}" width="14" height="14" fill="{mix(roof, "#ffffff", .5)}" stroke="{LEAD}" stroke-width="3"/>',
            f'<rect x="{x+20}" y="{y-16}" width="14" height="14" fill="{mix(roof, "#ffffff", .5)}" stroke="{LEAD}" stroke-width="3"/>',
            f'<rect x="{x-(len(name)*(5.6 if small else 8)+14)}" y="{(y+44) if below else (y-128)}" width="{len(name)*(11.2 if small else 16)+28}" height="{28 if small else 34}" rx="6" fill="#ffffff" stroke="{LEAD}" stroke-width="3"/>',
            t(x, (y + (63 if small else 68)) if below else (y - 104), name, "pxxs" if small else "pxs", LEAD)]


def castle(x, y, s, body, flag):
    p = ['<g>']
    def r(rx, ry, rw, rh, fill=body):
        p.append(f'<rect x="{x+rx*s}" y="{y+ry*s}" width="{rw*s}" height="{rh*s}" fill="{fill}" stroke="{LEAD}" stroke-width="{max(2.5, 4*s)}"/>')
    r(-100, -120, 200, 120)
    for tx in (-120, 60):
        r(tx, -190, 60, 190)
        for k in range(3):
            r(tx + k * 22, -208, 16, 18)
    r(-40, -170, 80, 50)
    for k in range(4):
        r(-40 + k * 22, -186, 14, 16)
    p.append(f'<path d="M{x-24*s} {y} L{x-24*s} {y-44*s} Q{x} {y-70*s} {x+24*s} {y-44*s} L{x+24*s} {y} Z" fill="{LEAD}"/>')
    for wx in (-98, 82):
        p.append(f'<rect x="{x+wx*s}" y="{y-150*s}" width="{16*s}" height="{26*s}" fill="#ffd27a" stroke="{LEAD}" stroke-width="{2*s+1}"/>')
    p.append(f'<line x1="{x}" y1="{y-186*s}" x2="{x}" y2="{y-250*s}" stroke="{LEAD}" stroke-width="{5*s}"/>')
    p.append(f'<path d="M{x} {y-250*s} L{x+48*s} {y-236*s} L{x} {y-222*s} Z" fill="{flag}" stroke="{LEAD}" stroke-width="{2*s+1}"/>')
    p.append('</g>')
    return p


def bot(x, y):
    """The reader's token: a small original robot."""
    return [f'<ellipse cx="{x}" cy="{y+40}" rx="30" ry="8" fill="{LEAD}" opacity=".35"/>',
            f'<line x1="{x}" y1="{y-46}" x2="{x}" y2="{y-62}" stroke="{LEAD}" stroke-width="5"/>',
            f'<circle cx="{x}" cy="{y-66}" r="7" fill="{C["acc"]}" stroke="{LEAD}" stroke-width="3"/>',
            f'<rect x="{x-28}" y="{y-46}" width="56" height="42" rx="10" fill="#ffffff" stroke="{LEAD}" stroke-width="5"/>',
            f'<circle cx="{x-11}" cy="{y-26}" r="6" fill="{C["action"]}"/><circle cx="{x+11}" cy="{y-26}" r="6" fill="{C["action"]}"/>',
            f'<rect x="{x-22}" y="{y}" width="44" height="34" rx="6" fill="{C["action"]}" stroke="{LEAD}" stroke-width="5"/>']



o = [f'<rect width="{W}" height="{H}" fill="{LEAD}"/>']
o.append(t(70, 76, "BOT PROCUREMENT WORLD", "pxt", "#ffffff", "start"))
o.append(t(70, 116, "Chapter 9 · From tender to change order", "dek", "#d9d6cf", "start"))
o.append(t(1730, 76, "WORLD 1", "pxt2", C["acc"], "end"))

X0, Y0, X1, Y1 = 40, 150, 1350, 1060
o += glass(X0, Y0, X1, Y1, C["sec"])
# a pond, for scenery
o.append(f'<ellipse cx="1150" cy="975" rx="150" ry="52" fill="{C["action"]}" stroke="{LEAD}" stroke-width="6"/>')
o.append(f'<path d="M1060 970 q20 -10 40 0 M1160 990 q20 -10 40 0" fill="none" stroke="#ffffff" stroke-width="3" opacity=".6"/>')
for hx, hy, s in ((110, 1040, .7), (340, 1045, .8), (880, 1040, .7), (1290, 470, .8), (1280, 720, .7), (130, 300, .8), (200, 760, .7)):
    o += hill(hx, hy, s)

# the process: tender to quote
R1, R2 = 940, 760
LV = [("1-1", 260, R1, "Tender"), ("1-2", 430, R1, "Bid"), ("1-3", 600, R1, "Contract"),
      ("1-4", 600, R2, "RFI"), ("1-5", 840, R2, "Contemplated change"), ("1-6", 1120, R2, "Quote")]
o += road([(140, R1), (600, R1), (600, R2), (1120, R2)])
# the three paths from the quote to the change order
CX, CY = 250, 560          # castle door
MX = 420                   # where the paths meet
PE, PV, PC = 440, 600, 250 # estimator, evaluator and consultant rows
o += road([(1120, R2), (1120, PC), (MX, PC), (MX, CY), (CX, CY)])
o += road([(1120, PE), (MX, PE)])
o += road([(1120, PV), (MX, PV), (MX, CY)])
# the secret path between the huts
o.append(f'<path d="M722 {PE+20} C 790 {PE+40}, 790 {PV-20}, 858 {PV-10}" fill="none" stroke="#f3e6c8" stroke-width="6" stroke-dasharray="3 12" stroke-linecap="round"/>')
o.append(f'<rect x="773" y="{(PE+PV)//2-17}" width="34" height="34" rx="4" fill="#ffd27a" stroke="{LEAD}" stroke-width="4"/>')
o.append(t(790, (PE+PV)//2 + 9, "?", "px", LEAD))

o.append(f'<rect x="60" y="{R1-34}" width="120" height="68" rx="34" fill="{C["acc"]}" stroke="{LEAD}" stroke-width="5"/>')
o.append(t(120, R1 + 10, "START", "pxs", "#ffffff"))
for num, x, y, name in LV:
    o += level(x, y, num, C["acc"] if num != "1-6" else C["action"], name)

o += hut(680, PE, C["action"], "ESTIMATOR", below=True)
o += hut(900, PV, C["sec_d"], "EVALUATOR")
o += hut(980, PC, C["ink2"], "CONSULTANT", below=True, small=True)
o += hut(760, PC, mix(C["ink2"], "#ffffff", .3), "SUB-CONSULTANT", below=True, small=True)
o += hut(540, PC, C["ink2"], "CONSULTANT", below=True, small=True)

# path notes
def note(x, y, lines, w):
    p = [f'<rect x="{x}" y="{y}" width="{w}" height="{18 + 26*len(lines)}" rx="8" fill="{LEAD}" opacity=".84"/>']
    for i, (s, c) in enumerate(lines):
        p.append(t(x + w/2, y + 32 + 26*i, s, c, "#ffffff"))
    return p
o += note(1150, 168, [("The slow road", "lab"), ("ten working days,", "labi"), ("an invoice at every pipe", "labi")], 190)
o += note(900, PE - 78, [("Minutes, not days", "lab")], 180)
o += note(560, PV + 40, [("One engine, two huts,", "lab"), ("and a secret path between", "labi")], 240)

# the castle: change order
o += castle(CX, CY, 1.0, mix(LEAD, "#ffffff", .18), C["acc"])
o.append(f'<rect x="{CX-130}" y="{CY+12}" width="260" height="56" rx="8" fill="#ffffff" stroke="{LEAD}" stroke-width="4"/>')
o.append(t(CX, CY + 48, "CHANGE ORDER", "pxs", LEAD))
o.append(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="none" stroke="#ffffff" stroke-width="6"/>')

# the other worlds
WORLDS = [("WORLD 2", "The Standard", C["sec_d"]),
          ("WORLD 3", "BIM for bots", C["action"]),
          ("WORLD 4", "Bot monitoring", C["ink2"]),
          ("WORLD 5", "Robotic construction", C["acc"])]
PX0, PX1, PG = 1390, 1760, 20
PH = (Y1 - Y0 - PG * 3) / 4
for i, (wn, name, base) in enumerate(WORLDS):
    py = int(Y0 + i * (PH + PG))
    o += glass(PX0, py, PX1, int(py + PH), base, cell=30, spread=(.15, .25, .35))
    ry = py + 140
    o += road([(PX0 + 30, ry), (PX0 + 290, ry)], w=14)
    o += level(PX0 + 110, ry, f"{i+2}-1", C["sec"] if base != C["sec_d"] else C["action"], None, size=54)
    o += castle(PX0 + 290, ry + 30, .42, mix(LEAD, "#ffffff", .18), C["acc"] if base != C["acc"] else C["action"])
    o.append(f'<rect x="{PX0+12}" y="{py+12}" width="{PX1-PX0-24}" height="58" rx="8" fill="{LEAD}" opacity=".84"/>')
    o.append(t(PX0 + 28, py + 38, wn, "pxs", "#ffd27a", "start"))
    o.append(t(PX0 + 28, py + 62, name, "lab", "#ffffff", "start"))
    o.append(t(PX0 + 110, ry + 52, "Field building", "labs", "#ffffff"))
    o.append(f'<rect x="{PX0}" y="{py}" width="{PX1-PX0}" height="{int(PH)}" fill="none" stroke="#ffffff" stroke-width="5"/>')

o.append(t(70, 1112, "The treasure is in another castle, but this is the path there.", "foot", "#ffffff", "start"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .pxt{{font-family:'Press Start 2P',monospace;font-size:34px;letter-spacing:.04em}}
  .pxt2{{font-family:'Press Start 2P',monospace;font-size:26px}}
  .px{{font-family:'Press Start 2P',monospace;font-size:20px}}
  .pxs{{font-family:'Press Start 2P',monospace;font-size:15px}}
  .pxxs{{font-family:'Press Start 2P',monospace;font-size:11px}}
  .dek{{font-family:Lora,Georgia,serif;font-style:italic;font-size:21px}}
  .lab{{font-family:Lora,Georgia,serif;font-weight:500;font-size:20px;paint-order:stroke;stroke:#2c2c2a;stroke-width:0}}
  .labi{{font-family:Lora,Georgia,serif;font-style:italic;font-size:18px}}
  .labs{{font-family:Lora,Georgia,serif;font-style:italic;font-size:16px;paint-order:stroke;stroke:#2c2c2a;stroke-width:4px}}
  .foot{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:28px}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "second-opinion"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#2c2c2a}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
