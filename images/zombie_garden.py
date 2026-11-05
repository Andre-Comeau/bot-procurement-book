"""The zombie garden, the introduction's figure: construction documents shambling between the designer's and
the buyer's rooms, bidders round the wall, one living bot-first spec, a slain PDF, and a level-up HUD with the
four treasures. Usage: python zombie_garden.py <out-stem> [moonlit|ink|glass|two-tone]. Writes <stem>.svg and
<stem>.html; render the html to PNG at 1600 x 1040 (see images/README.md)."""
import random, math, sys
random.seed(11)
W, H = 1600, 1160
INK = "#1f1f1d"; LEAD = "#2c2c2a"
COB = "#0064ff"; COB_D = "#004fcc"; FOR = "#0f6e56"; FOR_D = "#085041"; RUST = "#d85a30"; RUST_D = "#9e3d18"
GOLD = "#e0a526"; PALE = "#fbf6e9"; GRASS = "#2f7d62"; GRASS2 = "#3d8f72"

THEMES = {
 "glass": dict(bg=PALE, tiles=[GRASS, GRASS2, "#276b54", "#358468"], tile_stroke=FOR_D, wall="#8a8780", room="#dfe9ff",
     designer=COB, buyer=FOR, bidder=RUST, hat=GOLD, door=GOLD, zfill="#d9e3c9", eye=RUST, dead="#b9c2a8",
     plaque=PALE, bidplaque="#f6d9cc", hud_bg=INK, accent=GOLD, cards=[FOR_D, "#003a99", RUST_D, "#8a5d0e"],
     icons=None, card_text=PALE, ztag_fill="#ffffff", ztag_stroke=FOR_D, xp=GOLD),
 "moonlit": dict(bg="#f4f1ea", tiles=["#24352f", "#2a3d36", "#203029", "#2e433b"], tile_stroke="#17221e", wall="#6f6a60",
     room="#f3e3b5", designer="#3b5b8c", buyer="#2f6b57", bidder="#b4532d", hat="#c99a3a", door="#c99a3a",
     zfill="#c9d4b0", eye="#d85a30", dead="#9aa38a", plaque="#f3e3b5", bidplaque="#f3e3b5", hud_bg="#1b1f1d",
     accent="#c99a3a", cards=["#26302c"]*4, icons=["#5fb393", "#6f9be0", "#e08455", "#d9ab4b"], card_text="#f4f1ea",
     ztag_fill="#f4f1ea", ztag_stroke="#17221e", xp="#e8c15a"),
 "two-tone": dict(bg=PALE, tiles=[FOR, "#13785e", "#0c6650", "#167f63"], tile_stroke=FOR_D, wall="#7d7a72",
     room=PALE, designer=INK, buyer=INK, bidder=RUST, hat=RUST_D, door=RUST, zfill="#efe9d8", eye=RUST, dead="#cfc8b4",
     plaque=PALE, bidplaque=PALE, hud_bg=FOR_D, accent=RUST, cards=["#0b3d31"]*4, icons=[RUST]*4, card_text=PALE,
     ztag_fill="#ffffff", ztag_stroke=FOR_D, xp="#f0b089"),
 "ink": dict(bg="#fbf8f1", tiles=["#ece6d6", "#e6dfcc", "#efe9db", "#e9e2d1"], tile_stroke="#d3cab4", wall="#8a8780",
     room="#ffffff", designer="#5f5e5a", buyer="#5f5e5a", bidder="#5f5e5a", hat=RUST, door=RUST, zfill="#ffffff",
     eye=RUST, dead="#e4dfd2", plaque="#ffffff", bidplaque="#ffffff", hud_bg=INK, accent=RUST, cards=["#3a3a37"]*4,
     icons=[RUST]*4, card_text="#fbf8f1", ztag_fill=INK, ztag_stroke="#fbf8f1", xp=RUST),
}
T = THEMES[sys.argv[2] if len(sys.argv) > 2 else "moonlit"]
o = [f'<rect width="{W}" height="{H}" fill="{T["bg"]}"/>']

