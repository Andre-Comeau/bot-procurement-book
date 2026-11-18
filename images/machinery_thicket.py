"""The machinery as a thicket (home page figure), redrawn in the book's palette on 18 November 2026.

images/machinery-thicket.svg is the drawing (the thicket from the October pitch page, badges removed,
bot monitoring renamed bot admin). This script restyles it to match the book's other figures
(delivery_methods_2x2.py, project_hex_map.py): canvas ground, Instrument Serif names, Outfit tags,
solid fills darkened toward the lead colour, hatched fog for the far worlds, and a title block.

Usage: python images/machinery_thicket.py images/machinery-thicket
  writes images/machinery-thicket-book.svg and an .html beside it; then
  node images/project_hex_map_render.js "$PWD/images/machinery-thicket-book.html" images/machinery-thicket.png 1400 1360
"""
import re
import sys

C = dict(action="#0064ff", action_p="#004fcc", action_t="#e6efff",
         sec="#0f6e56", sec_d="#085041", sec_t="#e1f5ee",
         acc="#d85a30", acc_d="#9e3d18", acc_t="#faece7",
         canvas="#f9f8f5", surface="#ffffff", muted="#f3f4f6", hair="#e5e7eb",
         ink="#2c2c2a", ink2="#5f5e5a")


def _mix(a, b, f):
    A = [int(a[i:i + 2], 16) for i in (1, 3, 5)]; B = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(A[i] + (B[i] - A[i]) * f) for i in range(3))


DARK = 0.2  # the same darkening as the chapter 2 delivery-methods figure
D = {k: _mix(C[k], C["ink"], DARK) for k in ("acc", "sec", "ink2", "action")}

W, H = 1400, 1360
X0, Y0, SCALE = 70, 200, 1.18        # where the thicket sits and how large
VW, VH = 1060, 868                   # the thicket's own view box (legend below it is cropped)
SOLID = {"exists", "built", "proposed"}

STYLE = f"""
.bg{{fill:{C["canvas"]}}}
.eyebrow{{font-family:Outfit,sans-serif;font-weight:600;font-size:15px;letter-spacing:.16em;fill:{C["action"]}}}
.title{{font-family:'Instrument Serif',Georgia,serif;font-size:54px;fill:{C["ink"]}}}
.dek{{font-family:Lora,Georgia,serif;font-size:20px;fill:{C["ink2"]}}}
.foot{{font-family:Outfit,sans-serif;font-size:15px;fill:{C["ink2"]}}}
.key{{font-family:Outfit,sans-serif;font-size:15px;fill:{C["ink"]}}}
.ground{{stroke-width:1;stroke-dasharray:2 4}}
.ground.ours{{fill:{C["action_t"]};fill-opacity:.55;stroke:{C["action"]}}}
.ground.theirs{{fill:{C["hair"]};fill-opacity:.55;stroke:{C["ink2"]}}}
.soil{{fill:{C["canvas"]};stroke:{C["hair"]}}}
.root{{fill:none;stroke:{C["ink2"]};stroke-width:1;opacity:.45}}
.clump{{stroke-width:2}}
.clump.exists{{fill:{D["ink2"]};stroke:{C["ink"]}}}
.clump.built{{fill:{D["sec"]};stroke:{C["sec_d"]}}}
.clump.proposed{{fill:{D["action"]};stroke:{C["action_p"]}}}
.clump.improved,.clump.research{{fill:url(#fog);stroke:{C["ink2"]};stroke-dasharray:6 4}}
.ic{{fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;stroke:{C["ink2"]}}}
.ic.on{{stroke:#ffffff}}
.ic.improved{{stroke:{C["sec"]}}}
.tn{{font-family:'Instrument Serif',Georgia,serif;font-size:19px;fill:{C["ink"]}}}
.tg{{font-family:Outfit,sans-serif;font-size:10.5px;font-weight:600;letter-spacing:.12em;fill:{C["ink2"]};transform:translateY(-5px)}}
.tl{{font-family:Outfit,sans-serif;font-size:13.5px;fill:{C["ink"]}}}
.tn.on,.tl.on{{fill:#ffffff}}
.tg.on{{fill:#ffffff;opacity:.8}}
.vn{{fill:none;stroke:{C["sec"]};stroke-width:1.8}}
.vn.add{{stroke-width:1.3;stroke-dasharray:5 3}}
.vn.up{{stroke:{C["ink2"]};stroke-width:3.2;opacity:.75}}
.vl{{font-family:Outfit,sans-serif;font-size:14.5px;font-weight:500;fill:{C["sec_d"]};paint-order:stroke;stroke:{C["canvas"]};stroke-width:6px;stroke-linejoin:round}}
.vl.up{{fill:{C["ink2"]}}}
.sp{{fill:none;stroke:{C["sec"]};stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}}
.sp.key{{stroke-width:1.1}}
.sp .myc{{stroke:{C["ink2"]};stroke-width:1.1;stroke-dasharray:2 3;opacity:.8}}
.sp.mushroom circle{{fill:{C["canvas"]}}}
"""

