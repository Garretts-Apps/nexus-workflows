---
description: Draft release notes from commits since the last tag
---

# Changelog

Range: $ARGUMENTS

No range given? From the last tag to `HEAD`. No tags at all? From the first commit, and say so.

Release notes answer one question: what changes for me if I upgrade? Commit messages answer a different one.

- **Group by what readers do with it:** breaking changes first, with the upgrade step; then added, changed, fixed. Internal refactors and CI churn don't make the list unless they change behavior.
- **Translate, don't paste.** "Fix race in session saver" becomes what the user saw: "Sessions no longer lose the last message when you quit mid-save."
- A breaking change without an upgrade path is a bug in the notes.
- Never invent a feature to fill a section. A short release is allowed.
- Follow the repo's changelog format and its unreleased section if it has one.
- Tagging and publishing are outward-facing. **Ask** before either; drafting needs no permission.

**Done when** every bullet traces to at least one commit in the range, and breaking changes say how to upgrade.
