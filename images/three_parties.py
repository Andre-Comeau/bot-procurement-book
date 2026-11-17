"""Three parties at the door: the buyers, the bidders and the vendors (chapters 6a to 6c, one scene).
Usage: python images/three_parties.py images/three-parties   (writes the .svg and an .html; render at 1600 1260, see images/README.md)
"""
import sys, html, random, math
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
D = {k: mix(C[k], C["ink"], 0.2) for k in ("action", "sec", "acc", "ink2")}
W, H = 1600, 1260
GOLD = "#e0a526"; BARK = mix(C["acc"], C["ink"], 0.55)
GROUND = mix(C["ink2"], C["canvas"], 0.72); WALL = mix(C["ink2"], C["canvas"], 0.62); STONE = mix(C["ink2"], C["canvas"], 0.5)
GY = 860
L = f'stroke="{C["ink"]}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"'
def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'
def wrap(s, n):
    out, cur = [], ""
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: out.append(cur)
    return out
def person(x, y, body, kind="bidder", s=1.0, hat=None, skin="#e2b48c"):
    g = [f'<g transform="translate({x},{y}) scale({s})">']
    g.append(f'<path d="M-8,40 v18 M8,40 v18" stroke="{C["ink"]}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M-12,58 h8 M4,58 h8" stroke="{C["ink"]}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M-16,14 q16,-6 32,0 l3,28 h-38 z" fill="{body}" {L}/>')
    if kind == "bidder":
        g.append('<path d="M-15,26 h30 M-14,34 h28" stroke="#f3e9b0" stroke-width="3"/>')
    if kind in ("buyer", "porter"):
        g.append(f'<path d="M-5,11 l5,6 l5,-6" fill="#ffffff" {L}/><path d="M0,17 l-3,14 l3,4 l3,-4 z" fill="{C["ink"]}"/>')
    g.append(f'<circle cx="0" cy="0" r="11" fill="{skin}" {L}/>')
    if not hat:
        g.append(f'<path d="M-11,-2 q2,-12 11,-12 q9,0 11,12 q-4,-6 -11,-6 q-7,0 -11,6 z" fill="{C["ink"]}"/>')
    g.append(f'<circle cx="-4" cy="1" r="1.6" fill="{C["ink"]}"/><circle cx="4" cy="1" r="1.6" fill="{C["ink"]}"/>')
    if hat:
        g.append(f'<path d="M-11,-3 a11,10 0 0 1 22,0 z" fill="{hat}" {L}/><path d="M-14,-3 h28" {L}/>')
    if kind == "porter":
        g.append(f'<path d="M-16,16 l-8,18 M16,16 l2,14 l-8,4" {L} fill="none"/><rect x="16" y="34" width="18" height="13" rx="2" fill="#6b4a1e" {L}/>')
    elif kind == "reach":
        g.append(f'<path d="M-16,16 l-8,18 M16,16 l14,-30" {L} fill="none"/>')
    else:
        g.append(f'<path d="M-16,16 l-8,18 M16,16 l8,18" {L} fill="none"/>')
    g.append('</g>')
    return "".join(g)
def tag(x, y, text, anchor="middle", cls="tag", cw=8.6):
    w = len(text) * cw + 22
    x0 = {"middle": x - w / 2, "start": x, "end": x - w}[anchor]
    return (f'<rect x="{x0:.1f}" y="{y-18}" width="{w:.1f}" height="26" rx="13" fill="#ffffff" stroke="{C["ink"]}" stroke-width="1.5"/>'
            + t(x0 + w / 2, y, text, cls, C["ink"], "middle"))
def plant(x, hgt, col, bend=0, lw=3, leaves=3):
    g = [f'<path d="M{x:.1f},{GY} q{bend*0.5:.1f},-{hgt*0.5:.1f} {bend:.1f},-{hgt:.1f}" fill="none" stroke="{col}" stroke-width="{lw}" stroke-linecap="round"/>']
    for k in range(leaves):
        f = 0.35 + 0.55 * k / max(1, leaves - 1)
        ly = GY - hgt * f; lx = x + bend * f * 0.9; side = 1 if k % 2 == 0 else -1
        g.append(f'<ellipse cx="{lx+side*10:.1f}" cy="{ly:.1f}" rx="11" ry="5" fill="{col}" transform="rotate({-25*side} {lx+side*10:.1f} {ly:.1f})"/>')
    return "".join(g)
