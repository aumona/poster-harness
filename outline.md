# Poster outline · [Paper title]

This file is the editorial source of truth for the poster: the takeaway,
pane contents, selected visuals, and evidence behind every claim. Final
printed wording lives in `content.tex`. Fill this outline from `brief.md`
and the supplied sources, then show it to the user before building.

Default layout: 48 × 36 inches, landscape; left / center / right widths
20% / 60% / 20%. Plan in reading-priority order below.

For each content block, use:

- `Beat:` the one thing a reader should take away.
- `Content:` the planned text or supported claim.
- `Visual:` a local asset, intended crop, and caption; omit if unnecessary.
- `Source:` keys in `sources/citations.json` with page, section, figure/table,
  or data/analysis locators. Cover every claim, number, and reused figure.

Use `TODO[value]` for missing evidence, never invented results. Pure labels
can say `none; no factual claim`. Label schematics as illustrations on the
poster itself. These fields are editorial guidance; `make check` does not
parse them or verify source coverage.

## Center · Walking past

One or two plain-language sentences: the strongest supported finding and why
it matters. Keep the takeaway dominant. A central figure is optional.

### Main takeaway
- Beat: TODO[one finding worth remembering]
- Content: TODO[plain-language conclusion and significance]
- Source: TODO[primary evidence and exact locator]

### Main-result visual · optional
- Beat: TODO[how the visual makes the takeaway clearer at a glance]
- Content: TODO[short caption with essential conditions and units]
- Visual: TODO[assets/filename, crop, and labels]
- Source: TODO[original figure or data and analysis]

## Left · Reading independently

A self-contained overview useful without the presenter and in a photo.
Aim for about one minute of reading; use short bullets and essential jargon.

### Paper and authors
- Beat: Identify the work and its authors.
- Content: TODO[paper title, authors, affiliations, contact, venue]
- Source: TODO[paper metadata and confirmed contact information]

### Summary
- Beat: TODO[question, contribution, strongest finding, and relevance]
- Content: TODO[concise standalone summary]
- Source: TODO[paper sections and result locators]

### Brief method
- Beat: TODO[essential idea needed to understand the result]
- Content: TODO[a few method bullets]
- Visual: TODO[optional method diagram; remove this line if unused]
- Source: TODO[method section; diagram provenance or schematic label]

## Right · Discussing with the presenter

Select evidence for a conversation. Prioritize figures, comparisons, and
compact tables; keep prose minimal. Duplicate the evidence block only when
another result is essential and fits at the default print sizes.

### Supporting experiment or comparison
- Beat: TODO[what this evidence establishes]
- Content: TODO[short caption, evaluation conditions, units, uncertainty]
- Visual: TODO[assets/filename, crop, and readable labels]
- Source: TODO[figure/table or data file and analysis]

### Limitations
- Beat: TODO[boundary needed to interpret the finding]
- Content: TODO[essential assumption, scope, or limitation]
- Source: TODO[relevant evidence or paper discussion]

### References and acknowledgments
- Beat: Credit the work and support.
- Content: TODO[essential printed references, funding, collaborator credits]
- Source: TODO[source-register keys and confirmed acknowledgments]

## Footer · Following up

Preserve the template's two QR codes and institution logo arrangement.

### Paper and code
- Beat: Let readers find the paper and code after the session.
- Content: TODO[paper URL and code URL, or an agreed useful alternative]
- Visual: assets/qrcodes/paper-qr.png; assets/qrcodes/code-qr.png
- Source: TODO[confirmed destinations; verify encoded URLs]

### Institution logos
- Beat: Identify the actual affiliations.
- Content: TODO[institutions to display]
- Visual: TODO[local logo files with suitable contrast]
- Source: assets/LOGO-SOURCES.md; TODO[confirmed affiliations]
