"""Solution 06 -- Find the first implausible reading.

The `else` belongs to the `for`, not to the `if`, and it runs only when the loop
was not broken out of. Written with a flag instead, the same thing needs three
more lines and a name nobody wants:

    found = False
    for reading in readings:
        if reading > 85:
            found = True
            break
    if not found:
        ...

That is what `for ... else` replaces. The name is unfortunate -- read it as
"no break".
"""

readings = [21.7, 91.0, 22.4]

for reading in readings:
    if reading > 85:
        print("first implausible:", reading)
        break
else:
    print("all readings plausible")
