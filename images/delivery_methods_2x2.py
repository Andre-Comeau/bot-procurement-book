"""Draw the delivery-method 2x2 for chapter 2 (PI brand kit colours, no PI marks).

Usage: python images/delivery_methods_2x2.py images/delivery-methods-2x2
Writes the .svg and an .html; render the PNG with
node images/project_hex_map_render.js "$PWD/images/delivery-methods-2x2.html" images/delivery-methods-2x2.png 1600 1300
"""
import sys, html

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")

W, H = 1600, 1300
X0, Y0, QW, QH = 250, 300, 620, 400          # grid origin and quadrant size
XM, YM = X0 + QW, Y0 + QH                    # the axes cross here

# Pane fills darkened toward the lead colour of the stained-glass figures
# (failure_modes_glass.py, second_opinion.py) so the book's figures share one tone.
def _mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
DARK = 0.2
D = {k: _mix(C[k], C["ink"], DARK) for k in ("acc", "sec", "ink2", "action")}

# (col, row, fill, stroke, label colour, name, examples, trade lines, text top offset)
QUADS = [
    (0, 0, D["acc"], C["acc_d"], C["acc_t"], "Hard bid",
     ["The lump sum, whoever draws:", "Design-Bid-Build or Design-Build"],
     ["You trade trust in the counterparty", "for rock-bottom pricing."], 44),
    (1, 0, D["sec"], C["sec_d"], C["sec_t"], "Partnership",
     ["Principals entangled in a common interest"],
     ["You trade a higher share of the benefits", "for significantly less management effort."], 44),
    (0, 1, D["ink2"], C["ink"], C["muted"], "Construction Manager",
     ["Two agents, designer and builder,", "acting as checks on each other"],
     ["You trade accountability for a mild", "dose of certainty and optionality."], 180),
    (1, 1, D["action"], C["action_p"], C["action_t"], "Cost plus",
     ["The consulting contractor", "Progressive Design-Build"],
     ["You trade cost certainty", "for optionality."], 180),
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
o.append(t(80, 86, "CHAPTER 2 · CHOOSING A DELIVERY METHOD", "eyebrow"))
o.append(t(80, 148, "Who works for whom, and how they deal", "title"))
o.append(t(80, 190, "Two questions place every way to build: does the other party work for itself or for you,", "dek"))
o.append(t(80, 218, "and do you get there by competing or by cooperating?", "dek"))

for col, row, fill, stroke, lab, name, ex, trade, top in QUADS:
    x, y = X0 + col * QW, Y0 + row * QH
    o.append(f'<rect x="{x+6}" y="{y+6}" width="{QW-12}" height="{QH-12}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
    yy = y + top
    o.append(t(x + 40, yy + 30, name, "name", "#ffffff"))
    yy += 70
    for ln in ex:
        o.append(t(x + 40, yy, ln, "ex", lab)); yy += 30
    yy += 14
    for ln in trade:
        o.append(t(x + 40, yy, ln, "trade", "#ffffff")); yy += 30

# axis labels
o.append(t(X0 - 30, Y0 + QH/2 - 10, "PRINCIPAL TO", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, Y0 + QH/2 + 10, "PRINCIPAL", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, Y0 + QH/2 + 34, "works for itself", "axis-s", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 - 10, "PRINCIPAL TO", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 + 10, "AGENT", "axis", C["ink2"], "end"))
o.append(t(X0 - 30, YM + QH/2 + 34, "works for you", "axis-s", C["ink2"], "end"))
o.append(t(X0 + QW/2, Y0 + 2*QH + 40, "COMPETITIVE", "axis", C["ink2"], "middle"))
o.append(t(XM + QW/2, Y0 + 2*QH + 40, "COOPERATIVE", "axis", C["ink2"], "middle"))

# the diagonal: cheap and stressful (top left) to peaceful and expensive (bottom right)
o.append(t(X0 - 24, Y0 - 26, "↖ CHEAP AND STRESSFUL", "tag", C["acc_d"]))
o.append(t(X0 + 2*QW + 6, Y0 + 2*QH + 74, "PEACEFUL AND EXPENSIVE ↘", "tag", C["action_p"], "end"))

# the General Contractor with a Consultant balances both axes, so it sits on the cross
CW, CH = 480, 270
cx, cy = XM - CW/2, YM - CH/2
o.append(f'<rect x="{cx-8}" y="{cy-8}" width="{CW+16}" height="{CH+16}" rx="18" fill="{C["canvas"]}"/>')
o.append(f'<rect x="{cx}" y="{cy}" width="{CW}" height="{CH}" rx="14" fill="{C["surface"]}" stroke="{C["ink"]}" stroke-width="2"/>')
o.append(t(XM, cy + 56, "General Contractor", "name", C["ink"], "middle"))
o.append(t(XM, cy + 90, "with a Consultant", "cname", C["ink"], "middle"))
o.append(t(XM, cy + 128, "Design with an agent, build with a principal", "ex", C["ink2"], "middle"))
o.append(t(XM, cy + 172, "The synthesis: optionality where", "trade", C["ink"], "middle"))
o.append(t(XM, cy + 202, "it has the most leverage, competition", "trade", C["ink"], "middle"))
o.append(t(XM, cy + 232, "for the rest.", "trade", C["ink"], "middle"))

# the velocity drift: cooperation decays back to competition
ay = Y0 - 22
o.append(f'<line x1="{XM + QW - 60}" y1="{ay}" x2="{X0 + QW - 60}" y2="{ay}" stroke="{C["acc"]}" stroke-width="3" stroke-dasharray="9 7" marker-end="url(#ah-a)"/>')
o.append(t(XM - 40, ay - 14, "Profits = Margin × Velocity: velocity fades, and the Principal returns to the hungry parties", "drift", C["acc_d"], "middle"))

# self-performance sits outside the grid
o.append(t(80, H - 76, "Off the grid: self-performance, where the Principal and the Agent are one person.", "foot"))
o.append(t(80, H - 20, "The diagonal runs from cheap and stressful to peaceful and expensive; the centre square balances both axes.", "foot"))
o.append(t(80, H - 48, "Design-Build lands in two squares: a lump sum puts it beside Design-Bid-Build; progressive Design-Build agrees its price as the design grows.", "foot"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:42px}}
  .ex{{font-family:Outfit,sans-serif;font-weight:500;font-size:21px}}
  .trade{{font-family:Lora,Georgia,serif;font-style:italic;font-weight:500;font-size:22px}}
  .axis{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px;letter-spacing:.14em}}
  .axis-s{{font-family:Lora,Georgia,serif;font-style:italic;font-size:18px}}
  .tag{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px;letter-spacing:.14em}}
  .cname{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:28px}}
  .route{{font-family:'Instrument Serif',Georgia,serif;font-size:24px;paint-order:stroke;stroke:#f9f8f5;stroke-width:6px;stroke-linejoin:round}}
  .route-s{{font-family:Outfit,sans-serif;font-size:14px;paint-order:stroke;stroke:#f9f8f5;stroke-width:6px;stroke-linejoin:round}}
  .drift{{font-family:Outfit,sans-serif;font-weight:500;font-size:17px}}
  .foot{{font-family:Outfit,sans-serif;font-size:17px;fill:#5f5e5a}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "delivery-methods-2x2"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
