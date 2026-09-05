"""Solution 04 -- Converting between types."""

a = int("42")
b = float(10)
c = int(3.7)
d = bool(0)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Note c: int() truncates, it does not round. int(3.7) is 3, round(3.7) is 4.
