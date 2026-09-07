# Solution 07 — The test that cannot fail

**a) What each one asserts**

```python
assert mean([1.0, 2.0, 3.0])
```
Asserts that the mean is **truthy** — anything except `0.0`. It passes against
`return sum(values)`, against `return len(values)`, against `return 42`, and against
`return max(values)`. The only implementation it catches is one that returns exactly
zero or an empty container.

```python
try:
    parse_line("TH-04")
except ParseError:
    pass
```
Asserts **nothing**. If `parse_line` raises, the exception is swallowed and the test
passes. If it does not raise, the test also passes. It passes against a `parse_line`
that returns `None`, or `("TH-04", 0.0)`, or anything at all — including
`mutants/bug_02`, where the validation was removed.

```python
result = readings_above([("TH-04", 91.0)], 85.0)
assert result is not None
```
Asserts that the function returned *something*. It passes against `return []`, which
is the answer being wrong in the most consequential direction — a fault report that
never reports a fault.

**b) Why worse than no test**

Because of what a green suite makes people do. Three decisions, all reasonable if the
suite were honest:

- **Refactor without reading.** The point of tests is that you can change the
  implementation and find out. Somebody rewrites `readings_above`, the suite is
  green, and they ship.
- **Skip the manual check.** A reviewer who sees `test_parse` in the diff does not
  re-derive whether the validation still works.
- **Not write the real test.** The coverage is already "there". Nobody adds
  `test_parse_line_rejects_an_empty_tag`, because a test for that function exists.

With no test at all, none of those three happens: the absence is visible. A test that
cannot fail converts a known gap into an invisible one, and that is a strictly worse
position to be in.

**c) What this says about coverage**

Coverage observes **which lines were executed**. It cannot observe whether anything
was asserted about them. All three tests above call their function, so every line of
the function is marked covered — and the suite proves nothing.

So coverage is a *lower* bound on ignorance: 40% coverage tells you for certain that
60% of the code is untested. 100% coverage tells you almost nothing on its own. It is
useful for exactly one question — "is there a whole file nobody tests?" — and
misleading for every other.

What to use instead: **mutation testing**, which is what exercise 09 is. Change the
code deliberately and check that the suite goes red. That measures the property you
actually want, because it asks the tests to *fail*. `mutmut` and `cosmic-ray` do it
automatically for Python; the three folders in `mutants/` do it by hand, so the idea
is visible rather than delegated.
