"""Build the book site (books.andrecomeau.xyz/bot-procurement/) from manuscript/.

Copies the chapters listed in PUBLISHED into _site_src/docs, strips the hidden
<!-- --> notes, writes the home page and mkdocs.yml, then `mkdocs build`
writes the site to _site/bot-procurement/. A _redirects file sends
the bare books.andrecomeau.xyz to the book until there is a shelf page. Chapters not yet published still appear in the
home page's contents, marked "in progress".

Every chapter is also built into a "Working copy" section
(docs/working/), so the draft can be read without GitHub. The hidden notes are
stripped there too: they point at private folders and stay out of the site.

    pip install -r requirements.txt
    python build_site.py && mkdocs build -f _site_src/mkdocs.yml
"""
import json, pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).parent
SRC, OUT = ROOT / "manuscript", ROOT / "_site_src"
SLUG = "bot-procurement"  # the book's path on books.andrecomeau.xyz
# Shown in link previews (Discord and the like) for pages without prose of their own.
DESCRIPTION = ("A free, open guide to AI that prices and checks construction bids, tenders and change "
               "orders in public procurement: how accurate it is, who can rely on it, and a proposed open "
               "test of how far its prices miss.")

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
    "09-the-protocol-that-follows.md": ("social-card-world-2.png",
        "The Standard, World 2 of the overworld map: existing standards as levels, each with the change the book would ask of it, leading to a castle and a courthouse"),
    "06e-the-underwriters-chapter.md": ("social-card-one-losing-job.png",
        "Insuring the bidder's margin. One losing job is not a claim: completed jobs as mugs filled to their margin, and a policy that pays only when the average across many tenders falls short"),
    "02-the-tender-is-the-api.md": ("social-card-oak-falls.png",
        "The oak falls: the cost of bidding stood as an oak over the market for a century; where it stood, a thicket races for the light"),
    "02b-the-buyers.md": ("social-card-three-parties.png",
        "Three parties at the door: the buyers with more bids than eyes, the bidders racing for the light, the vendors selling shovels; what each needs, what a published check gives them, and the standard and the insurer beneath them"),
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
    "02-the-tender-is-the-api.md", "02b-the-buyers.md", "02c-the-bidders.md", "02d-the-vendors.md", "02e-the-designers.md", "06f-the-insurers.md",
    "06c-the-blessing-of-the-legal-department.md", "08b-the-zombie-lost-to-a-file-format.md",
    "09a-the-trades-who-holds-the-jig.md", "09b-the-monsters-we-kept.md",
    "00-front-matter.md", "01-expecting-a-divorce.md", "06-the-banana-peel.md",
    "06b-the-bot-in-the-witness-box.md", "04-two-centuries-of-one-loop.md", "10-the-meta-goal.md",
    "app-a-the-cards.md", "app-b-reading-list.md", "app-c-glossary.md",
    "app-f-who-to-talk-to-first.md",
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
    # File names keep their first numbers; this list is the reading order.
    # The part names are the book's questions, and each stakeholder has its own chapter number.
    ("Front matter", [("00-front-matter.md", "Front matter")]),
    ("Overview. Why do we need a standard?", [("00b-prologue.md", "Prologue")]),
    ("Part I. What is the problem?", [
        ("02-the-tender-is-the-api.md", "1. The tender and the flood of AI bids"),
        ("01-expecting-a-divorce.md", "2. Tensions built into the tender")]),
    ("Part II. How should we solve it?", [
        ("06e-the-underwriters-chapter.md", "3. Insuring the bidder's margin")]),
    ("Part III. Why not use other tools? Why not change the contract type?", [
        ("03-how-a-price-is-judged-today.md", "4. Why does the hard bid survive?"),
        ("08b-the-zombie-lost-to-a-file-format.md", "5. Where bids already travel as data"),
        ("09b-the-monsters-we-kept.md", "6. Bigger ideas set aside for now")]),
    ("Part IV. What do the stakeholders stand to gain?", [
        ("02b-the-buyers.md", "7. The buyers: more bids than they can read"),
        ("02c-the-bidders.md", "8. The bidders: what a check and cover change"),
        ("09a-the-trades-who-holds-the-jig.md", "9. The trades: who sets up the machines"),
        ("02e-the-designers.md", "10. The designers and consultants: checking the documents before issue"),
        ("02d-the-vendors.md", "11. The software vendors: why a shared test suits them"),
        ("06c-the-blessing-of-the-legal-department.md", "12. What a legal department needs before relying on a bot"),
        ("06f-the-insurers.md", "13. The insurers: a pilot, then a standard")]),
    ("Part V. How are we going to get there?", [
        ("03b-what-do-we-do-with-a-drunken-sailor.md", "14. How AI fails, and a remedy for each"),
        ("06-the-banana-peel.md", "14a. A bot should show what it does not know (to fold into chapter 14)"),
        ("00c-introduction.md", "15. What AI gets right"),
        ("07-building-an-estimator-in-public.md", "16. The estimator and the evaluator: a second opinion on every price"),
        ("09-the-protocol-that-follows.md", "17. Three standards, and how they could stick"),
        ("06b-the-bot-in-the-witness-box.md", "17a. One bot failure, from tender to court (to fold into chapter 17)")]),
    ("Part VI. How have things changed in the past?", [
        ("04-two-centuries-of-one-loop.md", "18. Two centuries of tendering")]),
    ("Part VII. Where does this end up?", [
        ("10-the-meta-goal.md", "19. The goal: more autonomy for the people who build")]),
    ("Appendices", [
        ("app-a-the-cards.md", "A. Procurement Machines"),
        ("app-b-reading-list.md", "B. Reading list"),
        ("app-c-glossary.md", "C. Glossary"),
        ("app-d-bibliography.md", "D. Bibliography"),
        ("app-e-pilot-term-sheet.md", "E. A draft term sheet for a pilot policy"),
        ("app-f-who-to-talk-to-first.md", "F. Who to talk to first")]),
]

