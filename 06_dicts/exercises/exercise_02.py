"""Exercise 02 -- Predict what dicts and sets do.

Replace each `...` with the value you expect, then run the file.

    uv run 06_dicts/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

# TODO: keys are unique, and `unique` is decided by ==. How many entries survive,
# and which value?
collapsed = {1: "int", 1.0: "float", True: "bool"}  # noqa: F601 -- the collision is the point

assert collapsed == ...


# TODO: what does `in` look at?
reading = {"tag": "TH-04", "value": 91.0}

assert ("value" in reading) == ...
assert (91.0 in reading) == ...


# TODO: which of the two lookups raises?
try:
    reading["unit"]
    from_brackets = "no error"
except KeyError:
    from_brackets = "KeyError"

assert from_brackets == ...
assert reading.get("unit") is ...


# TODO: += reads before it writes
counts = {}
try:
    counts["TH-04"] += 1
    outcome = "worked"
except Exception as err:
    outcome = type(err).__name__

assert outcome == ...


# TODO: a keys view looks at the dict -- it does not copy it
readings = {"TH-01": 21.7}
tags = readings.keys()
readings["TH-04"] = 91.0

assert sorted(tags) == ...


# TODO: | builds, |= mutates -- and an alias notices only one of the two
base = {"unit": "C"}
alias = base
combined = base | {"scale": 1.8}

assert alias == ...

base |= {"scale": 1.8}

assert alias == ...


# TODO: a set drops duplicates, and comparing sets ignores order
faults = {"TH-04", "TH-09", "TH-04"}

assert len(faults) == ...
assert faults == ...
