"""What a premium pays for: the chapter 3 figure (figures from the project's insurance model,
research files combined-check, 24 Nov 2026: medium bidder, typical bot checked at a 15% range edge,
bidder keeps 5%, cover pays 80%; sold on its own about $12,000 of which about $6,600 is expected
payouts; through the vendor about $8,800, with a yearly cap that trims payouts by about 1.5%).
Usage: python images/premium_build_up.py images/premium-build-up  (writes .svg and .html)
"""
import sys, html
C = dict(sec="#0f6e56", acc="#d85a30", acc_t="#f6d3c4", canvas="#f9f8f5", ink="#2c2c2a", ink2="#5f5e5a")
W, H = 1600, 760
X0, SCALE = 380, 0.075   # pixels per dollar: $12,000 -> 900 px
def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x:.0f}" y="{y:.0f}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'
ROWS = [("Sold on its own", "through a broker", 6600, 5400, "$12,000", "0.15% of the contract",
         "Commission, running costs, capital for a bad year"),
        ("Sold by the vendor", "with the bot", 6500, 2300, "$8,800", "0.11% of the contract",
         "Smaller commission, claims handled automatically, a yearly cap")]
o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>',
     t(80, 70, "THE PROJECT'S INSURANCE MODEL", "eyebrow"),
     t(80, 135, "What the premium pays for", "title"),
     t(80, 180, "The insurer's lowest price on one $8 million job won, for a typical bot whose bids are checked.", "dek")]
for i, (a, b, pay, cost, tot, pct, note) in enumerate(ROWS):
    y = 280 + i * 210
    o += [t(80, y + 32, a, "lab", C["ink"]), t(80, y + 64, b, "note", C["ink2"])]
    w1, w2 = pay * SCALE, cost * SCALE
    o.append(f'<rect x="{X0}" y="{y}" width="{w1:.0f}" height="80" fill="{C["sec"]}"/>')
    o.append(f'<rect x="{X0 + w1:.0f}" y="{y}" width="{w2:.0f}" height="80" fill="{C["acc"]}"/>')
    o.append(t(X0 + 18, y + 50, f"about ${pay:,} in expected payouts", "inbar", "#ffffff"))
    o.append(t(X0 + w1 + w2 / 2, y + 50, f"${cost:,}", "inbar", "#ffffff", "middle"))
    o.append(t(X0 + w1 + w2 + 24, y + 36, tot, "big", C["ink"]))
    o.append(t(X0 + w1 + w2 + 24, y + 70, pct, "note", C["ink2"]))
    o.append(t(X0 + w1 + 4, y + 118, note, "note", C["acc"]))
o.append(t(80, H - 40, "Model figures on stated assumptions; a real policy would be priced from a bidder's own books.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 50px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 24px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.note{{font:400 22px "IBM Plex Sans",Arial,sans-serif}}
.inbar{{font:600 24px "IBM Plex Sans",Arial,sans-serif}}
.big{{font:700 48px Georgia,serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "premium-build-up"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
