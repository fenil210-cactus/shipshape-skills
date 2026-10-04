# Whole-subsystem test audit

Use this guide when the requested scope covers every test owned by one
subsystem. Apply the value bar, retention bar, candidate evidence, and
validation in [SKILL.md](SKILL.md) throughout. Keep an evidence trail so a
large cleanup does not silently remove the only proof of a contract.

## 1. Baseline and inventory

Pin the starting commit. List every in-scope test file, its pass/fail result,
and the test/support line counts. Keep existing failures separate from cleanup
candidates; investigate them as possible product defects.

Group tests by production owner rather than filename prefix. Include relevant
shared-boundary and end-to-end tests, so each contract has a known owner.

## 2. Read-only ledger

Read each test declaration and its production path. Mark it:

- **R — retain:** name the independent contract and credible regression.
- **F — fix:** keep the contract but repair a weak or vacuous assertion.
- **C — consolidate:** name the stronger test that will absorb the contract.
- **D — delete:** name the remaining proof, or explain why no meaningful
  contract exists.

Judge assertions, not test names. Record evidence for every mark before
editing. A parameterized test may need different marks for different cases.

## 3. Owner-boundary plan

Name the keeper test for each contract. Prefer a boundary that exercises real
behavior over one that only verifies mocked collaborators. Identify any
test-only production seams that become unnecessary. Correct ledger mistakes
before using it as an edit list.

## 4. Apply and validate

Edit one coherent owner batch at a time. Coordinate shared fixtures and
support files so concurrent changes do not conflict. Move unique assertions
into their keeper before deleting a redundant layer. Remove production seams
only after checking non-test callers.

Run focused tests after each batch and the full relevant subsystem suite
before finishing. Compare removed coverage with the keeper tests; for a
material gap, restore proof and verify the repaired test can catch a plausible
production regression. Treat baseline failures that persist in keepers as
product bugs, not grounds for deletion.

## 5. Reconcile and report

If the target branch changes during a long audit, check new tests and
contracts before final validation. Report baseline and final counts, keeper
tests, removed layers, retained false positives, product defects, checks run,
and any remaining follow-ups. Follow the repository's normal review and
landing process when authorized.
