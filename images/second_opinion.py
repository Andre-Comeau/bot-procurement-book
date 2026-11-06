"""Chapter 9 figure: the estimator and the evaluator either side of tender day.

    python images/second_opinion.py images/second-opinion
    node images/project_hex_map_render.js "$PWD/images/second-opinion.html" images/second-opinion.png 1600 900
"""
import sys

C = dict(action="#0064ff", action_p="#004fcc", sec="#0f6e56", sec_d="#085041",
         acc="#d85a30", acc_d="#9e3d18", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
W, H = 1600, 900


def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}"{f} text-anchor="{anchor}">{s}</text>'


o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append(t(80, 78, "CHAPTER 9", "eyebrow"))
o.append(t(80, 136, "A second opinion on every price", "title"))
o.append(t(80, 176, "One engine, pointed either side of tender day.", "dek"))

# the three columns
PY, PH = 300, 400
LX, RX, PW = 80, 1000, 520
MX, MW = 640, 320

def panel(x, col, eyebrow, name, q, lines):
    o.append(f'<rect x="{x}" y="{PY}" width="{PW}" height="{PH}" rx="18" fill="{col}"/>')
    o.append(t(x + 40, PY + 56, eyebrow, "tag", "#ffffff"))
    o.append(t(x + 40, PY + 116, name, "name", "#ffffff"))
    o.append(t(x + 40, PY + 166, q, "q", "#ffffff"))
    yy = PY + 236
    for ln in lines:
        o.append(t(x + 40, yy, ln, "ex", "#ffffff")); yy += 38

panel(LX, C["action"], "BEFORE THE TENDER", "The Estimator", "“How much should this cost?”",
      ["Prices every line from past bids", "Learns from what the market paid",
       "Error rate known on unseen contracts", "Within about 10% at the total"])
panel(RX, C["sec"], "AFTER AWARD", "The Evaluator", "“Are we paying too much?”",
      ["Prices a change in minutes, not days", "Cites the past tenders behind each price",
       "Flags rare items, never prices them silently", "A named keyholder decides and signs"])

# tender day in the middle
cx = MX + MW / 2
o.append(f'<rect x="{MX}" y="{PY}" width="{MW}" height="{PH}" rx="18" fill="#ffffff" stroke="{C["hair"]}" stroke-width="2"/>')
o.append(t(cx, PY + 56, "TENDER DAY", "tag", C["ink2"], "middle"))
for i, dx in enumerate((-70, 0, 70)):
    ex, ey = cx + dx - 42, PY + 110 + (i % 2) * 14
    o.append(f'<rect x="{ex}" y="{ey}" width="84" height="58" rx="4" fill="#ffffff" stroke="{C["ink"]}" stroke-width="2.5"/>')
    o.append(f'<path d="M{ex} {ey} L{ex+42} {ey+32} L{ex+84} {ey}" fill="none" stroke="{C["ink"]}" stroke-width="2.5"/>')
o.append(t(cx, PY + 236, "The envelopes open:", "mid", C["ink"], "middle"))
o.append(t(cx, PY + 266, "for one afternoon, the", "mid", C["ink"], "middle"))
o.append(t(cx, PY + 296, "market is in the room.", "mid", C["ink"], "middle"))
o.append(t(cx, PY + 350, "After award, every change", "mids", C["ink2"], "middle"))
o.append(t(cx, PY + 376, "is bought from a supplier of one.", "mids", C["ink2"], "middle"))

o.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>')
# top arc: yardstick, estimator -> evaluator
o.append(f'<path d="M{LX+PW-80} {PY-6} C {LX+PW+120} {PY-70}, {RX-120} {PY-70}, {RX+80} {PY-6}" fill="none" stroke="{C["action"]}" stroke-width="3" marker-end="url(#ah)"/>')
o.append(t(W / 2, PY - 56, "Its price and error rate become the evaluator’s yardstick", "route", C["action_p"], "middle"))
# bottom arc: evidence, evaluator -> estimator
yb = PY + PH
o.append(f'<path d="M{RX+80} {yb+6} C {RX-120} {yb+70}, {LX+PW+120} {yb+70}, {LX+PW-80} {yb+6}" fill="none" stroke="{C["acc"]}" stroke-width="3" stroke-dasharray="9 7" marker-end="url(#ah)"/>')
o.append(t(W / 2, yb + 78, "Every checked price becomes evidence for the next estimate", "route", C["acc_d"], "middle"))

o.append(t(80, H - 40, "A slow review on every change raises the overhead, and a motivated contractor can always find something to claim against. The evaluator’s savings come after the tender.", "foot"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}}
  .tag{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px;letter-spacing:.14em}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:46px}}
  .q{{font-family:Lora,Georgia,serif;font-style:italic;font-weight:500;font-size:24px}}
  .ex{{font-family:Outfit,sans-serif;font-weight:500;font-size:21px}}
  .mid{{font-family:'Instrument Serif',Georgia,serif;font-size:26px}}
  .mids{{font-family:Lora,Georgia,serif;font-style:italic;font-size:17px}}
  .route{{font-family:'Instrument Serif',Georgia,serif;font-size:25px;paint-order:stroke;stroke:#f9f8f5;stroke-width:8px;stroke-linejoin:round}}
  .foot{{font-family:Outfit,sans-serif;font-size:16px;fill:#5f5e5a}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "second-opinion"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
