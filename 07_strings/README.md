# Module 07 — Strings and formatting

**Assumes:** modules 01–06 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 07_strings` says whether your exercises are done

## What this is about

One thing in this module is worth more than the rest of it together: **`==` and `is` mean the
opposite of what they mean in Java.**

| | compares content | compares identity |
| --- | --- | --- |
| Java | `a.equals(b)` | `a == b` |
| Python | `a == b` | `a is b` |

Four semesters of `str1 == str2` being a reference comparison have to be unlearned here, and the
reason it is hard is that Python makes the wrong habit look right: `is` on two string literals
comes back `True`, so the first test passes. It stops being `True` the moment the string was
built at runtime — read from a file, joined, or typed by a user. That is the shape of every bug
this produces: it works on your machine and fails on real data.

The rest:

- **f-strings**, and the format spec that goes after the colon: `:.2f`, `:>10`, `:,`. `f"{x=}"`
  prints name and value together, which is the shortest debugging tool in the language.
- **Strings are immutable**, as in Java. Every method hands back a result and leaves the original
  alone.
- **`"".join(parts)` is the `StringBuilder` answer.** `+=` in a loop builds a whole new string on
  every pass.
- **`.split()` with no argument** splits on runs of whitespace and drops the empties, which is not
  what `String.split(" ")` does.
- **A `str` is a sequence of code points**, so `len("👍")` is 1 where Java's `length()` says 2, and
  a byte count is a different question — one you ask with `.encode()`.

## What you can do afterwards

1. **say** which of `==` and `is` compares content, and why the wrong one sometimes appears to work;
2. **write** an f-string with alignment, a fixed number of decimals and a thousands separator;
3. **take a line apart** with `.split()` and **put one together** with `.join()`;
4. **say** why a loop that grows a string with `+=` is the wrong shape, and write the right one;
5. **explain** what `len` counts, and what `.encode("utf-8")` counts instead.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 07_strings`**
4. **`solutions/`** — last

## Left for later on purpose

`bytes` gets one section here, enough to make `len` against byte count concrete. Reading and
writing files with an encoding is module 08, and `bytes` on the wire — where getting it wrong
produces mojibake rather than an exception — is module 16.
