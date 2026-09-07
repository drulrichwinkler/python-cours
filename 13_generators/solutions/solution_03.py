"""Solution 03 -- Repair a function that walks twice."""


def summarise(values):
    # The caller may hand in a generator, which can be walked only once. Taking a
    # list first is the cheapest fix; the alternative is to make one pass and keep
    # a running total and count.
    values = list(values)
    return len(values), max(values)


def readings():
    yield 21.7
    yield 91.0
    yield 23.1


print(summarise(readings()))
print(summarise([21.7, 91.0, 23.1]))
