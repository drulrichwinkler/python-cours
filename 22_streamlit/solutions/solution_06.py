"""Solution 06 -- key=, and reading a widget from anywhere."""

from streamlit.testing.v1 import AppTest

SCRIPT = """
import streamlit as st

value = st.slider("limit", 0.0, 100.0, 85.0, key="limit")
st.write(f"returned={value} state={st.session_state['limit']}")
"""

app = AppTest.from_string(SCRIPT, default_timeout=30)
app.run()
print(app.markdown[0].value)

app.slider[0].set_value(20.0).run()
print(app.markdown[0].value)

# The key does two things: it puts the value in session_state under a name, and it
# identifies the widget between runs -- which is what pins the value of a widget
# that appears and disappears inside an `if`.
print("limit" in app.session_state)
print(app.session_state["limit"])