HOME = """# Bot Procurement Book

*A book in progress, written in public during the Protocol Institute's PiBoWriMo, November 2026.*

<p class="book-lead">{description}</p>

## Two editions, one argument

The same ideas are written twice: once as a book for people to read from start to finish, and once as short, sourced modules for AI assistants to look things up in.

<div class="grid cards book-doors" markdown>

-   **For people: the book**

    ---

    Chapters that build one argument, from the problem through the people who gain to the road there. Read it in order, or start with your own chapter.

    [Start with the prologue](working/00b-prologue.md) · [Contents](#contents) · [Outline](working/outline.md)

-   **For AI assistants: the AI edition**

    ---

    Thirty-five short modules, each answering its own questions, with the sources and asides the book leaves out. Point your assistant here.

    [AI edition](ai/README.md) · [Index](ai/INDEX.md) · [llms.txt](ai/llms.txt)

</div>

*This is not legal, insurance or financial advice. The legal and insurance points in this work have not been reviewed by a lawyer or an underwriter. Ask your own adviser before relying on them.*

![The machinery: the procurement system, the estimator and bot procurement on one ground; BIM, BIM for bots, bot admin and robotic construction on another, with what each machine makes for the next](images/machinery-thicket.png)

*The machinery, from today's procurement system to robotic construction: what each machine makes for the next.*

## Contents

Every chapter is in the [working copy](working/index.md) as it stands today, and it changes often. Chapters marked {drafted} can be read there as drafts. The source is on [GitHub](https://github.com/Andre-Comeau/bot-procurement-book).

{toc}

---

By Andre Comeau. Text licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
"""

SITE_NAME = "Bot Procurement Book"

CONFIG = """site_name: Bot Procurement Book
site_url: https://books.andrecomeau.xyz/{slug}/
site_description: {description}
site_author: Andre Comeau
copyright: Text by Andre Comeau, CC BY 4.0
repo_url: https://github.com/Andre-Comeau/bot-procurement-book
docs_dir: docs
hooks: [hooks.py]
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
markdown_extensions: [attr_list, footnotes, admonition, md_in_html, pymdownx.details]
nav:
  - Home: index.md
{nav}"""


WORKING_BANNER = """!!! warning "Working copy"
    Draft text, rebuilt from the manuscript on every change. None of it is final yet. [Back to the working copy contents](index.md)

"""

