"""Solution 03 -- Repair a shared default.

The default expression `[]` ran once, when the def ran. Every call that omitted
`log` appended to that same list, so the second call returned the first call's
readings as well.

None is the sentinel because it is immutable and cannot be a legitimate log. The
check is `is None`, not `== None`: identity is the right question, and a caller
passing an empty list must not be treated as if they had passed nothing --
`if not log:` would get that wrong.
"""


def add_reading(reading, log=None):
    if log is None:
        log = []
    log.append(reading)
    return log


first = add_reading(21.7)
print(first)
print(add_reading(23.1))
print(add_reading(99.9, first))
