---
description: Add or run one focused test and quote the result
---

# Test

Behavior: $ARGUMENTS

A test is a claim about behavior that someone depends on. Test that, not the current shape of the code, or the first refactor will delete your tests and your safety with them.

- **One reason to fail** per test, and a name that says the behavior.
- **A bug fix gets a test that fails without the fix.** Watching it fail is the only proof it tests anything.
- **Real collaborators first.** Mock at the edges you don't control: network, clock, randomness. Mocks of your own code mostly test the mock.
- **Deterministic or it's noise.** Fixed seeds, a frozen clock, no order dependence, no sleeps.
- **Wide input space?** Parsers, serializers, money, dates: a property-based test finds what three examples won't.
- **House style wins.** The project's runner and layout beat a better framework nobody runs.
- Production code stays untouched unless the fix was asked for too.

**Done when** the narrowest command that runs the test is quoted with its output.
