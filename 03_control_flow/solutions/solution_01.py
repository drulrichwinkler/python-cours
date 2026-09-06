"""Solution 01 -- Classify a reading.

Compare this with exercise 06 of module 02, which asked the same question as four
boolean lines. Four lines answered "which groups apply"; this one answers "which
group is it". The if/elif chain also stops at the first match, so the ranges do
not have to be written twice -- `elif reading <= 85` already knows that -40 was
ruled out.
"""

readings = [21.7, -55.0, 91.0]

for reading in readings:
    if reading < -40:
        state = "below range"
    elif reading <= 85:
        state = "plausible"
    else:
        state = "above limit"
    print(reading, state)
