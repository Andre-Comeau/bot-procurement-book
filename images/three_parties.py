"""Three parties at the door: the buyers, the bidders and the vendors (chapters 7a, 7b and 7e, three panels).
Usage: python images/three_parties.py images/three-parties   (writes the .svg and an .html; render at 1600 1530, see images/README.md)
"""
import sys, html, math, random
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
D = {k: mix(C[k], C["ink"], 0.2) for k in ("action", "sec", "acc", "ink2")}
W, H = 1600, 1530
GOLD = "#e0a526"; BARK = mix(C["acc"], C["ink"], 0.55)
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
def person(x, y, body, s=1.0):
    g = [f'<g transform="translate({x},{y}) scale({s})">']
    g.append(f'<path d="M-8,40 v18 M8,40 v18" stroke="{C["ink"]}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M-12,58 h8 M4,58 h8" stroke="{C["ink"]}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M-16,14 q16,-6 32,0 l3,28 h-38 z" fill="{body}" {L}/>')
    g.append(f'<circle cx="0" cy="0" r="11" fill="#e2b48c" {L}/>')
    g.append(f'<path d="M-11,-2 q2,-12 11,-12 q9,0 11,12 q-4,-6 -11,-6 q-7,0 -11,6 z" fill="{C["ink"]}"/>')
    g.append(f'<circle cx="-4" cy="1" r="1.6" fill="{C["ink"]}"/><circle cx="4" cy="1" r="1.6" fill="{C["ink"]}"/>')
    g.append(f'<path d="M-16,16 l-8,18 M16,16 l8,18" {L} fill="none"/>')
    g.append('</g>')
    return "".join(g)
def sun(x, y, r):
    g = []
    for k in range(8):
        a = k * math.pi / 4
        g.append(f'<line x1="{x+math.cos(a)*(r+6):.1f}" y1="{y+math.sin(a)*(r+6):.1f}" x2="{x+math.cos(a)*(r+16):.1f}" y2="{y+math.sin(a)*(r+16):.1f}" stroke="{GOLD}" stroke-width="3.5" stroke-linecap="round"/>')
    g.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{GOLD}"/>')
    return "".join(g)
TOP, BOT, CW = 250, 1190, 460
XS = (80, 570, 1060)
BAND = 190
o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append(t(80, 86, "CHAPTERS 7A, 7B AND 7E · THE BUYERS, THE BIDDERS, THE VENDORS", "eyebrow"))
o.append(t(80, 148, "Three parties at the door", "title"))
o.append(t(80, 190, "Each party's chapter asks the same questions: who they are, what they need from the tender,", "dek"))
o.append(t(80, 218, "and what a published check gives them. Below the three, the answer they cannot give each other: a standard, and someone behind its number.", "dek"))
# ---- icons, drawn inside the tinted band at the top of each panel
def icon_buyers(bx, by):
    gy = by + BAND - 14; g = []
    g.append(f'<line x1="{bx+30}" y1="{gy}" x2="{bx+430}" y2="{gy}" stroke="{C["ink2"]}" stroke-width="2"/>')
    g.append(f'<rect x="{bx+70}" y="{gy-125}" width="78" height="125" fill="{D["action"]}" stroke="{C["ink"]}" stroke-width="3"/>')
    g.append(f'<rect x="{bx+80}" y="{gy-115}" width="58" height="105" fill="none" stroke="{C["action_t"]}" stroke-width="1.5"/>')
    g.append(f'<circle cx="{bx+136}" cy="{gy-62}" r="4.5" fill="{GOLD}"/>')
    rnd = random.Random(7); yy = gy; k = 0
    while yy > gy - 150:
        h = rnd.choice((8, 9, 10)); jit = rnd.uniform(-5, 5)
        g.append(f'<rect x="{bx+200+jit:.1f}" y="{yy-h}" width="124" height="{h}" fill="#ffffff" stroke="{C["ink"]}" stroke-width="1.2"/>')
        if k % 5 == 2:
            g.append(f'<rect x="{bx+206+jit:.1f}" y="{yy-h+2}" width="24" height="{h-4}" fill="{C["acc"]}"/>')
        yy -= h; k += 1
    g.append(person(bx + 385, gy - 47, "#ffffff", 0.8))
    return "".join(g)
