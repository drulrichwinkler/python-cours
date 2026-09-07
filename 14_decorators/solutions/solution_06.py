"""Solution 06 -- Counting calls, and caching."""

import functools


def counted(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1  # state on the wrapper object -- a function is an object
        return function(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


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
# cache sits above counted, so the second call with 1 never reaches the counter.
print(cached_double.__wrapped__.calls)
print(cached_double.cache_info().hits, cached_double.cache_info().misses)
