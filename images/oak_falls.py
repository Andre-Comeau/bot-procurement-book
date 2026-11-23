"""The oak falls: the cost of bidding, before and after (chapter 1, schematic).
Usage: python images/oak_falls.py images/oak-falls   (writes the .svg and an .html; render at 1600 1000, see images/README.md)
"""
import sys, html, random, math
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
D = {k: mix(C[k], C["ink"], 0.2) for k in ("action", "sec", "acc", "ink2")}
W, H = 1600, 1000
BARK = mix(C["acc"], C["ink"], 0.55)
GROUND = mix(C["ink2"], C["canvas"], 0.72)
GOLD = "#e0a526"
def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'
o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append(t(80, 86, "CHAPTER 1 · THE OAK FALLS", "eyebrow"))
o.append(t(80, 148, "The oak falls", "title"))
o.append(t(80, 190, "For a century the cost of bidding stood over the market and shaded out everyone who could not afford to grow under it.", "dek"))
o.append(t(80, 218, "Then AI made the call nearly free.", "dek"))
PY0, PY1, GY = 270, 900, 800
panels = ((80, 760, "For a century"), (840, 1520, "Now"))
for (x0, x1, lab) in panels:
    o.append(f'<rect x="{x0}" y="{PY0}" width="{x1-x0}" height="{PY1-PY0}" fill="#ffffff" stroke="{C["hair"]}" stroke-width="2"/>')
    o.append(f'<rect x="{x0}" y="{GY}" width="{x1-x0}" height="{PY1-GY}" fill="{GROUND}"/>')
    o.append(t(x0, PY0-16, lab, "lab", C["ink"]))
# ---- left: the oak and its shade
cx = 420
o.append(f'<rect x="150" y="560" width="540" height="{GY-560}" fill="{C["ink"]}" opacity="0.07"/>')
o.append(f'<path d="M{cx-26},{GY} q-6,-120 -14,-250 h80 q-8,130 -14,250 z" fill="{BARK}"/>')
o.append(f'<path d="M{cx-30},540 q-60,-40 -120,-30 M{cx+30},540 q60,-40 120,-30 M{cx},520 q10,-60 40,-90" fill="none" stroke="{BARK}" stroke-width="14" stroke-linecap="round"/>')
rnd = random.Random(3)
for (dx, dy, r) in ((0, -110, 165), (-130, -60, 115), (130, -60, 115), (-70, -185, 100), (70, -185, 100), (0, -30, 90)):
    col = mix(C["sec"], C["ink"], rnd.uniform(0.25, 0.45))
    o.append(f'<circle cx="{cx+dx}" cy="{590+dy}" r="{r}" fill="{col}"/>')
o.append(t(cx, 470, "THE COST OF BIDDING", "canopy", C["canvas"], "middle"))
o.append(t(cx, 502, "an estimating department, a bonding line,", "canopynote", mix(C["canvas"], C["sec"], 0.15), "middle"))
o.append(t(cx, 528, "the patience to lose five bids in six", "canopynote", mix(C["canvas"], C["sec"], 0.15), "middle"))
o.append(f'<ellipse cx="{cx}" cy="{GY+10}" rx="290" ry="26" fill="{C["ink"]}" opacity="0.16"/>')
# a few large bidders, grown in its shade
for sx in (265, 330, 500, 565):
    o.append(f'<path d="M{sx},{GY} v-34" stroke="{BARK}" stroke-width="5"/>')
    for (dx, dy, r) in ((0, -50, 24), (-16, -40, 17), (16, -40, 17)):
        o.append(f'<circle cx="{sx+dx}" cy="{GY+dy}" r="{r}" fill="{mix(C["sec"], C["ink"], 0.3)}"/>')
# the rest, stunted seedlings
for i in range(26):
    sx = 170 + i * 20.5 + rnd.uniform(-4, 4)
    if 245 < sx < 350 or 480 < sx < 585 or abs(sx - cx) < 40:
        continue
    hgt = rnd.uniform(6, 14)
    col = mix(C["sec"], GROUND, 0.55)
    o.append(f'<path d="M{sx:.1f},{GY} v-{hgt:.1f} m0,{hgt*0.5:.1f} q-6,-4 -9,-9 m9,9 q6,-4 9,-9" fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round"/>')
