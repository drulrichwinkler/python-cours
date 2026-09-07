# Module 04 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 04_functions`.

---

## Exercise 07 — No overloading. Now what?

In Java you would write these three:

```java
String describe(String tag) { ... }
String describe(String tag, double reading) { ... }
String describe(String tag, double reading, String unit) { ... }
```

Python has one name and one function.

a) Write the single Python signature that covers all three calls.
b) Java also lets you overload on *type*: `area(int)` and `area(Rectangle)`.
   How would you write that in Python, and what do you lose?
c) `def area(side)` followed by `def area(width, height)` is not an error and
   produces no warning. Why does that follow from what a `def` actually is?

> **Hint on (b):** there is more than one answer — a check inside the body,
> `functools.singledispatch`, or not writing it that way at all. Say which you
> would pick for a sensor reading that might be a number or a pair.
> **Hint on (c):** what does `def` have in common with `=`?

**Check yourself:** your answer to (c) has to name what a `def` binds, not just
say that the second one wins.

---

## Exercise 08 — What a closure captures

```python
def counter():
    count = 0

    def tick():
        nonlocal count
        count += 1

    tick()
    tick()
    return count
```

a) What does `tick` capture — the value `0`, or the variable `count`?
b) Remove `nonlocal` and run it. Explain the error from what you know about
   scope, not by quoting the message.
c) In Java, a lambda may only capture a variable that is effectively final.
   Python has no such restriction. Name one thing that becomes possible, and one
   thing that becomes easy to get wrong.

> **Hint on (b):** what does an assignment to a name do to that name's scope
> inside a function, and when is that decided?

**Check yourself:** your answer to (b) has to explain why the error is about
*reading* `count`, given that the line looks like a write.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
