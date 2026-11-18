---
description: Reproduce a failure and name the cause before editing
---

# Debug

Symptom: $ARGUMENTS

A bug you can't reproduce is a rumor. Get it to fail on command first; everything after that is bookkeeping.

- **Reproduce, then shrink.** Find the smallest input, commit and environment that still fail. Intermittent means something varies: time, order, concurrency, data, environment. Find what.
- **Read the error literally.** All of it, including the part after the first line. The first frame in your own code is usually where to start.
- **Halve, don't theorize.** Bisect the history (`git bisect`), the input, the config. Three halvings beat an hour of plausible stories.
- **One change at a time,** and keep a note of what you tried so you don't try it twice.
- **Cause, not surface.** Where it blew up is rarely where it went wrong. A guard at the surface is a second fix, not the first one.
- **Suspect the recent and the assumed** before the compiler, the OS or the library. They are occasionally guilty. You are usually guiltier.
- If you were asked for a diagnosis, deliver a diagnosis. Edit only when a fix was asked for.

**Done when** you can name the cause with evidence, the repro is quoted failing (and passing, if you fixed it), and it's clear whether anything was edited.
