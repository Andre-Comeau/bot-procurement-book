"""Delivery-method 2x2 for chapter 3 as a stained-glass window (PI brand kit colours, no PI marks).

Same content as delivery_methods_2x2.py, redrawn in the stained-glass palette of
failure_modes_glass.py and second_opinion.py: jittered glass panes with lead lines,
pale glass label panels, and the General Contractor as a lead-framed centre light.

Usage: python images/delivery_methods_glass.py images/delivery-methods-glass
Then: node images/project_hex_map_render.js "$PWD/images/delivery-methods-glass.html" images/delivery-methods-glass.png 1600 1300
"""
import sys, html, random

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6",
         ink="#2c2c2a", ink2="#5f5e5a")
LEAD = "#2c2c2a"
PALE = "#fbf6e9"
W, H = 1600, 1300
X0, Y0, QW, QH = 250, 300, 620, 400          # window origin and pane size
X1, Y1 = X0 + 2 * QW, Y0 + 2 * QH
XM, YM = X0 + QW, Y0 + QH                    # the cross
random.seed(11)

def hexrgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def rgbhex(c): return "#%02x%02x%02x" % tuple(max(0, min(255, int(v))) for v in c)
def mix(a, b, t): A, B = hexrgb(a), hexrgb(b); return rgbhex([A[i] + (B[i] - A[i]) * t for i in range(3)])

def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'

# glass colours per pane (is_left, is_top), as in the failure-modes window
QUAD = {
    (True, True): [C["acc"], C["acc_d"], mix(C["acc"], "#ffffff", .25)],      # hard bid
    (False, True): [C["sec"], C["sec_d"], mix(C["sec"], "#ffffff", .25)],     # partnership
    (True, False): [C["ink2"], C["ink"], mix(C["ink2"], "#ffffff", .3)],      # construction manager
    (False, False): [C["action"], C["action_p"], mix(C["action"], "#ffffff", .3)],  # cost plus
}

# (col, row, accent for the name, name, examples, trade lines, panel top offset)
QUADS = [
    (0, 0, C["acc_d"], "Hard bid",
     ["The bidding contractor", "Lump-sum Design-Build"],
     ["You trade trust in the counterparty", "for rock-bottom pricing."], 30),
    (1, 0, C["sec_d"], "Partnership",
     ["Principals entangled in a common interest"],
     ["You trade a higher share of the benefits", "for significantly less management effort."], 30),
    (0, 1, LEAD, "Construction Manager",
     ["Two agents, designer and builder,", "acting as checks on each other"],
     ["You trade accountability for a mild", "dose of certainty and optionality."], 170),
    (1, 1, C["action_p"], "Cost plus",
     ["The consulting contractor", "Cost-plus Design-Build"],
     ["You trade cost certainty", "for optionality."], 170),
]

o = []
o.append(f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>')
o.append('<defs>'
         f'<clipPath id="win"><rect x="{X0}" y="{Y0}" width="{2*QW}" height="{2*QH}" rx="10"/></clipPath>'
         f'<marker id="ah-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C["acc"]}"/></marker>'
         '</defs>')
o.append(t(80, 86, "CHAPTER 3 · CHOOSING A DELIVERY METHOD", "eyebrow"))
o.append(t(80, 148, "Who works for whom, and how they deal", "title"))
o.append(t(80, 190, "Two questions place every way to build: does the other party work for itself or for you,", "dek"))
o.append(t(80, 218, "and do you get there by competing or by cooperating?", "dek"))

# glass: a jittered grid snapped to the cross, each cell coloured by its pane
cols, rows = 16, 10
gx = [X0 - 30 + i * (2 * QW + 60) / cols for i in range(cols + 1)]
gy = [Y0 - 30 + j * (2 * QH + 60) / rows for j in range(rows + 1)]
pts = {}
for i in range(cols + 1):
    for j in range(rows + 1):
        jx = 0 if i in (0, cols) else random.uniform(-26, 26)
        jy = 0 if j in (0, rows) else random.uniform(-22, 22)
        x, y = gx[i] + jx, gy[j] + jy
        if abs(gx[i] - XM) < 45: x = XM
        if abs(gy[j] - YM) < 45: y = YM
        pts[i, j] = (x, y)
g = ['<g clip-path="url(#win)">']
for i in range(cols):
    for j in range(rows):
        quad = [pts[i, j], pts[i + 1, j], pts[i + 1, j + 1], pts[i, j + 1]]
        cx = sum(p[0] for p in quad) / 4; cy = sum(p[1] for p in quad) / 4
        col = mix(random.choice(QUAD[(cx < XM, cy < YM)]), "#ffffff", random.uniform(0, .18))
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in quad) + " Z"
        g.append(f'<path d="{d}" fill="{col}" stroke="{LEAD}" stroke-width="5" stroke-linejoin="round"/>')
g.append(f'<line x1="{XM}" y1="{Y0-20}" x2="{XM}" y2="{Y1+20}" stroke="{LEAD}" stroke-width="16"/>'
         f'<line x1="{X0-20}" y1="{YM}" x2="{X1+20}" y2="{YM}" stroke="{LEAD}" stroke-width="16"/>')
g.append('</g>')
o += g
o.append(f'<rect x="{X0}" y="{Y0}" width="{2*QW}" height="{2*QH}" rx="10" fill="none" stroke="{LEAD}" stroke-width="22"/>')
o.append(f'<rect x="{X0}" y="{Y0}" width="{2*QW}" height="{2*QH}" rx="10" fill="none" stroke="#8a8780" stroke-width="4"/>')