# the plan room, built in the shade
o.append(f'<rect x="605" y="{GY-46}" width="56" height="46" fill="{mix(C["ink2"], C["canvas"], 0.35)}" stroke="{C["ink"]}" stroke-width="2"/>')
o.append(f'<path d="M599,{GY-46} l34,-26 l34,26 z" fill="{BARK}" stroke="{C["ink"]}" stroke-width="2"/>')
o.append(f'<rect x="626" y="{GY-24}" width="14" height="24" fill="{C["ink"]}"/>')
o.append(t(633, GY-80, "the plan room", "tiny", C["ink2"], "middle"))
o.append(t(420, GY+38, "A few large bidders grew in its shade.", "note", C["ink"], "middle"))
o.append(t(420, GY+64, "The rest were shaded out.", "note", C["ink"], "middle"))
o.append(t(420, GY+90, "The buyer's systems grew in the shade too, built for a few bids and time to read them.", "tiny", C["ink2"], "middle"))
# ---- right: the clearing and the thicket
rx0, rx1 = 840, 1520
o.append(f'<clipPath id="rp"><rect x="{rx0}" y="{PY0}" width="{rx1-rx0}" height="{GY-PY0}"/></clipPath>')
o.append('<g clip-path="url(#rp)">')
for (ax, bx) in ((900, 1080), (1120, 1250), (1300, 1400), (1430, 1520)):
    o.append(f'<path d="M1480,{PY0} L{ax},{GY} L{bx},{GY} Z" fill="{GOLD}" opacity="0.14"/>')
o.append('</g>')
# the stump and the fallen trunk
sx = 1000
o.append(f'<path d="M{sx-40},{GY} v-44 h80 v44 z" fill="{BARK}"/>')
for (rx, ry) in ((40, 12), (26, 8), (13, 4)):
    o.append(f'<ellipse cx="{sx}" cy="{GY-44}" rx="{rx}" ry="{ry}" fill="{C["acc_t"] if rx == 40 else "none"}" stroke="{C["ink2"]}" stroke-width="1.5"/>')
o.append(f'<g transform="rotate(-2 {sx+70} {GY-18})"><rect x="{sx+70}" y="{GY-40}" width="{rx1-sx-90}" height="40" rx="6" fill="{BARK}" opacity="0.92"/><ellipse cx="{sx+70}" cy="{GY-20}" rx="9" ry="20" fill="{C["acc_t"]}" stroke="{C["ink2"]}" stroke-width="1.5"/><ellipse cx="{sx+70}" cy="{GY-20}" rx="5" ry="11" fill="none" stroke="{C["ink2"]}" stroke-width="1"/></g>')
# the thicket
rnd2 = random.Random(11)
plants = []
for i in range(90):
    px = rnd0 = rnd2.uniform(rx0 + 30, rx1 - 30)
    if abs(px - sx) < 60:
        continue
    hgt = rnd2.choice((40, 60, 80, 100, 120, 140, 170, 200, 240, 290, 340))
    plants.append((px, hgt, rnd2.uniform(-18, 18), rnd2.random()))
plants.sort(key=lambda p: -p[1])
for (px, hgt, bend, r) in plants:
    col = mix(C["sec"], "#ffffff", 0.05 + 0.35 * r) if hgt < 200 else mix(C["sec"], C["ink"], 0.15 * r)
    o.append(f'<path d="M{px:.1f},{GY} q{bend*0.5:.1f},-{hgt*0.5:.1f} {bend:.1f},-{hgt:.1f}" fill="none" stroke="{col}" stroke-width="{2.5 + hgt/90:.1f}" stroke-linecap="round"/>')
    for k in (0.45, 0.7, 0.92):
        ly = GY - hgt * k; lx = px + bend * k * 0.9
        side = 1 if (k * 10) % 2 < 1 else -1
        o.append(f'<ellipse cx="{lx + side*9:.1f}" cy="{ly:.1f}" rx="10" ry="4.5" fill="{col}" transform="rotate({-25*side} {lx + side*9:.1f} {ly:.1f})"/>')
o.append(t(1180, GY+38, "The clearing fills with a thicket racing for the new sunlight.", "note", C["ink"], "middle"))
o.append(t(1180, GY+64, "Every seedling looks much like the next.", "note", C["ink"], "middle"))
for yy in (GY+70, GY+76):
    o.append(f'<path d="M{rx0+20},{yy} h{rx1-rx0-40}" stroke="{C["ink2"]}" stroke-width="1" stroke-dasharray="6 5" opacity="0.45"/>')
o.append(t(1180, GY+92, "the forest floor: what this work has cost before, which no bid-writing bot can polish", "tiny", C["ink2"], "middle"))
o.append(t(80, H-40, "The oak will not grow back. The question is who gets the light.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 24px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.note{{font:400 21px "IBM Plex Sans",Arial,sans-serif}}
.tiny{{font:italic 400 17px "IBM Plex Sans",Arial,sans-serif}}
.canopy{{font:700 24px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.1em}}
.canopynote{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "oak-falls"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
print("wrote", stem, len(plants), "plants")