def shrub(x, r, col, stem=36):
    g = [f'<path d="M{x},{GY} v-{stem}" stroke="{BARK}" stroke-width="6"/>']
    for (dx, dy, rr) in ((0, -stem - r * 0.6, r), (-r * 0.75, -stem - r * 0.2, r * 0.75), (r * 0.75, -stem - r * 0.2, r * 0.75)):
        g.append(f'<circle cx="{x+dx:.1f}" cy="{GY+dy:.1f}" r="{rr:.1f}" fill="{col}"/>')
    return "".join(g)
o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append(t(80, 86, "CHAPTERS 6A TO 6C · THE BUYERS, THE BIDDERS, THE VENDORS", "eyebrow"))
o.append(t(80, 148, "Three parties at the door", "title"))
o.append(t(80, 190, "The buyers' door is flooded. The bidders are the thicket. The vendors sell shovels to both, and would like to own the sun.", "dek"))
# ground and sun
o.append(f'<rect x="80" y="{GY}" width="{W-160}" height="70" fill="{GROUND}"/>')
SX, SY = 1495, 318
for k in range(12):
    a = k * math.pi / 6
    o.append(f'<line x1="{SX+math.cos(a)*68:.1f}" y1="{SY+math.sin(a)*68:.1f}" x2="{SX+math.cos(a)*88:.1f}" y2="{SY+math.sin(a)*88:.1f}" stroke="{GOLD}" stroke-width="4" stroke-linecap="round" opacity="0.8"/>')
o.append(f'<circle cx="{SX}" cy="{SY}" r="58" fill="{GOLD}"/>')
# ---- the buyers: a facade with five doors and a reading room
BX0, BX1 = 80, 580
o.append(f'<rect x="{BX0}" y="330" width="{BX1-BX0}" height="{GY-330}" fill="{WALL}" stroke="{C["ink"]}" stroke-width="5"/>')
o.append(f'<path d="M{BX0-10},330 L{(BX0+BX1)/2},262 L{BX1+10},330 z" fill="{STONE}" stroke="{C["ink"]}" stroke-width="5"/>')
o.append(t((BX0 + BX1) / 2, 318, "THE BUYERS", "sign", C["ink"], "middle"))
RX0, RY0, RX1, RY1 = 130, 370, 530, 630
o.append(f'<rect x="{RX0}" y="{RY0}" width="{RX1-RX0}" height="{RY1-RY0}" fill="{C["action_t"]}" stroke="{C["ink"]}" stroke-width="4"/>')
rnd = random.Random(2)
yy = RY1 - 4; k = 0
while yy > RY0 + 12:
    hgt = rnd.choice((8, 10, 12)); jit = rnd.uniform(-6, 6)
    o.append(f'<rect x="{395+jit:.1f}" y="{yy-hgt}" width="110" height="{hgt}" fill="#ffffff" stroke="{C["ink"]}" stroke-width="1.2"/>')
    if k % 6 == 3:
        o.append(f'<rect x="{395+jit+6:.1f}" y="{yy-hgt+2}" width="22" height="{hgt-4}" fill="{C["acc"]}"/>')
    yy -= hgt; k += 1
o.append(f'<rect x="{RX0+20}" y="{RY1-70}" width="200" height="12" fill="{BARK}"/><path d="M{RX0+40},{RY1-58} v54 M{RX0+200},{RY1-58} v54" stroke="{BARK}" stroke-width="8"/>')
for i, px in enumerate((RX0 + 60, RX0 + 120, RX0 + 180)):
    o.append(person(px, RY1 - 120, D["action"] if i != 1 else D["sec"], kind="buyer", s=0.95, skin=("#f1d7bd", "#9a623f", "#c68a5e")[i]))
