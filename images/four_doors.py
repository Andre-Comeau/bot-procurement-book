"""Four ways to answer a flooded door: cap, key, fee, published check (chapter 1, schematic).
Usage: python images/four_doors.py images/four-doors   (writes the .svg and an .html; render at 1600 1210, see images/README.md)
"""
import sys, html
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
D = {k: mix(C[k], C["ink"], 0.2) for k in ("action", "sec", "acc", "ink2")}
W, H = 1600, 1210
GOLD = "#e0a526"
SLAB = mix(C["ink2"], C["canvas"], 0.45)
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
o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append(t(80, 86, "CHAPTER 1 · FOUR WAYS TO ANSWER A FLOODED DOOR", "eyebrow"))
o.append(t(80, 148, "Four ways to answer a flooded door", "title"))
o.append(t(80, 190, "Software has four answers to a flooded interface. Construction has a twin for each,", "dek"))
o.append(t(80, 218, "and the twins show which answers a public buyer can live with.", "dek"))
COLS = [
    dict(name="Cap", sub="limit how often anyone may call",
         online="Clarkesworld closed its door. arXiv allows two papers a month.",
         constr="The shortlist, allowed only when it is announced in advance with the criteria stated.",
         verdict="Hits good and bad callers alike.", good=False),
    dict(name="Key", sub="decide who may call",
         online="Tighter rules on who may vouch for a newcomer.",
         constr="Prequalification and capacity ratings. Trade law bars a public buyer from requiring prior contracts.",
         verdict="Says who sent it, not whether it is right.", good=False),
    dict(name="Fee", sub="charge for each call",
         online="Make the sender pay, proposed in 1992. A price high enough to stop spam blocks honest senders too.",
         constr="The bid bond. Participation falls wherever a charge is levied.",
         verdict="Falls hardest on the newcomers.", good=False),
    dict(name="Published check", sub="check every call against rules anyone can read",
         online="From 2024, bulk mail must authenticate under public standards. Unauthenticated mail fell by about 65 percent.",
         constr="The price read against the market's record, and claims pointed at evidence.",
         verdict="The only answer that scales without shutting anyone out.", good=True),
]
DY0, DY1 = 290, 610
for i, c in enumerate(COLS):
    x0 = 80 + i * 365; w = 320
    fx0, fx1 = x0 + 60, x0 + 260
    slab = D["sec"] if c["good"] else SLAB
    # frame
    o.append(f'<rect x="{fx0-12}" y="{DY0-12}" width="{fx1-fx0+24}" height="{DY1-DY0+12}" fill="{mix(C["ink2"], C["canvas"], 0.3)}" stroke="{C["ink"]}" stroke-width="7"/>')
    if not c["good"]:
        o.append(f'<rect x="{fx0}" y="{DY0}" width="{fx1-fx0}" height="{DY1-DY0}" fill="{slab}" stroke="{C["ink"]}" stroke-width="3"/>')
        o.append(f'<rect x="{fx0+22}" y="{DY0+26}" width="{fx1-fx0-44}" height="110" rx="3" fill="none" stroke="{C["ink"]}" stroke-width="2" opacity="0.5"/>')
        o.append(f'<rect x="{fx0+22}" y="{DY0+170}" width="{fx1-fx0-44}" height="120" rx="3" fill="none" stroke="{C["ink"]}" stroke-width="2" opacity="0.5"/>')
        o.append(f'<circle cx="{fx1-34}" cy="{DY0+165}" r="8" fill="{C["ink"]}"/>')
    else:
        # door ajar: light from the opening, the slab swung inward
        o.append(f'<rect x="{fx0}" y="{DY0}" width="{fx1-fx0}" height="{DY1-DY0}" fill="{mix(GOLD, "#ffffff", 0.55)}"/>')
        o.append(f'<path d="M{fx0},{DY0} L{fx0+118},{DY0+34} L{fx0+118},{DY1-24} L{fx0},{DY1} Z" fill="{slab}" stroke="{C["ink"]}" stroke-width="3"/>')
        o.append(f'<circle cx="{fx0+100}" cy="{DY0+170}" r="7" fill="{C["ink"]}"/>')
    # devices
    if c["name"] == "Cap":
        o.append(f'<rect x="{fx0+40}" y="{DY0+62}" width="{fx1-fx0-80}" height="40" rx="4" fill="#ffffff" stroke="{C["ink"]}" stroke-width="2.5"/>')
        o.append(t((fx0+fx1)/2, DY0+90, "2 a month", "plate", C["ink"], "middle"))
        # rope barrier in front of the door
        for px in (fx0-30, fx1+30):
            o.append(f'<rect x="{px-5}" y="{DY1-80}" width="10" height="80" rx="3" fill="{D["acc"]}"/>')
            o.append(f'<circle cx="{px}" cy="{DY1-84}" r="9" fill="{D["acc"]}"/>')
        o.append(f'<path d="M{fx0-30},{DY1-76} q{(fx1-fx0+60)/2},56 {fx1-fx0+60},0" fill="none" stroke="{C["acc"]}" stroke-width="6" stroke-linecap="round"/>')
    elif c["name"] == "Key":
        kx, ky = (fx0+fx1)/2, DY0+150
        o.append(f'<circle cx="{kx}" cy="{ky}" r="22" fill="{C["ink"]}"/><path d="M{kx-12},{ky+10} l-10,52 h44 l-10,-52 z" fill="{C["ink"]}"/>')
        # a key on a hook beside the door
        hx, hy = fx1 + 44, DY0 + 120
        o.append(f'<path d="M{hx},{hy-30} q0,-14 12,-14" fill="none" stroke="{C["ink"]}" stroke-width="3"/>')
        o.append(f'<circle cx="{hx}" cy="{hy}" r="18" fill="none" stroke="{D["acc"]}" stroke-width="7"/>')
        o.append(f'<path d="M{hx},{hy+18} v78 M{hx},{hy+60} h14 M{hx},{hy+80} h20" fill="none" stroke="{D["acc"]}" stroke-width="7" stroke-linecap="round"/>')
    elif c["name"] == "Fee":
        sx, sy = (fx0+fx1)/2, DY0+150
        o.append(f'<rect x="{sx-58}" y="{sy-30}" width="116" height="60" rx="6" fill="#ffffff" stroke="{C["ink"]}" stroke-width="2.5"/>')
        o.append(f'<rect x="{sx-26}" y="{sy-6}" width="52" height="12" rx="3" fill="{C["ink"]}"/>')
        o.append(t(sx, sy-12, "INSERT BOND", "micro", C["ink2"], "middle"))
        cx, cy = fx1 + 46, DY0 + 150
        o.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="{GOLD}" stroke="{C["ink"]}" stroke-width="3"/><circle cx="{cx}" cy="{cy}" r="17" fill="none" stroke="{C["ink"]}" stroke-width="2" opacity="0.6"/>')
    else:
        # the rules, posted beside the door for anyone to read
        px, py = fx1 + 10, DY0 + 40
        o.append(f'<rect x="{px}" y="{py}" width="84" height="110" rx="3" fill="#ffffff" stroke="{C["ink"]}" stroke-width="2.5"/>')
        for k in range(5):
            yy = py + 22 + k * 18
            o.append(f'<path d="M{px+10},{yy} l5,5 l9,-11" fill="none" stroke="{D["sec"]}" stroke-width="2.5" stroke-linecap="round"/>')
            o.append(f'<line x1="{px+30}" y1="{yy}" x2="{px+72}" y2="{yy}" stroke="{C["ink2"]}" stroke-width="2.5" opacity="0.6"/>')
        o.append(t(px+42, py+134, "the rules,", "micro", C["ink2"], "middle"))
        o.append(t(px+42, py+150, "posted", "micro", C["ink2"], "middle"))
    # text
    y = DY1 + 70
    o.append(t(x0, y, c["name"], "lab", C["ink"]))
    y += 30
    for ln in wrap(c["sub"], 32):
        o.append(t(x0, y, ln, "sub", C["ink2"]))
        y += 26
    y += 18
    for head, body in (("Online.", c["online"]), ("Construction.", c["constr"])):
        lines = wrap(head + " " + body, 31)
        for j, ln in enumerate(lines):
            if j == 0:
                o.append(f'<text x="{x0}" y="{y}" class="note" fill="{C["ink"]}"><tspan font-weight="700">{html.escape(head)}</tspan>{html.escape(ln[len(head):])}</text>')
            else:
                o.append(t(x0, y, ln, "note", C["ink"]))
            y += 27
        y += 12
    vcol = D["sec"] if c["good"] else D["acc"]
    for ln in wrap(c["verdict"], 24):
        o.append(t(x0, y, ln, "verdict", vcol))
        y += 30
# the bottom line
o.append(f'<line x1="80" y1="1082" x2="{W-80}" y2="1082" stroke="{C["hair"]}" stroke-width="2"/>')
o.append(t(80, 1120, "Each of the first three helps one party at another's expense. The buyer gets less to read, and the newcomer gets the door.", "note", C["ink"]))
o.append(t(80, H-40, "Highway construction already has all four in rough form. The written parts of a bid have none, and that is where the thicket is growing.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 24px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.sub{{font:italic 400 20px "IBM Plex Sans",Arial,sans-serif}}
.note{{font:400 20px "IBM Plex Sans",Arial,sans-serif}}
.verdict{{font:700 24px Georgia,serif}}
.plate{{font:700 24px "IBM Plex Sans",Arial,sans-serif}}
.micro{{font:600 12px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.06em}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "four-doors"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
print("wrote", stem)
