"""Solution 05 -- A formatted reading.

`:.1f` only affects the output. The variable `reading` still holds 22.83333 --
that is the difference from round(), which produces a new value.
"""

tag = "TH-04"
reading = 22.83333

print(f"{tag} reports {reading:.1f} degrees.")
