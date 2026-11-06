"""Chapter 9 figure: the quest map from the estimator to the end-boss.

The estimator before the tender, tender day (the one afternoon the buyer sees the
market price), then a fork after award: the slow road of long reviews, where a
contractor finds its motivation to claim, or the evaluator's bridge. The road
ends at the end-boss, the standard, with robotic construction in the fog beyond.

    python images/second_opinion.py images/second-opinion
    node images/project_hex_map_render.js "$PWD/images/second-opinion.html" images/second-opinion.png 1800 1080
"""
import sys

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a", road="#e9e4d8", road_e="#d6cfbd")
W, H = 1800, 1080


def t(x, y, s, cls, fill=None, anchor="start", extra=""):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}"{f} text-anchor="{anchor}"{extra}>{s}</text>'


def lines(x, y, rows, cls, fill=None, anchor="start", step=26):
    return [t(x, y + i * step, r, cls, fill, anchor) for i, r in enumerate(rows)]


o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>',
     '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
     '<path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker>'
     '<radialGradient id="glow"><stop offset="0" stop-color="#ffd27a" stop-opacity=".9"/>'
     '<stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>'
     '<linearGradient id="fog" x1="0" x2="1"><stop offset="0" stop-color="#f9f8f5" stop-opacity="0"/>'
     '<stop offset=".45" stop-color="#f9f8f5" stop-opacity=".55"/><stop offset="1" stop-color="#f9f8f5" stop-opacity=".9"/></linearGradient></defs>']

o.append(t(80, 78, "CHAPTER 9", "eyebrow"))
o.append(t(80, 136, "A second opinion on every price", "title"))
o.append(t(80, 176, "The road from the first estimate to the end-boss.", "dek"))

# hills and ground
o.append(f'<path d="M0 700 C 300 660, 520 690, 760 680 S 1180 650, 1300 560 S 1500 520, 1800 600 L1800 {H} L0 {H} Z" fill="{C["sec_t"]}"/>')
o.append(f'<path d="M1180 640 C 1260 520, 1380 470, 1480 520 C 1540 550, 1560 600, 1620 640 Z" fill="#cfe9dd"/>')

# the main road: estimator -> hall -> fork
GY = 700
o.append(f'<path d="M60 {GY} C 200 {GY-10}, 330 {GY+8}, 470 {GY} S 700 {GY-6}, 780 {GY}" fill="none" stroke="{C["road_e"]}" stroke-width="40" stroke-linecap="round"/>')
o.append(f'<path d="M60 {GY} C 200 {GY-10}, 330 {GY+8}, 470 {GY} S 700 {GY-6}, 780 {GY}" fill="none" stroke="{C["road"]}" stroke-width="32" stroke-linecap="round"/>')
# the slow road dips into the swamp
slow = f"M780 {GY} C 860 {GY+40}, 900 {GY+170}, 1000 {GY+175} S 1150 {GY+140}, 1220 {GY-60} S 1330 560, 1390 548"
o.append(f'<path d="{slow}" fill="none" stroke="{C["road_e"]}" stroke-width="40" stroke-linecap="round"/>')
o.append(f'<path d="{slow}" fill="none" stroke="{C["road"]}" stroke-width="32" stroke-linecap="round"/>')
o.append(f'<path d="{slow}" fill="none" stroke="{C["acc"]}" stroke-width="3" stroke-dasharray="2 14" stroke-linecap="round"/>')
# swamp
o.append(f'<ellipse cx="1000" cy="{GY+190}" rx="190" ry="44" fill="{C["acc_t"]}"/>')
for x, y in ((880, GY + 192), (1110, GY + 200), (960, GY + 214), (1050, GY + 176)):   # thorns: claims
    o.append(f'<path d="M{x-14} {y} L{x-6} {y-24} L{x} {y-6} L{x+7} {y-30} L{x+14} {y}" fill="{C["acc"]}"/>')

# the evaluator's bridge over the swamp
o.append(f'<path d="M780 {GY-4} C 900 {GY-210}, 1150 {GY-230}, 1300 572" fill="none" stroke="{C["sec_d"]}" stroke-width="34" stroke-linecap="round"/>')
o.append(f'<path d="M780 {GY-4} C 900 {GY-210}, 1150 {GY-230}, 1300 572" fill="none" stroke="{C["sec"]}" stroke-width="24" stroke-linecap="round"/>')
for i in range(1, 9):   # bridge posts
    s = i / 9
    bx = (1 - s) ** 3 * 780 + 3 * (1 - s) ** 2 * s * 900 + 3 * (1 - s) * s * s * 1150 + s ** 3 * 1300
    by = (1 - s) ** 3 * (GY - 4) + 3 * (1 - s) ** 2 * s * (GY - 210) + 3 * (1 - s) * s * s * (GY - 230) + s ** 3 * 572
    o.append(f'<line x1="{bx:.0f}" y1="{by+12:.0f}" x2="{bx:.0f}" y2="{by+44:.0f}" stroke="{C["sec_d"]}" stroke-width="5"/>')