WORKING_HOME = """# Working copy

Every chapter as it stands in the manuscript today, with a one-page outline of the book.

{ready} chapters are also on the [home page](../index.md). {drafted} chapters are written
and still being revised. The outline is a one-page map of the whole book.

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


def with_meta(text, **meta):
    """Add keys to a page's front matter, making one if it has none. Used for
    `robots: noindex` on outline pages (search and AI indexes skip the outlines;
    drafted chapters stay findable; people can read every page)."""
    lines = "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in meta.items())
    if text.startswith("---\n"):
        return "---\n" + lines + text[4:]
    return f"---\n{lines}---\n\n" + text


# Files for machines: llms.txt (https://llmstxt.org/) at the domain root and in the
# book's folder, and llms-full.txt, the readable text in one file. Outlines are left
# out of both; the hidden notes and any source passages are stripped.
LLMS_SUMMARY = (DESCRIPTION + " Bot Procurement is a book in draft, written in public, on how "
                "that AI could be relied on by buyers, bidders, insurers and courts. Bot "
                "Procurement is a proposal; its test has not been run and no standards body has adopted it. "
                "Bot Construction is the wider field it belongs to. Text CC BY 4.0, by Andre Comeau. "
                "This is not legal, insurance or financial advice. The legal and insurance points in this work have not been reviewed by a lawyer or an underwriter. Ask your own adviser before relying on them.")


def page_url(name, working=False):
    stem = name[:-3]
    return f"https://books.andrecomeau.xyz/{SLUG}/" + ("working/" if working else "") + f"{stem}/"


def write_llms(site_root, docs):
    """llms.txt at the domain root (site_root) and, with llms-full.txt, in the book's
    folder (docs, which mkdocs copies as they are: its build empties _site/{SLUG})."""
    readable = [(n, t) for _, chapters in PARTS for n, t in chapters if status(n) != "outline"]
    lines = [f"# {SITE_NAME}", "", f"> {LLMS_SUMMARY}", "",
             "Bot Procurement is a proposal. Nothing is yet compliant with, certified "
             "under or conforming to Bot Procurement.", "", "## Chapters", ""]
    for name, title in readable:
        lines.append(f"- [{title}]({page_url(name, name not in PUBLISHED)}): "
                     f"{STATUS[status(name)][0]}")
    lines += ["", "## Optional", "",
              f"- [Whole text in one file](https://books.andrecomeau.xyz/{SLUG}/llms-full.txt)",
              f"- [Working copy contents](https://books.andrecomeau.xyz/{SLUG}/working/): "
              "every chapter as it stands",
              f"- [AI edition](https://books.andrecomeau.xyz/{SLUG}/ai/llms.txt): the same ideas "
              "in short, sourced modules, with their own llms.txt",
              "- [Source repository](https://github.com/Andre-Comeau/bot-procurement-book)", ""]
    index = "\n".join(lines)
    full = [f"# {SITE_NAME}", "", f"> {LLMS_SUMMARY}", ""]
    for name, title in readable:
        body = strip_notes((SRC / name).read_text(encoding="utf-8"))
        # Drafted chapters may still end with source passages kept for rewriting: leave them out.
        body = re.split(r"^## Source passages", body, maxsplit=1, flags=re.M)[0].strip()
        full += ["", "---", "", f"<!-- {title} | {STATUS[status(name)][0]} | {page_url(name, name not in PUBLISHED)} -->",
                 "", body, ""]
    for folder in (site_root, docs):
        (folder / "llms.txt").write_text(index, encoding="utf-8")
    (docs / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")


# The book's text is CC BY 4.0 and meant to be read, quoted and learned from, so the
# robots file says yes to search, AI answers and AI training (Cloudflare's Content
# Signals: https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/).
# If Cloudflare's managed robots.txt is on, it is added in front of this file.
ROBOTS = f"""# Text on this site is licensed CC BY 4.0. Search, AI answers and AI training
# are welcome, with attribution.
User-agent: *
Content-Signal: search=yes, ai-input=yes, ai-train=yes
Allow: /

Sitemap: https://books.andrecomeau.xyz/{SLUG}/sitemap.xml
"""


# The AI edition (ai/) is built by tools/build_ai.py into docs/ai, where mkdocs renders each
# module as a page. The hook then copies the Markdown itself next to the pages, so agents can
# read /ai/<module>.md, the address its llms.txt gives.
HOOKS = """import pathlib, shutil

def on_post_build(config):
    src = pathlib.Path(config["docs_dir"]) / "ai"
    out = pathlib.Path(config["site_dir"]) / "ai"
    for p in src.glob("*.md"):
        shutil.copy(p, out / p.name)
