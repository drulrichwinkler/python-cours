"""Exercise 05 -- cache_data, and what runs again without it.

The script below calls an expensive function three times. Run it twice: once as
written, and once with the decorator removed, and print what each says.

Then print the two sentences about which cache to use, exactly as below.

Expected output:

    cached calls=1
    uncached calls=3
    cache_data keys on the arguments and returns a copy
    cache_resource returns the same object -- for a connection, not a DataFrame

Hint: `CACHED.replace("@st.cache_data\\n", "")` gives you the second version without
writing it out twice. The difference matters because the script re-runs on every
keystroke -- an uncached read of the log would happen on every one of them.
"""

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

# TODO: the second version, the loop, and the two sentences
