---
name: lean
description: Use when a function's correctness matters more than its example cases: state its properties as a Lean 4 spec, prove what you can, and turn every property into a property-based test in the project's own runner
---

# Lean

**Use when** the code is the kind where three example tests lie: parsers and printers, money and rounding, dates, permissions, state machines, anything with "always" or "never" in its requirements. `/lean` loads this. `testing` covers the tests it produces.

The point isn't a proof for its own sake. Writing the spec forces you to say exactly what the code promises. Proving it finds the cases nobody thought of. The property tests then hold the real code to the same promises forever.

## 1. Say the properties first, in words

Before any Lean, list what must always hold. Good properties are short and boring:

- **Round trip:** `parse (print x) = x`.
- **Invariant:** a balance never goes negative; a sorted list stays sorted after insert.
- **Idempotence:** normalizing twice is normalizing once.
- **Bounds:** `clamp lo hi x` is always between `lo` and `hi`, and is `x` when `x` already is.
- **Equivalence:** the fast version agrees with the obvious slow one.

If you can't state a property in one sentence, you don't understand the function yet. Ask the maintainer now, while it's cheap, and only about behavior the code doesn't settle.

## 2. Write the spec in Lean 4

- **Model the function, not the codebase.** A small pure Lean definition that mirrors the logic: same branches, same edge cases. Leave out I/O, logging and frameworks.
- **One `theorem` per property,** named after it (`clamp_within_bounds`), stated over all inputs. The statement is the spec. Keep it readable by someone who doesn't know Lean.
- **Model the type honestly.** Machine integers overflow and `Nat` doesn't. If the code uses `int32` or floats, say so in the model (`Int32`, `UInt64`, or an explicit bound), or note the gap. Proving a property of `Nat` says nothing about an overflow.

## 3. Prove what you can

- Try the cheap tactics first: `simp`, `omega` for linear arithmetic, `decide` for finite cases, `induction` for lists and recursion.
- **A proof that won't go through is a finding.** Usually the property is false for some input. Ask Lean for the counterexample (`#eval` the model on the case, or `decide` on a bounded version) and check it against the real code.
- **Never `sorry` a property and call it proven.** An unproven property is reported as unproven, with what blocked it. It still becomes a test in step 4.
- Run `lake build` (or `lean <file>`) and quote the output. "No errors" is the evidence; a screenshot of the editor isn't.

## 4. Turn every property into a property-based test

- Use the project's property-testing library if it has one; if it doesn't, the standard one for its language. Add a dependency only with the maintainer's okay.
- **One generated test per theorem,** with the same name, so the spec and the test can be read side by side.
- **Generators cover the edges** the proof had to handle: zero, negatives, empty, maximum values, unicode, the boundary of every branch.
- **Counterexamples from step 3 become fixed example tests** as well, so they can never come back.
- Run the narrowest command and quote it, failure first if a property found a real bug.

## Where it lives

Put the Lean model next to the code it describes (`spec/lean/<module>.lean` or the repo's convention), with a comment naming the source file and the commit it modeled. A spec that silently drifts from the code is worse than none.

**Done when** each property is a named theorem marked proven or unproven (with the blocker), `lake build` output is quoted, and each property has a passing property-based test in the project's runner, with any counterexample pinned as an example test.
