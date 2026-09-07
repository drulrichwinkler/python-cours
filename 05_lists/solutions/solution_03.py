"""Solution 03 -- Repair a grid whose rows are one row."""


def blank_grid(size):
    # [[0] * size] * size repeats the reference to ONE row. The comprehension
    # evaluates [0] * size again on every pass, so the rows are separate objects.
    return [[0] * size for _ in range(size)]


grid = blank_grid(3)
grid[0][0] = 9

for row in grid:
    print(row)

print("rows are distinct:", grid[0] is not grid[1])
