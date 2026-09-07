"""Exercise 01 -- Read the log as text.

`data/sensors.csv` sits two folders up from this file. Print four lines:

  1. the file's name and its suffix, separated by a space
  2. how many lines the text has, then " lines"
  3. the code points and the bytes, as in the expected output below
  4. the second line of the file -- the first reading, not the header

Expected output:

    sensors.csv .csv
    6 lines
    129 code points, 134 bytes
    TH-01;21.7;°C;Hall

Hint: `Path(__file__).resolve().parent.parent / "data"` is the folder. Read the text
with `encoding="utf-8"` named, count lines with `.splitlines()`, and get the byte
count from `.read_bytes()`.
"""

from pathlib import Path

# __file__ is this file. .resolve() makes it absolute, .parent goes up one folder --
# twice, because this file sits in 08_files/exercises/ and the data is next to that.
DATA = Path(__file__).resolve().parent.parent / "data"
SENSORS = DATA / "sensors.csv"

# TODO: four prints
