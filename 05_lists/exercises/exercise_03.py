"""Exercise 03 -- Repair a grid whose rows are one row.

`blank_grid` is meant to return `size` separate rows of zeroes. It returns one row,
`size` times over -- so a single assignment appears to change a whole column.

Run it, look at the output, then fix the function. Do not change anything below it.

Expected output:

    [9, 0, 0]
    [0, 0, 0]
    [0, 0, 0]
    rows are distinct: True

Hint: `*` on a list repeats the reference, not the object. A comprehension
evaluates its expression again on every pass.
"""


def blank_grid(size):
    return [[0] * size] * size  # TODO: the bug is in this line


grid = blank_grid(3)
grid[0][0] = 9

for row in grid:
    print(row)

print("rows are distinct:", grid[0] is not grid[1])
