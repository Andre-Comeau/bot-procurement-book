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
import pathlib, re, shutil

ROOT = pathlib.Path(__file__).parent
SRC, OUT = ROOT / "manuscript", ROOT / "_site_src"
SLUG = "bot-procurement"  # the book's path on books.andrecomeau.xyz

# Chapters that go on the public site. Add a file here when it is ready to read.
PUBLISHED = {"00b-prologue.md"}

PARTS = [
    ("Front matter", [("00-front-matter.md", "Front matter"), ("00b-prologue.md", "Prologue")]),
    ("Part I. The question", [
        ("01-expecting-a-divorce.md", "1. Starting a relationship expecting a divorce"),
        ("02-the-tender-is-the-api.md", "2. The tender is the API"),
        ("03-how-a-price-is-judged-today.md", "3. How a price is judged today")]),
    ("Part II. The machines", [
        ("04-two-centuries-of-one-loop.md", "4. Two centuries of one loop"),
        ("05-liability-shifts.md", "5. Liability shifts to the user's bot"),
        ("06-the-banana-peel.md", "6. The banana peel"),
        ("06b-the-bot-in-the-witness-box.md", "7. The bot in the witness box")]),
    ("Part III. The proof", [
        ("07-building-an-estimator-in-public.md", "8. Building an estimator in public"),
        ("08-what-an-evaluator-needs.md", "9. What an evaluator needs")]),
    ("Part IV. The protocol that follows", [
        ("09-the-protocol-that-follows.md", "10. The protocol that follows"),
        ("10-the-meta-goal.md", "11. The meta-goal")]),
    ("Appendices", [
        ("app-a-the-cards.md", "A. Procurement Machines"),
        ("app-b-reading-list.md", "B. Reading list"),
        ("app-c-glossary.md", "C. Glossary")]),
]

HOME = """# Bot Procurement Book

*Working title. A book in progress, written in public during the Protocol Institute's PiBoWriMo, November 2026.*

**Is this price fair and reasonable?** A short manifesto on how anyone knows a construction price is fair, and what happens to procurement when a bot can answer that question.

![The machinery: the procurement system, the estimator and bot procurement on one ground; BIM, bot monitoring and robotic construction on another, with what each machine makes for the next](images/machinery-thicket.png)

*The machinery, from today's procurement system to robotic construction: what each machine makes for the next.*

![The project as a hex map: Field Building is the town and the Standard its temple; guild houses, libraries, workshops and towers feed them; adopters arrive on their own; BIM for bots, bot monitoring and robotic construction lie in the fog to the east](images/project-hex-map.png)

*The project as a hex map: one town, one temple, and fog to the east. The order of building comes from an old role-playing game: temple first, then followers, then the stronghold.*

Chapters appear here as they are drafted. The source is on [GitHub](https://github.com/Andre-Comeau/bot-procurement-book).

**Working copy.** Every chapter as it stands today, drafts and stubs included, is in the [working copy](working/index.md). It changes often.

## Contents

{toc}

---

By Andre Comeau. Text licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
"""

CONFIG = """site_name: Bot Procurement Book
site_url: https://books.andrecomeau.xyz/{slug}/
site_author: Andre Comeau
copyright: Text by Andre Comeau, CC BY 4.0
repo_url: https://github.com/Andre-Comeau/bot-procurement-book
docs_dir: docs
site_dir: ../_site/{slug}
theme:
  name: material
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
source passages laid out for rewriting are all shown. Chapters marked *published* on the
[home page](../index.md) are the ones ready to read.

- [Outline](outline.md)

{toc}
"""


def strip_notes(text):
    return re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)


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
                (docs / name).write_text(strip_notes(text), encoding="utf-8")
                toc.append(f"- [{title}]({name})")
                items.append(f'      - "{title}": {name}')
            else:
                toc.append(f"- {title} *(in progress)*")
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
            (work / name).write_text(WORKING_BANNER + text, encoding="utf-8")
            wtoc.append(f"- [{title}]({name})")
            wnav.append(f'      - "{title}": working/{name}')
        wtoc.append("")
    (work / "index.md").write_text(WORKING_HOME.format(toc="\n".join(wtoc)), encoding="utf-8")
    nav.append('  - "Working copy":\n' + "\n".join(wnav))
    shutil.copytree(ROOT / "images", docs / "images", ignore=shutil.ignore_patterns("README.md", "*.py", "*.js", "*.html"))
    (docs / "stylesheets").mkdir()
    shutil.copy(ROOT / "theme" / "book.css", docs / "stylesheets" / "book.css")
    (docs / "index.md").write_text(HOME.format(toc="\n".join(toc)), encoding="utf-8")
    site = ROOT / "_site"
    shutil.rmtree(site, ignore_errors=True)
    site.mkdir()
    (site / "_redirects").write_text(f"/ /{SLUG}/ 302\n", encoding="utf-8")
    (OUT / "mkdocs.yml").write_text(CONFIG.format(slug=SLUG, nav="\n".join(nav) + "\n"), encoding="utf-8")


if __name__ == "__main__":
    main()
