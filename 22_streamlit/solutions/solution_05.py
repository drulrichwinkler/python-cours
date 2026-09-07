"""Solution 05 -- cache_data, and what runs again without it."""

from streamlit.testing.v1 import AppTest

CACHED = """
import streamlit as st

CALLS = []


@st.cache_data
def expensive():
    CALLS.append(1)
    return [1, 2, 3]


expensive()
expensive()
expensive()
st.write(f"calls={len(CALLS)}")
"""

UNCACHED = CACHED.replace("@st.cache_data\n", "")

for label, script in (("cached", CACHED), ("uncached", UNCACHED)):
    app = AppTest.from_string(script, default_timeout=30)
    app.run()
    print(label, app.markdown[0].value)

# The script re-runs on every interaction, so an uncached read of the log happens
# on every keystroke. cache_data is module 14's decorator, and the reason the
# application in app.py is not slow.
print("cache_data keys on the arguments and returns a copy")
print("cache_resource returns the same object -- for a connection, not a DataFrame")
