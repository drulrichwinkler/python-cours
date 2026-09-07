"""Solution 02 -- Predict what dicts and sets do.

collapsed        is {1: 'bool'}. 1 == 1.0 == True and their hashes agree, so all
                 three are one key. The first one written keeps the key object,
                 the last one written supplies the value.
in               asks about keys: "value" is a key, 91.0 is a value, so the second
                 answer is False.
reading["unit"]  raises KeyError; reading.get("unit") returns None. That is the
                 whole difference, and it is why .get belongs where a missing key
                 is an expected case, not everywhere.
counts["TH-04"]  raises KeyError: += reads the key, adds one, and writes it back.
                 There is nothing to read on the first occurrence.
tags             is ['TH-01', 'TH-04']. A keys view looks at the dict rather than
                 copying it, so it has the key that was added afterwards.
alias            is {'unit': 'C'} after `|`, which built a new dict, and
                 {'unit': 'C', 'scale': 1.8} after `|=`, which changed the one
                 both names refer to. This is `+` against `+=` from module 05.
faults           has two entries and equals {'TH-04', 'TH-09'}: the duplicate is
                 dropped on the way in, and comparing sets ignores order.
"""

collapsed = {1: "int", 1.0: "float", True: "bool"}  # noqa: F601 -- the collision is the point

assert collapsed == {1: "bool"}


reading = {"tag": "TH-04", "value": 91.0}

assert ("value" in reading) is True
assert (91.0 in reading) is False


try:
    reading["unit"]
    from_brackets = "no error"
except KeyError:
    from_brackets = "KeyError"

assert from_brackets == "KeyError"
assert reading.get("unit") is None


counts = {}
try:
    counts["TH-04"] += 1
    outcome = "worked"
except Exception as err:
    outcome = type(err).__name__

assert outcome == "KeyError"


readings = {"TH-01": 21.7}
tags = readings.keys()
readings["TH-04"] = 91.0

assert sorted(tags) == ["TH-01", "TH-04"]


base = {"unit": "C"}
alias = base
combined = base | {"scale": 1.8}

assert alias == {"unit": "C"}

base |= {"scale": 1.8}

assert alias == {"unit": "C", "scale": 1.8}


faults = {"TH-04", "TH-09", "TH-04"}

assert len(faults) == 2
assert faults == {"TH-04", "TH-09"}
