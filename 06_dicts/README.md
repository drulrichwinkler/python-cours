# Module 06 — Dictionaries and sets

**Assumes:** modules 01–05 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 06_dicts` says whether your exercises are done

## What this is about

Module 05 ended on a question: a tuple can be a key, a list cannot. This module answers it, and
then spends its time on the thing that answer makes possible.

- **Hashability is the entry condition.** A key has to have a hash that stays put for as long as
  it is a key. That is why a list is refused — and why `(1, [2])` is refused too, although it is
  a tuple.
- **`dict` is where Java reaches for a class.** A literal, on one line, with no `put` and no
  builder. That is worth knowing both as an idiom and as a limit: `exercises/thinking.md` asks
  where the limit is.
- **Iterating a dict yields keys**, not entries. `for tag, value in d.items()` is module 05's
  unpacking arriving in the place you will use it every day.
- **`.keys()` and `.values()` are live views**, not copies — and changing the size of a dict
  while iterating it raises `RuntimeError`. Java's `keySet()` and
  `ConcurrentModificationException` work the same way; this is one of the places the two
  languages agree, and it is worth knowing which those are.
- **Insertion order is kept** — a guarantee since Python 3.7, and narrower than it sounds.
- **Counting and grouping** with `d.get(key, 0) + 1` and `d.setdefault(key, []).append(...)`,
  because `d[key] += 1` on a key that is not there raises `KeyError`.
- **Sets**: no duplicates, no order at all, and membership as the point. A set of strings can
  print in one order now and another after a restart, which is the clearest demonstration
  available that there is nothing to rely on.

## What you can do afterwards

1. **say** which objects can be a key and why the rule is about mutation;
2. **read** and **write** a dict literal, and use `in`, `.get` and `[...]` knowing which of them
   raises;
3. **loop** over a dict by key and by pair, and say what `.keys()` gives you;
4. **count** and **group** with `get` and `setdefault`;
5. **choose** between a dict, a tuple and a class for a record — and give your reason;
6. **use** a set for membership and for the four set operations, and say why its printed order
   is not evidence of anything.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 06_dicts`**
4. **`solutions/`** — last

## One thing left out on purpose

`collections.Counter` counts in one line, and `collections.defaultdict` groups in one. Both are
worth having, and neither is in this module: what belongs here is the language-level answer, so
that you can read the `get`/`setdefault` version in somebody else's code and write it where a
dependency on `collections` is not warranted. Module 10 has the stdlib.