# 1. the estimator: a signpost
sx = 200
o.append(f'<line x1="{sx+20}" y1="{GY-20}" x2="{sx+20}" y2="{GY-140}" stroke="{C["ink"]}" stroke-width="6"/>')
o.append(f'<rect x="{sx-100}" y="{GY-330}" width="290" height="196" rx="16" fill="{C["action"]}"/>')
o += lines(sx - 74, GY - 290, ["1 · BEFORE THE TENDER"], "tag", "#ffffff")
o.append(t(sx - 74, GY - 238, "The Estimator", "name", "#ffffff"))
o += lines(sx - 74, GY - 198, ["“How much should", "this cost?”"], "q", "#ffffff", step=28)

# 2. tender day: the hall, lit for one afternoon
hx, hy = 480, GY - 30
o.append(f'<circle cx="{hx+120}" cy="{hy-130}" r="210" fill="url(#glow)"/>')
o.append(f'<rect x="{hx}" y="{hy-200}" width="240" height="200" fill="{C["surface"]}" stroke="{C["ink"]}" stroke-width="3"/>')
o.append(f'<path d="M{hx-20} {hy-196} L{hx+120} {hy-290} L{hx+260} {hy-196} Z" fill="{C["ink"]}"/>')
o.append(t(hx + 120, hy - 222, "TENDER HALL", "sign", "#ffffff", "middle"))
for i, dx in enumerate((22, 88, 154)):   # three opened envelopes
    ex, ey = hx + dx, hy - 168 + (i % 2) * 10
    o.append(f'<rect x="{ex}" y="{ey}" width="64" height="44" rx="3" fill="#fff8e6" stroke="{C["ink"]}" stroke-width="2.2"/>')
    o.append(f'<path d="M{ex} {ey} L{ex+32} {ey-22} L{ex+64} {ey}" fill="#fff8e6" stroke="{C["ink"]}" stroke-width="2.2"/>')
    o.append(f'<line x1="{ex+12}" y1="{ey+18}" x2="{ex+52}" y2="{ey+18}" stroke="{C["ink2"]}" stroke-width="2"/>')
    o.append(f'<line x1="{ex+12}" y1="{ey+28}" x2="{ex+40}" y2="{ey+28}" stroke="{C["ink2"]}" stroke-width="2"/>')
o.append(f'<rect x="{hx+96}" y="{hy-82}" width="48" height="82" rx="24" fill="{C["ink"]}"/>')
o += lines(hx + 120, GY + 62, ["2 · TENDER DAY"], "tag", C["ink"], "middle")
o += lines(hx + 120, GY + 96, ["The envelopes open. For one", "afternoon, the buyer knows", "the market price."], "cap", C["ink"], "middle", step=27)

# 3a. the evaluator's bridge label
o.append(f'<rect x="850" y="292" width="360" height="142" rx="16" fill="{C["sec"]}"/>')
o += lines(878, 330, ["3 · AFTER AWARD"], "tag", "#ffffff")
o.append(t(878, 378, "The Evaluator", "name", "#ffffff"))
o.append(t(878, 414, "A second opinion in minutes", "q2", "#ffffff"))

# 3b. the slow road: clock, overhead meter, motivation
cx, cy = 760, GY + 190     # clock
o.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="{C["surface"]}" stroke="{C["acc_d"]}" stroke-width="4"/>')
o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-22}" stroke="{C["acc_d"]}" stroke-width="4" stroke-linecap="round"/>')
o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+16}" y2="{cy+8}" stroke="{C["acc_d"]}" stroke-width="4" stroke-linecap="round"/>')
o.append(t(cx, cy + 62, "10 working days", "small", C["acc_d"], "middle"))
o.append(t(cx, cy + 84, "(a service standard)", "smalli", C["acc_d"], "middle"))
mx, my = 1240, GY + 120    # the overhead meter, climbing
o.append(t(mx, my - 4, "OVERHEAD", "tag2", C["acc_d"]))
for i in range(6):
    h = 14 + i * 12
    o.append(f'<rect x="{mx + i*22}" y="{my + 80 - h}" width="15" height="{h}" rx="3" fill="{C["acc"]}" opacity="{0.4 + i*0.12:.2f}"/>')
