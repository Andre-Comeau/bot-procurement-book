"""Slack, and the other option: Galbraith's two choices (chapter 6, schematic, not data), with the book's slack and capacity instruments listed.
Usage: python images/slack_other_option.py images/slack-other-option   (writes the .svg and an .html; render at 1600 1240, see images/README.md)
"""
import sys, html
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
D = {k: mix(C[k], C["ink"], 0.2) for k in ("action", "sec", "acc", "ink2")}
W, H = 1600, 1240
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
o.append(t(80, 86, "CHAPTER 6 · SLACK, AND THE OTHER OPTION", "eyebrow"))
o.append(t(80, 148, "Slack, and the other option", "title"))
o.append(t(80, 190, "An organization facing more than it can process has two kinds of answer, Galbraith wrote: need less, which in construction means slack,", "dek"))
o.append(t(80, 218, "or raise its capacity to process information. AI took the slack away and left the attention needed exactly where it was.", "dek"))
# ---- the chart
X0, X1, Y0, Y1 = 160, 960, 330, 1080
ATT = 800
def bids_y(x):
    if x <= 760:
        return 1020 - (x - X0) * 0.05
    u = (x - 760) / (X1 - 760)
    return 1020 - (760 - X0) * 0.05 - 600 * (u ** 2.2)
pts = [(x, bids_y(x)) for x in range(X0, X1 + 1, 4)]
xcross = next(x for x, y in pts if y <= ATT)
before = [(x, y) for x, y in pts if x <= xcross] + [(xcross, ATT), (X0, ATT)]
after = [(x, y) for x, y in pts if x >= xcross] + [(X1, ATT), (xcross, ATT)]
o.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in before) + f'" fill="{C["sec_t"]}"/>')
o.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in after) + f'" fill="{C["acc_t"]}"/>')
for ex in (480, 760):
    o.append(f'<line x1="{ex}" y1="{Y0}" x2="{ex}" y2="{Y1}" stroke="{C["hair"]}" stroke-width="2" stroke-dasharray="6 6"/>')
