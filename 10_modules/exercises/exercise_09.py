"""Exercise 09 (bonus) -- A command line.

Write `build_parser()` returning an `argparse.ArgumentParser` with

  - `prog="report"` and `description="Summarise a sensor log."`
  - a required positional argument `path`
  - `--limit`, a float, defaulting to 85.0
  - `--verbose`, a flag that is True when present and False when not

Then parse three argument lists and print what comes back, as below. The third one
is invalid, and what it does is the thing worth remembering.

Expected output:

    data/readings.csv 90.0 False
    float
    85.0 False
    SystemExit 2

Hint: `parse_args(["..."])` with a list is how a parser is tested. `action="store_true"`
makes a flag. On a bad value argparse prints usage to standard error and ends the
process -- so the last one needs `except SystemExit as err:` and `err.code`.
"""

import argparse

# TODO: the function, then the three parses
