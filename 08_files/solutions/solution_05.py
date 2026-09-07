"""Solution 05 -- Write a report and read it back."""

import tempfile
from pathlib import Path

work = Path(tempfile.mkdtemp())
report = work / "report.txt"

lines = ["TH-04;91.0", "TH-02;88.4"]

with open(report, "w", encoding="utf-8") as fh:
    for line in lines:
        fh.write(line + "\n")  # write() adds no newline of its own

with open(report, "a", encoding="utf-8") as fh:
    fh.write("end\n")

print(repr(report.read_text(encoding="utf-8")))
print(report.exists(), report.name)

try:
    with open(report, "x", encoding="utf-8") as fh:
        fh.write("nope")
except FileExistsError:
    print("FileExistsError")
