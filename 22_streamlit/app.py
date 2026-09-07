"""The Streamlit application: the same numbers as module 21, without HTML.

Run it:

    uv run streamlit run 22_streamlit/app.py

It opens a browser at http://localhost:8501. Ctrl+C in the terminal stops it --
module 20.

Compare this file with 21_flask/app.py plus its four templates. There are no
routes, no templates, no `url_for`, and no HTML. What there is instead is an
execution model: **this whole file runs again on every interaction.**
"""

import streamlit as st

from sensorreport import LIMIT, faults, load_readings, summarise

st.set_page_config(page_title="Sensors", layout="centered")

st.title("Sensor summary")


# The file re-runs on every interaction, so reading the log would happen on every
# click. @st.cache_data makes it happen once -- module 14's decorator, and the
# reason this application is not slow.
@st.cache_data
def readings():
    return load_readings()


rows = readings()

# A widget returns its current value. On the first run that is the default; after
# an interaction, it is what the user chose -- because the file ran again.
above = st.slider("Fault above (°C)", min_value=0.0, max_value=100.0, value=LIMIT, step=0.5)

hot = [r for r in rows if r.value is not None and r.value > above]

left, middle, right = st.columns(3)
left.metric("Readings", len(rows))
middle.metric("Unreadable", sum(1 for r in rows if r.value is None))
right.metric("Above limit", len(hot))

st.subheader("By location")
st.dataframe(
    [
        {
            "location": s.location,
            "readings": s.readings,
            "usable": s.usable,
            "mean": s.mean,
            "highest": s.highest,
            "faults": s.faults,
        }
        for s in summarise(rows)
    ],
    hide_index=True,
)

st.subheader("Readings over the day")
chosen = st.multiselect(
    "Locations",
    options=sorted({r.location for r in rows}),
    default=sorted({r.location for r in rows}),
)
st.line_chart(
    {
        location: [r.value for r in rows if r.location == location and r.value is not None]
        for location in chosen
    }
)

st.subheader("Faults")
if faults(rows):
    for reading in faults(rows):
        st.write(f"**{reading.tag}** — {reading.value} {reading.unit} at {reading.at}")
else:
    st.write("None.")

with st.expander("How many times has this script run?"):
    # A plain variable would be 1 every time: the file starts fresh on each run.
    # session_state is the one thing that survives, and it is the answer to
    # "where do I keep something between interactions".
    st.session_state.setdefault("runs", 0)
    st.session_state["runs"] += 1
    st.write(f"This session has run the script {st.session_state['runs']} times.")
