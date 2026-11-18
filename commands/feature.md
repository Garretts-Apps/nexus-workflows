---
description: Break a large ask into shippable work items
---

# Feature breakdown

Goal: $ARGUMENTS

No goal given? The feature the branch, spec or conversation is heading toward. Say which.

A breakdown is good when each piece can ship, be seen working, and be thrown away without taking the others with it.

Load the `vertical-slicing` skill and cut the work its way: thin, riskiest first, each slice demoable. This command adds the breakdown around it.

- **Name the outcome** someone can see when it's done, in one line. If you can't, the ask isn't ready; say so and run `/discovery`.
- **Slice vertically.** Each item cuts from input to visible result, thin. "Build the schema" is not an item; "a user can save one draft" is.
- Each item gets acceptance checks someone could run, and a rough size. Anything bigger than a few days splits again.
- Name the dependencies between items and what can run in parallel.
- Defer polish, admin screens and bulk tools to a later list. They always wait anyway.
- Creating tracker items is outward-facing: **ask** first, and only if a tracker was named.

**Done when** every item has acceptance checks, the order is justified, and the riskiest one is first or explicitly flagged.
