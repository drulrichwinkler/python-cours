# Solution 08 — Two design decisions

**a) Why `+=` splits**

`a += b` first tries the in-place add. A list has one: it extends itself and hands
back the same object, so every name pointing at that list sees the new entries.

A tuple has none, and could not have one — extending in place is exactly what a
tuple is defined not to do. So Python falls back on `a = a + b`, which builds a new
tuple and rebinds the one name on the left. Other names keep the old tuple. The
asymmetry is not a preference; it is the only thing an immutable type can do.

For reading code: `x += y` on a name whose type you do not know tells you nothing
about who else is affected. If `x` came in as a parameter, the line is a caller-
visible mutation for a list and a purely local one for a tuple — the same line, two
different functions. That is worth a moment when you are reading unfamiliar code,
and it is an argument for a type annotation on the parameter.

**b) The rule the `None` follows**

Command–query separation: a method either changes the object or answers a question
about it, not both. `sort` changes; therefore it answers nothing. `pop` is the one
place the library breaks its own rule, and it is worth asking why that one is
allowed: without a return value it would be useless, and what it hands back is the
item, not the container.

The bug it makes impossible is the quiet alias. If `sort` returned the list, then

```python
sorted_values = values.sort()
```

would look like a fresh list and would in fact be a second name for `values` —
already sorted, and still connected. Every later change to one would show up in the
other, in code that reads as if it had made a copy. `None` turns that into an
immediate `AttributeError` or `TypeError` on the next line instead.

What it costs: no chaining. `values.sort().reverse()` is not available, and you
write two statements — or use `sorted(values, reverse=True)`, which is the better
line anyway.

**c) Where the wrong choice passes the test**

```python
def top_three(log):
    log.sort(reverse=True)
    return log[:3]
```

Called once, this returns the right three entries and every test passes. What it
also did was reorder the caller's list, permanently, as a side effect nobody asked
for. The next piece of code that assumed `log` was still in arrival order — a
timestamp column, a diff against a previous run — is now wrong, somewhere else, with
nothing to point back here.

`sorted(log, reverse=True)[:3]` is the same length and has no such effect. The test
that would have caught it is the second print in exercise 05: assert that the input
is unchanged.