"""


def build_ai(docs):
    """Copy the AI edition into the site and build its index files. Modules held back
    from publication (publish: hold) are left out, and any link to one fails the build."""
    shutil.copytree(ROOT / "ai", docs / "ai")
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_ai.py"), str(docs / "ai"),
                    "--public", "--strict"], check=True)
    # The sources sit in each module's front matter, which the page hides: list them on the page too.
    import yaml
    for p in sorted((docs / "ai").glob("bp-*.md")):
        text = p.read_text(encoding="utf-8")
        meta = yaml.safe_load(text.split("---", 2)[1]) or {}
        items = []
        for s in meta.get("sources") or []:
            s = s if isinstance(s, dict) else {"title": str(s)}
            items.append(f"- [{s['title']}]({s['url']})" if s.get("url") else f"- {s['title']}")
        if items and not re.search(r"^## Sources", text, flags=re.M):
            p.write_text(text.rstrip() + "\n\n## Sources\n\n" + "\n".join(items) + "\n", encoding="utf-8")


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    docs = OUT / "docs"
    docs.mkdir(parents=True)
    toc, nav = [], []
    for part, chapters in PARTS:
        toc.append(f'??? book-part "{part}"\n')
        items = []
        for name, title in chapters:
            if name in PUBLISHED:
                text = (SRC / name).read_text(encoding="utf-8")
                (docs / name).write_text(with_description(strip_notes(text), name), encoding="utf-8")
                toc.append(f"    - [{title}]({name})")
                items.append(f'      - "{title}": {name}')
            else:
                toc.append(f"    - [{title}](working/{name}) {badge(name)}")
        toc.append("")
        if items:
            nav.append(f'  - "{part}":\n' + "\n".join(items))
    # Working copy: every chapter and the outline, notes stripped.
    work = docs / "working"
    work.mkdir()
    wtoc, wnav = [], ['      - "Contents": working/index.md', '      - "Outline": working/outline.md']
    # The outline is a reader's map of the book; working notes stay out of the repository.
    outline = strip_notes((ROOT / "outline.md").read_text(encoding="utf-8"))
    (work / "outline.md").write_text(WORKING_BANNER + outline, encoding="utf-8")
    for part, chapters in PARTS:
        wtoc.append(f'??? book-part "{part}"\n')
        wnav.append(f'      - "{part}":')
        for name, title in chapters:
            text = strip_notes((SRC / name).read_text(encoding="utf-8"))
            line = STATUS[status(name)][1]
            prefix = WORKING_BANNER + f'<p class="book-status-line">{badge(name)} {line}</p>\n\n'
            # Stubs open with editorial notes, so only worked chapters get their own preview.
            text = with_description(text, name, prefix) if name in PREVIEWS else prefix + text
            if status(name) == "outline":
                text = with_meta(text, robots="noindex")
            (work / name).write_text(text, encoding="utf-8")
            wtoc.append(f"    - [{title}]({name}) {badge(name)}")
            wnav.append(f'          - "{title}": working/{name}')
        wtoc.append("")
    labels = {k: BADGE.format(kind=k, label=v[0]) for k, v in STATUS.items()}
    (work / "index.md").write_text(WORKING_HOME.format(toc="\n".join(wtoc), **labels), encoding="utf-8")
    nav.append('  - "Working copy":\n' + "\n".join(wnav))
    build_ai(docs)
    nav.append('  - "AI edition":\n      - "About": ai/README.md\n      - "Index": ai/INDEX.md\n      - "Questions": ai/FAQ.md')
    (OUT / "hooks.py").write_text(HOOKS, encoding="utf-8")
    shutil.copytree(ROOT / "images", docs / "images", ignore=shutil.ignore_patterns("README.md", "*.py", "*.js", "*.html"))
    (docs / "stylesheets").mkdir()
    shutil.copy(ROOT / "theme" / "book.css", docs / "stylesheets" / "book.css")
    shutil.copytree(ROOT / "theme" / "overrides", OUT / "overrides")
    (docs / "index.md").write_text(HOME.format(toc="\n".join(toc), description=DESCRIPTION, **labels), encoding="utf-8")
    site = ROOT / "_site"
    shutil.rmtree(site, ignore_errors=True)
    site.mkdir()
    (site / "_redirects").write_text(
        f"/ /{SLUG}/ 302\n"
        # Chapter 3a was folded into chapter 3.
        f"/{SLUG}/working/05-liability-shifts/ /{SLUG}/working/06e-the-underwriters-chapter/#who-answers-for-the-reading 301\n",
        encoding="utf-8")
    (site / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    write_llms(site, docs)
    (OUT / "mkdocs.yml").write_text(CONFIG.format(slug=SLUG, description=json.dumps(DESCRIPTION), nav="\n".join(nav) + "\n"), encoding="utf-8")


if __name__ == "__main__":
    main()
