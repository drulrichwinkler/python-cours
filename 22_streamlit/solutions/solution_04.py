"""Solution 04 -- A widget returns its value, and the script runs again."""

from streamlit.testing.v1 import AppTest

SCRIPT = """
import streamlit as st
from sensorreport import load_readings

above = st.slider("above", 0.0, 100.0, 85.0)
rows = load_readings()
hot = [r for r in rows if r.value is not None and r.value > above]

st.metric("readings", len(rows))
st.metric("above", len(hot))
"""

app = AppTest.from_string(SCRIPT, default_timeout=30)
app.run()

print(app.slider[0].value, app.metric[1].value)

# set_value(...).run() is the interaction: the whole script executes a second
# time, and this time st.slider returns 20.0 rather than the default.
app.slider[0].set_value(20.0).run()
print(app.slider[0].value, app.metric[1].value)

app.slider[0].set_value(100.0).run()
print(app.slider[0].value, app.metric[1].value)

# The first metric never moves: it does not depend on the widget.
print(app.metric[0].value)
