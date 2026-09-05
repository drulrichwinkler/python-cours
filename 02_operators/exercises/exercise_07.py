"""Exercise 07 -- Reading a status byte.

Print whether each of the four flags is set in `status`. Then set READY and print
the new byte in binary.

Expected output:

    Ready: False
    Limit: True
    Fault: False
    Calibrate: True
    New byte: 0b1011

Hint 1: status & MASK gives a NUMBER, not True/False. Without bool() the line
would read "Limit: 2" -- correct, but not an answer to the question asked.
Hint 2: setting a bit is OR. Printing in binary is bin().
"""

READY = 0b0001
LIMIT = 0b0010
FAULT = 0b0100
CALIBRATE = 0b1000

status = 0b1010

# TODO: four lines


# TODO: set READY and print the new byte in binary
