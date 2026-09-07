# Module 05 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 05_lists`.

---

## Exercise 07 — When is it a tuple?

Python has two sequence types where C and Java have one. Both hold things in order,
both are indexed from zero, both slice.

a) `("TH-04", 21.7)` and `[21.7, 22.0, 22.4]` are both sequences of two or three
   things. Say what makes the first a tuple and the second a list — in terms of
   what the positions *mean*, not in terms of whether anything gets appended.
b) A tuple can be a key in a `dict`; a list cannot. Try it:

   ```python
   hash(("TH-04", 21.7))
   hash(["TH-04", 21.7])
   ```

   The second raises `TypeError: unhashable type: 'list'`. Explain the refusal from
   what you know about mutation, not from the message. What would break if it were
   allowed?
c) `mixed = ([1], 2)` is a tuple, and `mixed[0].append(9)` works. So what exactly
   is immutable about a tuple? Predict what `hash(mixed)` does, then run it.

> **Hint on (a):** could you write a loop over the entries and do the same thing
> to each one? For which of the two would that even be a sensible question?
> **Hint on (b):** a dict finds a key by its hash. What has to stay true about
> that number for the key to be findable again a minute later?

**Check yourself:** your answer to (c) has to say which of the three — the tuple,
the slot, or the object in the slot — cannot change.

---

## Exercise 08 — Two design decisions

Both of these could have gone the other way, and in some languages they did.

```python
lst = [1, 2]; lst_alias = lst; lst += [3]      # lst_alias sees [1, 2, 3]
t = (1, 2);   t_alias = t;     t += (3,)       # t_alias stays (1, 2)

values = [23.1, 21.7]
result = values.sort()                          # result is None
```

a) `+=` on a list mutates, `+=` on a tuple rebinds. Say why the second one has no
   choice, and what that means for reading a line of code that uses `+=` on a name
   whose type you do not know.
b) `sort`, `reverse`, `append` and `extend` all return `None`, and this was decided
   on purpose. Name the rule it follows, and one bug it makes impossible. Then name
   what it costs you.
c) `x.sort()` and `sorted(x)` do the same work and differ in what they touch. Give a
   function for which the wrong choice passes the obvious test and still breaks
   something elsewhere. Then say what the test would have had to assert.

> **Hint on (b):** what would `y = x.sort()` have given you if `sort` returned the
> list, and how long would it have taken you to notice?

**Check yourself:** your answer to (a) has to be about what a tuple can and cannot
do, not about what the language designers preferred.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
