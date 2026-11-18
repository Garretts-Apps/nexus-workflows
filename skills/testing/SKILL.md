---
name: testing
description: Use when writing, generating or judging tests: what a test should pin, what it must never be, and how to prove it tests anything
---

# Testing

**Use when** adding a test, generating a test file, closing coverage gaps, or deciding whether an existing test is worth keeping. `/test`, `/testgen` and `/coverage` load this; each adds only its own angle.

A test is a claim about behavior someone depends on. Pin that, not the current shape of the code, or the first refactor deletes your tests and your safety with them.

## What a good test is

- **One reason to fail,** and a name that says the behavior. "returns 404 for a deleted draft" beats "test_get_3".
- **It would fail if the behavior broke.** If you can't say what would make it fail, it's decoration. Delete it.
- **The contract callers use,** not private helpers. Read the callers before you write the test.
- **The edges the code actually handles:** empty, one, boundary, invalid, the error path. Not every permutation of the same branch.
- **Wide input space** (parsers, serializers, money, dates): a property-based test finds what three examples won't.

## What it must never be

- **Flaky.** Fixed seeds, a frozen clock, no order dependence, no sleeps. A test that sometimes fails trains everyone to ignore it.
- **A test of its own mocks.** Use real collaborators first; mock only the edges you don't control: network, clock, randomness, the outside world.
- **Coverage theater.** Executing a line without asserting on it moves a number and protects nothing.

## Proving it

- **A bug fix shows red, then green.** The new test fails without the fix and passes with it. Without the red you don't know it tests anything.
- **Run the narrowest command** that runs it, and quote the command and output.
- **House style wins:** the project's runner, layout and fixtures beat a better framework nobody runs.
- Production code stays untouched unless the fix was asked for too.

**Done when** each new test names what it protects, the narrowest command that runs it is quoted with its output, and any fix was shown red before green.
