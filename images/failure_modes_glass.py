"""Failure-modes 2x2 as a stained-glass window (PI brand kit colours, no PI marks).

Usage: python images/failure_modes_glass.py images/failure-modes-glass
Then: node images/project_hex_map_render.js "$PWD/images/failure-modes-glass.html" images/failure-modes-glass.png 1600 1940
"""
import sys, html, random, math

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6",
         ink="#2c2c2a", ink2="#5f5e5a")
LEAD = "#2c2c2a"
W, H = 1600, 1940
WX0, WX1 = 180, 1420            # window sides
APEX, SHOULDER, WY1 = 330, 600, 1830
XM, YM = (WX0 + WX1) / 2, 1110   # the cross: Principal above, Agent below
random.seed(7)

def hexrgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def rgbhex(c): return "#%02x%02x%02x" % tuple(max(0, min(255, int(v))) for v in c)
def mix(a, b, t): A, B = hexrgb(a), hexrgb(b); return rgbhex([A[i] + (B[i] - A[i]) * t for i in range(3)])

# window outline: pointed (equilateral-ish) arch on a rectangle
R = (WX1 - WX0) * 0.85
def arch_path():
    return (f"M{WX0},{WY1} L{WX0},{SHOULDER} "
            f"A{R},{R} 0 0 1 {XM},{APEX} A{R},{R} 0 0 1 {WX1},{SHOULDER} L{WX1},{WY1} Z")

# glass: jittered grid, each cell coloured by its quadrant
QUAD = {  # (is_left, is_top): base colours
    (True, True): [C["acc"], C["acc_d"], mix(C["acc"], "#ffffff", .25)],
    (False, True): [C["sec"], C["sec_d"], mix(C["sec"], "#ffffff", .25)],
    (True, False): [C["ink2"], C["ink"], mix(C["ink2"], "#ffffff", .3)],
    (False, False): [C["action"], C["action_p"], mix(C["action"], "#ffffff", .3)],
}
cols, rows = 12, 14
gx = [WX0 - 40 + i * (WX1 - WX0 + 80) / cols for i in range(cols + 1)]
gy = [APEX - 40 + j * (WY1 - APEX + 80) / rows for j in range(rows + 1)]
pts = {}
for i in range(cols + 1):
    for j in range(rows + 1):
        jx = 0 if i in (0, cols) else random.uniform(-30, 30)
        jy = 0 if j in (0, rows) else random.uniform(-26, 26)
        x, y = gx[i] + jx, gy[j] + jy
        # snap lines onto the cross so the four panes stay clean
        if abs(gx[i] - XM) < 60: x = XM
        if abs(gy[j] - YM) < 45: y = YM
        pts[i, j] = (x, y)

o = []
o.append(f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>')
o.append(f'<defs><clipPath id="win"><path d="{arch_path()}"/></clipPath></defs>')

def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'

o.append(t(80, 86, "WHAT DO WE DO WITH A DRUNKEN SAILOR?", "eyebrow"))
o.append(t(80, 148, "How words and deeds go wrong", "title"))
o.append(t(80, 194, "Did it go wrong in what was said or in what was done, and did anyone mean it?", "dek"))
o.append(t(80, 226, "Four characters, one window, and a standard at its heart.", "dek"))

g = ['<g clip-path="url(#win)">']
for i in range(cols):
    for j in range(rows):
        quad = [pts[i, j], pts[i + 1, j], pts[i + 1, j + 1], pts[i, j + 1]]
        cx = sum(p[0] for p in quad) / 4; cy = sum(p[1] for p in quad) / 4
        base = QUAD[(cx < XM, cy < YM)]
        col = random.choice(base)
        col = mix(col, "#ffffff", random.uniform(0, .18))
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in quad) + " Z"
        g.append(f'<path d="{d}" fill="{col}" stroke="{LEAD}" stroke-width="5" stroke-linejoin="round"/>')
g.append('</g>')
o += g
# the cross bars (heavier lead) and the window frame
o.append(f'<g clip-path="url(#win)"><line x1="{XM}" y1="{APEX-20}" x2="{XM}" y2="{WY1+20}" stroke="{LEAD}" stroke-width="16"/>'
         f'<line x1="{WX0-20}" y1="{YM}" x2="{WX1+20}" y2="{YM}" stroke="{LEAD}" stroke-width="16"/></g>')
o.append(f'<path d="{arch_path()}" fill="none" stroke="{LEAD}" stroke-width="22" stroke-linejoin="round"/>')
o.append(f'<path d="{arch_path()}" fill="none" stroke="#8a8780" stroke-width="4" stroke-linejoin="round"/>')

# emblems, drawn as pale glass with lead outlines
PALE = "#fbf6e9"
def emb(d, fill=PALE, w=6):
    return f'<path d="{d}" fill="{fill}" stroke="{LEAD}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'

