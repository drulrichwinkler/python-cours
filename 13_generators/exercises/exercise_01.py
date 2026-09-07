"""Exercise 01 -- The protocol behind the for loop.

No loops in this file. Use `iter` and `next` directly, and print six lines:

  1. the type name of what `iter(values)` gives back
  2. the first two items, separated by a space
  3. the string StopIteration, from asking for a third
  4. the list twice over, on one line
  5. whether `list(iter(values))` equals `values`
  6. whether `iter(iterator)` is the same object as `iterator`

Expected output:

    list_iterator
    21.7 91.0
    StopIteration
    [21.7, 91.0] [21.7, 91.0]
    True
    True

Hint: `type(x).__name__` is the name of a type as a string. Line 4 shows that a list
can be walked twice; line 6 shows what distinguishes an iterator from an iterable.
"""

values = [21.7, 91.0]

# TODO: six prints
