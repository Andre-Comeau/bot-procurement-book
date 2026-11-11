# Theme

`book.css` styles the book site. It sets MkDocs Material's colours and fonts to the Protocol Institute brand kit (https://npc.here.now/protocolinstitutebrandkit/): Instrument Serif headings, Lora body text, Outfit for navigation and labels, on paper (#f9f8f5) with ink (#2c2c2a) and cobalt (#0064ff), and the kit's forest-950 surface in dark mode. The figures in `images/` use the same palette. None of the Institute's logos or marks are used: the book is Andre Comeau's, not an Institute publication.

`build_site.py` copies it into the site as `stylesheets/book.css`.

`overrides/main.html` adds the link-preview tags (Open Graph and Twitter card) to every page, so Discord and similar sites show a title, a description and `images/social-card.png` when a link is shared. Published chapters, and the chapters listed in `PREVIEWS` in `build_site.py`, use their first paragraph of prose as the description; chapters in `PREVIEWS` also get their own figure. Every other page uses `DESCRIPTION` and `images/social-card.png`. `build_site.py` copies the folder into the site build.

The chapter status labels (Ready to read, Drafted, Outline) are styled at the end of `book.css`. Which chapters count as drafted is the `DRAFTED` list in `build_site.py`: add a chapter's file there once its text is written, and it stops being marked as an outline.