# garden
GX0, GY0, GX1, GY1 = 120, 200, 1060, 1000
o.append('<g transform="translate(0,60)">')
o.append(f'<clipPath id="gclip"><rect x="{GX0}" y="{GY0}" width="{GX1-GX0}" height="{GY1-GY0}"/></clipPath><g clip-path="url(#gclip)">')
GX0, GY0, GX1, GY1 = 120, 200, 1060, 1000
# grass tiles, stained-glass style
for i in range(GX0, GX1, 47):
    for j in range(GY0, GY1, 47):
        c = random.choice(T["tiles"])
        o.append(f'<rect x="{i}" y="{j}" width="47" height="47" fill="{c}" stroke="{T["tile_stroke"]}" stroke-width="1.5"/>')
o.append('</g>')
o.append(f'<rect x="{GX0}" y="{GY0}" width="{GX1-GX0}" height="{GY1-GY0}" fill="none" stroke="{LEAD}" stroke-width="14"/>')
# wall stones
for x in range(GX0, GX1-30, 36):
    for y in (GY0, GY1):
        o.append(f'<rect x="{x-1}" y="{y-7}" width="34" height="14" fill="{T["wall"]}" stroke="{LEAD}" stroke-width="2"/>')
for y in range(GY0, GY1-30, 36):
    for x in (GX0, GX1):
        o.append(f'<rect x="{x-7}" y="{y-1}" width="14" height="34" fill="{T["wall"]}" stroke="{LEAD}" stroke-width="2"/>')

# two rooms, designer and buyer, with a lane between them for PDFs to flow
CX0, CY0, CX1, CY1 = 380, 480, 820, 720   # exclusion zone for random zombies
def plaque(x, y, text, w=None, fill=None):
    fill = fill or T["plaque"]
    w = w or (len(text) * 15 + 40)
    o.append(f'<rect x="{x-w/2}" y="{y-26}" width="{w}" height="40" rx="5" fill="{fill}" stroke="{LEAD}" stroke-width="3"/>')
    o.append(f'<text x="{x}" y="{y+5}" class="plq" text-anchor="middle">{text}</text>')
