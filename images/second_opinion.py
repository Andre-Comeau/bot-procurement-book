"""Chapter 9 figure: Bot Procurement World, a retro overworld map.

World 1: start; the reader stands just before the book level (the book will be
finished first); then the estimator's and the evaluator's huts with a path
between them, both branching on toward the Standard; the field-building level lies between us and the Standard's castle.
Roads from the castle lead to the other worlds of bot construction, each with
its own field-building level and castle. Stained-glass palette (the Protocol
Institute brand colours with lead outlines, as in failure_modes_glass.py).
Original drawing in the overworld-map genre: no game characters or sprites.

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
        p.append(f'<rect x="{x-62}" y="{y+h+14}" width="124" height="34" rx="6" fill="#ffffff" stroke="{LEAD}" stroke-width="3"/>')
        p.append(t(x, y + h + 38, sub, "lab", LEAD))
    return p


def hut(x, y, roof, name):
    return [f'<rect x="{x-42}" y="{y-30}" width="84" height="62" fill="#ffffff" stroke="{LEAD}" stroke-width="5"/>',
            f'<path d="M{x-58} {y-28} L{x} {y-82} L{x+58} {y-28} Z" fill="{roof}" stroke="{LEAD}" stroke-width="5" stroke-linejoin="round"/>',
            f'<rect x="{x-14}" y="{y}" width="28" height="32" fill="{LEAD}"/>',
            f'<rect x="{x-34}" y="{y-16}" width="14" height="14" fill="{mix(roof, "#ffffff", .5)}" stroke="{LEAD}" stroke-width="3"/>',
            f'<rect x="{x+20}" y="{y-16}" width="14" height="14" fill="{mix(roof, "#ffffff", .5)}" stroke="{LEAD}" stroke-width="3"/>',
            f'<rect x="{x-82}" y="{y-128}" width="164" height="34" rx="6" fill="#ffffff" stroke="{LEAD}" stroke-width="3"/>',
            t(x, y - 104, name, "pxs", LEAD)]


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

# header
o.append(t(70, 76, "BOT PROCUREMENT WORLD", "pxt", "#ffffff", "start"))
o.append(t(70, 116, "Chapter 9 · A second opinion on every price", "dek", "#d9d6cf", "start"))
o.append(t(1730, 76, "WORLD 1", "pxt2", C["acc"], "end"))

# ---- World 1 ----
X0, Y0, X1, Y1 = 40, 150, 1350, 1060
o += glass(X0, Y0, X1, Y1, C["sec"])
# a river with a bridge
o.append(f'<path d="M840 {Y0} C 800 360, 930 520, 920 700 S 860 920, 900 {Y1}" fill="none" stroke="{LEAD}" stroke-width="76"/>')
o.append(f'<path d="M840 {Y0} C 800 360, 930 520, 920 700 S 860 920, 900 {Y1}" fill="none" stroke="{C["action"]}" stroke-width="64"/>')
o.append(f'<path d="M840 {Y0} C 800 360, 930 520, 920 700 S 860 920, 900 {Y1}" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="14 30" opacity=".6"/>')
for hx, hy, s in ((120, 300, 1), (220, 280, .8), (620, 300, 1), (470, 280, .7), (1250, 1000, .9), (1150, 1020, .7), (700, 1030, .8), (110, 1040, .7)):
    o += hill(hx, hy, s)

# roads: start -> estimator; estimator <-> evaluator; both branch to the meeting point; on to book,
# field building and the Standard; and out of the world to the east
JX, JY = 600, 700
HX, BX, MX = 580, 400, 790                                 # huts, book, where the branches meet
o += road([(140, 900), (HX, 900)])                      # start, you, the book, the estimator
o += road([(HX, 900), (HX, 540)])                       # the path between the huts
o += road([(HX, 900), (MX, 900), (MX, JY)])             # estimator's branch
o += road([(HX, 540), (MX, 540), (MX, JY)])             # evaluator's branch
o += road([(MX, JY), (1100, JY), (1100, 480)])          # book, bridge, field building, castle
o += road([(1100, 380), (1100, 318), (X1 + 10, 318)])   # out to the other worlds
o.append(f'<rect x="874" y="{JY-30}" width="100" height="60" fill="#c9a46a" stroke="{LEAD}" stroke-width="5"/>')  # bridge deck
for k in range(5):
    o.append(f'<line x1="{884 + k*20}" y1="{JY-30}" x2="{884 + k*20}" y2="{JY+30}" stroke="{LEAD}" stroke-width="3"/>')
o += road([(874, JY), (974, JY)], w=14)

# start
o.append(f'<rect x="72" y="866" width="120" height="68" rx="34" fill="{C["acc"]}" stroke="{LEAD}" stroke-width="5"/>')
o.append(t(132, 910, "START", "pxs", "#ffffff"))

# the huts
o += hut(HX, 900, C["action"], "ESTIMATOR")
o += hut(HX, 540, C["sec_d"], "EVALUATOR")
o.append(f'<rect x="300" y="640" width="250" height="98" rx="8" fill="{LEAD}" opacity=".82"/>')
o.append(t(425, 668, "One engine, two huts", "lab", "#ffffff"))
o.append(t(425, 694, "How much should this cost?", "labi", "#ffffff"))
o.append(t(425, 720, "Are we paying too much?", "labi", "#ffffff"))

# you are here, just before the book
BOT = (262, 900)
o += bot(*BOT)
bx, by = BOX = (BOT[0], BOT[1] - 6)
o.append(f'<rect x="{bx-80}" y="{by-150}" width="160" height="44" rx="8" fill="#ffffff" stroke="{LEAD}" stroke-width="4"/>')
o.append(f'<path d="M{bx-12} {by-106} L{bx} {by-90} L{bx+12} {by-106} Z" fill="#ffffff" stroke="{LEAD}" stroke-width="4" stroke-linejoin="round"/>')
o.append(f'<rect x="{bx-12}" y="{by-110}" width="24" height="8" fill="#ffffff"/>')
o.append(t(bx, by - 122, "YOU ARE HERE", "pxxs", LEAD))

o += level(BX, 900, "1-1", C["acc"], "The book")
o += level(1100, 590, "1-2", C["action"], None)
o.append(f'<rect x="1150" y="560" width="190" height="60" rx="8" fill="{LEAD}" opacity=".82"/>')
o.append(t(1245, 586, "Field building", "lab", "#ffffff"))
o.append(t(1245, 610, "users, data, partners", "labi", "#ffffff"))

# the Standard: the next big castle
o += castle(1100, 420, 1.0, mix(LEAD, "#ffffff", .18), C["acc"])
o.append(f'<rect x="970" y="432" width="260" height="56" rx="8" fill="#ffffff" stroke="{LEAD}" stroke-width="4"/>')
o.append(t(1100, 468, "THE STANDARD", "pxs", LEAD))
o.append(t(1080, 120 + 52, "", "lab"))
o.append(f'<path d="M{X1-40} 300 l26 0" stroke="{LEAD}" stroke-width="0"/>')

# world frame
o.append(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="none" stroke="#ffffff" stroke-width="6"/>')

# ---- the other worlds ----
WORLDS = [("WORLD 2", "BIM for bots", C["action"]),
          ("WORLD 3", "Bot monitoring", C["ink2"]),
          ("WORLD 4", "Robotic construction", C["acc"])]
PX0, PX1, PH, PG = 1390, 1760, 270, 30
for i, (wn, name, base) in enumerate(WORLDS):
    py = Y0 + i * (PH + PG)
    o += glass(PX0, py, PX1, py + PH, base, cell=30, spread=(.15, .25, .35))
    o += road([(PX0 - 2, py + 168), (PX0 + 120, py + 168), (PX0 + 250, py + 168)], w=16)
    o += level(PX0 + 120, py + 168, f"{i+2}-1", C["sec"], None, size=60)
    o += castle(PX0 + 290, py + 214, .52, mix(LEAD, "#ffffff", .18), base if base != C["acc"] else C["action"])
    o.append(f'<rect x="{PX0+12}" y="{py+12}" width="{PX1-PX0-24}" height="64" rx="8" fill="{LEAD}" opacity=".82"/>')
    o.append(t(PX0 + 28, py + 40, wn, "pxs", C["acc"] if base != C["acc"] else "#ffd27a", "start"))
    o.append(t(PX0 + 28, py + 66, name, "lab", "#ffffff", "start"))
    o.append(t(PX0 + 120, py + 230, "Field building", "labs", "#ffffff"))
    o.append(f'<rect x="{PX0}" y="{py}" width="{PX1-PX0}" height="{PH}" fill="none" stroke="#ffffff" stroke-width="5"/>')
# the road east from the Standard reaches the worlds
for i in range(3):
    yy = Y0 + i * (PH + PG) + 168
    o.append(f'<path d="M{X1+3} 318 L1370 318 L1370 {yy} L{PX0-3} {yy}" fill="none" stroke="#f3e6c8" stroke-width="8" stroke-dasharray="8 8"/>')

# footer
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
