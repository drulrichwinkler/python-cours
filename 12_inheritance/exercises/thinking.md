# Module 12 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 12_inheritance`.

---

## Exercise 07 — `super()` is not your parent

```python
class A:
    def who(self): return "A"

class B(A):
    def who(self): return "B->" + super().who()

class C(A):
    def who(self): return "C->" + super().who()

class D(B, C): pass

B().who()   # 'B->A'
D().who()   # 'B->C->A'
```

a) The `super()` call in `B.who` is one line, and it reaches a different class
   depending on what was constructed. Say what it is actually looking up, and where
   that information lives.
b) `B` does not inherit from `C` and does not import it. Explain how a change made
   in `D` — a class written later, possibly by somebody else — alters what a line
   inside `B` does. Then say what that means for reading unfamiliar code.
c) This design has a name: cooperative multiple inheritance. Say what it buys, and
   name the condition every class in the chain has to meet for it to work. What
   happens when one class in the middle does not?

> **Hint on (a):** `D.__mro__` is a plain tuple and it is the whole answer.
> **Hint on (c):** what does `A.who` not do that `B.who` and `C.who` both do?

**Check yourself:** your answer to (b) has to say what you would have to look at,
beyond the file containing `B`, to know what that line does.

---

## Exercise 08 — When a protocol is the wrong idea

Module 09 gave `with` to any object with `__enter__` and `__exit__`; this module
gives `for`, `in` and `len` the same way. Nothing is declared, nothing is inherited.

a) Name what that buys over Java's approach, where a class states
   `implements Iterable<T>`. Be specific about a case that is easy in one and awkward
   in the other.
b) Name what it costs. In particular: how does a reader — or a type checker — know
   that your class is meant to be iterable, and what happens when you implement three
   of the four methods a protocol wants?
c) Somebody defines `__add__` on a `Log` class so that `log_a + log_b` merges two
   logs, and `__lt__` so that logs sort by their highest reading. Argue both sides,
   then say what you would do.

> **Hint on (b):** what does `typing.Protocol` add, and what does it still not
> enforce at runtime?
> **Hint on (c):** what does a reader of `total = a + b` have to know, and where do
> they have to go to find it?

**Check yourself:** your answer to (c) has to distinguish the two cases rather than
approving or rejecting both — one of them is more defensible than the other.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
