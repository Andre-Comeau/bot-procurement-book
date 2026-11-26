"""The tender is the API: one door between the design and the construction (chapter 1, schematic).
Usage: python images/tender_api_door.py images/tender-api-door   (writes the .svg and an .html; render at 1600 1100, see images/README.md)
"""
import sys, html
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
D = {k: mix(C[k], C["ink"], 0.2) for k in ("action", "sec", "acc", "ink2")}
W, H = 1600, 1100
L = f'stroke="{C["ink"]}" stroke-linejoin="round" stroke-linecap="round"'
def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'
def person(x, y, body, kind, s=1.0, hat=None, skin="#e2b48c"):
    Ls = f'stroke="{C["ink"]}" stroke-width="{2.5:.1f}" stroke-linejoin="round" stroke-linecap="round"'
    g = [f'<g transform="translate({x},{y}) scale({s})">']
    g.append(f'<path d="M-8,40 v18 M8,40 v18" stroke="{C["ink"]}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M-12,58 h8 M4,58 h8" stroke="{C["ink"]}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M-16,14 q16,-6 32,0 l3,28 h-38 z" fill="{body}" {Ls}/>')
    if kind == "builder":
        g.append('<path d="M-15,26 h30 M-14,34 h28" stroke="#f3e9b0" stroke-width="3"/>')
    if kind == "surety":
        g.append(f'<path d="M-5,11 l5,6 l5,-6" fill="#ffffff" {Ls}/><path d="M0,17 l-3,14 l3,4 l3,-4 z" fill="{C["ink"]}"/>')
    g.append(f'<circle cx="0" cy="0" r="11" fill="{skin}" {Ls}/>')
    g.append(f'<path d="M-11,-2 q2,-12 11,-12 q9,0 11,12 q-4,-6 -11,-6 q-7,0 -11,6 z" fill="{C["ink"]}"/>' if not hat else "")
    g.append(f'<circle cx="-4" cy="1" r="1.6" fill="{C["ink"]}"/><circle cx="4" cy="1" r="1.6" fill="{C["ink"]}"/>')
    if kind == "designer":
        g.append(f'<circle cx="-4.5" cy="1" r="4" fill="none" stroke="{C["ink"]}" stroke-width="1.6"/><circle cx="4.5" cy="1" r="4" fill="none" stroke="{C["ink"]}" stroke-width="1.6"/><path d="M-0.5,1 h1" stroke="{C["ink"]}" stroke-width="1.6"/>')
    if hat:
        g.append(f'<path d="M-11,-3 a11,10 0 0 1 22,0 z" fill="{hat}" {Ls}/><path d="M-14,-3 h28" {Ls}/>')
    g.append(f'<path d="M-16,16 l-8,18 M16,16 l8,18" {Ls} fill="none"/>')
    g.append('</g>')
    return "".join(g)
def plaque(x, y, text, w, cls="lab"):
    return (f'<rect x="{x-w/2}" y="{y-28}" width="{w}" height="44" rx="6" fill="#ffffff" stroke="{C["ink"]}" stroke-width="3"/>'
            + t(x, y+6, text, cls, C["ink"], "middle"))
def arrow(x1, x2, y, col, width=8):
    d = 1 if x2 > x1 else -1
    head = f'M{x2},{y} l{-d*26},-16 l0,32 z'
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - d*20}" y2="{y}" stroke="{col}" stroke-width="{width}" stroke-linecap="round"/>'
            f'<path d="{head}" fill="{col}"/>')

o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append(t(80, 86, "CHAPTER 1 · THE TENDER IS THE API", "eyebrow"))
o.append(t(80, 148, "One door between two rooms", "title"))
o.append(t(80, 190, "The design and the construction negotiate through the tender. The bill of quantities is the call every bidder makes,", "dek"))
o.append(t(80, 218, "and the bid is the answer that comes back. Nobody has to read the other side's source code.", "dek"))

Y0, Y1 = 300, 900
# rooms
for (x0, x1, fill, name) in ((80, 600, C["action_t"], "The design"), (1000, 1520, C["sec_t"], "The construction")):
    o.append(f'<rect x="{x0}" y="{Y0}" width="{x1-x0}" height="{Y1-Y0}" fill="{fill}" stroke="{C["ink"]}" stroke-width="6"/>')
    o.append(plaque((x0+x1)/2, Y0, name, 260))
