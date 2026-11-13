"""Build the book site (books.andrecomeau.xyz/bot-procurement/) from manuscript/.

Copies the chapters listed in PUBLISHED into _site_src/docs, strips the hidden
<!-- --> notes, writes the home page and mkdocs.yml, then `mkdocs build`
writes the site to _site/bot-procurement/. A _redirects file sends
the bare books.andrecomeau.xyz to the book until there is a shelf page. Chapters not yet published still appear in the
home page's contents, marked "in progress".

Every chapter and the outline are also built into a "Working copy" section
(docs/working/), so the draft can be read without GitHub. The hidden notes are
stripped there too: they point at private folders and stay out of the site.

    pip install -r requirements.txt
    python build_site.py && mkdocs build -f _site_src/mkdocs.yml
"""
import json, pathlib, re, shutil

ROOT = pathlib.Path(__file__).parent
SRC, OUT = ROOT / "manuscript", ROOT / "_site_src"
SLUG = "bot-procurement"  # the book's path on books.andrecomeau.xyz
# Shown in link previews (Discord and the like) for pages without prose of their own.
DESCRIPTION = ("When a bot causes harm, who pays? A short manifesto on liability in construction "
               "procurement, written in public during the Protocol Institute's PiBoWriMo, November 2026.")

# Link previews for chapters that have been worked on: their own figure (a card
# made by images/social_card.py) and their opening line as the description, in the
# working copy too. Every other page uses DESCRIPTION and images/social-card.png.
PREVIEWS = {
    "00c-introduction.md": ("social-card.png",
        "The zombie garden: construction documents shamble as zombies between the designer and the buyer, with the bidders all round the wall"),
    "03-how-a-price-is-judged-today.md": ("social-card-delivery-methods.png",
        "Who works for whom, and how they deal: the delivery methods on two axes, Principal to Principal or to Agent, and competitive or cooperative"),
    "03b-what-do-we-do-with-a-drunken-sailor.md": ("social-card-failure-modes.png",
        "How words and deeds go wrong: a stained-glass window of the Serpent, the Dragon, the Drunken Sailor and Who's on First, with the standard bot at its centre"),
    "07-building-an-estimator-in-public.md": ("social-card-second-opinion.png",
        "Bot Procurement World: an overworld map from tender to change order, with the estimator's and evaluator's huts, the slow road of haunted fortresses, and the Standard in the next world"),
    "00b-prologue.md": ("social-card-hex-map.png",
        "The project as a hex map: one town, one temple, and fog to the east"),
    "09-the-protocol-that-follows.md": ("social-card-world-2.png",
        "The Standard, World 2 of the overworld map: existing standards as levels, each with the change the book would ask of it, leading to a castle and a courthouse"),
    "06e-the-underwriters-chapter.md": ("social-card-one-losing-job.png",
        "One losing job is not a claim: completed jobs as mugs filled to their margin, and a policy that pays only when the average across many tenders falls short"),
    "app-e-pilot-term-sheet.md": ("social-card-one-losing-job.png",
        "A draft term sheet for a pilot policy insuring an estimating bot's margin, for an underwriter to mark up"),
}

# Chapters that go on the public site. Add a file here when it is ready to read.
PUBLISHED = {"00b-prologue.md"}

# Chapters with written text, as against an outline (a brief, notes and source
# passages laid out for writing). Add a file here once its text is drafted; every
# other chapter is marked "Outline" on the contents pages and at the top of the page.
DRAFTED = {
    "00b-prologue.md", "07-building-an-estimator-in-public.md",
    "03-how-a-price-is-judged-today.md", "03b-what-do-we-do-with-a-drunken-sailor.md",
    "00c-introduction.md", "06e-the-underwriters-chapter.md",
    "09-the-protocol-that-follows.md", "app-d-bibliography.md", "app-e-pilot-term-sheet.md",
    "02-the-tender-is-the-api.md", "02b-the-buyers.md", "02c-the-bidders.md", "02d-the-vendors.md",
}

# The labels, in plain words, and the line at the top of each working-copy page.
BADGE = '<span class="book-status book-status--{kind}">{label}</span>'
STATUS = {
    "ready": ("Ready to read", "This chapter is published on the home page."),
    "drafted": ("Drafted", "The chapter is written and still being revised."),
    "outline": ("Outline", "Not written yet: what follows is the plan for the chapter, "
                           "with notes and passages gathered to write it from."),
}


def status(name):
    return "ready" if name in PUBLISHED else "drafted" if name in DRAFTED else "outline"


def badge(name):
    kind = status(name)
    return BADGE.format(kind=kind, label=STATUS[kind][0])

