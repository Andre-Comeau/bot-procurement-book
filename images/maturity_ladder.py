"""From signer to autonomous bidding: the maturity ladder (schematic, not data).
Rungs follow chapter 17's versions and chapter 19's goal; the insurance column follows chapters 3 and 13.
Usage: python images/maturity_ladder.py images/maturity-ladder  (writes .svg and .html)
"""
import sys, html
C = dict(sec="#0f6e56", sec_t="#e1f5ee", acc="#d85a30", canvas="#f9f8f5", hair="#d6d3cc", ink="#2c2c2a", ink2="#5f5e5a")
W, H = 1600, 1180
def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x:.0f}" y="{y:.0f}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'
RUNGS = [  # bottom to top
    ("Version 1.0", "Momentum", ["One trade first. The template published,", "and every reading signed by a person."],
     "A person signs every line", "The bidder carries every miss"),
    ("Version 2.0", "Proof of work", ["The evaluator in an owner's hands, and the", "first tenders issued with the template."],
     "A named person signs each reading", "A pilot policy, on a few bidders"),
    ("Version 3.0", "The working model", ["The tool test built from the signed readings,", "with a published range."],
     "A person looks at what the test flags", "Margin insurance on checked bids"),
    ("The goal", "Autonomous bidding", ["The bot bids on its own, backed by the test,", "a public reference price and cover."],
     "Signing is a choice, not a rule", "Cover sold with the bot"),
]
o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>',
     t(80, 70, "SCHEMATIC, NOT DATA", "eyebrow"),
     t(80, 135, "From the signer to the bot that bids on its own", "title"),
     t(80, 180, "Each rung trusts the bot a little further, and each needs the one below it.", "dek")]
RX0, RX1 = 120, 200   # ladder rails
top, bot = 260, 1080
o.append(f'<line x1="{RX0}" y1="{top}" x2="{RX0}" y2="{bot}" stroke="{C["ink"]}" stroke-width="8"/>')
o.append(f'<line x1="{RX1}" y1="{top}" x2="{RX1}" y2="{bot}" stroke="{C["ink"]}" stroke-width="8"/>')
o.append(t(700, 250, "Who signs", "colhead", C["ink2"]))
o.append(t(1130, 250, "Who carries a miss", "colhead", C["ink2"]))
step = (bot - top - 40) / len(RUNGS)
for i, (ver, name, desc, sign, cover) in enumerate(RUNGS):
    y = bot - 40 - i * step
    goal = i == len(RUNGS) - 1
    o.append(f'<line x1="{RX0}" y1="{y:.0f}" x2="{RX1}" y2="{y:.0f}" stroke="{C["ink"]}" stroke-width="8"/>')
    bx, by, bw, bh = 240, y - 150, 1280, 170
    o.append(f'<rect x="{bx}" y="{by:.0f}" width="{bw}" height="{bh}" rx="10" fill="{C["sec_t"] if goal else "#ffffff"}" stroke="{C["sec"] if goal else C["hair"]}" stroke-width="{3 if goal else 2}"/>')
    o.append(t(bx + 24, by + 44, ver, "ver", C["sec"] if goal else C["ink2"]))
    o.append(t(bx + 24, by + 84, name, "lab", C["ink"]))
    for j, line in enumerate(desc):
        o.append(t(bx + 24, by + 118 + 28 * j, line, "note", C["ink2"]))
    o.append(t(700 - 240 + bx, by + 84, sign, "cell", C["ink"]))
    o.append(t(1130 - 240 + bx, by + 84, cover, "cell", C["acc"]))
o.append(t(80, H - 30, "The project is working toward the bottom rung now. Chapters 13, 17 and 19 describe the rest.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 50px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 24px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.colhead{{font:600 20px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase}}
.ver{{font:600 20px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.1em;text-transform:uppercase}}
.lab{{font:700 32px Georgia,serif}}
.cell{{font:600 23px "IBM Plex Sans",Arial,sans-serif}}
.note{{font:400 21px "IBM Plex Sans",Arial,sans-serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "maturity-ladder"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
