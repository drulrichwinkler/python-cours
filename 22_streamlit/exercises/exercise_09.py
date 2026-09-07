"""Exercise 09 (bonus) -- The whole application, tested.

`app.py` one folder up is the finished application. Write `run_with(above)`, which
runs it, moves the slider to `above` when that is not None, and returns the AppTest
object.

Then print: the exceptions or `none`, the title, the metrics as (label, value) pairs,
the number of table rows and the sorted multiselect value on one line -- and then, for
each of two slider positions, the position and the three metric values as a list.

Expected output:

    none
    Sensor summary
    [('Readings', '50'), ('Unreadable', '3'), ('Above limit', '3')]
    3 ['Hall', 'Office', 'Test rig']
    20.0 ['50', '3', '47']
    100.0 ['50', '3', '0']

Hint: `AppTest.from_file(str(APP), default_timeout=30)` -- the timeout matters,
because this app reads a file and draws a chart. Look at the last two lines: only the
third metric moves. The other two are facts about the file rather than about the
question being asked.
"""

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().parent.parent / "app.py"

# TODO: run_with, then the prints