o += lines(1000, GY + 268, ["THE SLOW ROAD"], "tag", C["acc_d"], "middle")
o += lines(1000, GY + 300, ["Slow every change and the overhead climbs. A contractor who would",
                            "have left happy with its margin finds its motivation, and something to claim."],
           "cap", C["acc_d"], "middle", step=27)

# 4. the end-boss: the standard's castle on the hill
kx, ky = 1330, 548
def castle(x, y, s, fill, op=1):
    p = []
    p.append(f'<g opacity="{op}">')
    p.append(f'<rect x="{x}" y="{y - 120*s}" width="{200*s}" height="{120*s}" fill="{fill}"/>')
    for tx in (x - 20*s, x + 160*s):
        p.append(f'<rect x="{tx}" y="{y - 190*s}" width="{60*s}" height="{190*s}" fill="{fill}"/>')
        for k in range(3):
            p.append(f'<rect x="{tx + k*22*s}" y="{y - 206*s}" width="{16*s}" height="{18*s}" fill="{fill}"/>')
    p.append(f'<rect x="{x + 60*s}" y="{y - 170*s}" width="{80*s}" height="{60*s}" fill="{fill}"/>')
    for k in range(4):
        p.append(f'<rect x="{x + 60*s + k*22*s}" y="{y - 186*s}" width="{14*s}" height="{18*s}" fill="{fill}"/>')
    p.append(f'<path d="M{x + 76*s} {y} L{x + 76*s} {y - 44*s} Q{x + 100*s} {y - 70*s} {x + 124*s} {y - 44*s} L{x + 124*s} {y} Z" fill="{C["canvas"]}"/>')
    p.append(f'<line x1="{x + 100*s}" y1="{y - 186*s}" x2="{x + 100*s}" y2="{y - 250*s}" stroke="{fill}" stroke-width="{4*s}"/>')
    p.append(f'<path d="M{x + 100*s} {y - 250*s} L{x + 146*s} {y - 236*s} L{x + 100*s} {y - 222*s} Z" fill="{C["acc"]}"/>')
    p.append('</g>')
    return p
o += castle(kx, ky, 1.0, C["ink"])
o += lines(kx + 100, 236, ["4 · THE END-BOSS"], "tag", C["ink"], "middle")
o.append(t(kx + 100, 274, "The Standard", "name2", C["ink"], "middle"))

# beyond: robotic construction in the fog
o += castle(1620, 600, 0.55, C["ink2"], 0.45)
o.append(f'<rect x="1540" y="380" width="260" height="300" fill="url(#fog)"/>')
o += lines(1676, 642, ["Robotic", "construction"], "smalli2", C["ink2"], "middle", step=24)

# the flywheel: checked prices feed the next estimate
o.append(f'<path d="M940 286 C 820 220, 480 210, 300 360" fill="none" stroke="{C["acc"]}" stroke-width="3" stroke-dasharray="9 7" marker-end="url(#ah)"/>')
o.append(t(620, 228, "Every checked price becomes evidence for the next estimate", "route", C["acc_d"], "middle"))

o += lines(1780, 740, ["The treasure is in another castle,", "but this is the path there."], "foot", None, "end", step=32)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}}
  .tag{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.14em}}
  .tag2{{font-family:Outfit,sans-serif;font-weight:600;font-size:13px;letter-spacing:.14em}}
  .sign{{font-family:Outfit,sans-serif;font-weight:600;font-size:14px;letter-spacing:.18em}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:40px}}
  .name2{{font-family:'Instrument Serif',Georgia,serif;font-size:36px}}
  .q{{font-family:Lora,Georgia,serif;font-style:italic;font-weight:500;font-size:21px}}
  .q2{{font-family:Lora,Georgia,serif;font-style:italic;font-weight:500;font-size:20px}}
  .cap{{font-family:Lora,Georgia,serif;font-size:19px}}
  .small{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px}}
  .smalli{{font-family:Lora,Georgia,serif;font-style:italic;font-size:15px}}
  .smalli2{{font-family:Lora,Georgia,serif;font-style:italic;font-size:19px}}
  .route{{font-family:'Instrument Serif',Georgia,serif;font-size:24px;paint-order:stroke;stroke:#f9f8f5;stroke-width:8px;stroke-linejoin:round}}
  .foot{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-size:26px;fill:#2c2c2a}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "second-opinion"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