# left room: designer and the drawing of a beam
o.append(person(190, 560, D["action"], "designer", s=1.8))
o.append(f'<rect x="300" y="500" width="260" height="190" rx="4" fill="#ffffff" stroke="{C["ink"]}" stroke-width="3"/>')
# I-beam section
o.append(f'<path d="M370,540 h120 v16 h-46 v60 h46 v16 h-120 v-16 h46 v-60 h-46 z" fill="{mix(C["action"], "#ffffff", 0.75)}" stroke="{C["ink"]}" stroke-width="2.5"/>')
o.append(f'<path d="M330,540 v92 M322,540 h16 M322,632 h16" stroke="{C["ink2"]}" stroke-width="1.5"/>')
o.append(f'<path d="M370,660 h120 M370,652 v16 M490,652 v16" stroke="{C["ink2"]}" stroke-width="1.5"/>')
o.append(t(430, 530, "W610 × 125", "tiny", C["ink2"], "middle"))
o.append(t(120, 760, "Why the engineer chose that beam.", "note", C["ink2"]))
o.append(t(120, 790, "The builder need not know.", "note", C["ink2"]))
# right room: the bonding company behind the builder, and the crew schedule
o.append(person(1215, 505, D["ink2"], "surety", s=2.1, skin="#c68a5e"))
o.append(person(1130, 575, D["acc"], "builder", s=1.8, hat="#e0a526", skin="#9a623f"))
o.append(plaque(1215, 455, "the bonding company", 240, "note"))
o.append(f'<rect x="1310" y="500" width="180" height="190" rx="4" fill="#ffffff" stroke="{C["ink"]}" stroke-width="3"/>')
for i in range(6):
    yy = 520 + i*27
    o.append(f'<line x1="1320" y1="{yy+22}" x2="1480" y2="{yy+22}" stroke="{C["hair"]}" stroke-width="1.5"/>')
bars = [(1320, 60, C["action"]), (1350, 70, C["sec"]), (1390, 80, C["acc"]), (1330, 50, C["sec"]), (1410, 70, C["action"]), (1370, 90, C["acc"])]
for i, (bx, bw, col) in enumerate(bars):
    o.append(f'<rect x="{bx}" y="{525+i*27}" width="{bw}" height="14" rx="3" fill="{col}" opacity="0.85"/>')
o.append(t(1040, 760, "How the builder schedules its crews.", "note", C["ink2"]))
o.append(t(1040, 790, "The designer need not know.", "note", C["ink2"]))
o.append(t(1040, 832, "One door means one builder answers for", "note", C["ink"]))
o.append(t(1040, 860, "everything behind it, whoever it hires.", "note", C["ink"]))
o.append(t(1040, 888, "A bonding company stands behind the builder.", "note", C["ink"]))
o.append(t(120, 860, "The design is tested once, by each bidder,", "note", C["ink"]))
o.append(t(120, 888, "in the few weeks before the bids close.", "note", C["ink"]))
# the door: a frame filled with a stack of PDFs
DX0, DX1, DY0 = 720, 880, 430
o.append(f'<rect x="{DX0-14}" y="{DY0-14}" width="{DX1-DX0+28}" height="{Y1-DY0+14}" fill="{mix(C["ink2"], C["canvas"], 0.5)}" stroke="{C["ink"]}" stroke-width="8"/>')
import random
rnd = random.Random(6)
yy = Y1 - 6
k = 0
while yy > DY0 + 10:
    hgt = rnd.choice((10, 12, 14, 16))
    jit = rnd.uniform(-5, 5)
    o.append(f'<rect x="{DX0+jit:.1f}" y="{yy-hgt}" width="{DX1-DX0}" height="{hgt}" fill="#ffffff" stroke="{C["ink"]}" stroke-width="1.5"/>')
    if k % 5 == 2:
        o.append(f'<rect x="{DX0+jit+8:.1f}" y="{yy-hgt+3}" width="34" height="{hgt-6}" fill="{C["acc"]}"/>')
    yy -= hgt; k += 1
o.append(plaque(800, 400, "the door", 150))
o.append(plaque(800, 955, "a stack of PDFs", 230, "note"))
# the call and the answer, through the door
def pill(x, y, text, col):
    w = len(text) * 11.5 + 30
    return (f'<rect x="{x-w/2}" y="{y-24}" width="{w}" height="34" rx="17" fill="#ffffff" stroke="{col}" stroke-width="2.5"/>'
            + t(x, y, text, "note", col, "middle"))
o.append(arrow(600, 1000, 540, C["action"]))
o.append(pill(800, 505, "the call: the bill of quantities", D["action"]))
o.append(arrow(1000, 600, 700, C["sec"]))
o.append(pill(800, 665, "the answer: the bid", D["sec"]))
o.append(t(80, H-40, "Schematic. The one medium both sides can read is the one the compiler cannot open.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 24px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.note{{font:400 21px "IBM Plex Sans",Arial,sans-serif}}
.tiny{{font:400 16px "IBM Plex Sans",Arial,sans-serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "tender-api-door"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
print("wrote", stem)
