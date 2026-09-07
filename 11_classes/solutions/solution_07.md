# Solution 07 — The getter you did not write

**a) What the Java advice protects against**

The day the field stops being a stored value. It becomes computed from two others,
or it has to be validated on the way in, or clamped, or logged, or read from a cache.

Without the getter, callers wrote `reading.celsius`. With the change, the value can
no longer be a public field, so it becomes `reading.getCelsius()` — and **every call
site has to be edited**, including in code you do not own. In a published library
that is a breaking change, so the advice is to pay the cost up front, once, in the
class, rather than never being able to make the change.

**b) Why the change is cheap here**

Because attribute access and method call are different syntax, and `@property` moves
the boundary between them without moving the syntax.

- Before: `reading.celsius` — a plain attribute.
- After: `reading.celsius` — a method, decorated with `@property`.

**The call site does not change.** Not the reads, not the writes if you add a setter,
not the code in other projects. The class gained a computation and nobody outside had
to know. That removes the entire reason for the pre-emptive getter, which is why
Python code that has them reads as translated Java.

**c) What it costs**

What the Java version gives you that `@property` does not: **a stable signature to
override and to mock.** `getCelsius()` is a method from the first day, so a subclass
overrides it the ordinary way, an interface can declare it, and a test double can
replace it without anyone caring how it was implemented.

A property is overridable, but not symmetrically, and the asymmetry is worth
measuring rather than assuming:

- A subclass **can** shadow a parent's property with a plain class attribute in its
  class body — `celsius = 99` works and wins.
- It **cannot** go the other way. If the parent's `__init__` writes
  `self.celsius = ...` and the subclass turns `celsius` into a read-only property,
  construction itself raises `AttributeError: property 'celsius' of 'Sub' object has
  no setter`.
- And `super().celsius = value` does not work at all: `super()` delegates reads to the
  parent's property and has no path for writes —
  `AttributeError: 'super' object has no attribute 'celsius'`.

Where starting plain really does cost you: **when something already holds the value.**
If callers have written `reading.celsius` into a dict, pickled the object, or built a
`@dataclass` around it, turning it into a computed property changes what those see —
a property is not stored, so it is not in `__dict__`, not in `vars()`, and not in
whatever serialised the object. The change is free for readers and not free for
anything that was treating the attribute as data.

The honest summary: the trade is real but lopsided. Java pays a small cost on every
class to keep one change cheap; Python pays nothing until that change arrives, and
then pays for it only if the attribute had been treated as storage.
