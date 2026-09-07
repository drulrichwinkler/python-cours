"""Exercise 06 -- Counting calls, and caching.

Write `counted`, a decorator that keeps a count of how often the function was
actually called. Then stack `@functools.cache` above it and read what the numbers
say.

Expected output:

    2 4 6
    3
    2
    1 2

Hint: a function is an object, so the wrapper can carry the counter --
`wrapper.calls = 0` before returning it, and `wrapper.calls += 1` inside. For the
stacked version, `cached_double.__wrapped__.calls` reaches past the cache to the
counter, and `cache_info()` has `.hits` and `.misses`.
"""

import functools

# TODO: counted


@counted
def double(value):
    return value * 2


@functools.cache
@counted
def cached_double(value):
    return value * 2


print(double(1), double(2), double(3))
print(double.calls)

cached_double(1)
cached_double(1)
cached_double(2)

print(cached_double.__wrapped__.calls)
print(cached_double.cache_info().hits, cached_double.cache_info().misses)