SKINS = ["#f1d7bd", "#e2b48c", "#c68a5e", "#9a623f", "#6e4329"]
HAIR = ["#2c2c2a", "#5a3a22", "#8a5a2b", "#b9b2a5", "#3b2a20"]
prng = random.Random(5)
def person(x, y, body, hat=None, s=1.0, kind="bidder"):
    """Front-view figure about 70px tall at s=1. kind: bidder, designer, buyer."""
    skin = prng.choice(SKINS); hair = prng.choice(HAIR)
    L = f'stroke="{LEAD}" stroke-width="{2.5*s:.1f}" stroke-linejoin="round" stroke-linecap="round"'
    g = [f'<g transform="translate({x},{y}) scale({s})">']
    # legs
    g.append(f'<path d="M-8,40 v18 M8,40 v18" stroke="{LEAD}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M-12,58 h8 M4,58 h8" stroke="{LEAD}" stroke-width="5" stroke-linecap="round"/>')
    # torso
    g.append(f'<path d="M-16,14 q16,-6 32,0 l3,28 h-38 z" fill="{body}" {L}/>')
    if kind == "bidder":   # hi-vis stripes
        g.append(f'<path d="M-15,26 h30 M-14,34 h28" stroke="#f3e9b0" stroke-width="3"/>')
    if kind == "buyer":    # shirt and tie
        g.append(f'<path d="M-5,11 l5,6 l5,-6" fill="#ffffff" {L}/><path d="M0,17 l-3,14 l3,4 l3,-4 z" fill="{RUST_D}" stroke="{LEAD}" stroke-width="1.5"/>')
    # head
    g.append(f'<circle cx="0" cy="0" r="11" fill="{skin}" {L}/>')
    if kind != "bidder" or prng.random() < 0.0:
        g.append(f'<path d="M-11,-2 q2,-12 11,-12 q9,0 11,12 q-4,-6 -11,-6 q-7,0 -11,6 z" fill="{hair}"/>')
    g.append(f'<circle cx="-4" cy="1" r="1.6" fill="{LEAD}"/><circle cx="4" cy="1" r="1.6" fill="{LEAD}"/>')
    if kind == "designer":  # glasses
        g.append(f'<circle cx="-4.5" cy="1" r="4" fill="none" stroke="{LEAD}" stroke-width="1.6"/><circle cx="4.5" cy="1" r="4" fill="none" stroke="{LEAD}" stroke-width="1.6"/><path d="M-0.5,1 h1" stroke="{LEAD}" stroke-width="1.6"/>')
    if hat:   # hard hat with brim
        g.append(f'<path d="M-11,-3 a11,10 0 0 1 22,0 z" fill="{hat}" {L}/><path d="M-14,-3 h28" {L}/><path d="M0,-13 v6" stroke="{LEAD}" stroke-width="1.5"/>')
    # arms and accessory
    acc = {"designer": "plans", "buyer": "briefcase"}.get(kind) or prng.choice(["clipboard", "calculator", "plans", "phone", "none"])
    if acc == "none":
        g.append(f'<path d="M-16,16 l-8,18 M16,16 l8,18" {L} fill="none"/>')
    else:
        g.append(f'<path d="M-16,16 l-8,18 M16,16 l2,14 l-8,4" {L} fill="none"/>')
    if acc == "clipboard":
        g.append(f'<rect x="-4" y="22" width="14" height="18" rx="1.5" fill="#c9a26a" {L}/><rect x="-1" y="25" width="8" height="12" fill="#ffffff"/><rect x="0" y="20" width="6" height="4" fill="{LEAD}"/>')
    elif acc == "calculator":
        g.append(f'<rect x="-3" y="24" width="12" height="16" rx="2" fill="#3b3b38" {L}/><rect x="-1" y="26" width="8" height="4" fill="#bfe3c9"/>')
    elif acc == "phone":
        g.append(f'<rect x="-1" y="24" width="8" height="13" rx="1.5" fill="#1f1f1d" {L}/>')
    elif acc == "plans":
        g.append(f'<g transform="rotate(-30 4 30)"><rect x="-8" y="26" width="26" height="8" rx="4" fill="#dbe8f7" {L}/><ellipse cx="18" cy="30" rx="2" ry="4" fill="#9fb8d8"/></g>')
    elif acc == "briefcase":
        g.append(f'<rect x="16" y="34" width="18" height="13" rx="2" fill="#6b4a1e" {L}/><path d="M21,34 v-3 h8 v3" fill="none" stroke="{LEAD}" stroke-width="2"/>')
    g.append('</g>')
    o.append("".join(g))
for (rx0, rx1, col, name) in ((400, 540, T["designer"], "Designer"), (680, 820, T["buyer"], "Buyer")):
    o.append(f'<rect x="{rx0}" y="520" width="{rx1-rx0}" height="170" fill="{T["room"]}" stroke="{LEAD}" stroke-width="10"/>')
    person((rx0+rx1)/2, 580, col, s=1.15, kind=("designer" if name == "Designer" else "buyer"))
    plaque((rx0+rx1)/2, 515, name, w=130)
    # door on the lane side
    dx = rx1 if rx0 < 600 else rx0
    o.append(f'<rect x="{dx-8}" y="585" width="16" height="44" fill="{T["door"]}" stroke="{LEAD}" stroke-width="3"/>')
