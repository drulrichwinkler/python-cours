"""Solution 05 -- Skip the gaps.

`is None` rather than `== None`: identity is the right question for None, and it
is the one case where `is` is the idiom (module 02).

`continue` reads better than wrapping the rest of the body in an `if` -- the
guard stands at the top and the main path stays at one level of indentation.
"""

readings = [21.7, None, 23.1, None, 22.4]

present = 0
gaps = 0

for reading in readings:
    if reading is None:
        gaps += 1
        continue
    present += 1
    print(reading)

print(f"{present} readings, {gaps} gaps")
