"""Solution 02 -- Predict what Streamlit does.

the slider       returns 85.0 on the first run: a widget call puts the widget on
                 the page AND returns its current value, which to begin with is
                 the default.
metric values    come back as strings -- '3', not 3. AppTest reports what the page
                 shows, and a page shows text.
after set_value  the metric is '47' and then '0'. Nothing was recomputed by a
                 callback: the WHOLE SCRIPT ran again, from the first line, and
                 this time st.slider returned 20.0 instead of 85.0. That is the
                 execution model, and everything else in this module follows from
                 it.
the two counters are ['plain=1', 'kept=3'] after three runs. A plain variable is
                 created again from the top every time, so it counts to one for
                 ever. st.session_state belongs to the browser session rather than
                 to the script run, and is the only thing that survives -- which is
                 where a basket, a history or a login has to live.
the cache        makes it 'calls=1'. Three calls, one execution. Without the
                 decorator it would be three, and since the script re-runs on every
                 keystroke, an uncached read of the log would happen on every one.
the exception    leaves 'displayed' on the page and never reaches the line below
                 it. The script IS the page, so an exception ends the page where it
                 happened -- and in a browser the traceback appears in the page,
                 which is the exposure module 20 described for Flask's debugger.
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

assert app.slider[0].value == 85.0

assert type(app.metric[0].value).__name__ == "str"
assert app.metric[0].value == "3"

# move it. There are 50 readings and 3 of them unreadable.
app.slider[0].set_value(20.0).run()

assert app.metric[0].value == "47"

app.slider[0].set_value(100.0).run()

assert app.metric[0].value == "0"


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

assert [item.value for item in app.markdown] == ["plain=1", "kept=3"]


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

assert app.markdown[0].value == "calls=1"


BOOM = """
import streamlit as st

st.write("displayed")
raise ValueError("kaputt")
st.write("never reached")
"""

app = AppTest.from_string(BOOM, default_timeout=30)
app.run()

assert [item.value for item in app.markdown] == ["displayed"]
assert [e.value for e in app.exception] == ["kaputt"]
