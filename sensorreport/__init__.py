"""The analysis that Part 5 presents five different ways.

Modules 21 to 25 solve one identical task -- show these readings to a person --
in Flask, Streamlit, FastAPI, Tkinter and Textual. For the comparison to say
anything about the frameworks, the analysis underneath has to be the same code.
This is that code.

It is a real installed package, listed in pyproject.toml, so every module can
write `import sensorreport` with no sys.path line anywhere. That is module 10's
point, made by the repository rather than asserted.
"""

from sensorreport.report import (
    LIMIT,
    Reading,
    Summary,
    faults,
    load_readings,
    summarise,
)

__all__ = ["LIMIT", "Reading", "Summary", "faults", "load_readings", "summarise"]
