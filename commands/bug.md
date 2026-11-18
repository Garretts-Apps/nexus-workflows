---
description: Draft a defect report with repro and expected vs actual
---

# Bug report

Symptom: $ARGUMENTS

No symptom given? Use the most recent failure in the conversation, the test output or the last CI run.

A bug report is a reproduction that someone else can run without you. Everything else is decoration.

- **Reproduce it first** and paste the exact command or steps and the actual output. "Sometimes fails" gets a frequency and what varies.
- Expected vs actual, each one sentence, both observable.
- **Environment only where it matters:** version, OS, config that changes the outcome. Not your whole `env`.
- Severity is about impact on people, not about how annoying it was to find.
- Candidate files are welcome; a diagnosis presented as fact isn't. Label guesses as guesses, or run `/debug` and stop guessing.
- Draft only. Filing it in a tracker is outward-facing: **ask** first, and only if a tracker was named.

**Done when** the report has a repro someone else can run, the quoted actual output, and expected behavior in one line.
