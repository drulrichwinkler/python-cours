"""Exercise 04 -- A widget returns its value, and the script runs again.

Write a script with a slider and two metrics: how many readings there are
altogether, and how many are above the slider's value. Then run it, move the slider
twice, and print four lines.

Each of the first three lines is the slider's value and the second metric, separated
by a space. The fourth is the first metric, which never moves.

Expected output:

    85.0 3
    20.0 47
    100.0 0
    50

Hint: `st.slider("above", 0.0, 100.0, 85.0)` -- label, minimum, maximum, default.
`app.slider[0].set_value(20.0).run()` is the interaction, and `.run()` is the part
that matters: the whole script executes again, and this time the slider returns 20.0.
Metric values come back as strings.
"""

from streamlit.testing.v1 import AppTest

# TODO: the script, then run it and print four lines