FOG = (f'<pattern id="fog" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
       f'<rect width="10" height="10" fill="{C["canvas"]}"/><path d="M0,0 V10" stroke="{C["hair"]}" stroke-width="4"/></pattern>')


def restyle(body):
    """Drop the links and mark the text and icons that sit on a solid clump."""
    body = re.sub(r"</?a\b[^>]*>", "", body)
    out, state = [], None
    for tok in re.split(r"(<[^>]+>)", body):
        m = re.match(r'<path class="clump (\w+)"', tok)
        if m:
            state = m.group(1)
        elif re.match(r'<(path|g) class="(vn|root|ground|soil|sp)', tok):
            state = None
        elif state in SOLID:
            tok = re.sub(r'class="(tn|tl|tg|ic)( [^"]*)?"', lambda k: f'class="{k.group(1)}{k.group(2) or ""} on"', tok)
        out.append(tok)
    return "".join(out)


def key(x, y, swatch, label):
    return swatch(x, y) + f'<text class="key" x="{x + 34}" y="{y + 15}">{label}</text>'


def blob(cls):
    return lambda x, y: f'<rect class="clump {cls}" x="{x}" y="{y}" width="24" height="20" rx="9"/>'


def main(stem):
    src = open(stem + ".svg", encoding="utf-8").read()
    inner = re.sub(r"^<svg[^>]*>", "", src).rsplit("</svg>", 1)[0]
    inner = re.sub(r"<style>.*?</style>", "", inner, flags=re.S)
    inner = restyle(inner)
    fy = Y0 + VH * SCALE + 34
    keys = "".join([
        key(X0, fy, blob("exists"), "exists today"),
        key(X0 + 190, fy, blob("built"), "built for this project"),
        key(X0 + 440, fy, blob("proposed"), "proposed: Bot Procurement"),
        key(X0 + 730, fy, blob("improved"), "others' ground, where the work leads"),
    ])
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="The machinery: what each machine makes for the next, from today\'s procurement system to robotic construction">'
           f'<style>{STYLE}</style><defs>{FOG}</defs>'
           f'<rect class="bg" width="{W}" height="{H}"/>'
           f'<text class="eyebrow" x="{X0}" y="78">THE PROJECT · THE MACHINERY</text>'
           f'<text class="title" x="{X0}" y="136">What each machine makes for the next</text>'
           f'<text class="dek" x="{X0}" y="174">Today\'s procurement system on one ground, the far worlds on another, and Bot Procurement between them.</text>'
           f'<svg x="{X0}" y="{Y0}" width="{VW * SCALE:.0f}" height="{VH * SCALE:.0f}" viewBox="0 0 {VW} {VH}" overflow="hidden">{inner}</svg>'
           f'{keys}'
           f'<text class="foot" x="{X0}" y="{fy + 62}">The arrows show what each machine passes to the next.</text>'
           f'</svg>')
    out = stem + "-book"
    open(out + ".svg", "w", encoding="utf-8").write(svg)
    open(out + ".html", "w", encoding="utf-8").write(
        '<!doctype html><html><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Lora:ital,wght@0,400;0,500;1,400&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">'
        f'<style>html,body{{margin:0;background:{C["canvas"]}}}</style></head><body>' + svg + "</body></html>")


if __name__ == "__main__":
    main(sys.argv[1])
