# Solution 10 — When is `match` worth it?

**a) For `describe(status)`**

`if`/`elif` would be the honest choice. Every case there tests a value or a range,
which is what `elif` is for, and the `match` version is two lines longer for it.
Exercise 07 uses `match` to show what it can do, not because that function needs
it.

**b) Where `match` wins**

When the pattern takes a structure apart and checks it in one step:

```python
match entry:
    case ("reading", time, value) if value > 85:
        ...
    case ("gap", time):
        ...
    case ("reading", _, _):
        ...
```

Written with `if`, each of those needs a length check, an index, and a separate
comparison — three chances to get it wrong, and the shape of the data is no
longer visible in the code. Module 06 has the dictionary version, which is where
this stops being a demonstration and starts being useful.

**c) Why `case IDLE:` is a trap**

A bare name in a pattern is a **capture pattern**: it matches anything and binds
what it matched to that name. So inside `match code:`, a `case IDLE:` does not
ask whether `code` equals the constant `IDLE`. It matches every possible value
and rebinds `IDLE` to it.

Python does not let that pass silently. With another `case` after it:

```
SyntaxError: name capture 'IDLE' makes remaining patterns unreachable
```

As the *last* case it does compile — and is then a `case _` with a name attached,
which is worse, because it looks like a comparison and behaves like a default.

To compare against a constant the pattern has to be a dotted name —
`case Status.IDLE:` — or a literal. That restriction is the reason enums and
constants in `match` are almost always written as `Class.MEMBER`.