# bidders around perimeter, outside the wall
bidders = [(x, 150) for x in (200, 340, 480, 720, 860, 1000)]
bidders += [(x, 1040) for x in (270, 430, 590, 750, 910, 1070)]
for y in range(300, 960, 170):
    bidders.append((70, y)); bidders.append((1110, y+60))
for i, (x, y) in enumerate(bidders):
    person(x, y - 30, T["bidder"], hat=T["hat"], s=0.9, kind="bidder")

# zombie documents
docs = ["Drawings", "Specifications", "Addendum 1", "Addendum 2", "Addendum 3", "RFI", "RFI response",
        "Bid form", "Bid bond", "Instructions to bidders", "Unit price form", "Geotech report",
        "Change order", "Shop drawing", "Submittal", "Schedule", "Contract", "Q&A log",
        "Bill of quantities", "Site photos", "Permit", "Insurance cert."]
def zombie(x, y, label, rot, live=False):
    fill = T["zfill"] if not live else "#ffffff"
    edge = LEAD if not live else COB
    eye = T["eye"] if not live else COB
    g = [f'<g transform="translate({x},{y}) rotate({rot})">']
    if live:
        g.append(f'<circle cx="0" cy="0" r="42" fill="{COB}" fill-opacity="0.25"/>')
    g.append(f'<path d="M-24,22 l-6,22 M8,22 l8,22" stroke="{LEAD}" stroke-width="4" stroke-linecap="round"/>')  # legs
    arms = (f'<path d="M-24,-10 l-24,-8 M24,-10 l26,-12" stroke="{LEAD}" stroke-width="4" stroke-linecap="round"/>' if not live
            else f'<path d="M-24,-6 l-18,10 M24,-6 l18,10" stroke="{LEAD}" stroke-width="4" stroke-linecap="round"/>')
    g.append(arms)
    g.append(f'<path d="M-24,-32 h34 l14,14 v40 h-48 z" fill="{fill}" stroke="{edge}" stroke-width="3"/>')
    g.append(f'<path d="M10,-32 v14 h14" fill="none" stroke="{edge}" stroke-width="2.5"/>')
    for ly in (6, 13):
        g.append(f'<path d="M-16,{ly} h28" stroke="#8b927f" stroke-width="2"/>')
    if live:
        g.append(f'<path d="M-12,-14 q6,8 12,0" fill="none" stroke="{COB}" stroke-width="2.5"/>')
    g.append(f'<circle cx="-10" cy="-18" r="3.5" fill="{eye}"/><circle cx="2" cy="-18" r="3.5" fill="{eye}"/>')
    g.append('</g>')
    o.append("".join(g))
    o.append(f'<text x="{x}" y="{y+60}" class="ztag" text-anchor="middle">{label}</text>')
DEADX, DEADY = 940, 880
# random placement (rejection sampling), avoiding the rooms and keeping zombies apart
spots = []
tries = 0
while len(spots) < 23 and tries < 20000:
    tries += 1
    x = random.uniform(GX0 + 70, GX1 - 70); y = random.uniform(GY0 + 70, GY1 - 80)
    if 360 < x < 860 and 430 < y < 760:
        continue
    if (x-DEADX)**2 + (y-DEADY)**2 < 150**2:
        continue
    if all((x-a)**2 + (y-b)**2 > 125**2 for a, b in spots):
        spots.append((x, y))
random.shuffle(spots)
live_i = 7
for i, (x, y) in enumerate(spots[:len(docs) + 1]):
    if i == live_i:
        zombie(x, y, "bot-first spec", random.uniform(-6, 6), live=True)
    else:
        lab = docs[i if i < live_i else i - 1]
        sc = random.uniform(0.75, 1.25)
        o.append(f'<g transform="translate({x},{y}) scale({sc:.2f}) translate({-x},{-y})">')
        zombie(x, y, lab, random.uniform(-40, 40))
        o.append('</g>')

