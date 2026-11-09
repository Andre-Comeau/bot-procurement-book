"""Chapter 1 figure: how the estimator is checked, as three stained-glass windows side by side.

Same glass as failure_modes_glass.py (a jittered grid of cells in a leaded pointed-arch
window, Protocol Institute brand colours, none of its marks). One window per stage, left to
right from older contracts to newer: Learn (blue), Rehearse (green) and Final test (rust, in
pale glass because it has not been run yet). Each window has a pale-glass emblem (a book, a
loop, a padlock) and a pale panel with the stage's name, its contracts, what happens and the
researchers' term (training, validation, test data). All wording is Claude's draft for Andre.

Usage: python images/testing_process.py images/testing-process
Then: node images/project_hex_map_render.js "$PWD/images/testing-process.html" images/testing-process.png 1700 1250
"""
import sys, html, random, math

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", ink="#2c2c2a", ink2="#5f5e5a")
LEAD, PALE = "#2c2c2a", "#fbf6e9"
W, H = 1700, 1250
WD, GAP, X_START = 460, 70, 90          # window width, gap between windows, left margin
APEX, RISE = 290, 110                   # top of the arch, height of the arch above the shoulder
SHOULDER = APEX + RISE
PT, PH = SHOULDER + 170, 420            # panel top, panel height
WY1 = PT + PH + 50                      # bottom of the windows
random.seed(7)


def hexrgb(h): return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
def rgbhex(c): return "#%02x%02x%02x" % tuple(max(0, min(255, int(v))) for v in c)
def mix(a, b, t): A, B = hexrgb(a), hexrgb(b); return rgbhex([A[i] + (B[i] - A[i]) * t for i in range(3)])


def t(x, y, s, cls, fill=None, anchor="start"):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}>{html.escape(s)}</text>'


def emb(d, fill=PALE, w=6):
    return f'<path d="{d}" fill="{fill}" stroke="{LEAD}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'


def book(cx, cy):      # an open book: the estimator learns from what was written
    left = f"M{cx},{cy+30} Q{cx-36},{cy+8} {cx-80},{cy+18} L{cx-80},{cy-46} Q{cx-36},{cy-56} {cx},{cy-32} Z"
    right = f"M{cx},{cy+30} Q{cx+36},{cy+8} {cx+80},{cy+18} L{cx+80},{cy-46} Q{cx+36},{cy-56} {cx},{cy-32} Z"
    out = emb(left) + emb(right)
    for k in range(3):
        for sgn in (-1, 1):
            out += (f'<path d="M{cx+sgn*16},{cy-14+k*14} Q{cx+sgn*40},{cy-24+k*14} {cx+sgn*64},{cy-18+k*14}" '
                    f'fill="none" stroke="{LEAD}" stroke-width="4" stroke-linecap="round"/>')
    return out


def loop(cx, cy):      # two arrows chasing round a ring: improve, then rehearse again
    r = 56
    out = ""
    for a0, a1 in ((200, 318), (20, 138)):
        p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
        p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
        d = f"M{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 0 1 {p1[0]:.1f},{p1[1]:.1f}"
        out += f'<path d="{d}" fill="none" stroke="{LEAD}" stroke-width="34" stroke-linecap="round"/>'
        out += f'<path d="{d}" fill="none" stroke="{PALE}" stroke-width="22" stroke-linecap="round"/>'
    for a1 in (318, 138):
        th = math.radians(a1)
        e = (cx + r * math.cos(th), cy + r * math.sin(th))
        tg, nm = (-math.sin(th), math.cos(th)), (math.cos(th), math.sin(th))
        tip = (e[0] + tg[0] * 48, e[1] + tg[1] * 48)
        b1 = (e[0] + nm[0] * 27, e[1] + nm[1] * 27)
        b2 = (e[0] - nm[0] * 27, e[1] - nm[1] * 27)
        out += emb(f"M{tip[0]:.1f},{tip[1]:.1f} L{b1[0]:.1f},{b1[1]:.1f} L{b2[0]:.1f},{b2[1]:.1f} Z", PALE, 5)
    return out


def padlock(cx, cy):   # locked until there is a product
    sh = f"M{cx-30},{cy-8} L{cx-30},{cy-34} Q{cx-30},{cy-68} {cx},{cy-68} Q{cx+30},{cy-68} {cx+30},{cy-34} L{cx+30},{cy-8}"
    return (f'<path d="{sh}" fill="none" stroke="{LEAD}" stroke-width="26" stroke-linecap="round"/>'
            f'<path d="{sh}" fill="none" stroke="{PALE}" stroke-width="14" stroke-linecap="round"/>'
            + emb(f"M{cx-52},{cy-10} L{cx+52},{cy-10} L{cx+52},{cy+64} L{cx-52},{cy+64} Z", PALE, 6)
            + f'<circle cx="{cx}" cy="{cy+20}" r="9" fill="{LEAD}"/><rect x="{cx-3.5}" y="{cy+22}" width="7" height="22" fill="{LEAD}"/>')


# name, contracts, what happens, researchers' term, glass colours, emblem, term colour, pale glass?
WINDOWS = [
    ("1 · Learn", ["Texas contracts let", "before May 2026"],
     ["The estimator learns its", "prices from what bidders", "actually charged."],
     "Researchers call this training data",
     [C["action"], C["action_p"], mix(C["action"], "#ffffff", .3)], book, C["action_p"]),
    ("2 · Rehearse", ["Texas contracts let", "from May 2026"],
     ["Each version is checked on", "them, improved, then checked", "again. Three versions so far:", "v0.1, v0.2 and v0.3."],
     "Researchers call this validation data",
     [C["sec"], C["sec_d"], mix(C["sec"], "#ffffff", .25)], loop, C["sec_d"]),
    ("3 · Final test", ["Newer bid results,", "piling up online"],
     ["Left alone until there is a", "product and someone who", "wants the answer. The error", "bands we quote come only", "from here."],
     "Researchers call this test data",
     [mix(C["acc"], "#ffffff", .5), mix(C["acc"], "#ffffff", .64), mix(C["acc"], "#ffffff", .74)], padlock, C["acc_d"]),
]


