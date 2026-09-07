"""Exercise 03 -- Repair an app that forgets.

The script counts button clicks. Run it: the count is 0 after one click, and 0 after
three.

The variable is created again on every run, because **the whole file runs again** on
every interaction. Fix it so the count survives.

Expected output:

    clicks=0
    clicks=1
    clicks=3

Hint: `st.session_state` is a dict that belongs to the browser session rather than to
the script run, and it is the only thing that persists.
`st.session_state.setdefault("clicks", 0)` gives it a starting value without
overwriting it on the next run.
"""

from streamlit.testing.v1 import AppTest

SCRIPT = """
import streamlit as st

clicks = 0  # TODO: this does not survive a re-run

if st.button("count"):
    clicks += 1

st.write(f"clicks={clicks}")
"""

app = AppTest.from_string(SCRIPT, default_timeout=30)
app.run()
print(app.markdown[0].value)

app.button[0].click().run()
print(app.markdown[0].value)

app.button[0].click().run()
app.button[0].click().run()
print(app.markdown[0].value)
