"""Draw the project's hex map (PI brand kit, Institute vein, no PI marks)."""
import math, sys, html

R = 92                      # hex circumradius (pointy-top)
W3 = math.sqrt(3)
OX, OY = 120, 250           # grid origin
COLS, ROWS = 9, 6

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a", dark="#0a1f17", mint="#bff0dd")

def center(c, r):
    return OX + R * W3 * (c + 0.5 * (r & 1)), OY + R * 1.5 * r

def hexpts(x, y, s=R):
    return " ".join(f"{x + s*math.cos(math.radians(60*i-30)):.1f},{y + s*math.sin(math.radians(60*i-30)):.1f}" for i in range(6))

# kind -> (fill, stroke, label colour, kind label)
KIND = {
    "town":     (C["action_t"], C["action"], C["action_p"], "TOWN"),
    "temple":   (C["action"],   C["action_p"], "#ffffff",   "TEMPLE"),
    "workshop": (C["sec_t"],    C["sec"],    C["sec_d"],    "WORKSHOP"),
    "library":  (C["acc_t"],    C["acc"],    C["acc_d"],    "LIBRARY"),
    "guild":    (C["surface"],  C["ink2"],   C["ink2"],     "GUILD HOUSE"),
    "tower":    (C["muted"],    C["ink2"],   C["ink2"],     "TOWER"),
    "fog":      ("url(#fog)",   C["ink2"],   C["ink2"],     "UNEXPLORED"),
    "followers":(C["surface"],  C["action"], C["action_p"], "FOLLOWERS"),
}

# (col,row): (kind, name lines, note)
HEX = {
    (3,2): ("town", ["Field Building"], "human-led, the bottleneck"),
    (4,2): ("temple", ["The Standard"], "spec + conformance test"),
    (2,1): ("guild", ["Protocol", "Institute"], ""),
    (3,1): ("guild", ["Yak", "Collective"], ""),
    (2,2): ("library", ["Case study"], "current tensions"),
    (2,3): ("library", ["Procurement", "Machines"], "since 493 BCE"),
    (3,3): ("workshop", ["Estimator"], "first reference impl."),
    (4,3): ("workshop", ["F&R", "Evaluator"], "for buyers"),
    (5,3): ("workshop", ["Procurement", "bots"], "worked example"),
    (4,4): ("tower", ["Bot Council"], "other points of view"),
    (3,4): ("tower", ["Offline AI"], "pinned weights"),
    (4,1): ("followers", ["Adopters"], "arrive on their own"),
    (6,2): ("fog", ["BIM for bots"], ""),
    (7,2): ("fog", ["Bot", "Monitoring"], ""),
    (8,2): ("fog", ["Robotic", "Construction"], "the far-off land"),
}
FOG_EXTRA = {(6,1),(7,1),(8,1),(6,3),(7,3),(8,3),(7,4),(8,4),(8,5)}