o.append(tag(255, RY0 + 32, "more bids than eyes"))
doors = [(110, "slot"), (205, "pdfs"), (300, "grand"), (395, "shut"), (490, "porter")]
for n, (dx, kind) in enumerate(doors, 1):
    dw, dh = 64, 150
    if kind == "grand":
        dw, dh = 76, 178
    x0, y0 = dx - dw / 2, GY - dh
    o.append(f'<rect x="{x0}" y="{y0}" width="{dw}" height="{dh}" rx="3" fill="{mix(C["ink2"], C["canvas"], 0.3)}" stroke="{C["ink"]}" stroke-width="3"/>')
    o.append(f'<path d="M{x0},{y0} a{dw/2},{dw/2} 0 0 1 {dw},0" fill="{mix(C["ink2"], C["canvas"], 0.3)}" stroke="{C["ink"]}" stroke-width="3"/>')
    o.append(f'<circle cx="{dx+dw/2-14}" cy="{y0+dh*0.55}" r="4" fill="{C["ink"]}"/>')
    if kind == "slot":
        o.append(f'<rect x="{dx-20}" y="{y0+50}" width="40" height="8" rx="2" fill="{C["ink"]}"/>')
        o.append(f'<g transform="rotate(-18 {dx+22} {y0+48})"><rect x="{dx+4}" y="{y0+40}" width="36" height="16" rx="2" fill="{C["action"]}" stroke="{C["ink"]}" stroke-width="1.5"/><path d="M{dx+10},{y0+45} h22 M{dx+10},{y0+51} h14" stroke="#ffffff" stroke-width="2"/></g>')
    elif kind == "pdfs":
        for j in range(5):
            o.append(f'<rect x="{dx-34+j*3}" y="{GY-16-j*14}" width="30" height="14" fill="#ffffff" stroke="{C["ink"]}" stroke-width="1.2"/><rect x="{dx-30+j*3}" y="{GY-14-j*14}" width="10" height="10" fill="{C["acc"]}"/>')
    elif kind == "grand":
        o.append(f'<line x1="{dx}" y1="{y0+dw/2}" x2="{dx}" y2="{GY}" stroke="{C["ink"]}" stroke-width="3"/>')
        o.append(f'<path d="M{dx-40},{GY-6} q10,-14 24,-16 q-8,10 -4,16" fill="none" stroke="{C["ink2"]}" stroke-width="1.5" opacity="0.7"/>')
    elif kind == "shut":
        o.append(f'<rect x="{dx-26}" y="{y0+44}" width="52" height="22" rx="3" fill="#ffffff" stroke="{C["ink"]}" stroke-width="2"/>' + t(dx, y0 + 60, "PRIVATE", "micro", C["ink"], "middle"))
        o.append(f'<rect x="{dx-dw/2-6}" y="{y0+dh*0.55-5}" width="{dw+12}" height="10" rx="3" fill="{D["acc"]}"/>')
    elif kind == "porter":
        o.append(person(dx - 44, GY - 72, D["ink2"], kind="porter", s=0.9, skin="#c68a5e"))
    o.append(f'<circle cx="{dx}" cy="{y0-26}" r="15" fill="#ffffff" stroke="{C["ink"]}" stroke-width="2"/>' + t(dx, y0 - 20, str(n), "num", C["ink"], "middle"))
# ---- the bidders: the thicket, by species
TX0, TX1 = 620, 1180
o.append(t((TX0 + TX1) / 2, 318, "THE BIDDERS", "sign", C["ink"], "middle"))
G1 = C["sec"]; G3 = mix(C["sec"], C["ink"], 0.3); G4 = mix(C["sec"], "#ffffff", 0.45)
rnd2 = random.Random(7)
# the new species first, behind everything: identical pale stalks
for px in list(range(770, 800, 7)) + list(range(1146, 1184, 5)):
    o.append(plant(px + rnd2.uniform(-2, 2), 96 + rnd2.uniform(-8, 8), G4, bend=rnd2.uniform(-6, 6), lw=2, leaves=2))
