"""Solution 05 -- The part that is not a window."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from logic import label_for, verdict  # noqa: E402

from sensorreport import load_readings  # noqa: E402

readings = load_readings()

test_rig = [r for r in readings if r.location == "Test rig"]
hall = [r for r in readings if r.location == "Hall"]

# `r.value or 0.0` would be wrong on a reading of exactly 0.0, so the None rows are
# filtered out first rather than defaulted.
worst = max((r for r in test_rig if r.value is not None), key=lambda r: r.value or 0.0)

print(label_for(worst, 85.0))
print(label_for(worst, 95.0))

unreadable = next(r for r in readings if r.value is None)
print(label_for(unreadable, 85.0))

print(verdict(test_rig, 85.0))
print(verdict(hall, 85.0))
