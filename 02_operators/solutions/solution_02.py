"""Solution 02 -- Predict the precedence.

  2 + 3 * 4     14, because multiplication binds tighter than addition.
  (2 + 3) * 4   20, because brackets beat everything.
  2 ** 3 ** 2   512, because ** groups from the RIGHT: 2 ** (3 ** 2) = 2 ** 9.
                Every other arithmetic operator groups from the left.
  -3 ** 2       -9, because ** binds tighter than the minus sign: -(3 ** 2).
                "minus three, squared" would be (-3) ** 2.
  10 - 4 - 3    3, because subtraction groups from the left: (10 - 4) - 3.

The two surprises are both about **. When in doubt, use brackets -- they cost
nothing and settle the argument for the next reader.
"""

assert 2 + 3 * 4 == 14
assert (2 + 3) * 4 == 20
assert 2 ** 3 ** 2 == 512  # fmt: skip
assert -3 ** 2 == -9  # fmt: skip
assert 10 - 4 - 3 == 3