PARTS = [
    # File names keep their first numbers; this list is the reading order
    # (since 2026-11-07, Part I follows the vgr_zirp review's order for a newcomer).
    ("Front matter", [("00-front-matter.md", "Front matter"), ("00b-prologue.md", "Prologue")]),
    ("Part I. The way in", [
        ("07-building-an-estimator-in-public.md", "1. A second opinion on every price"),
        ("03-how-a-price-is-judged-today.md", "2. How a price is judged today"),
        ("03b-what-do-we-do-with-a-drunken-sailor.md", "3. What do we do with a drunken sailor?"),
        ("00c-introduction.md", "4. The zombie garden")]),
    ("Part II. The question", [
        ("01-expecting-a-divorce.md", "5. Starting a relationship expecting a divorce"),
        ("02-the-tender-is-the-api.md", "6. The tender is the API"),
        # The three parties at the tender's door, drafted 2026-11-13; numbering to be decided.
        ("02b-the-buyers.md", "6a. The buyers: more bids than eyes"),
        ("02c-the-bidders.md", "6b. The bidders: racing for the light"),
        ("02d-the-vendors.md", "6c. The vendors: players, not referees")]),
    ("Part III. The machines", [
        ("04-two-centuries-of-one-loop.md", "7. Two centuries of one loop"),
        ("05-liability-shifts.md", "8. Liability shifts to the user's bot"),
        ("06-the-banana-peel.md", "9. The banana peel"),
        ("06b-the-bot-in-the-witness-box.md", "10. The bot in the witness box"),
        ("06e-the-underwriters-chapter.md", "The underwriters' chapter (draft, place to be decided)")]),
    ("Part IV. The protocol that follows", [
        ("09-the-protocol-that-follows.md", "11. The protocol that follows"),
        ("10-the-meta-goal.md", "12. The meta-goal")]),
    ("Appendices", [
        ("app-a-the-cards.md", "A. Procurement Machines"),
        ("app-b-reading-list.md", "B. Reading list"),
        ("app-c-glossary.md", "C. Glossary"),
        ("app-d-bibliography.md", "D. Bibliography"),
        ("app-e-pilot-term-sheet.md", "E. A draft term sheet for a pilot policy")]),
]

HOME = """# Bot Procurement Book

*Working title. A book in progress, written in public during the Protocol Institute's PiBoWriMo, November 2026.*

**When a bot causes harm, who pays?** A short manifesto on liability in construction procurement, public and private, and the standard that has to exist before owners, bidders and courts can rely on a bot.

![The machinery: the procurement system, the estimator and bot procurement on one ground; BIM, bot monitoring and robotic construction on another, with what each machine makes for the next](images/machinery-thicket.png)

*The machinery, from today's procurement system to robotic construction: what each machine makes for the next.*

![The project as a hex map: Field Building is the town and the Standard its temple; guild houses, libraries, workshops and towers feed them; adopters arrive on their own; BIM for bots, bot monitoring and robotic construction lie in the fog to the east](images/project-hex-map.png)

*The project as a hex map: one town, one temple, and fog to the east. The order of building comes from an old role-playing game: temple first, then followers, then the stronghold.*

Chapters appear here as they are finished. The source is on [GitHub](https://github.com/Andre-Comeau/bot-procurement-book).

**Working copy.** Every chapter as it stands today is in the [working copy](working/index.md), and it changes often. In the contents below, chapters marked {drafted} have been written and can be read there as drafts. Chapters marked {outline} are not written yet: they hold the plan for the chapter and the notes gathered to write it.

## Contents

{toc}

---

By Andre Comeau. Text licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
"""

CONFIG = """site_name: Bot Procurement Book
site_url: https://books.andrecomeau.xyz/{slug}/
site_description: {description}
site_author: Andre Comeau
copyright: Text by Andre Comeau, CC BY 4.0
repo_url: https://github.com/Andre-Comeau/bot-procurement-book
docs_dir: docs
site_dir: ../_site/{slug}
theme:
  name: material
  custom_dir: overrides
  features: [navigation.sections, navigation.footer, navigation.top]
  font: false
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: custom
      accent: custom
      toggle: {{icon: material/brightness-4, name: Dark mode}}
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: custom
      accent: custom
      toggle: {{icon: material/brightness-7, name: Light mode}}
extra_css: [stylesheets/book.css]
markdown_extensions: [attr_list, footnotes, admonition]
nav:
  - Home: index.md
{nav}"""


WORKING_BANNER = """!!! warning "Working copy"
    Draft text, rebuilt from the manuscript on every change. Stubs and source passages
    are still here, and none of it is final. [Back to the working copy contents](index.md)

"""

