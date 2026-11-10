---
name: new-poster
description: "Start a research poster with the Poster Harness LaTeX template: gather the brief and sources, show a three-pane outline, then build and inspect. Use for a new poster or /new-poster; existing poster edits follow that project's AGENTS.md."
---

# New poster

Every new poster starts from `~/Projects/poster-harness`.
Default poster collection: `~/Projects/presentations/posters/`. The template and each poster
are separate folders; the current working directory is not the destination.
This skill gets the project started with a brief, sources, and an outline.
The poster folder's own `AGENTS.md` drives content, layout, and verification.

## Steps

1. **Find the template.** Use `~/Projects/poster-harness`, unless
   the user supplies another location. Require `scripts/new-poster.py`.
   If the checkout is absent, clone it there:

   ```sh
   mkdir -p ~/Projects
   git clone https://github.com/aumona/poster-harness.git ~/Projects/poster-harness
   ```

   If the directory exists without the creation script, report the incomplete
   checkout; do not overwrite it. Do not automatically pull an existing
   checkout. Resolve template paths against this checkout, not the skill's
   installation directory.

2. **Stamp the folder.** Use the user's destination, otherwise
   `~/Projects/presentations/posters/YYYY-MM-DD-venue-slug`, with the presentation date.
   Infer the date and slug from the request; ask if they are missing. Do not
   substitute today's date for an unknown presentation date.

   ```sh
   python3 ~/Projects/poster-harness/scripts/new-poster.py ~/Projects/presentations/posters/YYYY-MM-DD-venue-slug
   ```

   Substitute the resolved template and destination paths. Never create inside
   the template or overwrite a project. Use the creation script rather than
   copying an older poster. Work in the new folder from here, and read its
   `README.md`, `AGENTS.md`, and `brief.md` before editing.

3. **Fill `brief.md`.** Record what the user already supplied. Ask in one
   message only for missing answers that affect the poster: audience and
   background knowledge, main takeaway, language, presentation date and venue,
   conference requirements, what exists on disk and where, restrictions, and
   material to reuse. Also resolve paper/code QR destinations when needed.
   Extend the brief with relevant fields absent from the starter. Infer
   authors and affiliations from the paper; use the template's recorded
   defaults without asking again. Read the paper and propose the takeaway if
   the user has not chosen one. Optional preferences may remain blank.

4. **Gather sources.** Use paths and URLs in the brief's “What exists, and
   where” and “Material to reuse” sections, or material discoverable from
   those locations. There is no fixed list of content folders to scan
   automatically. Do not treat neighboring projects as inputs. Copy relevant
   papers, TeX sections, data, and supporting documents into `sources/`;
   keep reused or new figure scripts in `figures/`, and display images and
   generated figures in `assets/`. Create source/script folders as needed.
   The template's `content.tex`, `main.tex`, `poster-style.sty`, and example
   assets supply layout/design references, not research content or results.
   Keep the project standalone,
   with no symlinks or references to files outside it. Do not copy an entire
   research checkout when a few files suffice.

   Maintain `sources/citations.json` as a keyed source register. For each
   source, record its title, authors when available, original path or URL,
   and local file when available. Give claims and figures precise locators:
   page, section, figure/table number, or data file and analysis. Preserve
   provenance for copied assets. Original paths/URLs record provenance;
   copy figure-script dependencies locally so they can be reproduced without
   external project files. Sources fetched from supplied URLs belong
   in the register too. Do not invent results, citations, or links; record
   missing evidence as `TODO[value]` in the outline until resolved.

5. **Outline first, shown to the user.** Before replacing `content.tex`,
   fill the stamped folder's `outline.md` and show its proposed takeaway, pane contents, and
   selected figures in chat. Use the three-pane structure below, not a slide
   sequence or a miniature paper. Incorporate feedback; if a decision is
   needed to choose the story, resolve it before implementing that choice.
   Keep the outline current as the poster changes.

6. **Build the poster.** Follow the new folder's `AGENTS.md`. Translate the
   outline into `content.tex`, using the existing macros and design. Preserve
   the default 48 × 36 inch landscape layout and 20% / 60% / 20% pane widths
   unless requirements call for changes. Shorten text before shrinking print
   typography. Replace example content and both QR destinations. Run
   `make check`, render `output/pdf/main.pdf`, inspect the entire page and
   detailed crops, and verify QR destinations and figure legibility. Repeat
   after corrections. Compilation alone is insufficient. Report unresolved
   evidence, placeholders, or missing inputs before calling the poster ready.

Do not initialize Git, commit, push, or register the poster in a collection
unless requested. The poster's brief and `AGENTS.md` govern this project;
audience or content rules from another poster do not carry over.

## Three-pane outline

`outline.md` is the editorial source of truth: what each pane communicates,
what appears there, and where its claims come from. Final printed wording
lives in `content.tex`. Use these sections in reading-priority order:

- **Center · Walking past.** One or two plain-language sentences stating the
  strongest supported finding and why it matters. The takeaway dominates.
  Include a central figure only if it makes that finding immediately clearer.
- **Left · Reading independently.** Paper title, authors/affiliations, a
  self-contained summary, and a brief method. Explain the question,
  contribution, strongest finding, and relevance in about one minute of
  reading. Make it useful in a photo taken for later.
- **Right · Discussing with the presenter.** Selected experiments, labeled
  figures, comparisons, or compact tables. Minimal prose; retain conditions,
  units, uncertainty, and limitations that affect interpretation. Select
  evidence for a conversation rather than compressing the whole paper.
- **Footer · Following up.** Paper and code destinations (or an agreed useful
  alternative), matching QR codes, institution logos, and compact attribution
  or acknowledgments as needed. Preserve the template footer arrangement.

Under each pane, use one subsection per proposed content block, with:

- `Beat:` the one thing this block should communicate.
- `Content:` the planned text or supported claim, concise enough to judge fit.
- `Visual:` the local asset and intended crop/caption, or an explicitly labeled
  schematic; omit when no visual is needed.
- `Source:` source-register keys and exact locators for every claim, number,
  and reused figure, or `TODO[value]`. Pure labels can say `none; no factual
  claim`. Distinguish a schematic from measured results on the poster itself.

These are editorial fields, not automatically parsed build inputs. Check
source coverage manually: `make check` does not enforce the outline or the
source register. Keep detailed evidence in the project files and only the
references necessary for readers on the printed poster.

## Material from older posters or talks

Reuse only material identified by the user or traced from the brief's sources.
Copy source files into `sources/`, selected figures into `assets/`, and any
needed figure-generation scripts into `figures/`. Name them in the outline's
`Source` and `Visual` fields and retain attribution. Never copy an older
poster's layout files, reuse an older poster's or talk's `_src/` files, or
symlink its assets into the new project.

## Improving the template

Research-specific text and figures belong in the poster folder. When asked to
improve the reusable workflow, change `~/Projects/poster-harness`;
a fix made only in one poster will not reach the next. Do not commit or push
those changes unless requested.
