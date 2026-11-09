"""Draw the testing-process figure for chapter 1 (PI brand kit colours, no PI marks).

Usage: python images/testing_process.py images/testing-process
Writes the .svg and an .html; render the PNG with
node images/project_hex_map_render.js "$PWD/images/testing-process.html" images/testing-process.png 1600 940

Three sets of Texas contracts, split by date: learn, rehearse, final test.
Same simple framing and 20% darkened fills as delivery_methods_2x2.py (the stained-glass
pattern belongs to chapter 3 only).
"""
import sys, html

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")


def _mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))


DARK = 0.2
D = {k: _mix(C[k], C["ink"], DARK) for k in ("sec", "action")}

W, H = 1600, 940
PW, PH, GAP = 440, 400, 60          # panel width, height, gap
X0, Y0 = 80, 330


def t(x, y, s, cls, fill=None, anchor="start", extra=""):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{f}{extra}>{html.escape(s)}</text>'


# (name, set of contracts, what happens, researchers' word, fill, stroke, name colour, label colour, body colour, dashed)
PANELS = [
    ("1 · Learn", ["Texas contracts let", "before May 2026"],
     ["The estimator learns its", "prices from what bidders", "actually charged."],
     "Researchers call this training data",
     D["action"], C["action_p"], "#ffffff", C["action_t"], "#ffffff", False),
    ("2 · Rehearse", ["Texas contracts let", "from May 2026"],
     ["Each version is checked on", "them, improved, then checked", "again. Three versions so far:", "v0.1, v0.2 and v0.3."],
     "Researchers call this validation data",
     D["sec"], C["sec_d"], "#ffffff", C["sec_t"], "#ffffff", False),
    ("3 · Final test", ["Newer bid results,", "piling up online"],
     ["Left alone until there is a", "product and someone who", "wants the answer. The error", "bands we pitch come only", "from here."],
     "Researchers call this test data",
     C["acc_t"], C["acc_d"], C["ink"], C["acc_d"], C["ink"], True),
]

o = []
o.append(f'<rect width="{W}" height="{H}" fill="{C["canvas"]}"/>')
o.append('<defs>'
         f'<marker id="ah-i" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink2"]}"/></marker>'
         f'<marker id="ah-l" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C["ink"]}"/></marker>'
         '</defs>')
o.append(t(80, 86, "CHAPTER 1 · WHAT THE SCORES SAY", "eyebrow"))
o.append(t(80, 148, "How the estimator is checked", "title"))
o.append(t(80, 190, "The contracts are split by date. The estimator learns from the older ones", "dek"))
o.append(t(80, 218, "and is checked on the newer ones.", "dek"))

# the time axis
ay = Y0 - 34
o.append(f'<line x1="{X0}" y1="{ay}" x2="{X0 + 3*PW + 2*GAP}" y2="{ay}" stroke="{C["ink2"]}" stroke-width="2.5" marker-end="url(#ah-i)"/>')
o.append(t(X0, ay - 14, "OLDER CONTRACTS", "axis", C["ink2"]))
o.append(t(X0 + 3*PW + 2*GAP, ay - 14, "NEWER CONTRACTS", "axis", C["ink2"], "end"))

for i, (name, sets, body, rname, fill, stroke, ncol, lcol, bcol, dashed) in enumerate(PANELS):
    x = X0 + i * (PW + GAP)
    dash = ' stroke-dasharray="12 8"' if dashed else ""
    sw = 2.5 if dashed else 1.5
    o.append(f'<rect x="{x}" y="{Y0}" width="{PW}" height="{PH}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
    tx = x + 36
    o.append(t(tx, Y0 + 68, name, "name", ncol))
    yy = Y0 + 118
    for ln in sets:
        o.append(t(tx, yy, ln, "ex", lcol)); yy += 30
    yy += 24
    for ln in body:
        o.append(t(tx, yy, ln, "trade", bcol)); yy += 31
    o.append(t(tx, Y0 + PH - 30, rname, "axis-s", lcol))
    if i < 2:  # arrow to the next panel
        ax = x + PW + 8
        o.append(f'<line x1="{ax}" y1="{Y0 + PH/2}" x2="{ax + GAP - 16}" y2="{Y0 + PH/2}" stroke="{C["ink2"]}" stroke-width="2.5" marker-end="url(#ah-i)"/>')

# "not run yet" tag on the final test
px = X0 + 2 * (PW + GAP) + PW - 36 - 150
o.append(f'<rect x="{px}" y="{Y0 + 28}" width="150" height="34" rx="17" fill="{C["acc_d"]}"/>')
o.append(t(px + 75, Y0 + 51, "NOT RUN YET", "pill", "#ffffff", "middle"))

# the rehearsal loop: improve the estimator, then rehearse again
x1 = X0 + (PW + GAP) + PW / 2
x0 = X0 + PW / 2
yb = Y0 + PH + 4
o.append(f'<path d="M{x1},{yb} C{x1},{yb + 80} {x0},{yb + 80} {x0},{yb + 6}" fill="none" stroke="{C["ink"]}" stroke-width="2.5" stroke-dasharray="9 7" marker-end="url(#ah-l)"/>')
o.append(t((x0 + x1) / 2, yb + 92, "improve the estimator, then rehearse again", "drift", C["ink"], "middle"))

o.append(t(80, H - 56, "Rehearsal marks show how the estimator is doing. Each version was built knowing the last score, so they probably flatter it a little.", "foot"))
o.append(t(80, H - 24, "The final test uses newer contracts the project has left alone, so it can say what a buyer should expect.", "foot"))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:#0064ff}}
  .title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:#2c2c2a}}
  .dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:#5f5e5a}}
  .name{{font-family:'Instrument Serif',Georgia,serif;font-size:42px}}
  .ex{{font-family:Outfit,sans-serif;font-weight:500;font-size:21px}}
  .trade{{font-family:Lora,Georgia,serif;font-style:italic;font-weight:500;font-size:22px}}
  .axis{{font-family:Outfit,sans-serif;font-weight:600;font-size:16px;letter-spacing:.14em}}
  .axis-s{{font-family:Lora,Georgia,serif;font-style:italic;font-size:18px}}
  .pill{{font-family:Outfit,sans-serif;font-weight:600;font-size:14px;letter-spacing:.14em}}
  .drift{{font-family:Outfit,sans-serif;font-weight:500;font-size:17px}}
  .foot{{font-family:Outfit,sans-serif;font-size:17px;fill:#5f5e5a}}
</style>
{chr(10).join(o)}
</svg>'''

out = sys.argv[1] if len(sys.argv) > 1 else "testing-process"
open(out + ".svg", "w").write(svg)
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#f9f8f5}}</style></head><body>{svg}</body></html>"""
open(out + ".html", "w").write(page)
