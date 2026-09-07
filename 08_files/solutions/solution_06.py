"""Solution 06 -- Limits out of JSON."""

import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

limits = json.loads((DATA / "limits.json").read_text(encoding="utf-8"))


def high_for(tag):
    """The sensor's own high limit if it has one, otherwise the default."""
    return limits["sensors"].get(tag, limits["default"])["high"]


print(high_for("TH-04"))
print(high_for("TH-01"))
print(limits["unit"], type(limits["strict"]).__name__)
print(sorted(limits["sensors"]))
