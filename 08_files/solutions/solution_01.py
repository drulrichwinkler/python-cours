"""Solution 01 -- Read the log as text."""

from pathlib import Path

# __file__ is this file. .resolve() makes it absolute, .parent goes up one folder --
# twice, because this file sits in 08_files/solutions/ and the data is next to that.
DATA = Path(__file__).resolve().parent.parent / "data"
SENSORS = DATA / "sensors.csv"

text = SENSORS.read_text(encoding="utf-8")

print(SENSORS.name, SENSORS.suffix)
print(len(text.splitlines()), "lines")
print(len(text), "code points,", len(SENSORS.read_bytes()), "bytes")
print(text.splitlines()[1])
