# Module 06 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 06_dicts`.

---

## Exercise 07 — Dict or class?

A sensor record can be either of these:

```python
sensor = {"tag": "TH-04", "unit": "C", "high": 85.0}
```

```python
class Sensor:
    def __init__(self, tag, unit, high):
        self.tag = tag
        self.unit = unit
        self.high = high
```

a) Name three things the dict version cannot do for you that the class version can.
   At least one of them should be about a mistake being caught earlier.
b) Name two situations in which the dict is nevertheless the right answer. "It is
   shorter" is not one of them.
c) `sensor["untit"]` and `sensor.untit` both fail. Say **when** each one fails, and
   what that difference is worth on a program that runs for a week.

> **Hint on (b):** where do the keys come from? Are they written by you in the
> editor, or read from something outside the program?
> **Hint on (c):** one of the two can be reported by a tool that never runs the
> program. Which, and why can it not do the same for the other?

**Check yourself:** your answer to (b) has to name a source of keys that is not
known while the code is being written.

---

## Exercise 08 — Views, and where Java agrees

```python
readings = {"TH-01": 21.7}
tags = readings.keys()
readings["TH-04"] = 91.0
print(list(tags))          # both keys
```

```python
for tag in readings:
    readings["TH-09"] = 23.1   # RuntimeError: dictionary changed size during iteration
```

a) `.keys()` gives a view rather than a copy. Name what that buys and what it costs,
   and say how you would take a snapshot when you want one.
b) The `RuntimeError` is Python's version of Java's
   `ConcurrentModificationException`, and `Map.keySet()` is a view in Java too. Say
   why both languages arrived at the same answer — what would the alternative have
   to do?
c) Replacing the value of a key that already exists during the loop is allowed;
   adding one is not, and neither is removing one key and adding another in the same
   pass — that last one keeps the count and still raises, with a different message.
   Explain the distinction from what the loop has to keep track of.

> **Hint on (c):** the loop holds a position in a table. Which of the operations can
> move an entry it has not reached yet, and which one leaves every entry where it is?

**Check yourself:** your answer to (b) has to say what the language would have to
give up to make the loop safe instead of loud.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
