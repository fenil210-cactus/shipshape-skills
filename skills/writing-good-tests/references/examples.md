# Examples

Use these patterns as guidance, not as framework-specific templates.

## Independent expectation

Bad: the expected result is produced by the function being tested.

```python
expected = build_query(tag="urgent")
assert build_query(tag="urgent") == expected
```

Good: the expected behavior is hand-derived.

```python
assert build_query(tag="urgent") == 'tag:"urgent"'
```

## Behavior instead of constants

Low value:

```python
assert MAX_RETRIES == 5
```

Higher value:

```python
result = run_with_retry(always_fails)
assert result.attempt_count == 5
assert result.exhausted is True
```

Protect the retry behavior, not the spelling of the constant.

## Mock boundary

Over-mocked:

```python
repo = AsyncMock()
planner = AsyncMock()
tool_router = AsyncMock()
provider = AsyncMock()
service = RunService(repo=repo, planner=planner, router=tool_router, provider=provider)

await service.run(...)
repo.save.assert_awaited_once()
planner.plan.assert_awaited_once()
tool_router.route.assert_awaited_once()
```

This mostly proves that configured mocks were called.

Prefer keeping application behavior real and replacing the final external boundary:

```python
provider = FakeModelProvider(response=fixture_response)
app = build_real_test_app(model_provider=provider, database=test_database)

response = await app.run(user_request)

assert response.status == "completed"
assert await test_database.load_run(response.run_id) == expected_persisted_run
```

Now the test can catch broken orchestration, parsing, state transitions, and persistence behavior.

## Specific fake

Weak:

```python
provider.generate.return_value = {"ok": True}
```

Better:

```python
provider = FakeProvider(
    expected_model="research-model",
    expected_tools=["search", "write_file"],
    response=REALISTIC_PROVIDER_FIXTURE,
)
```

Make the fake reject unexpected arguments when those arguments are part of the contract.

## Bug regression

A bug caused an empty `session_id` to be persisted.

Useful regression test:

```python
with pytest.raises(InvalidSessionError):
    await create_run(session_id="", request="hello")

assert await run_repo.count() == 0
```

The test names a concrete production break: invalid data reaching persistence.

## Duplicate tests

If these three tests all fail only when the same normalization function stops trimming whitespace:

- `test_name_trims_left_whitespace`
- `test_name_trims_right_whitespace`
- `test_name_trims_surrounding_whitespace`

one representative table-driven test may provide the same protection more clearly.

## Mutation question

For every important test, ask:

"What small wrong implementation would make this test fail?"

If plausible wrong implementations still pass, the test needs a stronger assertion or a better boundary.
