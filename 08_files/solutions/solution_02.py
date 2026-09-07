"""Solution 02 -- Predict what files do.

ascii            raises UnicodeDecodeError on the first byte of `°`. latin-1 maps
                 all 256 byte values to characters, so it cannot fail -- and hands
                 back 'TH-01;21.7;Â°C;Hall', the two UTF-8 bytes read as two
                 characters. The encoding that raises is the lucky one.
type(...)        is str. A CSV file is text and has no types; converting is the
                 caller's job, and float() on a bad field is where bad data
                 announces itself.
line             is 'tag;value;unit;location\\n'. Iterating a file hands you what
                 is in the file, line ending included. .splitlines() on the whole
                 text is the version that drops them.
back["tags"]     is a list: JSON has arrays and no tuples. sorted(back) is
                 ['3', 'tags'] -- a JSON object's keys are strings by definition, so
                 the int key 3 comes back as "3". Neither conversion says anything.
json.dumps(set)  raises TypeError. Of the three, this is the only one you find out
                 about at the line that caused it.
target           is empty. Mode "w" truncates the file when it opens it, before any
                 write happens -- which is why "w" on the wrong path destroys the
                 file even if the program crashes immediately afterwards.
"""

import csv
import json
import tempfile
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
SENSORS = DATA / "sensors.csv"

try:
    SENSORS.read_text(encoding="ascii")
    strict = "no error"
except UnicodeDecodeError:
    strict = "UnicodeDecodeError"

loose = SENSORS.read_text(encoding="latin-1").splitlines()[1]

assert strict == "UnicodeDecodeError"
assert loose == "TH-01;21.7;Â°C;Hall"


with open(SENSORS, newline="", encoding="utf-8") as fh:
    first = next(csv.DictReader(fh, delimiter=";"))

assert type(first["value"]) is str


with open(SENSORS, encoding="utf-8") as fh:
    line = next(iter(fh))

assert line == "tag;value;unit;location\n"


original = {"tags": ("TH-04", "TH-09"), 3: "an int key"}
back = json.loads(json.dumps(original))

assert type(back["tags"]) is list
assert sorted(back) == ["3", "tags"]


try:
    json.dumps({"seen": {"TH-04"}})
    outcome = "worked"
except Exception as err:
    outcome = type(err).__name__

assert outcome == "TypeError"


target = Path(tempfile.mkdtemp()) / "x.txt"
target.write_text("abc\n", encoding="utf-8")

with open(target, "w", encoding="utf-8"):
    pass

assert target.read_text(encoding="utf-8") == ""
