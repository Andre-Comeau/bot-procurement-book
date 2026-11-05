"""Make images/social-card.png, the 1200 x 630 preview image that Discord and
other sites show when a link to the book site is shared.

The zombie garden figure is scaled to the card's height and centred on its own
paper colour. Needs Pillow:  python images/social_card.py
"""
import pathlib
from PIL import Image

HERE = pathlib.Path(__file__).parent
W, H = 1200, 630
PAPER = (244, 241, 234)  # the zombie garden's background

fig = Image.open(HERE / "zombie-garden.png").convert("RGB")
fig = fig.resize((round(fig.width * H / fig.height), H), Image.LANCZOS)
card = Image.new("RGB", (W, H), PAPER)
card.paste(fig, ((W - fig.width) // 2, 0))
card.save(HERE / "social-card.png", optimize=True)
