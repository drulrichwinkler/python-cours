# Module 13 — Iterators and generators

**Assumes:** modules 01–12 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 13_generators` says whether your exercises are done

## What this is about

`yield` is the thing in this course with no equivalent in C and only a distant one in Java. It is
also the last piece of the `for` loop you have been using since module 03 — because a `for` loop
was never about lists.

- **A `for` loop calls `iter()`, then `next()` until `StopIteration`.** That is the whole
  protocol, and it is why the same loop works on a list, a string, a dict, a file, and the `Log`
  you gave `__iter__` to in module 12.
- **An iterable is not an iterator.** A list can be walked twice; the thing `iter()` hands back
  cannot. That distinction is the source of the module's one real trap.
- **A function with `yield` in it does not run when you call it.** It builds a generator and
  returns it; the body runs a piece at a time, and the state is the paused function itself —
  local variables, loop position and all. Writing that by hand is a class with attributes, which
  is exactly what Java makes you do.
- **A generator is used up.** Walking it a second time yields nothing, and nothing raises. A
  function that takes an iterable and passes over it twice works on a list and silently returns
  nothing on a generator.
- **Size is the point.** A generator over a million items is a few hundred bytes, because there
  is nothing in it but a paused function. That is why module 08 could read a 40 GB file line by
  line.
- **`yield from`**, and one thing to know about `return` inside a generator: the value goes into
  the `StopIteration` and an ordinary caller never sees it.

## What you can do afterwards

1. **say** what a `for` loop calls, and what ends it;
2. **write** an iterator as a class, then the same thing as four lines with `yield`;
3. **say** why a generator can be read once, and what to do when you need it twice;
4. **build** a lazy pipeline — read, filter, convert — that never holds more than one item;
5. **choose** between a list comprehension and a generator expression, with a reason.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 13_generators`**
4. **`solutions/`** — last

## Where this goes

Part 4 starts with decorators, which is where the `@` you have been reading since module 00
finally gets explained — and a decorator is a function that takes a function, which is module 04
plus one idea. From module 15 the feedback stops being an expected output and becomes a test
suite you write yourself.
