"""Build and check the AI-first edition of Bot Procurement.

The edition is a flat folder of Markdown modules, each with YAML front matter.
This script checks the modules against each other (one meaning per term, every
link resolves, status words used the same way) and writes the routing files:

    INDEX.md      a human-readable map, grouped by module type
    INDEX.json    the same map for machines
    FAQ.md        every question a module answers, with a short answer and a link
    llms.txt      the front door for agents (https://llmstxt.org/)
    llms-full.txt every module in one file
    modules.jsonl one module per line, front matter plus body, for datasets

README.md is written by hand. Run from anywhere:

    python build_ai.py path/to/ai [--strict] [--public]

--strict turns warnings into errors (for CI).
--public leaves out modules marked `publish: hold` (use for anything that goes online).
"""
import json, re, sys, pathlib, datetime
import yaml

BASE_URL = "https://books.andrecomeau.xyz/bot-procurement/ai/"
REPO_URL = "https://github.com/Andre-Comeau/bot-procurement-book"
GENERATED = {"INDEX.md", "FAQ.md"}
HANDWRITTEN = {"README.md"}

TYPES = {  # order = order in INDEX.md
    "overview": "Start here",
    "problem": "The problem",
    "proposal": "What the project proposes",
    "tool": "Tools in development",
    "stakeholder": "Stakeholders: what each stands to gain",
    "alternative": "Why not something else",
    "risk": "AI: what it gets wrong, what it gets right, and the risks",
    "evidence": "Evidence",
    "history": "How things changed before",
    "future": "Where this ends up",
    "reference": "Reference",
}
STATUSES = {"draft", "outline"}
RELATIONS = {"part-of", "has-part", "depends-on", "supports", "contrasts", "example-of",
             "answers", "see-also", "next"}
REQUIRED = ["id", "title", "type", "status", "summary", "updated", "audience",
            "questions", "related", "sources", "book"]

# Words the project has ruled out of reader text, and why. Errors.
BANNED = [
    (r"\bsealed test\b|\bblind test\b|\bscored once\b|\bunseen (?:data|contracts|test)",
     "test language rule: never 'sealed', 'blind', 'scored once' or 'unseen' for the project's test"),
    (r"\brehearsal contracts?\b|\byardstick\b|\bfinal test\b",
     "no-jargon rule: say it in plain words"),
    (r"\bhas been earned\b|\bstandard (?:is|was|has been) (?:tested|proven|validated)",
     "never call the standard earned, tested or proven until the test has run"),
    (r"(?i)when a bot causes (?:financial )?harm, who pays",
     "retired spine question (2026-11-18): use 'who is liable' or name the party"),
]
# Words that need a second look. Warnings.
WATCH = [
    (r"\b(?:compliant|conforming|conformity|certified)\b",
     "check: nothing complies with or is certified under Bot Procurement yet"),
    (r"(?i)\bas (?:mentioned|noted|discussed) (?:above|below|earlier)\b|\bsee above\b",
     "back-reference: modules are read alone; name the module instead"),
    (r"\btested\b", "check: 'tested' must not describe the standard or the project's estimator"),
]
STATUS_SENTENCE = re.compile(r"(?i)\bproposal\b")


def split_front(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, flags=re.S)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)), m.group(2)


def load(folder, public=False):
    """With public=True, leave out modules whose front matter says `publish: hold`.
    Any link to a held module then fails the check, so nothing points at an unpublished page."""
    mods = {}
    for p in sorted(folder.glob("*.md")):
        if p.name in GENERATED | HANDWRITTEN:
            continue
        meta, body = split_front(p.read_text(encoding="utf-8"))
        if public and str(meta.get("publish", "")).startswith("hold"):
            print(f"held: {p.name} left out (publish: hold)")
            continue
        mods[p.stem] = {"path": p, "meta": meta, "body": body}
    return mods