o.append(f'<line x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}" stroke="{C["ink2"]}" stroke-width="2"/>')
o.append(f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{C["ink2"]}" stroke-width="2"/>')
o.append(f'<line x1="{X0}" y1="{ATT}" x2="{X1}" y2="{ATT}" stroke="{C["action"]}" stroke-width="3.5" stroke-linecap="round"/>')
o.append('<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="none" stroke="{C["acc"]}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>')
o.append(f'<circle cx="{X1}" cy="{bids_y(X1):.1f}" r="7" fill="{C["acc"]}" stroke="{C["canvas"]}" stroke-width="2"/>')
o.append(f'<circle cx="{X1}" cy="{ATT}" r="7" fill="{C["action"]}" stroke="{C["canvas"]}" stroke-width="2"/>')
o.append(t(X0 - 8, Y0 - 14, "how many", "axis", C["ink2"], "start"))
for (xa, xb, lab) in ((X0, 480, "the plan room"), (480, 760, "the plan room online"), (760, X1, "AI makes the call nearly free")):
    o.append(t((xa + xb) / 2, Y1 + 34, lab, "axis", C["ink2"], "middle"))
o.append(t((X0 + X1) / 2, Y1 + 62, "time, left to right", "axisnote", C["ink2"], "middle"))
# region labels: slack below the attention line, the thicket above it
o.append(t(400, 870, "slack", "lab", D["sec"], "middle"))
o.append(t(400, 898, "the oak kept the stack of bids", "note", C["ink"], "middle"))
o.append(t(400, 923, "small enough for a committee to read;", "note", C["ink"], "middle"))
o.append(t(400, 948, "under it, the cushion, the contingency,", "note", C["ink"], "middle"))
o.append(t(400, 973, "the long tender, the margin that eats the error", "note", C["ink"], "middle"))
o.append(t(880, 560, "the thicket", "lab", D["acc"], "end"))
o.append(t(880, 588, "slack released without", "note", C["ink"], "end"))
o.append(t(880, 614, "the capacity to meet it", "note", C["ink"], "end"))
o.append(f'<line x1="{X1-50}" y1="{bids_y(X1)-30:.1f}" x2="{X1-14}" y2="{bids_y(X1)-30:.1f}" stroke="{C["acc"]}" stroke-width="3.5"/>')
o.append(t(X1 - 60, bids_y(X1) - 24, "bids arriving at the door", "note", C["ink"], "end"))
o.append(f'<line x1="{X0+16}" y1="{ATT-26}" x2="{X0+56}" y2="{ATT-26}" stroke="{C["action"]}" stroke-width="3.5"/>')
o.append(t(X0 + 66, ATT - 20, "the attention available to read them", "note", C["ink"], "start"))
o.append(f'<line x1="{X0}" y1="{Y0+4}" x2="{X0+36}" y2="{Y0+4}" stroke="{C["acc"]}" stroke-width="3.5"/>')
o.append(t(X0 + 46, Y0 + 10, "bids per tender", "legend", C["ink2"]))
o.append(f'<line x1="{X0+230}" y1="{Y0+4}" x2="{X0+266}" y2="{Y0+4}" stroke="{C["action"]}" stroke-width="3.5"/>')
o.append(t(X0 + 276, Y0 + 10, "eyes to read them", "legend", C["ink2"]))
# ---- the two choices, with where the book finds each
RX = 1040
o.append(t(RX, 334, "Two kinds of answer, through the book", "lab", C["ink"]))
boxes = [
    (360, "Add slack", D["ink2"], C["hair"],
     ["A bid cushion for the drawings' errors", "A long tender, a plan room, a committee", "The oak: five bids in six lost, as overhead",
      "A contingency for the rest", "Changes bought from a supplier of one", "Reviews by whoever has time",
      "The margin eats the error; the surety waits", "Taylorism and the largest firms plateau"],
     "Construction's habit. It no longer works: AI removed the slack and left the attention needed exactly where it was."),
    (730, "Raise the capacity", D["sec"], C["sec_t"],
     ["A second opinion on every price", "The tender as a data file", "The same check, the same way, every bid",
      "A measured miss rate, and a record", "The door open: no cap, no key, no fee", "The evaluator, and the keyholder who signs",
      "Insurance on the margin picks up the tails", "A standard: template, record, public test"],
     "The other option. More data moves faster through the door without anyone acquiring a say they did not have before."),
]
for (by, title, col, fill, items, verdict) in boxes:
    o.append(f'<rect x="{RX}" y="{by}" width="{W-80-RX}" height="350" rx="8" fill="{fill}" stroke="{col}" stroke-width="3"/>')
    o.append(t(RX + 24, by + 44, title, "boxtitle", col))
    y = by + 78
    for it in items:
        o.append(f'<rect x="{RX+24}" y="{y-12}" width="8" height="8" fill="{col}"/>')
        o.append(t(RX + 42, y, it, "item", C["ink"])); y += 26
    y += 6
    for ln in wrap(verdict, 46):
        o.append(t(RX + 24, y, ln, "tiny", C["ink2"])); y += 23
o.append(t(80, H - 40, "Schematic, not data: the lines show the idea, not counts. The lists are sentences from across the book, shortened.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 23px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.boxtitle{{font:700 27px Georgia,serif}}
.note{{font:400 20px "IBM Plex Sans",Arial,sans-serif}}
.item{{font:400 19px "IBM Plex Sans",Arial,sans-serif}}
.legend{{font:600 18px "IBM Plex Sans",Arial,sans-serif}}
.axis{{font:400 19px "IBM Plex Sans",Arial,sans-serif}}
.axisnote{{font:italic 400 17px "IBM Plex Sans",Arial,sans-serif}}
.tiny{{font:italic 400 18px "IBM Plex Sans",Arial,sans-serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "slack-other-option"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
print("wrote", stem, "cross at", xcross)