def tricorn(cx, cy):   # Long John Silver's hat
    return emb(f"M{cx-95},{cy+10} Q{cx-60},{cy-70} {cx},{cy-62} Q{cx+60},{cy-70} {cx+95},{cy+10} "
               f"Q{cx+40},{cy-8} {cx},{cy+20} Q{cx-40},{cy-8} {cx-95},{cy+10} Z") + emb(f"M{cx-70},{cy-14} Q{cx},{cy-30} {cx+70},{cy-14}", "none", 4)

def serpent(cx, cy):   # the Serpent: arrow head, forked tongue, apple
    body = (f"M{cx-110},{cy+70} C{cx-40},{cy+96} {cx-20},{cy+24} {cx-48},{cy+2} "
            f"C{cx-78},{cy-24} {cx-50},{cy-44} {cx-4},{cy-40}")
    head = (f"M{cx-12},{cy-62} Q{cx+34},{cy-66} {cx+62},{cy-44} Q{cx+68},{cy-38} {cx+62},{cy-32} "
            f"Q{cx+34},{cy-12} {cx-12},{cy-18} Z")
    tongue = f"M{cx+64},{cy-38} L{cx+88},{cy-38} M{cx+88},{cy-38} L{cx+100},{cy-48} M{cx+88},{cy-38} L{cx+100},{cy-28}"
    return (f'<path d="{body}" fill="none" stroke="{LEAD}" stroke-width="34" stroke-linecap="round"/>'
            f'<path d="{body}" fill="none" stroke="{PALE}" stroke-width="22" stroke-linecap="round"/>'
            + f'<path d="{tongue}" fill="none" stroke="{C["acc_d"]}" stroke-width="5" stroke-linecap="round"/>'
            + emb(head)
            + f'<circle cx="{cx+30}" cy="{cy-46}" r="6" fill="{LEAD}"/>'
            + emb(f"M{cx+78},{cy+40} m-28,0 a28,28 0 1,0 56,0 a28,28 0 1,0 -56,0", C["acc"])
            + emb(f"M{cx+78},{cy+12} q4,-14 16,-18", "none", 4))

def dragon(cx, cy):    # the Dragon, breathing fire
    head = (f"M{cx-100},{cy+70} C{cx-95},{cy+10} {cx-80},{cy-20} {cx-40},{cy-42} L{cx-70},{cy-92} L{cx-18},{cy-56} "
            f"L{cx-30},{cy-100} L{cx+6},{cy-56} C{cx+30},{cy-50} {cx+60},{cy-44} {cx+82},{cy-30} L{cx+88},{cy-14} "
            f"L{cx+48},{cy-6} L{cx+12},{cy+4} L{cx+62},{cy+16} L{cx+46},{cy+36} C{cx+10},{cy+46} {cx-20},{cy+44} {cx-40},{cy+48} "
            f"C{cx-55},{cy+56} {cx-60},{cy+66} {cx-62},{cy+80} Z")
    flame = (f"M{cx+60},{cy+4} L{cx+128},{cy-26} L{cx+108},{cy-2} L{cx+150},{cy+4} L{cx+106},{cy+16} "
             f"L{cx+132},{cy+40} L{cx+62},{cy+12} Z")
    return (emb(flame, C["acc"], 5) + emb(head)
            + f'<circle cx="{cx+18}" cy="{cy-30}" r="7" fill="{LEAD}"/>'
            + emb(f"M{cx+70},{cy-26} l6,-2", "none", 4))

def bottle(cx, cy):    # the Drunken Sailor's bottle, tipped
    return (f'<g transform="rotate(-24 {cx} {cy})">'
            + emb(f"M{cx-30},{cy+70} L{cx-30},{cy-10} Q{cx-30},{cy-34} {cx-12},{cy-44} L{cx-12},{cy-80} "
                  f"L{cx+12},{cy-80} L{cx+12},{cy-44} Q{cx+30},{cy-34} {cx+30},{cy-10} L{cx+30},{cy+70} Z")
            + emb(f"M{cx-30},{cy+10} L{cx+30},{cy+10} L{cx+30},{cy+40} L{cx-30},{cy+40} Z", C["action_t"], 4)
            + '</g>')

def diamond(cx, cy):   # "Who's on First?": a baseball diamond
    s = 62
    out = emb(f"M{cx},{cy+s} L{cx+s},{cy} L{cx},{cy-s} L{cx-s},{cy} Z", C["sec_t"])
    for bx, by in ((cx + s, cy), (cx, cy - s), (cx - s, cy)):
        out += emb(f"M{bx-12},{by} L{bx},{by-12} L{bx+12},{by} L{bx},{by+12} Z", PALE, 4)
    out += emb(f"M{cx-12},{cy+s-4} L{cx+12},{cy+s-4} L{cx+12},{cy+s+8} L{cx},{cy+s+18} L{cx-12},{cy+s+8} Z", PALE, 4)
    out += t(cx, cy + 20, "?", "q", LEAD, "middle")
    return out

