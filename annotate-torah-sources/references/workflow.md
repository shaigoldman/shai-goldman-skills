# Workflow details

## Inputs and location evidence
For PDF run `python scripts/pdf_inventory.py input.pdf --output inventory.json` (requires PyMuPDF). Review warnings and visual page renders. Script returns native text blocks and coordinates, not semantically reliable paragraph numbers. Manually identify columns, continuation paragraphs and footnotes in reading order. Record physical page and printed page separately. If extracted Hebrew is in visual rather than logical order, never treat raw output as a reliable transcription; use original DOCX/Pages text or visual check. Missing OCR must be identified.

For DOCX run `python scripts/docx_footnotes.py input.docx --output notes.json`. The inspection uses only stdlib and lists footnote/endnote references, definitions, text, empty bodies, dangling references, and duplicate ids. It does not judge whether every implied source has a marker. Compare against content manually.

A ledger entry should carry occurrence ID, claim, manuscript location and paragraph opening, original source identity, full-note location and excerpt, primary quotation and exact edition, source evidence link, confidence/status, and requested action. Iterate in reading order and distinguish quote completeness from claim coverage. Include unresolved entries.

## Output and formatting
For Hebrew manuscripts use RTL paragraph direction, appropriate alignment and correct bidi ordering; retain mixed Hebrew/English punctuation. Avoid rewriting argument merely to add references. In an appendix quote user's notes as notes, not as the original rishon. If the desired quote is absent, mark it absent, verify elsewhere, and clearly attribute. Distinguish source evidence, scholarly inference and editorial proposals. For DOCX use true footnotes, verify references and definitions, render PDF and inspect. For PDF with multiple columns verify right then left and footnote area. Check page breaks, clipping, missing glyphs and quote fidelity. Save all requested versions.