# PDFs flowing in the lane between designer and buyer
for (lx, ly, lab, r) in ((610, 560, "Addendum 4", -8), (612, 680, "Revised drawing", 10)):
    o.append(f'<g transform="translate({lx},{ly}) scale(0.8) translate({-lx},{-ly})">')
    zombie(lx, ly, lab, r)
    o.append('</g>')
# the slain zombie: flat on its back, X eyes, a stake through it, XP rising toward the HUD
dx, dy = DEADX, DEADY
o.append(f'<ellipse cx="{dx}" cy="{dy+30}" rx="70" ry="16" fill="{T["tile_stroke"]}" fill-opacity="0.6"/>')
o.append(f'<g transform="translate({dx},{dy}) rotate(84)">'
         f'<path d="M-24,22 l-3,24 M8,22 l4,24 M-24,-10 l-28,0 M24,-10 l28,0" stroke="{LEAD}" stroke-width="4" stroke-linecap="round"/>'
         f'<path d="M-24,-32 h34 l14,14 v40 h-48 z" fill="{T["dead"]}" stroke="{LEAD}" stroke-width="3"/>'
         f'<path d="M10,-32 v14 h14" fill="none" stroke="{LEAD}" stroke-width="2.5"/>'
         f'<path d="M-14,-23 l8,8 M-6,-23 l-8,8 M0,-23 l8,8 M8,-23 l-8,8" stroke="{RUST_D}" stroke-width="3"/>'
         f'</g>')
o.append(f'<path d="M{dx+6},{dy-60} L{dx-2},{dy+8}" stroke="#6b4a1e" stroke-width="7" stroke-linecap="round"/>')
o.append(f'<path d="M{dx-8},{dy-46} L{dx+18},{dy-42}" stroke="#6b4a1e" stroke-width="6" stroke-linecap="round"/>')
o.append(f'<text x="{dx}" y="{dy+70}" class="ztag" text-anchor="middle">PDF (slain)</text>')
for k, (ox, oy, t) in enumerate(((40, -20, "+XP"), (58, -56, "+XP"))):
    o.append(f'<text x="{dx+ox}" y="{dy+oy}" class="xp">{t}</text>')
plaque(600, 150, "The Bidders", w=180, fill=T["bidplaque"])
o.append('</g>')
def icon(k, x, y, col):
    st = f'stroke="{col}" stroke-width="3.5" fill="none" stroke-linejoin="round" stroke-linecap="round"'
    if k == 0:   # hourglass
        o.append(f'<path d="M{x-14},{y-18} h28 M{x-14},{y+18} h28 M{x-11},{y-18} q0,14 11,18 q-11,4 -11,18 M{x+11},{y-18} q0,14 -11,18 q11,4 11,18" {st}/>')
        o.append(f'<path d="M{x-6},{y+14} q6,-8 12,0 z" fill="{col}"/>')
    elif k == 1: # sealed envelope
        o.append(f'<rect x="{x-18}" y="{y-12}" width="36" height="25" {st}/><path d="M{x-18},{y-12} l18,14 l18,-14" {st}/>')
        o.append(f'<circle cx="{x}" cy="{y+6}" r="7" fill="{RUST}" stroke="{LEAD}" stroke-width="1.5"/>')
    elif k == 2: # isometric cube
        o.append(f'<path d="M{x},{y-18} l17,9 v19 l-17,9 l-17,-9 v-19 z M{x-17},{y-9} l17,9 l17,-9 M{x},{y} v19" {st}/>')
    else:        # robot head
        o.append(f'<rect x="{x-15}" y="{y-10}" width="30" height="24" rx="4" {st}/><path d="M{x},{y-10} v-8" {st}/><circle cx="{x}" cy="{y-20}" r="3" fill="{col}"/>')
        o.append(f'<circle cx="{x-6}" cy="{y}" r="3" fill="{col}"/><circle cx="{x+6}" cy="{y}" r="3" fill="{col}"/><path d="M{x-6},{y+8} h12" {st}/>')
