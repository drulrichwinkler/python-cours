"""Exercise 06 -- yield from, and an endless generator.

Write three things:

  - `lines_of(name)`, yielding `name:1` and `name:2`
  - `files(names)`, yielding every line of every name as one flat stream -- with
    `yield from`, not a nested loop over the inner generator's results
  - `rising(start)`, which never ends: it yields start, start + 1, start + 2 ...

Expected output:

    ['a.log:1', 'a.log:2', 'b.log:1', 'b.log:2']
    [10, 11, 12]
    [0, 1, 2, 3]
    [(1, 2), (2, 3)]

Hint: `while True:` in `rising` is correct and not a mistake -- an endless generator
is fine as long as the consumer stops. `itertools.islice` takes the first few;
`itertools.pairwise` gives consecutive pairs. Never call `list(rising(0))`.
"""

import itertools

# TODO: the three functions


print(list(files(["a.log", "b.log"])))
print(list(itertools.islice(rising(10), 3)))

taken = []
for number in rising(0):
    if number > 3:
        break
    taken.append(number)

print(taken)
print(list(itertools.pairwise([1, 2, 3])))
