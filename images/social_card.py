"""Make the 1200 x 630 preview images that Discord and other sites show when a
link to the book site is shared.

Each figure is scaled to the card's height and centred on its own paper colour.
`social-card.png`, from the zombie garden, is the book's default; the others go
with the chapters that use their figure (PREVIEWS in build_site.py).
Needs Pillow:  python images/social_card.py
"""
import pathlib
from PIL import Image

HERE = pathlib.Path(__file__).parent
W, H = 1200, 630
CARDS = [  # (figure, card)
    ("zombie-garden.png", "social-card.png"),
    ("delivery-methods-2x2.png", "social-card-delivery-methods.png"),
    ("failure-modes-glass.png", "social-card-failure-modes.png"),
    ("second-opinion.png", "social-card-second-opinion.png"),
    ("project-hex-map.png", "social-card-hex-map.png"),
    ("world-2-standards.png", "social-card-world-2.png"),
    ("one-losing-job.png", "social-card-one-losing-job.png"),
]

for figure, card_name in CARDS:
    fig = Image.open(HERE / figure).convert("RGB")
    paper = fig.getpixel((5, 5))  # the figure's background
    fig = fig.resize((round(fig.width * H / fig.height), H), Image.LANCZOS)
    card = Image.new("RGB", (W, H), paper)
    card.paste(fig, ((W - fig.width) // 2, 0))
    card.save(HERE / card_name, optimize=True)
