"""Exercise 01 -- The script is the page.

Run the script below with `AppTest` and print four lines:

  1. the exceptions it raised, or the string `none`
  2. the title
  3. every markdown item it produced, as a list
  4. how many markdown items there are

Expected output:

    none
    Sensor summary
    ['One row per location.', 'Hall: 22.12', 'Office: 22.34', 'Test rig: 32.83']
    4

Hint: `AppTest.from_string(SCRIPT, default_timeout=30)` then `.run()`. Elements come out by type --
`app.title`, `app.markdown`, `app.metric` -- and each has a `.value`. There is no
browser and no port: this is module 15's test client for a Streamlit app.
"""

from streamlit.testing.v1 import AppTest

SCRIPT = """
import streamlit as st
from sensorreport import load_readings, summarise

st.title("Sensor summary")
st.write("One row per location.")

for s in summarise(load_readings()):
    st.write(f"{s.location}: {s.mean}")
"""

# TODO: run it, then four prints
