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
dict holds its entries in a table and the loop holds a position in that table. Add a
key and the table may have to grow, which moves everything into a larger one; delete
a key and the entry the loop was about to reach may no longer be where it was. Either
way the position stops meaning what it meant, and entries can be skipped or seen
twice.

What the check actually is, measured rather than assumed: the loop compares the
dict's size against the size it saw at the start, which catches an add or a delete
immediately — `dictionary changed size during iteration`. A delete and an add in the
same pass leave the size alone and get past that comparison. A second check catches
some of those and reports `dictionary keys changed during iteration`; on a larger
dict it catches nothing at all, the loop finishes without complaint, and a key it
should have visited is silently missing from the walk. Replacing the value of an
existing key touches none of this and is allowed.

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

And both stop short of promising it. Java's javadoc calls fail-fast behaviour
best-effort and says it would be wrong to write a program that depends on the
exception; Python makes no promise either, as the five-entry dict in section 3
demonstrates. The exception is there to find your bug, not to make the operation
safe.

**c) Replacing against adding**

`readings[tag] = 99.9` on a key that is already there writes into the slot that key
already occupies. Nothing moves, the set of keys is what it was, and the loop's
position still means what it meant.

Adding a key needs a slot that is not in use, and can push the dict past the point
where it grows the table and moves everything. Deleting one takes an entry out from
under a loop that has not reached it yet. Both change the answer to "which keys are
there", which is what the loop was told at the start, and both are caught by the size
comparison. A swap that keeps the count slips past that comparison — sometimes into
the second check, sometimes into no check at all.

Hence the standard move when a loop has to add or delete: iterate over a snapshot,
`for tag in list(readings):`, and leave the dict free to change underneath.
