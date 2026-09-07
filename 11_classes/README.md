# Module 11 — Classes

**Assumes:** modules 01–10 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 11_classes` says whether your exercises are done

## What this is about

You have written classes for four semesters. The syntax will cost you an hour; the habits are the
expensive part.

- **`self` is the first parameter**, written out in the definition and passed for you at the
  call. `__init__` is not a constructor — the object already exists when it runs.
- **Attributes are created by assignment**, not declared. Which means a misspelled attribute name
  is a new attribute rather than an error, and the state of an object is whatever has been
  assigned to it so far.
- **A class attribute is one object, shared.** If it is mutable, every instance shares the
  changes — module 04's mutable default argument, one floor up. Reading and writing are not
  symmetric: `a.kind = x` never changes the class.
- **There is no `private`.** `_name` is a convention that every reader honours and nothing
  enforces; `__name` is name mangling, which exists to stop subclass collisions and not to keep
  anyone out.
- **No getters.** In Java you write one in case the field becomes computed later. Here the call
  site is `sensor.value` either way, so you start with a plain attribute and add `@property` on
  the day you need it — without touching a single caller.
- **`__repr__` for you, `__str__` for the user.** A container always shows the repr, which is why
  an object with only a `__str__` still prints as `<object at 0x...>` inside a list.
- **`==` is identity until you write `__eq__`** — and writing it makes the class unhashable,
  which is module 06's rule about keys being enforced rather than explained.

## What you can do afterwards

1. **write** a class with `__init__`, methods and a `__repr__`, and say what `self` is;
2. **say** what `a.kind = x` does when `kind` is a class attribute, and what it does not do;
3. **explain** why a mutable class attribute is shared, and write the version that is not;
4. **turn** a plain attribute into a computed one without changing any call site;
5. **write** `__eq__`, and say what it costs you if you write nothing else.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 11_classes`**
4. **`solutions/`** — last

## The `@` sign, again

`@property`, `@classmethod` and `@staticmethod` all appear here, and `@pytest.mark.your_turn` has
been in every test file since module 00. A decorator is a function handed your function, giving
back something to bind to the name instead. Module 14 is where you write one; until then, reading
`@x` as "wrap the function below in `x`" is enough to use them.
