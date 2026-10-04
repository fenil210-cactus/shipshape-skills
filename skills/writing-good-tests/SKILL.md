---
name: writing-good-tests
description: Write, modify, and review high-value automated tests without test bloat or mock-heavy false confidence. Use whenever creating or changing unit, integration, regression, API, or end-to-end tests; fixing a bug that may need a regression test; adding fixtures, fakes, stubs, mocks, spies, snapshots, or test-only helpers; reviewing generated tests; or deciding whether a code change needs new tests. Prefer the minimum test surface that protects real behavior, independently derived expectations, real components where practical, and mocks only at genuine external, slow, nondeterministic, or unsafe boundaries.
---
# Writing Good Tests

Create tests that catch realistic production regressions. Do not optimize for test count, line coverage, or mock verification.

## Core rule

Every proposed test must answer both questions before it is written:

1. What realistic production break should make this test fail?
2. Does this test exercise enough real behavior to detect that break?

If the first question has no concrete answer, do not add the test. If the second answer is no, change the test boundary before writing it.

## Workflow

### 1. Inspect before adding tests

- Read the changed behavior, nearby tests, fixtures, and test conventions.
- Determine whether an existing test already protects the behavior.
- Do not add a new test merely because a file or function changed.
- Do not duplicate the same protection at several levels without a distinct risk reason.
- Prefer the smallest number of tests that protect distinct failure modes.

### 2. Name the break

For each test, identify one concrete regression such as:

- wrong branch selected
- wrong argument or payload produced
- missing validation
- incorrect boundary handling
- missing state transition or side effect
- broken API or persistence contract
- incorrect error propagation or recovery
- a previously reported bug returning

The test name should describe observable behavior and, when useful, the condition that would break it.

Reject tests whose only meaningful failure is:

- a constant was intentionally renamed or changed
- private implementation structure moved
- source text no longer contains a particular line
- a framework changed its own internal behavior
- a mock or fixture was removed
- code coverage decreased

Test the behavior that depends on those decisions instead.

### 3. Choose the right test boundary

Use the narrowest boundary that still exercises the behavior that matters.

Prefer, in order:

1. Real in-process collaborators and domain objects.
2. Lightweight real repositories or disposable local infrastructure when practical.
3. Purpose-built fakes for boundaries that cannot reasonably be real.
4. Stubs or spies for a specific boundary condition.
5. General mocking frameworks only when the simpler options are impractical.

Do not turn an integration behavior into a unit test by mocking every collaborator.

For agentic or LLM systems, normally keep orchestration, tool routing, parsing, state transitions, persistence logic, and application services real. Replace the final model/provider/network boundary when deterministic tests require it. Use a small opt-in live contract test separately when provider compatibility itself matters.

### 4. Derive expectations independently

Expected values must not be produced by the same logic being tested.

Prefer:

- hand-checked literals
- explicit fixtures
- small table-driven cases with literal expected outputs
- independently constructed expected state

Avoid:

- calling the production helper to compute the expected value
- reproducing the implementation algorithm inside the test
- builders that hide the expected behavior
- assertions so weak that many wrong implementations would pass

When exact output is large, assert the meaningful contract rather than duplicating the implementation.

### 5. Use mocks only when they earn their place

Before mocking a method or component:

1. Identify its real side effects.
2. Identify which of those side effects the test depends on.
3. Keep required side effects real.
4. Mock the slower, external, nondeterministic, expensive, or unsafe layer below them.

Good mock boundaries include third-party APIs, model providers, payment gateways, email delivery, clock/randomness when determinism matters, and infrastructure that cannot be provisioned cheaply for the test.

Do not mock internal application code merely because mocking makes the test easier to write.

A test should normally assert the system's observable result, not the existence of the mock. Assert calls, arguments, counts, or ordering only when that interaction is itself part of the contract being protected.

When using a double:

- make it specific enough that the wrong branch cannot accidentally pass
- model success, failure, malformed, and other relevant responses separately
- mirror the real response shape closely enough to detect integration mistakes
- avoid permissive mocks that accept any arguments and return a happy result

