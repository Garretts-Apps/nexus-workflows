---
name: vertical-slicing
description: Use when planning or building a feature: ship the thinnest path from input to visible result first
---

# Vertical slicing

**Use when** planning or building anything bigger than one sitting, or when a plan starts with "first we'll build the layer for".

A slice is the thinnest path from something a person does to something they can see. It proves the idea and the plumbing at the same time, which is the point.

- **Name the outcome** in one line someone could demo. If you can't demo it, the slice is too wide or not a slice.
- **One entry point first.** One route, one flag, one screen. The second one waits until the first works.
- **Cut through every layer, thinly:** contract, logic, storage, interface. Hardcode what you must; the next slice replaces it.
- **Riskiest slice first.** The integration you're unsure of, the performance you're guessing at, the user flow nobody has tried.
- **Each slice ships with the test that proves its outcome,** and is green before the next starts.
- Defer the cross-cutting polish (admin screens, bulk tools, fancy logging) to a list. That list is allowed to stay a list.

## Smells

- Layers with nothing callable at the end ("the schema is done").
- Feature flags hiding half-built flows with no test.
- A shared abstraction before there are two call sites.

**Done when** the slice can be demoed end to end and its outcome test is green.
