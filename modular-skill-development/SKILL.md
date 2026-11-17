---
name: modular-skill-development
description: Design, create, review, or improve skills using progressive disclosure, reusable scripts, and assets; use when the user asks to build or revise a skill or apply modular skill-development practices.
---

# Modular skill development

Apply the user's skill-building preferences alongside the applicable skill-creation and installation workflow. User instructions take precedence. Build for recurring use, not just the current example.

1. Identify representative requests, inputs, outputs, constraints, failure modes, and available tools. Map each step to either a repeatable operation or a judgment that depends on meaning or context.
2. Keep metadata clear about scope and triggers. Make this file a concise workflow and routing map: put specialized or lengthy instructions in directly linked `references/` files and load them only when needed. Avoid duplication and deeply nested reference chains.
3. Automate repeatable, objective, fragile or frequently recreated operations with parameterized `scripts/`. Use clear inputs, validation, useful errors, safe defaults, and predictable outputs. Don't claim that a script verifies matters requiring interpretation. Test scripts on representative cases including failure cases.
4. Use `assets/` for reusable templates, examples, schemas, or other output material when they materially improve fidelity or consistency. Avoid placeholder or redundant assets. Preserve user-provided source material accurately and respect usage restrictions.
5. Retain human or model judgment for source interpretation, relevance, ambiguity, design decisions, and exceptions that cannot be reliably reduced to a rule. State where automation ends; never present candidate matches as verified conclusions.
6. Validate the skill with the applicable creation workflow and run its scripts. Exercise realistic tasks and inspect results; iterate until the skill works, without making scripts or assets merely to satisfy a checklist. Verify installation and requested delivery.

For design choices and checks, consult [references/design.md](references/design.md). Run `python scripts/audit_skill.py PATH` for a quick structural and local Markdown-link audit; it is advisory, not a replacement for official validation or behavioral testing.
