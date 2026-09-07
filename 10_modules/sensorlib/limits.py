"""Deciding whether a reading is out of bounds."""

DEFAULT_HIGH = 85.0

# Printed once, when this module is first imported -- and not again, however many
# times it is imported after that. Import is a one-off; the result is cached.
print("[sensorlib.limits imported]")


def is_fault(value, high=DEFAULT_HIGH):
    return value > high
