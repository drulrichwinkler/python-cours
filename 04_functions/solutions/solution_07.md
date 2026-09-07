# Solution 07 — No overloading. Now what?

**a) One signature**

```python
def describe(tag: str, reading: float | None = None, unit: str = "C") -> str:
    ...
```

Defaults do what the overload set did, and the caller gets something Java's
version cannot offer: `describe("TH-04", 21.7, unit="F")` names the argument at
the call site.

**b) Overloading on type**

Three honest answers, in the order you should consider them:

1. **Do not.** If a function has to ask what type it was handed, that is usually
   two functions wearing one name. `describe_reading` and `describe_range` cost
   nothing and read better at every call site.
2. **Check inside the body** — `if isinstance(value, tuple):`. Fine for two cases,
   unreadable at five.
3. **`functools.singledispatch`** — a decorator that dispatches on the first
   argument's type and lets each case be registered separately. Real dispatch, at
   the cost of a mechanism the reader has to know.

For a reading that is either a number or a pair, take (1). The two cases have
different meanings — a value against a range — and a name for each says so.

What you lose either way: the compiler no longer picks for you, so a wrong type
arrives inside the function instead of being rejected at the call. That is what
`mypy` is for.

**c) Why the redefinition is silent**

Because `def` is an assignment. It builds a function object and binds it to a
name, exactly as `=` binds any other value. A second `def area(...)` rebinds
`area`; nothing is being *redeclared*, because there was no declaration — the
first function is simply unreferenced and collected.

That is also why a function can be passed, stored in a list, and rebound at
runtime. The absence of overloading is not a missing feature; it is what follows
from functions being ordinary values.
