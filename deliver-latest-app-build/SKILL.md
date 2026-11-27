---
name: deliver-latest-app-build
description: Find and deliver the latest installable build of a project, especially an Android APK from GitHub Actions. Use when asked for a current app download, a fresh build, or to repair an expired or broken artifact link.
---

# Deliver the latest app build

1. Identify the repository and requested platform using the request and project context. For Shai's Teeny Dungeon, use `shaigoldman/commandLineDungeon`; its default branch is `master` and its Android workflow is named `Android test APK`. Verify these details afresh because they can change.
2. Inspect the current default branch head and recent workflow runs. Select a successful, completed run for that exact commit, branch, and platform. Check its unexpired artifacts. If the head has no successful build, say so; do not silently call an older or PR build the latest. Identify an older build only as such, or build the current version if authorized and feasible.
3. Inspect release assets too when appropriate; do not assume the newest release includes current changes. Prefer an installable binary, not source code. Record commit, run, artifact, and build type. Distinguish debug/test builds from production releases.
4. Download the artifact through the GitHub connector's workflow artifact download operation. Do not present an untested Actions artifact URL as a direct download: it can require authentication or return 404. Extract the requested installer from the ZIP, checking filenames and archive paths for traversal. Verify the extracted file is nonempty and is the expected format; preserve its signing identity, and do not modify or re-sign it.
5. Save the actual installer as a user-accessible durable file using the applicable file delivery workflow. Provide a direct link to the installer, not just the ZIP or a short-lived signed URL. Mention platform, test/debug status, and any relevant install step. If the file cannot be delivered, state what failed and offer a confirmed alternative; do not imply success. Warn that a differently signed APK may not update an existing installation only when this is known or installation fails.

For other projects, discover the repository, workflow, branch, platform and artifact rather than assuming these dungeon-specific details. Never expose private credentials or signed transfer URLs.