# the small firm: short and broad
for dx_, h_ in ((-14, 70), (0, 92), (14, 72), (-26, 50), (26, 52)):
    o.append(plant(655 + dx_, h_, G1, bend=dx_ * 0.3, lw=4, leaves=3))
# the ambitious smaller firm: leaning hard toward the light
o.append(plant(735, 230, G1, bend=70, lw=4, leaves=5))
o.append(plant(726, 120, G1, bend=20, lw=3, leaves=3))
# the medium and large firms: two big shrubs
o.append(shrub(850, 52, G3, stem=60)); o.append(shrub(922, 46, G3, stem=48))
# the largest firms: a broad flat-topped tree, grown as wide as it will
o.append(f'<path d="M1025,{GY} q-4,-120 -10,-180 h44 q-6,60 -10,180 z" fill="{BARK}"/>')
o.append(f'<rect x="975" y="{GY-232}" width="124" height="66" rx="28" fill="{G3}"/>')
o.append(f'<line x1="990" y1="{GY-232}" x2="1084" y2="{GY-232}" stroke="{C["canvas"]}" stroke-width="3" stroke-dasharray="6 4"/>')
# the surgical team: three stems tied together
for dx_ in (-9, 0, 9):
    o.append(plant(1125 + dx_, 150 + abs(dx_), G1, bend=dx_ * 0.4, lw=3.5, leaves=3))
o.append(f'<rect x="1107" y="{GY-78}" width="36" height="12" rx="4" fill="{GOLD}" stroke="{C["ink"]}" stroke-width="1.5"/>')
# tags, staggered so none sits on a crown
o.append(tag(655, GY - 128, "the small firm"))
o.append(tag(735, GY - 270, "the ambitious smaller firm"))
o.append(tag(848, GY - 178, "the medium and large firms"))
o.append(tag(1037, GY - 262, "the largest firms"))
o.append(tag(1125, GY - 104, "the surgical team"))
o.append(tag(1180, GY + 28, "the new species", "end"))
# ---- the vendors: a stall of shovels, and a ladder to the sun
VX0, VX1 = 1220, 1520
o.append(t(1290, 318, "THE VENDORS", "sign", C["ink"], "middle"))
o.append(f'<rect x="1270" y="{GY-120}" width="180" height="120" fill="{mix(C["acc"], "#ffffff", 0.7)}" stroke="{C["ink"]}" stroke-width="3"/>')
o.append(f'<path d="M1256,{GY-120} h208 l-14,-30 h-180 z" fill="{D["acc"]}" stroke="{C["ink"]}" stroke-width="3"/>')
for j in range(6):
    o.append(f'<rect x="{1262+j*32}" y="{GY-150}" width="16" height="30" fill="{C["canvas"]}" opacity="0.6"/>')
o.append(f'<rect x="1302" y="{GY-106}" width="116" height="30" rx="3" fill="#ffffff" stroke="{C["ink"]}" stroke-width="2"/>' + t(1360, GY - 85, "SHOVELS", "plate", C["ink"], "middle"))
o.append(t(1360, GY - 50, "liability capped at", "micro2", C["ink2"], "middle"))
o.append(t(1360, GY - 32, "a year's fees", "micro2", C["ink2"], "middle"))
# the vendor at the stall, and the shovels leaning beside it, one colour per species
o.append(person(1242, GY - 66, D["acc"], kind="buyer", s=0.95, skin="#e2b48c"))
for (sx_, col) in ((1462, C["action"]), (1484, D["sec"]), (1506, C["acc"]), (1528, C["ink2"])):
    o.append(f'<g transform="rotate(12 {sx_} {GY-10})"><line x1="{sx_}" y1="{GY-10}" x2="{sx_}" y2="{GY-180}" stroke="{BARK}" stroke-width="5"/><path d="M{sx_-12},{GY-38} h24 v24 q-12,15 -24,0 z" fill="{col}" stroke="{C["ink"]}" stroke-width="1.5"/></g>')
