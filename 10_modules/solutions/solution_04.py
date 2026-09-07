"""Solution 04 -- The main guard."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(MODULE))

from sensorlib.limits import is_fault  # noqa: E402


def main():
    readings = [21.7, 91.0, 23.1]
    faults = [value for value in readings if is_fault(value)]
    print("checked", len(readings))
    print("faults", faults)


print("__name__ is", __name__)

# True when this file was started, false when it was imported. Without it, the
# import would run main() as a side effect.
if __name__ == "__main__":
    main()
