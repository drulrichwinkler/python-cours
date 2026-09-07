"""Solution 01 -- The protocol behind the for loop."""

values = [21.7, 91.0]

iterator = iter(values)

print(type(iterator).__name__)
print(next(iterator), next(iterator))

try:
    next(iterator)
except StopIteration:
    print("StopIteration")

# A list is an iterable and can be walked again; an iterator is used up.
print(list(values), list(values))
print(list(iter(values)) == values)
print(iter(iterator) is iterator)