def check(mods, glossary_terms):
    errors, warnings = [], []
    for stem, m in mods.items():
        meta, body = m["meta"], m["body"]
        where = m["path"].name
        if meta is None:
            errors.append(f"{where}: no front matter")
            continue
        for k in REQUIRED:
            if k not in meta:
                errors.append(f"{where}: missing '{k}'")
        if meta.get("id") != stem:
            errors.append(f"{where}: id '{meta.get('id')}' does not match the file name")
        if meta.get("type") not in TYPES:
            errors.append(f"{where}: type '{meta.get('type')}' not one of {sorted(TYPES)}")
        if meta.get("status") not in STATUSES:
            errors.append(f"{where}: status '{meta.get('status')}' not one of {sorted(STATUSES)}")
        for r in meta.get("related") or []:
            if r.get("id") not in mods:
                errors.append(f"{where}: related id '{r.get('id')}' has no module")
            if r.get("relation") not in RELATIONS:
                errors.append(f"{where}: relation '{r.get('relation')}' not one of {sorted(RELATIONS)}")
        for t in meta.get("terms") or []:
            if glossary_terms is not None and t not in glossary_terms:
                errors.append(f"{where}: term '{t}' is not defined in bp-glossary")
        if meta.get("status") == "draft" and not meta.get("sources"):
            warnings.append(f"{where}: a draft module with no sources")
        # Links inside the body to other modules must resolve.
        for target in re.findall(r"\]\((bp-[a-z0-9-]+)\.md(?:#[^)]*)?\)", body):
            if target not in mods:
                errors.append(f"{where}: link to missing module {target}.md")
        text = (meta.get("summary") or "") + "\n" + body
        for pat, why in BANNED:
            for hit in re.findall(pat, text):
                errors.append(f"{where}: '{hit}': {why}")
        allowed = set(meta.get("allow_words") or [])
        for pat, why in WATCH:
            for hit in set(re.findall(pat, text)):
                if hit not in allowed:
                    warnings.append(f"{where}: '{hit}': {why}")
        if meta.get("type") == "proposal" and not STATUS_SENTENCE.search(meta.get("summary") or ""):
            errors.append(f"{where}: a proposal module's summary must say 'proposal' in the sentence")
        words = len(body.split())
        if words > 2500:
            warnings.append(f"{where}: {words} words; consider splitting (agents read modules whole)")
    # Relations should be visible from both ends.
    for stem, m in mods.items():
        for r in (m["meta"] or {}).get("related") or []:
            other = mods.get(r.get("id"))
            if other and stem not in [x.get("id") for x in (other["meta"].get("related") or [])]:
                warnings.append(f"{other['path'].name}: does not link back to {stem}")
    return errors, warnings


def glossary(mods):
    g = mods.get("bp-glossary")
    if not g:
        return None
    return set(re.findall(r"^### (.+?)\s*\{#", g["body"], flags=re.M)) | \
        set(re.findall(r"^### (.+?)\s*$", g["body"], flags=re.M))


def entry(m):
    meta = m["meta"]
    return {
        "id": meta["id"], "title": meta["title"], "type": meta["type"], "status": meta["status"],
        "summary": " ".join(str(meta["summary"]).split()), "updated": str(meta["updated"]),
        "url": BASE_URL + meta["id"] + ".md", "audience": meta.get("audience") or [],
        "questions": meta.get("questions") or [], "related": meta.get("related") or [],
        "book": meta.get("book") or [], "words": len(m["body"].split()),
    }