def icon_bidders(bx, by):
    gy = by + BAND - 14; g = []
    g.append(f'<line x1="{bx+30}" y1="{gy}" x2="{bx+430}" y2="{gy}" stroke="{C["ink2"]}" stroke-width="2"/>')
    g.append(sun(bx + 395, by + 50, 26))
    hs = (62, 96, 74, 128, 86, 112, 70, 150, 92, 120, 80)
    cols = (C["sec"], D["sec"], mix(C["sec"], C["canvas"], 0.3))
    for k, h in enumerate(hs):
        x = bx + 58 + k * 30; bend = 10 + h * 0.16; col = cols[k % 3]
        g.append(f'<path d="M{x},{gy} q{bend*0.4:.1f},-{h*0.55:.1f} {bend:.1f},-{h}" fill="none" stroke="{col}" stroke-width="3.5" stroke-linecap="round"/>')
        for j in range(3):
            f = 0.4 + 0.27 * j; ly = gy - h * f; lx = x + bend * f * 0.9; side = 1 if j % 2 == 0 else -1
            g.append(f'<ellipse cx="{lx+side*9:.1f}" cy="{ly:.1f}" rx="10" ry="4.5" fill="{col}" transform="rotate({-28*side} {lx+side*9:.1f} {ly:.1f})"/>')
    return "".join(g)