If mock setup is larger or harder to understand than the behavior under test, switch to a more integrated test.

### 6. Do not pollute production code for tests

Keep test-only cleanup, reset helpers, factories, and inspection utilities in test support code unless the production component genuinely owns that lifecycle or capability.

Do not add production methods solely so a test can reach private state or clean up a mock.

Do not weaken encapsulation simply to satisfy generated tests.

### 7. Keep the test set minimal

Do not create tests for every branch by reflex.

Add a test only when it protects a distinct, meaningful risk. Typical changes need some combination of:

- one representative success-path test
- one regression test for the actual bug
- one or a few important boundary/error cases

Not every change needs all three.

If two tests would fail for the same production regression, keep the clearer or higher-value one unless they protect materially different contracts.

Do not add tests solely to raise coverage. Coverage can reveal untested areas; it does not justify low-value tests.

### 8. Prefer behavior over implementation details

Assert things a caller or neighboring system can observe:

- return values
- API responses
- persisted state
- emitted events
- messages or payloads sent across a real boundary
- externally meaningful side effects
- errors and validation outcomes

Avoid asserting:

- private method call sequences
- exact internal object layout
- source-code text
- trivial constructors, getters, constants, or forwarding methods
- framework mechanics already covered upstream

Snapshot tests are appropriate only when the serialized representation itself is a meaningful, intentionally reviewed contract. Do not use large snapshots as a substitute for understanding expected behavior.

### 9. Prove the test has teeth

Run the relevant test and perform a mutation check before finishing.

Mentally or temporarily change the production behavior in plausible ways:

- wrong branch
- wrong constant or argument
- missing state update
- missing side effect
- empty/default return
- validation removed
- unauthorized, zero, empty, null, or malformed input accepted

At least one test should fail for every realistic regression the change is supposed to protect.

For a bug fix, when practical, verify that the regression test fails against the broken behavior and passes with the fix.

### 10. Review generated tests aggressively

Delete or rewrite a test when any of these are true:

- it cannot name a realistic bug it catches
- setup and expected value reuse the same production logic
- it mostly proves a mock was configured
- it passes even if the claimed behavior is replaced with a default or no-op
- it fails mostly on harmless refactors
- it tests the framework instead of application behavior
- it greps implementation source instead of executing behavior
- it adds large fixtures or mocks for tiny confidence gain
- it duplicates another test's protection
- it exists because "we should test everything"

## Decision gate before writing a test

Use this sequence:

```text
What production regression will this catch?
  none -> do not add the test
  only an intentional implementation change -> test dependent behavior instead
  concrete user/system-visible break -> continue

Is the expected result independent of production logic?
  no -> replace it with a literal or hand-checked fixture

Can meaningful behavior run with real components?
  yes -> keep them real
  no -> isolate the smallest external/slow/nondeterministic boundary

Would this test still fail if the claimed behavior were implemented incorrectly?
  no -> strengthen, move, or delete the test

Does another test already catch the same break?
  yes -> keep the stronger one unless contracts differ
```

## When reviewing an existing test suite

Classify each questionable test as:

- KEEP: protects a distinct meaningful regression with a trustworthy assertion.
- REWRITE: valuable behavior, but the current test is tautological, over-mocked, weak, or implementation-coupled.
- DELETE: no meaningful regression, duplicate protection, framework test, coverage-only test, or mock-only assertion.

Prioritize removing false confidence over increasing test count.

## Output expectations

When asked to write tests:

- implement the smallest useful set of tests
- reuse the repository's existing testing conventions
- explain unusual mocks or test levels briefly in code comments only when the reason is not obvious
- do not manufacture additional cases just to appear thorough

When asked to review tests:

- identify which tests are low-value and why
- recommend KEEP, REWRITE, or DELETE where helpful
- call out unnecessary mocks and the real boundary that should be exercised instead
- identify important realistic regressions that remain unprotected

## Reference examples

Read `references/examples.md` when a concrete example is useful for distinguishing strong behavior tests from mock-heavy or tautological tests.
