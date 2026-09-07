# Solution 08 — Lazy, and when not to be

**a) Three things a generator cannot do**

1. **`len()`** — there is no length, because the items do not exist yet. Instead:
   count as you go (`sum(1 for _ in it)`, which consumes it), or keep a counter in
   the loop that was going to walk it anyway.
2. **Indexing and slicing** — `values[3]` and `values[2:5]` both fail. Instead:
   `itertools.islice(values, 2, 5)`, which walks and discards rather than jumping,
   and returns an iterator rather than a list.
3. **A second pass** — see exercise 07. Instead: build a `list` when you need it
   twice and can afford it, or call the generator function again to get a fresh one.

A fourth worth knowing: you cannot look at it in a debugger without changing it.
Printing a generator shows `<generator object ...>`, and the only way to see the
contents is to consume them — which means the code after your inspection gets nothing.

**b) The traceback**

The chain is there, and better than people expect. Measured, with the pipeline built
in one function and consumed in another:

```python
def build():
    return middle(inner())      # nothing runs here


def consume(pipeline):
    return list(pipeline)       # everything runs here


consume(build())
```

```
File "...", line 20, in <module>     <- consume(build())
File "...", line 16, in consume      <- the list(pipeline) line
File "...", line 7,  in middle       <- the `for v in source` line
File "...", line 3,  in inner        <- the raise
ValueError: kaputt
```

Every stage of the pipeline appears, innermost last, exactly as module 09 said to
read it. What is missing is `build`: the function that assembled the pipeline has no
frame at all.

What is genuinely different is **which line of your code is at the top**. It is the
line that *consumed* the pipeline — `list(...)`, or a `for` loop, or `sum(...)` —
which may be in a different function, a different module, and hundreds of lines from
where the pipeline was assembled. The construction site (`middle(inner())`) does not
appear as a frame at all: building a generator runs nothing, so there is nothing to
show.

So when a pipeline raises, the question "who built this?" is not answered by the
traceback. How to find it: read the frames from the bottom to identify the failing
stage, then search for where that generator function is called — that call site,
which the traceback does not name, is where the input came from.

**c) Progress every 1000 rows**

It goes in **its own stage**, between two others:

```python
def counted(items, every=1000):
    for number, item in enumerate(items, start=1):
        if number % every == 0:
            print(f"{number} rows", flush=True)
        yield item
```

and the pipeline becomes `above(readings(counted(rows(text))), 85.0)`.

What it costs: nothing structurally. It is lazy like every other stage, holds one
item, and the laziness survives — which is the answer to the hint. It can go at any
point in the chain, and where you put it decides what is being counted: rows read,
rows that converted, or rows that passed the filter. That choice is now explicit,
which it would not have been with a counter buried in one of the other stages.

With a list at each stage, the same feature is a `print` inside whichever loop builds
the list — arguably simpler to write the first time. What it costs is what it always
costs: each stage has to finish before the next begins, so the first progress line
appears after the whole file has been read, and the memory is three copies of the
data rather than three paused functions. The progress line would also be measuring
the wrong thing — how far the first stage has got, not how far the work has got.
