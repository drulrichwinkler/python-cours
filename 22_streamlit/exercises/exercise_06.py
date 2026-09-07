"""Exercise 06 -- key=, and reading a widget from anywhere.

Write a script with a slider that has `key="limit"`, and one line printing both the
returned value and the value in `session_state`. Run it, move the slider, and print
four lines.

Expected output:

    returned=85.0 state=85.0
    returned=20.0 state=20.0
    True
    20.0

Hint: `st.slider("limit", 0.0, 100.0, 85.0, key="limit")`. The last two lines are
about the test object rather than the script: `"limit" in app.session_state` and
`app.session_state["limit"]`. A key does two things -- it names the value in
session_state, and it identifies the widget between runs.
"""

from streamlit.testing.v1 import AppTest

# TODO: the script, then run it and print four lines
