"""Exercise 09 (bonus) -- A registry.

Not every decorator wraps. Write `check(name)`, which puts the function into the
`CHECKS` dict under that name and returns it **unchanged** -- no wrapper at all.
Then write `failures(value)`, returning the sorted names of the checks that a value
fails.

This is the shape every framework in Part 5 uses: `@app.route("/")` registers your
function and hands it back.

Expected output:

    ['high', 'low']
    ['high']
    ['low']
    []
    too_high True

Hint: the decorator's body is two lines -- store, then return the function. Because
nothing is wrapped, `too_high` is still exactly the function you wrote, which is what
the last line shows.
"""

CHECKS = {}


# TODO: check, then failures


@check("high")
def too_high(value):
    return value > 85


@check("low")
def too_low(value):
    return value < -20


print(sorted(CHECKS))
print(failures(91.0))
print(failures(-30.0))
print(failures(21.7))
print(too_high.__name__, too_high(91.0))
