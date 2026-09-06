"""Exercise 07 -- Decode a status word with match.

The sensor reports a status code. Write `describe(status)` so that:

    0            -> "idle"
    1 or 2       -> "warming up"
    above 100    -> "fault <code>", with the number filled in
    anything else -> "unknown"

Use `match`. No `break` is needed anywhere -- there is no fallthrough.

Expected output:

    0 -> idle
    2 -> warming up
    250 -> fault 250
    7 -> unknown

Hint: `case 1 | 2:` is an or-pattern. A guard is `case int() as code if code > 100:`
-- it matches, binds the value to `code`, and only then checks the condition.
"""


def describe(status: int) -> str:
    """Return a human-readable description of a status code."""
    # TODO
    return ""


for s in (0, 2, 250, 7):
    print(s, "->", describe(s))
