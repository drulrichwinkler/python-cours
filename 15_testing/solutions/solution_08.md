# Solution 08 — What to test, and what not to

**a) Twelve tests, and the six that survive a cut**

What each function contributes:

- **`parse_line`** has the most surface: it splits, it strips, it converts, and it
  has three separate ways to refuse. Six of the twelve tests are here, and that is
  proportionate — every `raise` in the code is a promise, and a promise nobody tests
  is a promise nobody keeps.
- **`mean`** has one line of logic and one edge: nothing. Three tests — the ordinary
  case, the float case, and the empty case.
- **`readings_above`** is a one-line comprehension whose entire risk is the
  comparison operator. Three tests, one of which is the boundary.

If it had to be six, these:

1. `test_parse_line_splits_tag_and_value` — the happy path, which nothing else covers
2. `test_parse_line_rejects_an_empty_tag` — catches `bug_02`
3. `test_parse_line_rejects_an_unreadable_value` — the failure that real data produces
4. `test_mean_of_three` — the happy path
5. `test_mean_of_nothing_raises` — catches `bug_03`
6. `test_readings_above_is_strict_at_the_limit` — catches `bug_01`

Dropped first: `test_parse_line_ignores_surrounding_whitespace` and
`test_readings_above_on_nothing`. Both are real properties, and both are covered
incidentally by the tests that remain — the whitespace case shares its code path with
the happy path, and an empty input through a comprehension has essentially no way to
be wrong on its own.

Note what the six have in common: **three of them exist because a mutant exists.** A
suite chosen by "what could break" looks different from one chosen by "what does the
function do".

**b) Three things not to test**

- **The exact wording of an error message.** `assert str(err) == "not a reading:
  'n/a'"` breaks when somebody improves the wording, and the improvement is then
  reverted to keep the suite green. Test that the message contains the offending
  value — that is the part a user needs and the part you are willing to promise.
- **A private helper.** If `parsing.py` grows a `_split_fields`, testing it directly
  pins an implementation detail: the tests then have to change whenever the internals
  do, which is exactly backwards. Test it through `parse_line`, which is what has a
  contract.
- **Something that is true today and might reasonably change.** That `parse_line`
  raises `ParseError` and not `ValueError` is worth testing, because the docstring
  promises it. That it splits on `;` specifically is not — a separator is a
  configuration decision waiting to happen, and a dozen tests hard-coding `;` is what
  makes it expensive.

A fourth, milder one: the type of a returned float. `isinstance(value, float)` adds
nothing that `== 91.0` did not already establish.

**c) The class of bug, and a fourth mutant**

All three live **at the edge of the input space**, not in the middle:

- `>` against `>=` — the boundary value itself, where the two implementations differ
  for exactly one input;
- the dropped empty-tag check — the degenerate input, an empty string;
- `mean([])` returning `0.0` — the empty collection.

Each one is invisible to a test that uses ordinary data. `readings_above` with 91.0
against a limit of 85.0 gives the same answer either way; the mutant only shows itself
at exactly 85.0. That is the general shape: **a boundary bug produces the correct
answer for almost every input**, which is why it survives casual testing and why
"empty, one, and exactly at the limit" is the checklist.

A fourth mutant I would plant: **`parse_line` splitting with `split(";", 1)` instead
of `split(";")`.** Measured on the correct version, `"TH-04;91.0;extra"` raises
`ParseError: expected two fields, got 3`. With `maxsplit=1` the split gives
`['TH-04', '91.0;extra']`, the length check passes, and the failure arrives from
`float("91.0;extra")` instead — the same exception class, a different message, and
the shape of the line never questioned.

The model suite as written **does not catch that**: nothing tests a line with too
**many** fields, only one with too few. Which is the honest answer to "twelve tests
for twenty lines" — twelve is not many, and the thirteenth was already missing before
anybody asked for a fourth mutant.
