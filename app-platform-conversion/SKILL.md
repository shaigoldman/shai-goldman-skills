---
name: app-platform-conversion
description: Convert an existing codebase or algorithm into a usable web, Android, or iOS app. Use when asked to port a project, expose an existing engine through a web UI, package a web app for mobile, or deliver installable builds while preserving core behavior.
---

# Convert projects into web and mobile apps

1. Inspect the actual project, instructions, entry points, dependencies, data files, license, tests, deployment, and existing UI. Run `python scripts/inventory.py PROJECT_ROOT` for a read-only inventory; inspect its evidence and relevant code before deciding what it means. Check user expectations for offline access, target devices, distribution and native features; make reversible choices autonomously, and ask only when a consequential choice cannot be inferred.
2. Establish baseline behavior and use representative examples. Separate the portable core from I/O, process assumptions and UI. Reuse the core when feasible; port only with evidence of behavior parity. Determine whether computation, private data and credentials can safely run on-device. Do not put secrets in client code.
3. Pick architecture from measured constraints: static browser computation (including WASM), a client with hosted backend, installable web app, packaged web app, or native UI. Distinguish PWA, remote-site wrapper, bundled hybrid, and native app; state online/offline and distribution implications. Read [web.md](references/web.md) for web work, [mobile.md](references/mobile.md) for mobile work, and [verification.md](references/verification.md) for validation and shipping.
4. Implement the actual user flow, responsive interface, error and progress states, cancellation, and platform lifecycle as applicable. Preserve data files and functionality. Use isolated branches and existing build and deployment conventions. Test the core and UI, including platform-specific failure cases and representative real or emulated devices where possible. Record exact evidence and do not claim device testing based on compilation or desktop simulation.
5. Deliver a usable, reviewable artifact or PR and clear installation instructions. Verify the build and destination; distinguish debug signing from a release and hosting from app-store publication. Follow existing user authorization for publishing or release, and communicate blockers and partial results precisely.