# pale glass label panels, kept clear of the centre light
PW, PH = 470, 200
for col, row, accent, name, ex, trade, top in QUADS:
    x, y = X0 + col * QW, Y0 + row * QH
    px = x + 34 if col == 0 else x + QW - 34 - PW
    py = y + top
    o.append(f'<rect x="{px}" y="{py}" width="{PW}" height="{PH}" rx="10" fill="{PALE}" stroke="{LEAD}" stroke-width="5"/>')
    yy = py + 50
    o.append(t(px + 28, yy, name, "name", accent))
    yy += 38
    for ln in ex:
        o.append(t(px + 28, yy, ln, "ex", LEAD)); yy += 27
    yy += 10
    for ln in trade:
        o.append(t(px + 28, yy, ln, "trade", C["ink2"])); yy += 27

# axis labels
o.append(t(X0 - 30, Y0 + QH/2 - 10, "PRINCIPAL TO", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, Y0 + QH/2 + 10, "PRINCIPAL", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, Y0 + QH/2 + 34, "works for itself", "axis-s", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 - 10, "PRINCIPAL TO", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 + 10, "AGENT", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 + 34, "works for you", "axis-s", C["ink2"], "end"))
o.append(t(X0 + QW/2, Y1 + 50, "COMPETITIVE", "axis", C["ink2"], "middle"))
o.append(t(XM + QW/2, Y1 + 50, "COOPERATIVE", "axis", C["ink2"], "middle"))

# the diagonal
o.append(t(X0 - 24, Y0 - 30, "↖ CHEAP AND STRESSFUL", "tag", C["acc_d"]))
o.append(t(X1 + 6, Y1 + 84, "PEACEFUL AND EXPENSIVE ↘", "tag", C["action_p"], "end"))

# the General Contractor with a Consultant: the centre light on the cross
CW, CH = 480, 270
cx, cy = XM - CW/2, YM - CH/2
o.append(f'<rect x="{cx-14}" y="{cy-14}" width="{CW+28}" height="{CH+28}" rx="22" fill="{mix(C["action"], "#ffffff", .8)}" stroke="{LEAD}" stroke-width="6"/>')
for k in range(4):  # corner jewels in the four pane colours
    jx = cx - 14 if k % 2 == 0 else cx + CW + 14
    jy = cy - 14 if k < 2 else cy + CH + 14
    jc = [C["acc"], C["sec"], C["ink2"], C["action"]][k]
    o.append(f'<circle cx="{jx}" cy="{jy}" r="17" fill="{jc}" stroke="{LEAD}" stroke-width="6"/>')
o.append(f'<rect x="{cx}" y="{cy}" width="{CW}" height="{CH}" rx="14" fill="#ffffff" stroke="{LEAD}" stroke-width="8"/>')
o.append(f'<rect x="{cx+12}" y="{cy+12}" width="{CW-24}" height="{CH-24}" rx="8" fill="none" stroke="{LEAD}" stroke-width="2"/>')
o.append(t(XM, cy + 62, "General Contractor", "cbig", LEAD, "middle"))
o.append(t(XM, cy + 96, "with a Consultant", "cname", LEAD, "middle"))
o.append(t(XM, cy + 134, "Design with an agent, build with a principal", "ex", LEAD, "middle"))
o.append(t(XM, cy + 176, "The synthesis: optionality where", "ctrade", C["action_p"], "middle"))
o.append(t(XM, cy + 204, "it has the most leverage, competition", "ctrade", C["action_p"], "middle"))
o.append(t(XM, cy + 232, "for the rest.", "ctrade", C["action_p"], "middle"))

# the velocity drift
ay = Y0 - 26
o.append(f'<line x1="{XM + QW - 60}" y1="{ay}" x2="{X0 + QW - 60}" y2="{ay}" stroke="{C["acc"]}" stroke-width="3" stroke-dasharray="9 7" marker-end="url(#ah-a)"/>')
o.append(t(XM - 40, ay - 14, "Profits = Margin × Velocity: velocity fades, and the Principal returns to the hungry parties", "drift", C["acc_d"], "middle"))

o.append(t(80, H - 76, "Off the grid: self-performance, where the Principal and the Agent are one person.", "foot"))
o.append(t(80, H - 48, "Design-Build lands in two squares: a lump sum keeps it Principal to Principal; cost plus makes it Principal to Agent.", "foot"))
o.append(t(80, H - 20, "The diagonal runs from cheap and stressful to peaceful and expensive; the centre square balances both axes.", "foot"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:42px}}
  .cbig{{font-family:'Instrument Serif',Georgia,serif;font-size:44px}}
  .ex{{font-family:Outfit,sans-serif;font-weight:500;font-size:20px}}
  .trade{{font-family:Lora,Georgia,serif;font-style:italic;font-size:20px}}
  .ctrade{{font-family:Lora,Georgia,serif;font-style:italic;font-weight:500;font-size:21px}}
  .axis{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px;letter-spacing:.14em}}
  .axis-s{{font-family:Lora,Georgia,serif;font-style:italic;font-size:18px}}
  .tag{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px;letter-spacing:.14em}}
  .cname{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:28px}}
  .drift{{font-family:Outfit,sans-serif;font-weight:500;font-size:17px}}
  .foot{{font-family:Outfit,sans-serif;font-size:17px;fill:#5f5e5a}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "delivery-methods-glass"
open(out + ".svg", "w").write(svg)
open(out + ".html", "w").write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>""")
