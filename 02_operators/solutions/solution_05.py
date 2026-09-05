"""Solution 05 -- Range check.

Three nearly identical lines -- and that should bother you. Module 03 introduces
the loop that removes exactly this repetition. Until then we spell it out.

Note the chain: -40 <= reading <= 85 checks both bounds at once.
"""

reading = 21.7
print(f"{reading} plausible: {-40 <= reading <= 85}")

reading = -55.0
print(f"{reading} plausible: {-40 <= reading <= 85}")

reading = 85.0
print(f"{reading} plausible: {-40 <= reading <= 85}")
