# Design and review guide

- Start from concrete tasks and observed errors; decide what must generalize and what is specific to an example.
- Route optional depth from SKILL.md to a small number of plainly named references. Give the reader a reason to open each reference.
- For each operation ask: can it be specified and checked deterministically? If yes, consider a tested script; otherwise preserve judgment and evidence. Weigh dependency, maintenance, execution risk, and frequency before automating.
- Use assets for stable source templates or schemas; parameterize variable content. Do not hard-code sensitive data or overwrite the user's work.
- Specify what a script proves and does not prove. Include negative and edge cases. Check dependencies and fail clearly if missing. Keep the original input intact unless editing is explicitly requested.
- Prefer small cohesive tools, explicit arguments, stable machine-readable output where useful, and no network or side effects unless the task calls for them. Avoid excessive scaffolding.
- Test an end-to-end representative request, local references, input validation, and failure reporting. Verify an artifact's actual result, not only process exit status. Review whether the instructions trigger appropriately and whether resource loading is selective.
- Record uncertainty where sources, interpretation, or state remain unresolved; do not conceal failures or claim verification that did not happen.