WORKING_HOME = """# Working copy

Every chapter as it stands in the manuscript today, with the outline. Drafts, stubs and
source passages laid out for rewriting are all shown.

{ready} chapters are also on the [home page](../index.md). {drafted} chapters are written
and still being revised. {outline} chapters are not written yet: they hold the plan for the
chapter and the notes gathered to write it.

- [Outline](outline.md)

{toc}
"""


def strip_notes(text):
    return re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)


def with_description(text, name, prefix=""):
    """Put the chapter's first paragraph of prose in its front matter, for link
    previews, with its card from PREVIEWS if it has one. `prefix` (the working-copy
    banner) goes after the front matter."""
    meta = {}
    if name in PREVIEWS:
        meta["image"], meta["image_alt"] = PREVIEWS[name]
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        # Skip headings, figures, admonitions, tables, quotes, lists, HTML and rules.
        if not para or para.startswith(("#", "!", "|", ">", "- ", "* ", "1. ", "<", "---")):
            continue
        plain = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", para)  # links and images to their text
        plain = re.sub(r"[*_`]", "", " ".join(plain.split()))
        # Curly quotes: Material writes the description into an attribute unescaped.
        plain = re.sub(r'"([^"]*)"', "\u201c\\1\u201d", plain).replace('"', "\u201d")
        if len(plain) < 40:
            continue
        if len(plain) > 200:
            plain = plain[:200].rsplit(" ", 1)[0].rstrip(",;:") + "\u2026"
        meta["description"] = plain
        break
    if not meta:
        return prefix + text
    front = "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in meta.items())
    return f"---\n{front}---\n\n" + prefix + text


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    docs = OUT / "docs"
    docs.mkdir(parents=True)
    toc, nav = [], []
    for part, chapters in PARTS:
        toc.append(f"**{part}**\n")
        items = []
        for name, title in chapters:
            if name in PUBLISHED:
                text = (SRC / name).read_text(encoding="utf-8")
                (docs / name).write_text(with_description(strip_notes(text), name), encoding="utf-8")
                toc.append(f"- [{title}]({name})")
                items.append(f'      - "{title}": {name}')
            else:
                toc.append(f"- [{title}](working/{name}) {badge(name)}")
        toc.append("")
        if items:
            nav.append(f'  - "{part}":\n' + "\n".join(items))
    # Working copy: every chapter and the outline, notes stripped.
    work = docs / "working"
    work.mkdir()
    wtoc, wnav = [], ['      - "Contents": working/index.md', '      - "Outline": working/outline.md']
    outline = strip_notes((ROOT / "outline.md").read_text(encoding="utf-8"))
    (work / "outline.md").write_text(WORKING_BANNER + outline, encoding="utf-8")
    for part, chapters in PARTS:
        wtoc.append(f"**{part}**\n")
        for name, title in chapters:
            text = strip_notes((SRC / name).read_text(encoding="utf-8"))
            line = STATUS[status(name)][1]
            prefix = WORKING_BANNER + f'<p class="book-status-line">{badge(name)} {line}</p>\n\n'
            # Stubs open with editorial notes, so only worked chapters get their own preview.
            text = with_description(text, name, prefix) if name in PREVIEWS else prefix + text
            (work / name).write_text(text, encoding="utf-8")
            wtoc.append(f"- [{title}]({name}) {badge(name)}")
            wnav.append(f'      - "{title}": working/{name}')
        wtoc.append("")
    labels = {k: BADGE.format(kind=k, label=v[0]) for k, v in STATUS.items()}
    (work / "index.md").write_text(WORKING_HOME.format(toc="\n".join(wtoc), **labels), encoding="utf-8")
    nav.append('  - "Working copy":\n' + "\n".join(wnav))
    shutil.copytree(ROOT / "images", docs / "images", ignore=shutil.ignore_patterns("README.md", "*.py", "*.js", "*.html"))
    (docs / "stylesheets").mkdir()
    shutil.copy(ROOT / "theme" / "book.css", docs / "stylesheets" / "book.css")
    shutil.copytree(ROOT / "theme" / "overrides", OUT / "overrides")
    (docs / "index.md").write_text(HOME.format(toc="\n".join(toc), **labels), encoding="utf-8")
    site = ROOT / "_site"
    shutil.rmtree(site, ignore_errors=True)
    site.mkdir()
    (site / "_redirects").write_text(f"/ /{SLUG}/ 302\n", encoding="utf-8")
    (OUT / "mkdocs.yml").write_text(CONFIG.format(slug=SLUG, description=json.dumps(DESCRIPTION), nav="\n".join(nav) + "\n"), encoding="utf-8")


if __name__ == "__main__":
    main()