def write(folder, mods):
    entries = [entry(m) for m in mods.values()]
    order = list(TYPES)
    entries.sort(key=lambda e: (order.index(e["type"]), e["title"]))
    today = datetime.date.today().isoformat()
    head = ("AI construction procurement, in the sense used here: AI that prices and generates "
            "construction bids for bidders (AI bid generation and estimating), and AI that checks bids, tenders and change "
            "orders for buyers (AI bid and tender evaluation). Bot Procurement is a proposal, "
            "made in 2026 by a public project, for how such AI could be relied on by buyers, bidders, "
            "insurers and courts. Its test has not been run and no standards body has adopted it.")
    note = ("This is not legal, insurance or financial advice. The legal and insurance points in this work have not been reviewed by a lawyer or an underwriter. Ask your own adviser before relying on them.")
    (folder / "INDEX.json").write_text(json.dumps(
        {"name": "Bot Procurement: AI-first edition", "description": head, "license": "CC-BY-4.0",
         "base_url": BASE_URL, "repository": REPO_URL, "generated": today, "modules": entries},
        indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Index", "", f"> {head}", "", f"*{note}*", "",
             f"{len(entries)} modules. Each is self-contained and can be read alone. "
             "[FAQ](FAQ.md) routes questions to modules; [README](README.md) explains the edition. "
             f"Generated {today} from the modules' front matter.", ""]
    for t, label in TYPES.items():
        group = [e for e in entries if e["type"] == t]
        if not group:
            continue
        lines += [f"## {label}", ""]
        for e in group:
            flag = " *(outline)*" if e["status"] == "outline" else ""
            lines.append(f"- [{e['title']}]({e['id']}.md){flag}: {e['summary']}")
        lines.append("")
    (folder / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    # Answered FAQ: one entry per module, headed by the module's first question and answered by
    # its summary, so each question on the page carries its answer (a list of bare links does not).
    faq = ["# Questions and answers on AI construction procurement", "", f"> {head}", "", f"*{note}*", "",
           "Each question is answered in a few sentences, then linked to the module that answers it in full. "
           "Generated from the modules' front matter; to add a question, add it to the module that answers it.", ""]
    for t, label in TYPES.items():
        group = [e for e in entries if e["type"] == t and e["questions"]]
        if not group:
            continue
        faq += [f"## {label}", ""]
        for e in group:
            first, rest = e["questions"][0], e["questions"][1:]
            faq += [f"### {first}", "", e["summary"], "", f"Read more: [{e['title']}]({e['id']}.md)."]
            if rest:
                faq += ["", "The same module also answers: " + " ".join(rest)]
            faq.append("")
    (folder / "FAQ.md").write_text("\n".join(faq), encoding="utf-8")
    llms = ["# Bot Procurement", "", f"> {head} Text CC BY 4.0.", "", note, "",
            "Bot Procurement is a proposal. Nothing is yet compliant with, certified under or conforming to "
            "Bot Procurement. Every module is Markdown with YAML front matter; INDEX.json lists them all.",
            "", "## About", "",
            "- Name: Bot Procurement (the proposal and the book); Bot Construction is the wider field it belongs to.",
            "- Not to be confused with: Build-Operate-Transfer (BOT) contracts, purchasing bots (robotic process "
            "automation in procurement software), or standards for buying AI systems.",
            "- Subject: AI construction procurement in a narrow sense: AI bid generation and estimating for bidders, "
            "AI bid and tender evaluation for buyers, change order pricing, and margin insurance for construction bids.",
            "- Author: Andre Comeau. Written in public from November 2026, during the Protocol Institute's book-writing month.",
            "- Status: a proposal in draft. Its test has not been run; the project's estimator and pricing model are in development.",
            "- Editions: the human-first book (https://books.andrecomeau.xyz/bot-procurement/) and this AI-first edition "
            f"({BASE_URL}), with the same argument.",
            f"- Licence: CC BY 4.0. Cite the module title, its id and its `updated` date. Source: {REPO_URL}",
            "", "## Routing", "",
            f"- [README]({BASE_URL}README.md): what this edition is and how to read it",
            f"- [INDEX]({BASE_URL}INDEX.md): every module with a one-line summary ([JSON]({BASE_URL}INDEX.json))",
            f"- [FAQ]({BASE_URL}FAQ.md): questions, each linked to the module that answers it", ""]
    for t, label in TYPES.items():
        group = [e for e in entries if e["type"] == t and e["status"] == "draft"]
        if group:
            llms += [f"## {label}", ""] + [f"- [{e['title']}]({e['url']}): {e['summary']}" for e in group] + [""]
    llms += ["## Optional", "", f"- [All modules in one file]({BASE_URL}llms-full.txt)",
             f"- [All modules as JSON lines]({BASE_URL}modules.jsonl)",
             "- [The human-first book](https://books.andrecomeau.xyz/bot-procurement/)",
             f"- [Source repository]({REPO_URL})", ""]
    (folder / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
    full = [f"# Bot Procurement: AI-first edition, all modules", "", f"> {head}", "", note, ""]
    with open(folder / "modules.jsonl", "w", encoding="utf-8") as jl:
        for e in entries:
            m = mods[e["id"]]
            # Body only, with a one-line source note: the YAML stays in the module files.
            full += ["", "---", "", f"<!-- {e['id']} | {e['status']} | {e['url']} -->", "", m["body"].strip(), ""]
            jl.write(json.dumps(dict(e, body=m["body"].strip()), ensure_ascii=False) + "\n")
    (folder / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")
    return entries


def main():
    folder = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "ai")
    strict = "--strict" in sys.argv
    mods = load(folder, public="--public" in sys.argv)
    errors, warnings = check(mods, glossary(mods))
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    if errors or (strict and warnings):
        sys.exit(1)
    entries = write(folder, mods)
    words = sum(e["words"] for e in entries)
    print(f"ok: {len(entries)} modules, {words} words, {len(warnings)} warnings")


if __name__ == "__main__":
    main()
