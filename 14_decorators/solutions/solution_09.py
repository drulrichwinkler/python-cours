"""Solution 09 (bonus) -- A registry."""

CHECKS = {}


def check(name):
    """Register the function under `name` and hand it back unchanged."""

    def decorator(function):
        CHECKS[name] = function
        return function  # no wrapper: the function is registered, not modified

    return decorator


@check("high")
def too_high(value):
    return value > 85


@check("low")
def too_low(value):
    return value < -20


def failures(value):
    return sorted(name for name, test in CHECKS.items() if test(value))


print(sorted(CHECKS))
print(failures(91.0))
print(failures(-30.0))
print(failures(21.7))
print(too_high.__name__, too_high(91.0))