def glyph(kind, x, y, col):
    s = []
    if kind == "temple":   # pediment + columns
        s.append(f'<path d="M{x-16},{y-4} L{x},{y-16} L{x+16},{y-4} Z" fill="none" stroke="{col}" stroke-width="2.2" stroke-linejoin="round"/>')
        for dx in (-11,-4,4,11): s.append(f'<line x1="{x+dx}" y1="{y-2}" x2="{x+dx}" y2="{y+11}" stroke="{col}" stroke-width="2.2"/>')
        s.append(f'<line x1="{x-17}" y1="{y+13}" x2="{x+17}" y2="{y+13}" stroke="{col}" stroke-width="2.2"/>')
    elif kind == "town":   # three roofs
        for dx, h in ((-13,0),(0,-5),(13,0)):
            s.append(f'<path d="M{x+dx-7},{y+12} V{y+h} L{x+dx},{y+h-8} L{x+dx+7},{y+h} V{y+12} Z" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
    elif kind == "workshop":  # anvil
        s.append(f'<path d="M{x-16},{y-6} H{x+12} Q{x+18},{y-6} {x+18},{y-1} H{x+6} V{y+4} L{x+10},{y+12} H{x-10} L{x-6},{y+4} V{y-1} H{x-12} Z" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
    elif kind == "library":   # open book
        s.append(f'<path d="M{x},{y-6} Q{x-9},{y-12} {x-18},{y-9} V{y+10} Q{x-9},{y+7} {x},{y+13} Q{x+9},{y+7} {x+18},{y+10} V{y-9} Q{x+9},{y-12} {x},{y-6} V{y+13}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
    elif kind == "guild":     # banner
        s.append(f'<line x1="{x-10}" y1="{y-14}" x2="{x-10}" y2="{y+14}" stroke="{col}" stroke-width="2"/>')
        s.append(f'<path d="M{x-10},{y-13} H{x+12} L{x+6},{y-6} L{x+12},{y+1} H{x-10}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
    elif kind == "tower":
        s.append(f'<path d="M{x-8},{y+13} V{y-6} H{x-11} V{y-14} H{x-6} V{y-10} H{x-2} V{y-14} H{x+2} V{y-10} H{x+6} V{y-14} H{x+11} V{y-6} H{x+8} V{y+13} Z" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
    elif kind == "followers": # three heads
        for dx in (-13,0,13):
            s.append(f'<circle cx="{x+dx}" cy="{y-5}" r="4.5" fill="none" stroke="{col}" stroke-width="2"/>')
            s.append(f'<path d="M{x+dx-7},{y+12} Q{x+dx},{y-1} {x+dx+7},{y+12}" fill="none" stroke="{col}" stroke-width="2"/>')
    elif kind == "fog":       # sail
        s.append(f'<path d="M{x-4},{y-15} V{y+8} M{x-2},{y-13} L{x+13},{y+5} H{x-2} M{x-16},{y+9} H{x+14} L{x+9},{y+15} H{x-11} Z" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
    return "".join(s)

def arrow(a, b, col, label=None, dash=False, lab_off=(0,0), shorten=0.30):
    (x1,y1),(x2,y2) = center(*a), center(*b)
    dx, dy = x2-x1, y2-y1
    L = math.hypot(dx, dy); ux, uy = dx/L, dy/L
    mx0, my0 = (x1+x2)/2, (y1+y2)/2
    half = 15 if L < 2*R*1.2 else shorten
    sx, sy = mx0-ux*half, my0-uy*half
    ex, ey = mx0+ux*half, my0+uy*half
    d = ' stroke-dasharray="6 6"' if dash else ""
    out = [f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#f9f8f5" stroke-width="9" stroke-linecap="round"/>', f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{col}" stroke-width="3"{d} marker-end="url(#ah-{col[1:]})"/>']
    if label:
        mx, my = (sx+ex)/2 + lab_off[0], (sy+ey)/2 + lab_off[1]
        out.append(f'<text x="{mx:.1f}" y="{my:.1f}" class="road" text-anchor="middle" fill="{col}">{html.escape(label)}</text>')
    return "".join(out)

def build():
    Wd, Ht = 1800, 1200
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wd}" height="{Ht}" viewBox="0 0 {Wd} {Ht}">']
    cols = {C["action"], C["sec"], C["acc"], C["ink2"], C["action_p"]}
    o.append("<defs>")
    o.append(f'<pattern id="fog" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="12" height="12" fill="{C["canvas"]}"/><line x1="0" y1="0" x2="0" y2="12" stroke="{C["hair"]}" stroke-width="5"/></pattern>')
    for col in cols:
        o.append(f'<marker id="ah-{col[1:]}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>')
    o.append("""<style>
      .eyebrow{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}
      .title{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}
      .dek{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}
      .name{font-family:'Instrument Serif',Georgia,serif;font-size:23px}
      .kind{font-family:Outfit,sans-serif;font-weight:600;font-size:10.5px;letter-spacing:.12em}
      .note{font-family:Outfit,sans-serif;font-size:12px}
      .road{font-family:Outfit,sans-serif;font-weight:600;font-size:13px;paint-order:stroke;stroke:#f9f8f5;stroke-width:6px;stroke-linejoin:round}
      .step-n{font-family:'Instrument Serif',Georgia,serif;font-size:40px;fill:#0064ff}
      .step-t{font-family:'Instrument Serif',Georgia,serif;font-size:24px;fill:#2c2c2a}
      .step-b{font-family:Lora,Georgia,serif;font-size:15.5px;fill:#5f5e5a}
      .lg{font-family:Outfit,sans-serif;font-size:13px;fill:#2c2c2a}
      .lgh{font-family:Outfit,sans-serif;font-weight:600;font-size:11px;letter-spacing:.14em;fill:#5f5e5a}
      .foot{font-family:Outfit,sans-serif;font-size:12px;fill:#5f5e5a}
      .side{font-family:Lora,Georgia,serif;font-style:italic;font-size:17px}
    </style></defs>""")
    o.append(f'<rect width="{Wd}" height="{Ht}" fill="{C["canvas"]}"/>')
    # title
    o.append('<text x="64" y="78" class="eyebrow">THE PROJECT AS A HEX MAP</text>')
    o.append('<text x="64" y="138" class="title">One town, one temple, and fog to the east</text>')
    o.append('<text x="64" y="176" class="dek">Field Building turns evidence and working tools into a standard. What lies beyond the standard is a destination, not a plan.</text>')

    # empty grid first
    for r in range(ROWS):
        for c in range(COLS):
            if (c,r) in HEX: continue
            x, y = center(c, r)
            if x > 1500 or r == 0 or r == 5: continue
            if (c,r) in FOG_EXTRA:
                o.append(f'<polygon points="{hexpts(x,y,R-3)}" fill="url(#fog)" stroke="{C["hair"]}" stroke-width="1.5"/>')
            else:
                o.append(f'<polygon points="{hexpts(x,y,R-3)}" fill="none" stroke="{C["hair"]}" stroke-width="1.5"/>')

    # roads (under hexes' text but over fills -> draw hexes then roads then labels). Draw hex fills now.
    for (c,r),(kind,lines,note) in HEX.items():
        x, y = center(c, r)
        fill, stroke, lab, _ = KIND[kind]
        dash = ' stroke-dasharray="7 6"' if kind in ("fog","followers") else ""
        o.append(f'<polygon points="{hexpts(x,y,R-3)}" fill="{fill}" stroke="{stroke}" stroke-width="2.4"{dash}/>')

    for (c,r),(kind,lines,note) in HEX.items():
        x, y = center(c, r)
        fill, stroke, lab, klabel = KIND[kind]
        o.append(f'<text x="{x:.1f}" y="{y-44:.1f}" class="kind" text-anchor="middle" fill="{lab}">{klabel}</text>')
        o.append(glyph(kind, x, y-14, lab))
        ny = y + 22 if len(lines) == 1 else y + 16
        for i, ln in enumerate(lines):
            o.append(f'<text x="{x:.1f}" y="{ny + i*22:.1f}" class="name" text-anchor="middle" fill="{C["ink"] if kind!="temple" else "#ffffff"}">{html.escape(ln)}</text>')
        if note:
            o.append(f'<text x="{x:.1f}" y="{y+ (44 if len(lines)==1 else 60):.1f}" class="note" text-anchor="middle" fill="{lab}">{html.escape(note)}</text>')

    # roads
    o.append(arrow((2,1),(3,2), C["ink2"], shorten=0.36))
    o.append(arrow((3,1),(3,2), C["ink2"], shorten=0.36))
    o.append(arrow((2,2),(3,2), C["acc_d"], shorten=0.36))
    o.append(arrow((2,3),(3,2), C["acc_d"], shorten=0.36))
    o.append(arrow((3,3),(3,2), C["sec"], shorten=0.36))
    o.append(arrow((3,2),(4,2), C["action"], shorten=0.36))
    o.append(arrow((3,3),(4,2), C["sec"], shorten=0.36))
    o.append(arrow((4,3),(4,2), C["sec"], shorten=0.36))
    o.append(arrow((5,3),(4,2), C["sec"], shorten=26))
    o.append(arrow((3,4),(3,3), C["ink2"], shorten=0.36))
    o.append(arrow((4,4),(4,3), C["ink2"], shorten=0.36))
    o.append(arrow((6,2),(7,2), C["ink2"], dash=True))
    o.append(arrow((7,2),(8,2), C["ink2"], dash=True))
    o.append(arrow((4,1),(4,2), C["action"], dash=True, shorten=0.36))
    # the voyage east: dashed line from the Standard into the fog
    (sx,sy),(ex,ey) = center(4,2), center(6,2)
    o.append(f'<path d="M{sx+R*0.62:.1f},{sy:.1f} C{sx+R*1.2:.1f},{sy-40:.1f} {ex-R*1.2:.1f},{ey+40:.1f} {ex-R*0.62:.1f},{ey:.1f}" fill="none" stroke="{C["action"]}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round" marker-end="url(#ah-{C["action"][1:]})"/>')

    # side annotations (left margin), each next to its source
    def side(x, y, txt, col, anchor="end"):
        o.append(f'<text x="{x}" y="{y}" class="side" text-anchor="{anchor}" fill="{col}">{html.escape(txt)}</text>')
    gx, gy = center(2,1); side(gx-R-6, gy+6, "theory, people, legitimacy", C["ink2"])
    cx, cy = center(2,2); side(cx-R-6, cy-4, "evidence", C["acc_d"])
    px, py = center(2,3); side(px-R-6, py+6, "evidence, from history", C["acc_d"])
    bx, by = center(3,4); side(bx-R-6, by+6, "make the work cheaper", C["ink2"])
    wx, wy = center(5,4); side(wx-10, wy-6, "reference implementations:", C["sec"], "start")
    side(wx-10, wy+16, "each must pass the Standard's test", C["sec"], "start")
    sx2, sy2 = center(5,2); side(sx2+12, sy2-34, "the voyage east", C["action_p"], "middle")
    fx, fy = center(4,1); side(fx+R*0.2, fy-R-10, "you cannot hire followers", C["action_p"], "start")
    rx, ry = center(8,2); side(rx, ry+R+30, "a destination, not a plan", C["action_p"], "middle")
    # bards: the book on the road from the town to the guild houses
    tx, ty = center(3,2); gx2, gy2 = center(2,1)
    bxm, bym = (tx+gx2)/2, (ty+gy2)/2

    # legend (right column)
    lx, ly = 1530, 250
    o.append(f'<text x="{lx}" y="{ly}" class="lgh">ON THE MAP</text>')
    items = [("town","Town: where people gather"),("temple","Temple: the Standard"),("workshop","Workshop: tools"),
             ("library","Library: the evidence"),("guild","Guild house: allied groups"),("tower","Tower: labs"),
             ("followers","Followers: adopters"),("fog","Fog: the territories")]
    for i,(k,t) in enumerate(items):
        y = ly + 34 + i*40
        fill, stroke, lab, _ = KIND[k]
        dash = ' stroke-dasharray="4 3"' if k in ("fog","followers") else ""
        o.append(f'<polygon points="{hexpts(lx+14,y-5,14)}" fill="{fill}" stroke="{stroke}" stroke-width="1.8"{dash}/>')
        o.append(f'<text x="{lx+38}" y="{y}" class="lg">{t}</text>')
    y = ly + 34 + len(items)*40 + 6
    o.append(f'<text x="{lx}" y="{y}" class="lg" fill="{C["ink2"]}">Empty hexes are normal:</text>')
    o.append(f'<text x="{lx}" y="{y+18}" class="lg" fill="{C["ink2"]}">most of any map is empty.</text>')

    # the cleric's ladder (bottom band)
    by0 = 965
    o.append(f'<line x1="64" y1="{by0-30}" x2="{Wd-64}" y2="{by0-30}" stroke="{C["hair"]}" stroke-width="1.5"/>')
    o.append(f'<text x="64" y="{by0}" class="eyebrow">THE ORDER OF BUILDING</text>')
    steps = [("1","Temple first","Publish the standard: a public, versioned test,", "free to use, that any bot can be checked against."),
             ("2","Then followers","Adopters arrive on their own, or not at all.", "Bards carry the word between towns; this book is one."),
             ("3","Then the stronghold, at half price","Implementations get cheaper because others help", "build them. No walls until there is bread to protect.")]
    colw = (Wd-128)/3
    for i,(n,t,b1,b2) in enumerate(steps):
        x = 64 + i*colw
        o.append(f'<text x="{x}" y="{by0+64}" class="step-n">{n}</text>')
        o.append(f'<text x="{x+40}" y="{by0+56}" class="step-t">{html.escape(t)}</text>')
        o.append(f'<text x="{x+40}" y="{by0+86}" class="step-b">{html.escape(b1)}</text>')
        o.append(f'<text x="{x+40}" y="{by0+108}" class="step-b">{html.escape(b2)}</text>')
    o.append(f'<text x="64" y="{Ht-36}" class="foot">Andre Comeau, The Bot Procurement Book, CC BY 4.0. The order of building follows the cleric\'s stronghold rule in the AD&amp;D 1st edition Dungeon Masters Guide (1979). Colours and type follow the Protocol Institute brand kit; not a Protocol Institute figure.</text>')
    o.append("</svg>")
    return "\n".join(o), Wd, Ht

svg, Wd, Ht = build()
out = sys.argv[1]
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
print(Wd, Ht)