# (emblem fn, emblem centre, corner name, character, remedy lines)
BW, BH, GAP = 520, 262, 190
LX, RX = XM - 310, XM + 310
TOPY, BOTY = YM - GAP - BH, YM + GAP
# (emblem fn, column x, row top?, corner name, character, remedy lines)
PANES = [
    (serpent, LX, True, "Manipulation", "The Serpent",
     ["Caught by a bond posted", "in advance, and by the", "courts' yardstick."]),
    (diamond, RX, True, "Miscommunication", "\u201cWho\u2019s on First?\u201d",
     ["Eased by a shared reference:", "the reading a judge", "measures against."]),
    (dragon, LX, False, "Malice", "The Dragon",
     ["Not yet: force needs a body.", "Close the tender and pray", "for a dragon-slayer."]),
    (bottle, RX, False, "Misadventure", "The Drunken Sailor",
     ["Controlled by consequences.", "The standard is the floor", "to roll back to."]),
]
for fn, cx, top, name, who, rem in PANES:
    by = TOPY if top else BOTY
    o.append(fn(cx, by - 125 if top else by + BH + 125))
    o.append(f'<rect x="{cx-BW/2}" y="{by}" width="{BW}" height="{BH}" rx="12" fill="{PALE}" stroke="{LEAD}" stroke-width="3"/>')
    o.append(t(cx, by + 64, name, "name", LEAD, "middle"))
    o.append(t(cx, by + 108, who, "who", C["ink2"], "middle"))
    for k, ln in enumerate(rem):
        o.append(t(cx, by + 156 + 36 * k, ln, "rem", LEAD, "middle"))

# the rose at the crossing: the standard bot
RR = 140
petals = []
for k in range(12):
    a0 = k * math.pi / 6; a1 = a0 + math.pi / 6
    p = [(XM + RR * math.cos(a0), YM + RR * math.sin(a0)), (XM + (RR + 38) * math.cos((a0 + a1) / 2), YM + (RR + 34) * math.sin((a0 + a1) / 2)),
         (XM + RR * math.cos(a1), YM + RR * math.sin(a1))]
    fill = C["action_t"] if k % 2 else C["acc_t"]
    petals.append(f'<path d="M{XM},{YM} L{p[0][0]:.1f},{p[0][1]:.1f} L{p[1][0]:.1f},{p[1][1]:.1f} L{p[2][0]:.1f},{p[2][1]:.1f} Z" fill="{fill}" stroke="{LEAD}" stroke-width="6" stroke-linejoin="round"/>')
o += petals
o.append(f'<circle cx="{XM}" cy="{YM}" r="{RR}" fill="#ffffff" stroke="{LEAD}" stroke-width="10"/>')
o.append(f'<circle cx="{XM}" cy="{YM}" r="{RR-18}" fill="none" stroke="{LEAD}" stroke-width="2"/>')
o.append(t(XM, YM - 30, "The standard", "rose", LEAD, "middle"))
o.append(t(XM, YM + 12, "bot", "rose", LEAD, "middle"))
o.append(t(XM, YM + 52, "reads every tender", "rose-s", C["action_p"], "middle"))
o.append(t(XM, YM + 80, "the same way", "rose-s", C["action_p"], "middle"))

# axes, outside the window
o.append(t(WX0 - 26, TOPY + BH / 2 - 6, "WORDS", "axis", C["ink2"], "end"))
o.append(t(WX0 - 26, TOPY + BH / 2 + 26, "what is said", "axis-s", C["ink2"], "end"))
o.append(t(WX0 - 26, BOTY + BH / 2 - 6, "DEEDS", "axis", C["ink2"], "end"))
o.append(t(WX0 - 26, BOTY + BH / 2 + 26, "what is done", "axis-s", C["ink2"], "end"))
o.append(t((WX0 + XM) / 2, WY1 + 70, "MALICIOUS", "axis", C["ink2"], "middle"))
o.append(t((XM + WX1) / 2, WY1 + 70, "ACCIDENTAL", "axis", C["ink2"], "middle"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:23px;fill:#5f5e5a}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:56px}}
  .who{{font-family:Lora,Georgia,serif;font-style:italic;font-size:30px}}
  .rem{{font-family:Outfit,sans-serif;font-weight:500;font-size:29px}}
  .rose{{font-family:'Instrument Serif',Georgia,serif;font-size:39px}}
  .rose-s{{font-family:Lora,Georgia,serif;font-style:italic;font-size:22px}}
  .rose-tag{{font-family:Outfit,sans-serif;font-weight:600;font-size:13px;letter-spacing:.16em}}
  .q{{font-family:'Instrument Serif',Georgia,serif;font-size:64px}}
  .axis{{font-family:Outfit,sans-serif;font-weight:600;font-size:24px;letter-spacing:.14em}}
  .axis-s{{font-family:Lora,Georgia,serif;font-style:italic;font-size:22px}}
  .foot{{font-family:Outfit,sans-serif;font-size:20px;fill:#5f5e5a}}
</style>
{chr(10).join(o)}
</svg>'''
out = sys.argv[1] if len(sys.argv) > 1 else "failure-modes-glass"
open(out + ".svg", "w").write(svg)
open(out + ".html", "w").write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>""")