o.append(tag(1500, GY + 56, "shovels: the platforms, the specialists, the startups, the general model", "end", cw=8.2))
# the referee's whistle, on its own hook at the top of the stall's world
o.append(f'<g transform="translate(1232,404)"><path d="M0,-28 q0,-12 10,-12" fill="none" stroke="{C["ink"]}" stroke-width="2.5"/><path d="M0,0 h26 a10,10 0 0 1 0,20 h-26 z" fill="{STONE}" stroke="{C["ink"]}" stroke-width="2"/><path d="M-6,8 q-10,0 -10,-10" fill="none" stroke="{C["ink"]}" stroke-width="2"/></g>')
o.append(tag(1272, 420, "a referee's whistle, Germany only", "start"))
# the ladder toward the sun
lx0, ly0, lx1, ly1 = 1456, GY, 1500, 430
o.append(f'<line x1="{lx0}" y1="{ly0}" x2="{lx1}" y2="{ly1}" stroke="{BARK}" stroke-width="7"/><line x1="{lx0+38}" y1="{ly0}" x2="{lx1+38}" y2="{ly1}" stroke="{BARK}" stroke-width="7"/>')
for k in range(1, 12):
    f = k / 12
    o.append(f'<line x1="{lx0+(lx1-lx0)*f:.1f}" y1="{ly0+(ly1-ly0)*f:.1f}" x2="{lx0+38+(lx1-lx0)*f:.1f}" y2="{ly0+(ly1-ly0)*f:.1f}" stroke="{BARK}" stroke-width="5"/>')
o.append(person(1507, 486, D["action"], kind="reach", s=0.9, skin="#9a623f"))
o.append(tag(1440, 470, "the bid platform, up the ladder:", "end"))
o.append(tag(1440, 500, "it owns the memory and wants the sun", "end"))
# ---- what a published check does for each
y = GY + 112
o.append(t(80, y, "The buyers", "caphead", C["ink"])); y += 28
for ln in ("1  the highway agency: a bid file the owner writes", "2  the public building owner: PDFs, every one read", "3  the megaproject: few knock", "4  the private owner: may shut the door", "5  the Construction Manager: answers to the owner"):
    o.append(t(80, y, ln, "tiny", C["ink2"])); y += 22
y += 6
for ln in wrap("They need volume without hiring, awards that survive a protest, and the door kept open. The law leaves a public buyer the fourth answer: a published check, with no cap, key or fee.", 48):
    o.append(t(80, y, ln, "note", C["ink"])); y += 24
y = GY + 112
o.append(t(620, y, "The bidders", "caphead", C["ink"])); y += 28
for ln in wrap("They want a check before the bid goes in, a fair and predictable hearing, and their own data kept their own. In the thicket a polished bid is only polish; a bid that read the same documents and priced the same quantities is the bidder showing it is alive.", 54):
    o.append(t(620, y, ln, "note", C["ink"])); y += 24
y = GY + 112
o.append(t(1220, y, "The vendors", "caphead", C["ink"])); y += 28
for ln in wrap("They need a target to build to and the referee nobody is building. Today the user pays and the vendor sells the shovel. With a standard they are test-takers, not targets, and the sun was never for sale.", 30):
    o.append(t(1220, y, ln, "note", C["ink"])); y += 24
o.append(t(80, H - 30, "Chapters 6a to 6c take the parties one at a time: who they are, what they need, and what a published check does for them.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 23px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.sign{{font:700 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.14em}}
.tag{{font:500 15px "IBM Plex Sans",Arial,sans-serif}}
.num{{font:700 16px "IBM Plex Sans",Arial,sans-serif}}
.plate{{font:700 18px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.08em}}
.micro{{font:700 11px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.08em}}
.micro2{{font:italic 400 13px "IBM Plex Sans",Arial,sans-serif}}
.caphead{{font:700 24px Georgia,serif}}
.note{{font:400 19px "IBM Plex Sans",Arial,sans-serif}}
.tiny{{font:italic 400 17px "IBM Plex Sans",Arial,sans-serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "three-parties"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
print("wrote", stem)
