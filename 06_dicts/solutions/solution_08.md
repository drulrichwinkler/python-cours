# Solution 08 — Views, and where Java agrees

**a) What a view buys and costs**

It buys two things: no copy, so asking for `.keys()` on a dict with a million entries
costs nothing; and a live answer, so a view handed to another function keeps telling
the truth as the dict changes.

It costs the guarantee you may have assumed you had. `tags = readings.keys()` looks
like a snapshot and is not, so code that stores it and comes back later sees
something else. And a view cannot be indexed — `tags[0]` fails — because a dict has
no positions to index.

The snapshot is `list(tags)`, `set(tags)` or `sorted(tags)`. Each builds something
that no longer follows the dict, which is exactly the point.

**b) Why both languages refuse**

Because the loop is walking a structure while the structure is being rearranged. A
dict has a fixed number of slots; adding an entry can make it outgrow them, and then
everything is moved into a larger table. The position the loop was holding no longer
means anything: entries can be skipped, seen twice, or the walk can run off the end.

The alternative is what the concurrent collections do: iterate over a snapshot, or
keep the old table alive until every iteration over it has finished. Both cost memory
and bookkeeping on every loop, to make a case work that is almost always a mistake.
Both languages decided that the ordinary loop should stay cheap and that this case
should be loud instead of quiet — Python with `RuntimeError`, Java with
`ConcurrentModificationException`, both raised as early as they can be noticed rather
than at the point where the wrong result appears.

Which is the answer to "why the same answer twice": it is not a shared style, it is
the same constraint. The languages that do let you do it are the ones that paid for
it somewhere else.

**c) Replacing against adding**

`readings[tag] = 99.9` on a key that is already there writes into the slot that key
already occupies. Nothing moves, the number of entries is the same, and the loop's
position still means what it meant.

Adding a key needs a slot that is not in use, and can push the dict past the point
where it grows the table and moves everything. That is why the check is on the size —
`dictionary changed size during iteration` — and not on the contents. Deleting has
the same problem for the same reason and raises the same error.

Hence the standard move when a loop has to add or delete: iterate over a snapshot,
`for tag in list(readings):`, and leave the dict free to change underneath.