def icon_vendors(bx, by):
    gy = by + BAND - 14; g = []
    g.append(f'<line x1="{bx+30}" y1="{gy}" x2="{bx+430}" y2="{gy}" stroke="{C["ink2"]}" stroke-width="2"/>')
    g.append(f'<rect x="{bx+60}" y="{gy-60}" width="190" height="60" fill="{BARK}" stroke="{C["ink"]}" stroke-width="2.5"/>')
    g.append(f'<rect x="{bx+50}" y="{gy-70}" width="210" height="11" fill="{mix(BARK, C["ink"], 0.3)}" stroke="{C["ink"]}" stroke-width="2.5"/>')
    # a whistle on the counter
    g.append(f'<rect x="{bx+118}" y="{gy-92}" width="40" height="18" rx="9" fill="{GOLD}" {L}/>')
    g.append(f'<rect x="{bx+152}" y="{gy-88}" width="22" height="10" rx="2" fill="{GOLD}" {L}/>')
    g.append(f'<circle cx="{bx+114}" cy="{gy-76}" r="6" fill="none" {L}/>')
    # a shovel leaning on the counter, with a tag
    g.append(f'<path d="M{bx+300},{gy-2} q-18,-6 -16,-26 l6,-26 h26 l6,26 q2,20 -16,26 z" fill="{mix(C["ink2"], C["canvas"], 0.35)}" {L}/>')
    g.append(f'<line x1="{bx+307}" y1="{gy-54}" x2="{bx+352}" y2="{gy-168}" stroke="{BARK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M{bx+344},{gy-166} l-14,-8 l12,-16 l16,8 z" fill="none" stroke="{BARK}" stroke-width="6" stroke-linejoin="round"/>')
    g.append(f'<line x1="{bx+330}" y1="{gy-112}" x2="{bx+352}" y2="{gy-96}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    g.append(f'<rect x="{bx+350}" y="{gy-100}" width="40" height="24" rx="3" fill="#ffffff" {L}/>')
    g.append(f'<circle cx="{bx+357}" cy="{gy-88}" r="2" fill="{C["ink"]}"/>')
    # the sun, tagged
    g.append(sun(bx + 395, by + 44, 22))
    g.append(f'<line x1="{bx+395}" y1="{by+66}" x2="{bx+395}" y2="{by+92}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    g.append(f'<rect x="{bx+338}" y="{by+92}" width="114" height="30" rx="3" fill="#ffffff" {L}/>')
    g.append(t(bx + 395, by + 113, "not for sale", "tagtext", C["ink"], "middle"))
    return "".join(g)
parties = [
    dict(name="The buyers", sub="more bids than eyes", tint=C["action_t"], dark=D["action"], icon=icon_buyers,
         q="Their question: what should the work cost?",
         need=["Volume handled without hiring", "Decisions that survive a challenge", "The door kept open, as the law asks",
               "Time back: funds freed sooner", "Capacity on jobs too big for one head"],
         gives=["Same bid, same answer, measured miss", "No cap, no key, no fee at the door",
                "Claims checked against evidence", "A shorter tender, an earlier award", "Who is liable when a bot is wrong"],
         catch=["Two answers to one bid invite a claim;", "their records become the market's memory."]),
    dict(name="The bidders", sub="racing for the light", tint=C["sec_t"], dark=D["sec"], icon=icon_bidders,
         q="Their question: what will it cost us, and what will it take to win?",
         need=["A check before the bid goes in", "Trust in bids a manager did not build", "Fewer wasted bids: five in six lose",
               "Same bid, same answer, reasons given", "Room to spread the price their own way", "Their own data kept their own"],
         gives=["A cheaper bid, with the margin covered", "A growing pie: more projects built",
                "The surgical team in as a principal", "Proof of life in a polished thicket"],
         catch=["The record proves what they knew;", "everyone leaning on the same bot."]),
    dict(name="The vendors", sub="players, not referees", tint=C["acc_t"], dark=D["acc"], icon=icon_vendors,
         q="Their terms: the user verifies, and the user pays.",
         need=["A strict, public format to build to", "Demand from users carrying the risk",
               "Protection from the general models", "Their moat kept: data, service, habit"],
         gives=["Test-takers, not targets", "The referee nobody is building",
                "A premium an underwriter can price", "The sun was never for sale"],
         catch=["Credible cheap code squeezes margins;", "every incumbent wants the pen."]),
]
NAME_Y = TOP + BAND + 52
Y_NEED = NAME_Y + 66 + 2 * 26 + 24
Y_GIVES = Y_NEED + 38 + 6 * 30 + 16
Y_CATCH = Y_GIVES + 38 + 5 * 30 + 16
def block(x, y, label, items, col, cls):
    o.append(t(x + 24, y, label, "blab", col))
    o.append(f'<line x1="{x+24}" y1="{y+10}" x2="{x+CW-24}" y2="{y+10}" stroke="{C["hair"]}" stroke-width="2"/>')
    y += 38
    for it in items:
        o.append(f'<rect x="{x+24}" y="{y-13}" width="9" height="9" fill="{col}"/>')
        o.append(t(x + 44, y, it, cls, C["ink"] if cls == "item" else C["ink2"]))
        y += 30
for x, p in zip(XS, parties):
    o.append(f'<rect x="{x}" y="{TOP}" width="{CW}" height="{BOT-TOP}" rx="10" fill="#ffffff" stroke="{C["hair"]}" stroke-width="2"/>')
    o.append(f'<path d="M{x},{TOP+10} a10,10 0 0 1 10,-10 h{CW-20} a10,10 0 0 1 10,10 v{BAND-10} h-{CW} z" fill="{p["tint"]}"/>')
    o.append(p["icon"](x, TOP))
    o.append(t(x + 24, NAME_Y, p["name"], "lab", C["ink"]))
    o.append(t(x + 24, NAME_Y + 30, p["sub"], "sub", C["ink2"]))
    y = NAME_Y + 66
    for ln in wrap(p["q"], 42):
        o.append(t(x + 24, y, ln, "q", C["ink"])); y += 26
    block(x, Y_NEED, "WHAT THEY NEED", p["need"], p["dark"], "item")
    block(x, Y_GIVES, "WHAT A PUBLISHED CHECK GIVES THEM", p["gives"], p["dark"], "item")
    block(x, Y_CATCH, "THE CATCH", p["catch"], D["acc"], "catch")
def icon_rules(x, y):
    g = [f'<rect x="{x}" y="{y}" width="64" height="84" rx="3" fill="#ffffff" {L}/>']
    for k in range(4):
        g.append(f'<line x1="{x+12}" y1="{y+18+k*13}" x2="{x+52}" y2="{y+18+k*13}" stroke="{C["ink2"]}" stroke-width="2.5"/>')
    g.append(f'<path d="M{x+16},{y+70} l9,9 l23,-22" fill="none" stroke="{C["sec"]}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>')
    return "".join(g)
def icon_umbrella(x, y):
    g = [f'<path d="M{x},{y+42} a32,32 0 0 1 64,0 q-8,-8 -16,0 q-8,-8 -16,0 q-8,-8 -16,0 q-8,-8 -16,0 z" fill="{C["action_t"]}" {L}/>']
    g.append(f'<line x1="{x+32}" y1="{y+10}" x2="{x+32}" y2="{y+4}" {L}/>')
    g.append(f'<line x1="{x+32}" y1="{y+42}" x2="{x+32}" y2="{y+80}" stroke="{C["ink"]}" stroke-width="4"/>')
    g.append(f'<path d="M{x+32},{y+80} a8,8 0 0 1 -16,0" fill="none" stroke="{C["ink"]}" stroke-width="3.5" stroke-linecap="round"/>')
    return "".join(g)
BY0, BH = BOT + 30, 236
for x in XS:
    o.append(f'<line x1="{x+CW/2}" y1="{BOT}" x2="{x+CW/2}" y2="{BY0}" stroke="{C["ink2"]}" stroke-width="2.5"/>')
o.append(f'<rect x="80" y="{BY0}" width="{W-160}" height="{BH}" rx="10" fill="{mix(C["hair"], C["canvas"], 0.55)}" stroke="{C["ink"]}" stroke-width="2"/>')
o.append(t(104, BY0 + 40, "THE ANSWER THEY CANNOT GIVE EACH OTHER", "bhead", C["ink"]))
o.append(t(104, BY0 + 72, "The three meet as principals, none the agent or partner of another, so the answer has to stand outside them: a standard, and someone behind its number.", "bsub", C["ink2"]))
halves = [
    (104, "The standard", icon_rules, "A published check: the same answer to the same bid, a measured miss rate, and a record of what was checked. The referee none of the three can be for the others."),
    (820, "Behind the number", icon_umbrella, "The buyer stands behind the standard bot's number. Insurance on the margin, priced from the test's measured misses, covers those who cannot carry the misses alone."),
]
for hx, name, icon, body in halves:
    o.append(icon(hx, BY0 + 104))
    o.append(t(hx + 90, BY0 + 128, name, "ans", C["ink"]))
    yy = BY0 + 160
    for ln in wrap(body, 56):
        o.append(t(hx + 90, yy, ln, "anstext", C["ink"])); yy += 26
o.append(t(80, H - 40, "Each list is its chapter's sentences, shortened; who carries the loss is chapters 3 and 7g.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 23px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.sub{{font:italic 400 21px "IBM Plex Sans",Arial,sans-serif}}
.q{{font:italic 400 20px "IBM Plex Sans",Arial,sans-serif}}
.blab{{font:600 16px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.1em}}
.item{{font:400 20px "IBM Plex Sans",Arial,sans-serif}}
.catch{{font:italic 400 20px "IBM Plex Sans",Arial,sans-serif}}
.tagtext{{font:600 17px "IBM Plex Sans",Arial,sans-serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
.bhead{{font:600 18px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.1em}}
.bsub{{font:italic 400 20px "IBM Plex Sans",Arial,sans-serif}}
.ans{{font:700 26px Georgia,serif}}
.anstext{{font:400 20px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "three-parties"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
print("wrote", stem, "blocks at", Y_NEED, Y_GIVES, Y_CATCH)
