---
description: State a function's properties as a Lean 4 spec, prove what holds, and turn each into a property-based test
---

# Lean

Target: $ARGUMENTS

No target given? The function the working diff changed that has the widest input space: a parser, a calculation, a state transition. Say which, and why.

Load the `lean` skill and follow it. The order matters, so it's numbered:

1. **Properties in words,** one sentence each. Show the list before writing Lean; it's the cheapest place to be wrong.
2. **The Lean 4 model and one theorem per property.** Model the real types: an overflow the model can't have is a bug the proof can't find.
3. **Prove what you can.** A proof that won't close is usually a counterexample. Check it against the real code.
4. **A property-based test per theorem** in the project's runner, plus a fixed test for every counterexample found.

- No Lean toolchain on the machine? Say so, write the spec anyway, and mark every theorem unproven. The property tests still get written and run.
- **Ask** only when a property is a product decision the code doesn't settle, or before adding a test dependency.

**Done when** each property is a theorem marked proven or unproven, the `lake build` output is quoted (or its absence is stated), and every property has a passing property-based test.
