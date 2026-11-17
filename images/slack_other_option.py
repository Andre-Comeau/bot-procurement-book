"""Slack, and the other option: Galbraith's two choices, found across the book (chapter 6; a ledger, not data).
Usage: python images/slack_other_option.py images/slack-other-option   (writes the .svg and an .html; render at 1600 1200, see images/README.md)
"""
import sys, html
C = dict(action="#0064ff", action_t="#e6efff", sec="#0f6e56", sec_t="#e1f5ee",
         acc="#d85a30", acc_t="#faece7", canvas="#f9f8f5", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")
def mix(a, b, f):
    A = [int(a[i:i+2], 16) for i in (1, 3, 5)]; B = [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))
D = {k: mix(C[k], C["ink"], 0.2) for k in ("action", "sec", "acc", "ink2")}
W, H = 1600, 1200
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
o.append(t(80, 190, "An organization facing more than it can process has two choices, Galbraith wrote: add slack, or raise its capacity to", "dek"))
o.append(t(80, 218, "process information. Construction has always chosen slack. Here is where this book finds it, and what the project puts in its place.", "dek"))
# ---- the two columns and the spine between them
LX0, LX1, RX0, RX1, SX = 80, 660, 940, 1520, 800
CWID = LX1 - LX0
o.append(t(LX0, 302, "Add slack", "lab", D["ink2"]))
o.append(t(LX0, 332, "construction's habit: more time, more money, more cushion between the parts", "note", C["ink2"]))
o.append(f'<line x1="{LX0}" y1="348" x2="{LX1}" y2="348" stroke="{D["ink2"]}" stroke-width="3"/>')
o.append(t(RX0, 302, "Raise the capacity", "lab", D["sec"]))
o.append(t(RX0, 332, "the other option: the same check for every bid, with a record", "note", C["ink2"]))
o.append(f'<line x1="{RX0}" y1="348" x2="{RX1}" y2="348" stroke="{D["sec"]}" stroke-width="3"/>')
rows = [
    ("The drawings",
     "Bug-free drawings are a mythical beast, so the bid carries a cushion for their errors.",
     "A second opinion on every price: a check that flags a line for the firm's own review before the bid goes in."),
    ("The tender",
     "A long tender period, a plan room and an evaluation committee, built for a few large bidders and time to read.",
     "The tender as a data file, and the same check applied the same way to every bid: same bid, same answer, a measured miss rate."),
    ("The cost of bidding",
     "The oak: an estimating department, a bonding line and the patience to lose five bids in six, billed as overhead to the jobs that are won.",
     "A published check reads a thousand bids the same way, so the door stays open without a cap, a key or a fee, and the cost to bid drops."),
    ("After the award",
     "The contingency carries a cushion for the rest, and every change is a purchase from a supplier of one, reviewed by whoever has time.",
     "The evaluator prices each line of a change and hands it to the keyholder, who signs with a reason and leaves a record of what was checked."),
    ("Who pays",
     "The margin eats the error: a miss the size of the winner's lead is the year's profit on the job, and the surety stands behind the firm.",
     "Insurance on the margin picks up the tails a probabilistic tool will always have, priced from the test's measured misses."),
    ("The whole industry",
     "Taylorism's gains have plateaued, and so has the largest firm: it bids on a lot and works on a lot, and its size stays where it is.",
     "A standard: a template and a record, a public test, and a market memory anyone can read against, so more workers step into principal roles."),
]
Y0, PITCH, CH = 380, 110, 96
o.append(f'<line x1="{SX}" y1="{Y0-6}" x2="{SX}" y2="{Y0+len(rows)*PITCH-14}" stroke="{C["hair"]}" stroke-width="3"/>')
for i, (station, left, right) in enumerate(rows):
    y = Y0 + i * PITCH
    o.append(f'<rect x="{LX0}" y="{y}" width="{CWID}" height="{CH}" rx="8" fill="{C["hair"]}" stroke="{D["ink2"]}" stroke-width="1.5"/>')
    yy = y + 34
    for ln in wrap(left, 50):
        o.append(t(LX0 + 22, yy, ln, "cell", C["ink"])); yy += 26
    o.append(f'<rect x="{RX0}" y="{y}" width="{CWID}" height="{CH}" rx="8" fill="{C["sec_t"]}" stroke="{D["sec"]}" stroke-width="1.5"/>')
    yy = y + 34
    for ln in wrap(right, 50):
        o.append(t(RX0 + 22, yy, ln, "cell", C["ink"])); yy += 26
    o.append(f'<circle cx="{SX}" cy="{y+16}" r="9" fill="{C["canvas"]}" stroke="{C["ink"]}" stroke-width="3"/>')
    o.append(f'<text x="{SX}" y="{y+52}" class="station" text-anchor="middle" fill="{C["ink"]}" stroke="{C["canvas"]}" stroke-width="10" paint-order="stroke" stroke-linejoin="round">{html.escape(station)}</text>')
# ---- what changed, in one band
yb = Y0 + len(rows) * PITCH + 16
o.append(f'<line x1="80" y1="{yb}" x2="{W-80}" y2="{yb}" stroke="{C["hair"]}" stroke-width="2"/>')
o.append(t(80, yb + 40, "What changed: AI made the call nearly free. It did not remove the uncertainty. It removed the slack, and left the", "cell", C["ink"]))
o.append(t(80, yb + 68, "attention needed exactly where it was. The thicket is slack released without the capacity to meet it.", "cell", C["ink"]))
MX0, MX1, MY = 1250, 1470, yb + 56
o.append(f'<line x1="{MX0}" y1="{MY}" x2="{MX1}" y2="{MY}" stroke="{C["action"]}" stroke-width="3" stroke-linecap="round"/>')
pts = []
for k in range(0, 101):
    u = k / 100; x = MX0 + (MX1 - MX0) * u
    yv = MY + 30 - 12 * u - 56 * (u ** 4)
    pts.append(f"{x:.1f},{yv:.1f}")
o.append(f'<path d="M' + " L".join(pts) + f'" fill="none" stroke="{C["acc"]}" stroke-width="3" stroke-linecap="round"/>')
o.append(t(MX1 + 12, MY + 6, "eyes", "mini", C["ink"]))
o.append(t(MX1 + 12, MY - 34, "bids", "mini", C["ink"]))
o.append(t(80, H - 40, "A ledger, not data: each cell is a sentence of the book, shortened; the two lines on the right show the idea, not counts.", "foot", C["ink2"]))
css = f'''<style>
.eyebrow{{font:600 22px "IBM Plex Sans",Arial,sans-serif;letter-spacing:.12em;fill:{C["ink2"]}}}
.title{{font:700 54px Georgia,"Times New Roman",serif;fill:{C["ink"]}}}
.dek{{font:400 23px "IBM Plex Sans",Arial,sans-serif;fill:{C["ink2"]}}}
.lab{{font:700 30px Georgia,serif}}
.station{{font:700 22px Georgia,serif}}
.note{{font:400 20px "IBM Plex Sans",Arial,sans-serif}}
.cell{{font:400 21px "IBM Plex Sans",Arial,sans-serif}}
.mini{{font:600 17px "IBM Plex Sans",Arial,sans-serif}}
.foot{{font:italic 400 19px "IBM Plex Sans",Arial,sans-serif}}
</style>'''
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{css}' + "".join(o) + "</svg>"
stem = sys.argv[1] if len(sys.argv) > 1 else "slack-other-option"
open(stem + ".svg", "w").write(svg)
open(stem + ".html", "w").write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#f9f8f5}</style></head><body>' + svg + "</body></html>")
print("wrote", stem, "band at", yb)