def arch_path(x0, x1):
    xm, r = (x0 + x1) / 2, (x1 - x0) * 0.85
    return (f"M{x0},{WY1} L{x0},{SHOULDER} A{r},{r} 0 0 1 {xm},{APEX} A{r},{r} 0 0 1 {x1},{SHOULDER} L{x1},{WY1} Z")


o = [f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>']
o.append('<defs>'
         f'<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink2"]}"/></marker>')
for i in range(3):
    x0 = X_START + i * (WD + GAP)
    o.append(f'<clipPath id="win{i}"><path d="{arch_path(x0, x0 + WD)}"/></clipPath>')
o.append('</defs>')

o.append(t(80, 86, "CHAPTER 1 · WHAT THE SCORES SAY", "eyebrow"))
o.append(t(80, 148, "How the estimator is checked", "title"))
o.append(t(80, 190, "The contracts are split by date. The estimator learns from the older ones", "dek"))
o.append(t(80, 218, "and is checked on the newer ones.", "dek"))

COLS, ROWS = 6, 12
for i, (name, sets, body, term, base, emblem, tcol) in enumerate(WINDOWS):
    x0 = X_START + i * (WD + GAP); x1 = x0 + WD; xm = (x0 + x1) / 2
    # the glass: a jittered grid, clipped to the window
    gx = [x0 - 20 + k * (WD + 40) / COLS for k in range(COLS + 1)]
    gy = [APEX - 30 + k * (WY1 - APEX + 60) / ROWS for k in range(ROWS + 1)]
    pts = {}
    for a in range(COLS + 1):
        for b in range(ROWS + 1):
            jx = 0 if a in (0, COLS) else random.uniform(-20, 20)
            jy = 0 if b in (0, ROWS) else random.uniform(-17, 17)
            pts[a, b] = (gx[a] + jx, gy[b] + jy)
    g = [f'<g clip-path="url(#win{i})">']
    for a in range(COLS):
        for b in range(ROWS):
            quad = [pts[a, b], pts[a + 1, b], pts[a + 1, b + 1], pts[a, b + 1]]
            col = mix(random.choice(base), "#ffffff", random.uniform(0, .16))
            d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in quad) + " Z"
            g.append(f'<path d="{d}" fill="{col}" stroke="{LEAD}" stroke-width="5" stroke-linejoin="round"/>')
    g.append('</g>')
    o += g
    o.append(f'<path d="{arch_path(x0, x1)}" fill="none" stroke="{LEAD}" stroke-width="22" stroke-linejoin="round"/>')
    o.append(f'<path d="{arch_path(x0, x1)}" fill="none" stroke="#8a8780" stroke-width="4" stroke-linejoin="round"/>')

    o.append(emblem(xm, SHOULDER + 74))

    # the panel
    px, pw = x0 + 40, WD - 80
    o.append(f'<rect x="{px}" y="{PT}" width="{pw}" height="{PH}" rx="12" fill="{PALE}" stroke="{LEAD}" stroke-width="3"/>')
    o.append(t(xm, PT + 66, name, "name", LEAD, "middle"))
    yy = PT + 112
    for ln in sets:
        o.append(t(xm, yy, ln, "who", C["ink2"], "middle")); yy += 33
    yy += 22
    for ln in body:
        o.append(t(xm, yy, ln, "rem", LEAD, "middle")); yy += 34
    o.append(t(xm, PT + PH - 30, term, "term", tcol, "middle"))
    if i == 2:  # not run yet
        o.append(f'<rect x="{xm-88}" y="{PT-17}" width="176" height="34" rx="17" fill="{C["acc_d"]}" stroke="{LEAD}" stroke-width="3"/>')
        o.append(t(xm, PT + 6, "NOT RUN YET", "pill", "#ffffff", "middle"))

# the time axis, under the windows
ay = WY1 + 78
o.append(f'<line x1="{X_START}" y1="{ay}" x2="{X_START + 3*WD + 2*GAP}" y2="{ay}" stroke="{C["ink2"]}" stroke-width="2.5" marker-end="url(#ah)"/>')
o.append(t(X_START, ay - 16, "OLDER CONTRACTS", "axis", C["ink2"]))
o.append(t(X_START + 3 * WD + 2 * GAP, ay - 16, "NEWER CONTRACTS", "axis", C["ink2"], "end"))

o.append(t(80, H - 56, "Rehearsal marks show how the estimator is doing. Each version was built knowing the last score, so they probably flatter it a little.", "foot"))
o.append(t(80, H - 24, "The final test uses newer contracts the project has left alone, so it can say what a buyer should expect.", "foot"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:50px}}
  .who{{font-family:Lora,Georgia,serif;font-style:italic;font-size:25px}}
  .rem{{font-family:Outfit,sans-serif;font-weight:500;font-size:25px}}
  .term{{font-family:Lora,Georgia,serif;font-style:italic;font-size:21px}}
  .pill{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.14em}}
  .axis{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px;letter-spacing:.14em}}
  .foot{{font-family:Outfit,sans-serif;font-size:17px;fill:#5f5e5a}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "testing-process"
open(out + ".svg", "w").write(svg)
open(out + ".html", "w").write(f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>""")
