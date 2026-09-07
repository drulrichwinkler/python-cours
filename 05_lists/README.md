# Module 05 — Lists and tuples

**Assumes:** modules 01–04 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 05_lists` says whether your exercises are done

## What this is about

Module 01 wrote `b = a` with a number and promised that the answer changes when `a` is a list.
This is that module. Everything else in it hangs off the same fact.

- **A list is not an array.** No fixed size, no element type, no `new`. It grows, and it holds
  whatever you put in it.
- **A name is a reference.** `b = a` gives one list two names. `b.append(3)` is then visible
  through `a`, and that is not a special case — it is what assignment has always done, only now
  the object can change.
- **`+=` mutates a list and rebinds a tuple.** Same operator, two behaviours, and the difference
  is exactly the one above. This is the sharpest thing in the module.
- **Slicing**, for which C has nothing at all and Java only `subList` and `Arrays.copyOfRange`:
  a sub-list in three characters, a copy, a reversal, and an assignment target.
- **Copying is shallow unless you say otherwise.** `list(x)`, `x[:]` and `copy.copy(x)` all give
  you a new outer list whose elements are still the old objects. `[[0] * 3] * 3` is the version of
  that mistake which costs a whole afternoon.
- **Tuples**, unpacking, and `a, *rest`. A tuple is not a read-only list; it is a value with a
  fixed shape.
- **`x.sort()` returns `None`.** Every method that mutates a list does. The mistake is worth
  making once, on purpose, here.
- **Comprehensions**, the idiom that replaces most of the loops you would write in C.

## What you can do afterwards

1. **say** what `b = a` does when `a` is a list, and what it does when `a` is an `int`;
2. **explain** why `lst += [3]` reaches an alias and `t += (3,)` does not;
3. **write** a slice for the last three items, every second item, and the whole thing reversed;
4. **copy** a list of lists so that changing the copy leaves the original alone, and **say** why
   `[:]` is not enough;
5. **choose** between `sorted(x)` and `x.sort()`, and say what the second one returns;
6. **write** a list comprehension with a condition — and say when a plain loop reads better.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 05_lists`**
4. **`solutions/`** — last

## Where this goes next

`dict` and `set` in module 06 are built on the same reference rule, and they add a condition a
list cannot meet: a key has to be hashable. `exercises/thinking.md` asks you what tuples have to
do with that, before module 06 answers it.
