---
name: new-poster
description: Start a new research poster project from the RAFALES LaTeX template, gather the poster brief, and build and inspect the poster. Use when the user requests a new RAFALES poster; existing poster edits follow that project's AGENTS.md.
---

# New RAFALES poster

The reusable template and each research poster are separate folders. The
current working directory is not automatically the template or destination.

1. Locate the template at `~/Projects/rafales-poster-template`, unless the user
   supplies another location. Check for the file `scripts/new-poster.py` inside
   it. If that file exists, use this template. If the file is missing and the
   template path does not exist, create its parent directory if needed and clone
   the reusable template there:

   ```sh
   mkdir -p ~/Projects
   git clone https://github.com/aumona/rafales-poster-template.git ~/Projects/rafales-poster-template
   ```

   Substitute the user-supplied path in both commands when applicable. After
   cloning, require `scripts/new-poster.py` to exist before proceeding. If the
   template path already exists but that file is missing, report the incomplete
   or incompatible checkout and ask how to proceed; do not overwrite it. Do not
   clone inside the current project or automatically pull changes into an
   existing checkout.
2. Use the requested destination. Otherwise choose a descriptive sibling of
   the template, such as `~/Projects/iclr-2027-poster`. If the request provides
   no useful project name, ask for the name along with other missing inputs.
   Never create the new project inside the template, overwrite an existing
   project, or initialize/commit/push Git automatically.
3. Run `python3 <template>/scripts/new-poster.py <destination>`. From this point,
   work in the destination and read its `README.md`, `AGENTS.md`, and `brief.md`.
   Keep the reusable template unchanged while making a research poster.
4. Fill the brief from the conversation. Ask together for missing inputs that
   affect the work, especially the source paper and conference requirements.
   Defaults already recorded in the brief do not need confirmation. Optional
   preferences can stay blank. Read the supplied paper and propose the takeaway
   if the user has not chosen one. Record answers in the brief. Read only the
   source material relevant to this poster; neighboring projects are not inputs
   unless the user identifies them.
5. Follow the new project's `AGENTS.md` to populate `content.tex`, copy selected
   assets, replace QR links, and build. Preserve supported claims and the default
   design unless changes were requested. Run `make check`, render and inspect
   the complete PDF, and verify QR destinations. Report missing inputs or
   unfinished placeholders rather than calling an incomplete poster ready.

Keep template improvements in the reusable template when explicitly requested;
research-specific text and figures belong in the new poster folder.
