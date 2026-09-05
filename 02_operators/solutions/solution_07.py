"""Solution 07 -- Reading a status byte.

bool() is needed because status & LIMIT gives the number 2, not True. Without it
the line would read "Limit: 2" -- correct, but not an answer to the question.
"""

READY = 0b0001
LIMIT = 0b0010
FAULT = 0b0100
CALIBRATE = 0b1000

status = 0b1010

print(f"Ready: {bool(status & READY)}")
print(f"Limit: {bool(status & LIMIT)}")
print(f"Fault: {bool(status & FAULT)}")
print(f"Calibrate: {bool(status & CALIBRATE)}")

new_byte = status | READY
print(f"New byte: {bin(new_byte)}")
