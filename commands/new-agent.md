---
description: Scaffold a helper agent file with tools and read-only default
---

# New agent

Name: $ARGUMENTS

No name given? Ask for one, with a suggestion based on what the conversation needs a helper for. This is the one place a bare command can't guess.

A helper is a narrow job with a fixed report. The narrower it is, the more you can trust what it sends back.

- **One job.** If the description needs "and", that's two helpers.
- **Read-only unless editing is the job.** List only the tools it needs; every extra tool is a way to wander off.
- **Say what it returns:** the report shape, severity labels, what to do when it finds nothing. A helper without an output format writes essays.
- Name what's off limits: paths, network, anything outward-facing.
- Match the frontmatter and tool names the project's harness already uses; look at an existing helper first.

**Done when** the file has `name`, `description` and `tools` frontmatter, a stated job, and a report shape.
