"""Solution 07 -- Decode a status word with match.

Three things a switch cannot do, all in one function:

  case 1 | 2                  one case, two values, and no fallthrough to fake it
  case int() as code if ...   a type test, a binding and a guard together
  case _                      the default

The first matching case wins and execution leaves the match -- forgetting a
`break` is not a category of bug that exists here.

For a plain value switch this is more machinery than an if/elif chain. `match`
starts paying off when the pattern takes a structure apart, which is module 06.
"""


def describe(status: int) -> str:
    """Return a human-readable description of a status code."""
    match status:
        case 0:
            return "idle"
        case 1 | 2:
            return "warming up"
        case int() as code if code > 100:
            return f"fault {code}"
        case _:
            return "unknown"


for s in (0, 2, 250, 7):
    print(s, "->", describe(s))
