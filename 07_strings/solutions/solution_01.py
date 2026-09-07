"""Solution 01 -- A report line."""

tag = "TH-04"
value = 91.037
limit = 85.0

print(f"{tag:<10}{value:>8.2f} C")
print(f"{tag:*^15}")
print(f"{value / limit:.1%} of the limit")
print(f"{value=}")
