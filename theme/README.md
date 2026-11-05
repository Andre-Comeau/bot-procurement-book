# Theme

`book.css` styles the book site. It sets MkDocs Material's colours and fonts to the Protocol Institute brand kit (https://npc.here.now/protocolinstitutebrandkit/): Instrument Serif headings, Lora body text, Outfit for navigation and labels, on paper (#f9f8f5) with ink (#2c2c2a) and cobalt (#0064ff), and the kit's forest-950 surface in dark mode. The figures in `images/` use the same palette. None of the Institute's logos or marks are used: the book is Andre Comeau's, not an Institute publication.

`build_site.py` copies it into the site as `stylesheets/book.css`.

`overrides/main.html` adds the link-preview tags (Open Graph and Twitter card) to every page, so Discord and similar sites show a title, a description and `images/social-card.png` when a link is shared. Each published chapter's description is its first paragraph of prose; the home page and the working copy use `DESCRIPTION` in `build_site.py`. `build_site.py` copies the folder into the site build.
