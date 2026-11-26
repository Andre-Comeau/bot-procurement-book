"""Checking the bid first: the chapter 3 figure (data from the project's insurance model).
Reads images/premium-with-checks-data.json (smoothed curves of the bids a typical bot sends in,
alone and checked against the range edge 15% below the standard).
Usage: python images/premium_with_checks.py images/premium-with-checks  (writes .svg and .html)
"""
import sys, json, html, os
C = dict(action="#0064ff", sec="#0f6e56", acc="#d85a30", acc_t="#f6d3c4", canvas="#f9f8f5",
         hair="#d6d3cc", ink="#2c2c2a", ink2="#5f5e5a")
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "premium-with-checks-data.json")))
W, H = 1600, 1240
X0, X1, LO, HI = 90, 1090, -0.25, 0.25
def px(v): return X0 + (v - LO) / (HI - LO) * (X1 - X0)
def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x:.0f}" y="{y:.0f}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'
YMAX = max(max(D["alone"]), max(D["checked"])) * 1.08
def one_in(p):
    n = 1 / p
    n = round(n, -2) if n >= 300 else round(n, -1)
    return f"1 in {n:,.0f}"
def panel(ytop, key, head, sub, big, dollars, lines):
    o = [t(X0, ytop, head, "lab", C["ink"]), t(X0, ytop + 34, sub, "dek")]
    base, hgt = ytop + 360, 280
    pts = [(px(x), base - y / YMAX * hgt) for x, y in zip(D["x"], D[key]) if LO <= x <= HI]
    def area(a, b, fill):
        seg = [(X, Y) for (X, Y), x in zip(pts, [x for x in D["x"] if LO <= x <= HI]) if a <= x <= b]
        if not seg: return ""
        d = f"M{seg[0][0]:.1f},{base} " + " ".join(f"L{X:.1f},{Y:.1f}" for X, Y in seg) + f" L{seg[-1][0]:.1f},{base} Z"
        return f'<path d="{d}" fill="{fill}"/>'
    o.append(area(-0.15, -0.05, C["acc_t"]))
    o.append(area(LO, -0.15, C["acc"]))
    # the low tail again, drawn ten times taller so the costly part can be seen
    xs = [x for x in D["x"] if LO <= x <= -0.05]
    zp = []
    for x, y in zip(D["x"], D[key]):
        if x < LO: continue
        if y * 10 / YMAX > 0.55: break
        zp.append((px(x), base - y * 10 / YMAX * hgt))
    dz = f"M{zp[0][0]:.1f},{base} " + " ".join(f"L{X:.1f},{Y:.1f}" for X, Y in zp if X <= px(-0.15)) + f" L{px(-0.15):.1f},{base} Z"
    o.append(f'<path d="{dz}" fill="{C["acc"]}" opacity="0.55"/>')
    o.append('<path d="M' + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in zp) + f'" fill="none" stroke="{C["acc"]}" stroke-width="3" stroke-dasharray="4 5"/>')
    o.append('<path d="M' + " L".join(f"{X:.1f},{Y:.1f}" for X, Y in pts) + f'" fill="none" stroke="{C["ink"]}" stroke-width="4"/>')
    o.append(f'<line x1="{X0}" y1="{base}" x2="{X1}" y2="{base}" stroke="{C["ink2"]}" stroke-width="2"/>')
    o.append(f'<line x1="{px(0):.1f}" y1="{base}" x2="{px(0):.1f}" y2="{base-hgt-20}" stroke="{C["ink"]}" stroke-width="3"/>')
    for v in (-0.05, -0.15):
        o.append(f'<line x1="{px(v):.1f}" y1="{base}" x2="{px(v):.1f}" y2="{base-hgt-20}" stroke="{C["ink2"]}" stroke-width="2" stroke-dasharray="8 6"/>')
    o.append(t(px(0) + 12, base - hgt, "True cost", "note", C["ink"]))
    o.append(t(px(-0.05) - 10, base - hgt, "Bidder keeps", "note", C["ink2"], "end"))
    o.append(t(px(-0.05) - 10, base - hgt + 26, "the first 5%", "note", C["ink2"], "end"))
    o.append(t(px(-0.15) - 10, base - hgt + 70, "15% low", "note", C["ink2"], "end"))
    o.append(t(1150, ytop + 130, big, "big", C["ink"]))
    o.append(t(1150, ytop + 168, "of the contract price", "note", C["ink2"]))
    o.append(t(1150, ytop + 200, dollars, "note", C["ink2"]))
    for i, s in enumerate(lines):
        o.append(t(1150, ytop + 250 + 28 * i, s, "note", C["ink"]))
    return o
o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>',
     t(80, 70, "THE PROJECT'S INSURANCE MODEL", "eyebrow"),
     t(80, 135, "Checking the bid first cuts off the costly tail", "title"),
     t(80, 180, "Bids a typical bot sends in, compared with the true cost of the job. The bidder keeps the first 5%", "dek"),
     t(80, 210, "of a miss and the cover pays 80% of the rest. Dashed: the low tail drawn ten times taller.", "dek")]
o += panel(290, "alone", "The bot on its own", "Two estimates in three land within 6 percent of the true cost.",
           f"about {D['premium_alone']:.1f}%", "$86,000 on an $8 million job",
           [f"Bids more than 15% low:", f"{one_in(D['alone_beyond15'])}"])
o += panel(740, "checked", "The same bot, checked before the bid goes in",
           "A bid more than 15% below the standard goes back to be priced by hand, and is not covered.",
           f"about {D['premium_checked']:.2f}%", "$12,000 on an $8 million job",
           [f"Bids more than 15% low:", f"{one_in(D['checked_beyond15'])}", f"1 bid in {round(1/D['repriced'])} re-priced by hand"])
for v, s in ((-0.2, "20% low"), (-0.1, "10% low"), (0, "True cost"), (0.1, "10% high"), (0.2, "20% high")):
    o.append(t(px(v), 1135, s, "note", C["ink2"], "middle"))
o.append(t(80, H - 40, "Model figures on stated assumptions: one bidder on a bot, 1 gross miss in 100 bids, a 15% return for the insurer, before tax.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 50px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 24px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.note{{font:400 22px "IBM Plex Sans",Arial,sans-serif}}
.big{{font:700 64px Georgia,serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "premium-with-checks"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
