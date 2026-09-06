"""Solution 01 -- Arithmetic.

Note lines 4 and 5: 45 / 6 gives 7.5, a float. 45 // 6 gives 7 -- floored, which
is neither rounded nor truncated. The difference only shows on negatives:
-45 // 6 is -8, where C would give -7. 45 % 6 is the remainder, 3, and
7 * 6 + 3 = 45 -- the identity a == (a // b) * b + a % b is what ties the two
operators together.
"""

print(15 + 27)
print(100 - 43)
print(8 * 7)
print(45 / 6)
print(45 // 6)
print(45 % 6)
print(2**10)
