"""Draw the delivery-method 2x2 for chapter 3 (PI brand kit colours, no PI marks).

Usage: python images/delivery_methods_2x2.py images/delivery-methods-2x2
Writes the .svg and an .html; render the PNG with
node images/project_hex_map_render.js "$PWD/images/delivery-methods-2x2.html" images/delivery-methods-2x2.png 1600 1200
"""
import sys, html

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")

W, H = 1600, 1200
X0, Y0, QW, QH = 250, 300, 620, 380          # grid origin and quadrant size
XM, YM = X0 + QW, Y0 + QH                    # the axes cross here

# (col, row, fill, stroke, label colour, name, examples, trade lines, text top offset)
QUADS = [
    (0, 0, C["acc_t"], C["acc"], C["acc_d"], "Hard bid",
     ["The General Contractor's tender", "Lump-sum Design-Build"],
     ["You trade trust in the counterparty", "for rock-bottom pricing."], 44),
    (1, 0, C["sec_t"], C["sec"], C["sec_d"], "Partnership",
     ["Principals entangled in a common interest"],
     ["You trade a higher share of the benefits", "for significantly less management effort."], 44),
    (0, 1, C["muted"], C["ink2"], C["ink2"], "Construction Manager",
     ["Two agents, designer and builder,", "acting as checks on each other"],
     ["You trade accountability for a mild", "dose of certainty and optionality."], 150),
    (1, 1, C["action_t"], C["action"], C["action_p"], "Cost plus",
     ["The design consultant", "Cost-plus Design-Build"],
     ["You trade cost certainty", "for optionality."], 150),
]

def t(x, y, s, cls, fill=None, anchor="start", extra=""):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}{extra}>{html.escape(s)}</text>'

o = []
o.append(f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>')
o.append('<defs>'
         f'<marker id="ah-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C["acc"]}"/></marker>'
         f'<marker id="ah-i" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink"]}"/></marker>'
         '</defs>')
o.append(t(80, 86, "CHAPTER 3 · CHOOSING A DELIVERY METHOD", "eyebrow"))
o.append(t(80, 148, "Who works for whom, and how they deal", "title"))
o.append(t(80, 190, "Two questions place every way to build: does the other party work for itself or for you,", "dek"))
o.append(t(80, 218, "and do you get there by competing or by cooperating?", "dek"))

for col, row, fill, stroke, lab, name, ex, trade, top in QUADS:
    x, y = X0 + col * QW, Y0 + row * QH
    o.append(f'<rect x="{x+6}" y="{y+6}" width="{QW-12}" height="{QH-12}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    yy = y + top
    o.append(t(x + 40, yy + 30, name, "name", C["ink"]))
    yy += 70
    for ln in ex:
        o.append(t(x + 40, yy, ln, "ex", lab)); yy += 26
    yy += 14
    for ln in trade:
        o.append(t(x + 40, yy, ln, "trade", C["ink"])); yy += 26

# axis labels
o.append(t(X0 - 30, Y0 + QH/2 - 10, "PRINCIPAL TO", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, Y0 + QH/2 + 10, "PRINCIPAL", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, Y0 + QH/2 + 34, "works for itself", "axis-s", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 - 10, "PRINCIPAL TO", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 + 10, "AGENT", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 + 34, "works for you", "axis-s", C["ink2"], "end"))
o.append(t(X0 + QW/2, Y0 + 2*QH + 40, "COMPETITIVE", "axis", C["ink2"], "middle"))
o.append(t(XM + QW/2, Y0 + 2*QH + 40, "COOPERATIVE", "axis", C["ink2"], "middle"))

# the General Contractor route: design as agent (cost plus), then build by tender (hard bid)
sx, sy, ex_, ey = XM + 150, YM + 110, XM - 150, YM - 110
o.append(f'<path d="M{sx},{sy} C{XM+40},{YM+10} {XM-40},{YM-10} {ex_},{ey}" fill="none" stroke="{C["canvas"]}" stroke-width="10"/>')
o.append(f'<path d="M{sx},{sy} C{XM+40},{YM+10} {XM-40},{YM-10} {ex_},{ey}" fill="none" stroke="{C["ink"]}" stroke-width="3" marker-end="url(#ah-i)"/>')
o.append(f'<circle cx="{sx}" cy="{sy}" r="6" fill="{C["ink"]}"/>')
o.append(t(XM + 22, YM - 78, "General Contractor", "route", C["ink"]))
o.append(t(XM + 22, YM - 56, "design as an agent,", "route-s", C["ink2"]))
o.append(t(XM + 22, YM - 36, "then build by tender", "route-s", C["ink2"]))

# the velocity drift: cooperation decays back to competition
ay = Y0 - 22
o.append(f'<line x1="{XM + QW - 60}" y1="{ay}" x2="{X0 + QW - 60}" y2="{ay}" stroke="{C["acc"]}" stroke-width="3" stroke-dasharray="9 7" marker-end="url(#ah-a)"/>')
o.append(t(XM - 40, ay - 14, "Profits = Margin × Velocity: velocity fades, and the Principal returns to the hungry parties", "drift", C["acc_d"], "middle"))

# self-performance sits outside the grid
o.append(t(80, H - 70, "Off the grid: self-performance, where the Principal and the Agent are one person.", "foot"))
o.append(t(80, H - 44, "Design-Build lands in two squares: a lump sum keeps it Principal to Principal; cost plus makes it Principal to Agent.", "foot"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:36px}}
  .ex{{font-family:Outfit,sans-serif;font-size:17px}}
  .trade{{font-family:Lora,Georgia,serif;font-style:italic;font-size:19px}}
  .axis{{font-family:Outfit,sans-serif;font-weight:600;font-size:14px;letter-spacing:.14em}}
  .axis-s{{font-family:Lora,Georgia,serif;font-style:italic;font-size:16px}}
  .route{{font-family:'Instrument Serif',Georgia,serif;font-size:24px;paint-order:stroke;stroke:#f9f8f5;stroke-width:6px;stroke-linejoin:round}}
  .route-s{{font-family:Outfit,sans-serif;font-size:14px;paint-order:stroke;stroke:#f9f8f5;stroke-width:6px;stroke-linejoin:round}}
  .drift{{font-family:Outfit,sans-serif;font-weight:500;font-size:14px}}
  .foot{{font-family:Outfit,sans-serif;font-size:14px;fill:#5f5e5a}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "delivery-methods-2x2"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
