# Solution 08 — Explaining

**a) The difference between `==` and `is`**

`==` asks about the value, `is` about identity. In Java terms the names are swapped: Python's
`==` is `.equals()`, Python's `is` is Java's `==`.

For two sensor readings you use `==`. You want to know whether the same temperature was
reported, not whether both names point at one object.

**b) `a is b` gives different answers in a file and in a notebook**

What follows is not an explanation, it is a rule: **do not use `is` on values.** Use it for
exactly one case — `if result is None`.

Why the answers differ is an implementation detail. When Python compiles a file, both `1000`
literals sit in the same code block and it stores the constant once; in a notebook each cell is
its own block. That behaviour is not promised by the language and may change between versions.
A rule you rely on should not rest on something that is allowed to change.

**c) Why the guard does not crash**

Short-circuit evaluation. With `and`, Python evaluates the left operand first; if it is false the
result of the whole expression is already settled, and the right operand is never evaluated.
`count != 0` is false when `count` is `0`, so the division never happens.

This is a promise of the language, not an optimisation. You are meant to rely on it and to order
your guards accordingly. Swap the two sides and it crashes.
