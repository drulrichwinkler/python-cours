"""Deciding whether a reading is out of bounds."""

DEFAULT_HIGH = 85.0

# Printed when this module is first imported, and not again: import runs the file
# once and caches the module object in sys.modules.
print("[sensorlib.limits imported]")


def is_fault(value, high=DEFAULT_HIGH):
    return value > high