# HUD: level-up panel
HX, HY, HW, HH = 1190, 230, 370, 830
o.append(f'<rect x="{HX}" y="{HY}" width="{HW}" height="{HH}" rx="14" fill="{T["hud_bg"]}" stroke="{T["accent"]}" stroke-width="5"/>')
o.append(f'<text x="{HX+HW/2}" y="{HY+62}" class="hudt" text-anchor="middle">LEVEL UP!</text>')
o.append(f'<text x="{HX+HW/2}" y="{HY+96}" class="huds" text-anchor="middle">Zombie slain. Choose your treasure.</text>')
abilities = [
    (FOR_D, "Freed Time", "Hand the take-offs", "to the bots. Spend the", "hours on creation."),
    ("#003a99", "Sealed Alternates", "Propose a better build;", "the standard bot gives", "the review certainty."),
    (RUST_D, "BIM Vision", "The model becomes the", "tender, not a secondary", "reference."),
    ("#8a5d0e", "Robot Command", "Robots program", "themselves from the", "documents you priced."),
]
for k, (col, name, *lines) in enumerate(abilities):
    y = HY + 130 + k * 170
    o.append(f'<rect x="{HX+22}" y="{y}" width="{HW-44}" height="150" rx="10" fill="{T["cards"][k] if T["icons"] else col}" stroke="{T["accent"]}" stroke-width="3"/>')
    o.append(f'<rect x="{HX+38}" y="{y+18}" width="54" height="54" rx="8" fill="{T["card_text"] if not T["icons"] else T["hud_bg"]}" stroke="{LEAD}" stroke-width="2.5"/>')
    icon(k, HX+65, y+45, T["icons"][k] if T["icons"] else col)
    o.append(f'<text x="{HX+106}" y="{y+54}" class="abn" fill="{T["card_text"]}">{name}</text>')
    for j, l in enumerate(lines):
        o.append(f'<text x="{HX+40}" y="{y+96+j*21}" class="abl" fill="{T["card_text"]}">{l}</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H-120}" viewBox="0 120 {W} {H-120}">
<style>
.title{{font-family:'Instrument Serif',Georgia,serif;font-size:60px;fill:{INK}}}
.dek{{font-family:Lora,Georgia,serif;font-style:italic;font-size:22px;fill:#5f5e5a}}
.tag{{font-family:Outfit,sans-serif;font-weight:600;font-size:20px;fill:{INK}}}
.tagw{{font-family:Outfit,sans-serif;font-weight:600;font-size:17px}}
.plq{{font-family:'Instrument Serif',Georgia,serif;font-size:28px;fill:{INK}}}
.xp{{font-family:Outfit,sans-serif;font-weight:600;font-size:22px;fill:{T["xp"]};paint-order:stroke;stroke:{T["ztag_stroke"]};stroke-width:4px}}
.ztag{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;fill:{T["ztag_fill"]};paint-order:stroke;stroke:{T["ztag_stroke"]};stroke-width:4px}}
.hudt{{font-family:Outfit,sans-serif;font-weight:600;font-size:40px;letter-spacing:.12em;fill:{T["accent"]}}}
.huds{{font-family:Lora,Georgia,serif;font-style:italic;font-size:19px;fill:{PALE}}}
.abn{{font-family:Outfit,sans-serif;font-weight:600;font-size:25px}}
.abl{{font-family:Lora,Georgia,serif;font-size:17px}}
.icon{{font-family:Outfit,sans-serif;font-weight:600;font-size:30px}}
</style>{"".join(o)}</svg>'''
open(sys.argv[1]+".svg","w").write(svg)
open(sys.argv[1]+".html","w").write(f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Lora:ital@0;1&family=Outfit:wght@400;600&display=block" rel="stylesheet">
<style>html,body{{margin:0;background:{T["bg"]}}}</style></head><body>{svg}</body></html>''')
