# Solution 07 — The pass that is not there

**a) Step by step**

With a generator:

1. `list(values)` calls `iter(values)`. A generator returns **itself**, so this is the
   same object.
2. `list` walks it to the end. The generator is now exhausted — its function has run
   off the end.
3. `len(...)` gives the right number, because the list built in step 2 is real.
4. `max(values)` calls `iter(values)` again, gets the same exhausted generator, asks
   for one item and is told `StopIteration` immediately.
5. `max` on nothing raises `ValueError: max() iterable argument is empty`.

With a list, step 1 returns a **new** `list_iterator` each time, and the list itself
is untouched by walking it. So step 4 gets a fresh iterator over the same three
values.

The whole difference is what `iter()` returns: a new iterator for a list, the same
used-up object for a generator.

**b) What the caller would have to know**

Whether the function walks its argument more than once. Nothing in the signature says
so, and **`Iterable[float]` does not distinguish it**: a list, a generator, a file
object and a `range` are all `Iterable[float]`, and only two of them survive a second
pass.

`Iterator[float]` would at least say "this is single-use", but it is the wrong
annotation for a function that wants to accept lists too. `Sequence[float]` says
"re-walkable, has a length, can be indexed" and is the honest annotation for
`summarise` as written — it excludes generators at type-check time, which is what you
want here.

So: the annotation can carry the requirement, but only if you choose the narrower one
on purpose. `Iterable` is the polite choice and the one that hides this bug.

**c) The two fixes**

**`values = list(values)` at the top.** Right when the input is small or already in
memory, and when the function genuinely needs two passes. It is one line, it makes
the function total over anything iterable, and it says what it is doing.

**One pass, keeping a count and a running maximum.** Right when the input might be
large — and that is where the first fix is wrong. `list(values)` on the 40 GB file
from module 08 does exactly what module 08 said not to do: it undoes the laziness the
caller went to the trouble of arranging, and does it invisibly, inside a function
whose signature promised nothing about memory.

The rule that follows: **a library function that accepts an iterable should make one
pass.** If it cannot, it should take a `Sequence` and say so, so the caller finds out
at the type check rather than at 40 GB.
