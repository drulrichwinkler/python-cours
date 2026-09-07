# Module 11 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 11_classes`.

---

## Exercise 07 — The getter you did not write

In Java, the advice is to make every field private and give it a getter, even when
the getter does nothing:

```java
private double celsius;
public double getCelsius() { return celsius; }
```

In Python the same class starts as `self.celsius = celsius`, and nobody writes an
accessor until there is something to compute.

a) Say precisely what the Java advice is protecting against — what change, later,
   would be expensive without it?
b) Say why that change is not expensive in Python. Name the language feature, and
   say what the call site looks like before and after.
c) The trade is not free. Name one thing the Java version gives you that
   `@property` does not, and one situation in Python where starting with a plain
   attribute really does cost you later.

> **Hint on (a):** what does a caller write, and what would have to change in every
> caller?
> **Hint on (c):** think about a subclass, and about a value somebody has already
> stored somewhere.

**Check yourself:** your answer to (b) has to state what does *not* change when a
plain attribute becomes a property.

---

## Exercise 08 — Nothing is private

```python
class Sensor:
    def __init__(self):
        self._buffer = []      # "internal"
        self.__cache = {}      # mangled to _Sensor__cache
```

a) Neither line prevents access. Say what each one is actually for, and who each one
   is addressed to.
b) A colleague writes `__` in front of every attribute "for encapsulation". Name two
   concrete things that get worse, one of them at debugging time.
c) Python's position is that a convention is enough. Give the argument for that — and
   then the strongest argument against it that you can make, in a codebase with
   twenty contributors.

> **Hint on (a):** one of the two is read by people and tools; the other is read by
> the interpreter and has a specific job involving subclasses.
> **Hint on (b):** what does the attribute show up as in a traceback, in `vars()`,
> and in a subclass that wanted to reuse it?

**Check yourself:** your answer to (c) has to include a case where the convention
demonstrably fails, not just one where it might.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
