# Module 12 — Inheritance, protocols and `@dataclass`

**Assumes:** modules 01–11 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 12_inheritance` says whether your exercises are done

## What this is about

Three things, in increasing order of how much they change what you write.

- **Inheritance is mostly familiar** — with one difference that bites: the parent's `__init__` is
  not called for you. Java inserts an implicit `super()` and refuses to compile without one.
  Python leaves the attribute unset and says nothing until something reads it.
- **`super()` does not mean "my parent".** It means the next class in the method resolution order
  *of the object's type*, which is not decided by the class the line is written in. With one
  parent the two are the same; with two they are not, and the same line reaches a class it does
  not inherit from.
- **Protocols are the part with no Java equivalent.** Every piece of syntax is a call to a method
  with a name in double underscores. Write `__len__`, `__iter__`, `__contains__` and your type
  works with `len`, `for` and `in` — with nothing declared and nothing inherited. `with` in
  module 09 was the first of these.
- **`@dataclass` writes `__init__`, `__repr__` and `__eq__`** from the annotated fields. It is
  the one thing in this module you will use every week, and it is where the annotations you have
  been writing since module 04 stop being merely notation.

Two threads close here. A mutable default on a dataclass field is **an error** rather than the
trap module 04 showed. And a `@dataclass` is unhashable for the reason module 11 gave, with
`frozen=True` as the declarative answer to module 06's rule about keys.

## What you can do afterwards

1. **call** a parent's `__init__`, and say what goes wrong when you forget;
2. **read** a class's MRO and say which method `super()` reaches in a diamond;
3. **make** your own type work with `for`, `in` and `len`, and say why an empty one is falsy;
4. **write** a `@dataclass`, with a default that is a list and is not shared;
5. **say** why a dataclass cannot be a dict key, and which argument changes that.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 12_inheritance`**
4. **`solutions/`** — last

## The question module 06 left open

Dict or class, for a record? The answer this module can finally give: **a dict when the keys are
data, a frozen dataclass when they are your design.** Three lines buy you field names an editor
checks, a readable repr in every traceback, equality that means what you meant, and `asdict()`
when the dict has to go back out as JSON.
