"""Solution 03 -- Repair an app that forgets."""

from streamlit.testing.v1 import AppTest

SCRIPT = """
import streamlit as st

# A plain variable is created again on every run, because the whole file runs
# again. session_state belongs to the browser session and is the only thing that
# survives an interaction.
st.session_state.setdefault("clicks", 0)

if st.button("count"):
    st.session_state["clicks"] += 1

st.write(f"clicks={st.session_state['clicks']}")
"""

app = AppTest.from_string(SCRIPT, default_timeout=30)
app.run()
print(app.markdown[0].value)

app.button[0].click().run()
print(app.markdown[0].value)

app.button[0].click().run()
app.button[0].click().run()
print(app.markdown[0].value)
