"""Solution 01 -- The script is the page."""

from streamlit.testing.v1 import AppTest

SCRIPT = """
import streamlit as st
from sensorreport import load_readings, summarise

st.title("Sensor summary")
st.write("One row per location.")

for s in summarise(load_readings()):
    st.write(f"{s.location}: {s.mean}")
"""

# AppTest runs the script in-process and collects what it produced, by type. No
# browser, no port -- module 15's test client for a Streamlit app.
app = AppTest.from_string(SCRIPT, default_timeout=30)
app.run()

print([e.value for e in app.exception] or "none")
print(app.title[0].value)
print([item.value for item in app.markdown])
print(len(app.markdown))
