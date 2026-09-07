"""Exercise 02 -- Predict what Streamlit does.

Replace each `...` with the value you expect, then run the file.

    uv run 22_streamlit/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

from streamlit.testing.v1 import AppTest

WIDGET = """
import streamlit as st
from sensorreport import load_readings

above = st.slider("above", 0.0, 100.0, 85.0)
hot = [r for r in load_readings() if r.value is not None and r.value > above]
st.metric("above", len(hot))
"""

app = AppTest.from_string(WIDGET, default_timeout=30)
app.run()

# TODO: on the first run a widget returns its default
assert app.slider[0].value == ...

# TODO: metric values come back as what type?
assert type(app.metric[0].value).__name__ == ...
assert app.metric[0].value == ...

# TODO: move it. There are 50 readings and 3 of them unreadable.
app.slider[0].set_value(20.0).run()

assert app.metric[0].value == ...

app.slider[0].set_value(100.0).run()

assert app.metric[0].value == ...


PERSISTENCE = """
import streamlit as st

plain = 0
plain += 1
st.write(f"plain={plain}")

st.session_state.setdefault("kept", 0)
st.session_state["kept"] += 1
st.write(f"kept={st.session_state['kept']}")

st.button("again")
"""

app = AppTest.from_string(PERSISTENCE, default_timeout=30)
app.run()
app.button[0].click().run()
app.button[0].click().run()

# TODO: three runs. One of the two counters counted.
assert [item.value for item in app.markdown] == ...


CACHE = """
import streamlit as st

CALLS = []


@st.cache_data
def expensive():
    CALLS.append(1)
    return 1


expensive()
expensive()
expensive()
st.write(f"calls={len(CALLS)}")
"""

app = AppTest.from_string(CACHE, default_timeout=30)
app.run()

# TODO: three calls to a cached function
assert app.markdown[0].value == ...


BOOM = """
import streamlit as st

st.write("displayed")
raise ValueError("kaputt")
st.write("never reached")
"""

app = AppTest.from_string(BOOM, default_timeout=30)
app.run()

# TODO: the script is the page, so where does an exception leave it?
assert [item.value for item in app.markdown] == ...
assert [e.value for e in app.exception] == ...
