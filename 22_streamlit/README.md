# Module 22 — Streamlit

**Assumes:** modules 01–21 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 22_streamlit` says whether your exercises are done

## What this is about

The same numbers as module 21, and the sharpest comparison in Part 5: **no routes, no templates,
no HTML, no `url_for`.** `app.py` is under a hundred lines and there is not a tag in it.

```console
uv run streamlit run 22_streamlit/app.py
```

Opens a browser at <http://localhost:8501>. Ctrl+C stops it — module 20.

What replaces all that markup is an execution model, and it is the one thing here you have to
actually understand:

> **The whole script runs again, top to bottom, on every interaction.**

Measured: a slider at 85 gives 3 faults; `set_value(20.0)` gives 47. Nothing was recomputed by a
callback — the file was executed a second time, and `st.slider(...)` returned a different number.

Everything else in the module follows from that:

- **A widget call does two things:** it puts the widget on the page, and it **returns the value
  the widget currently has.** There is no event handler anywhere.
- **A plain variable does not survive.** Measured over three runs: `plain=1`, `plain=1`,
  `plain=1` — created again from the top every time. `st.session_state` counted to 3, and it is
  the only thing that persists. Which is where a basket, a history or a login has to live.
- **Everything expensive runs again**, on every keystroke in a text box. `@st.cache_data` —
  module 14's decorator — is why the application is not slow. Measured: three calls, one
  execution.
- **The script is the page**, so an exception ends the page where it happened: everything above
  is displayed, everything below never runs, and in a browser the traceback appears **in the
  page** — the same exposure module 20 described for Flask's debugger.

## Testing without a browser

`AppTest` runs the script in-process and hands back the elements it produced, by type:

```python
app = AppTest.from_string(SCRIPT)
app.run()
app.slider[0].set_value(20.0).run()      # the interaction is a second run
app.metric[0].value                       # '47' -- a string, because a page shows text
```

Every cell in the notebook and every exercise uses it. No browser, no port.

## What you can do afterwards

1. **say** what happens to the script when a user moves a slider, and what a widget returns;
2. **say** why a plain variable does not survive an interaction, and put something in
   `session_state` that does;
3. **use** `@st.cache_data`, and say what it costs when the cached function is not pure;
4. **test** an app without a browser, including an interaction;
5. **say** what Streamlit gives up in exchange for having no HTML — and name the three requests
   that mean you have outgrown it.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 22_streamlit`**
4. **`solutions/`** — last

## Flask or Streamlit

| | Flask (21) | Streamlit (22) |
| --- | --- | --- |
| the page | your HTML, in templates | Streamlit's widgets, in its layout |
| URLs | you design them | one page; multipage is a directory convention |
| interaction | a request per click | the script re-runs |
| state | a session or a database | `st.session_state` |
| a chart | pick a library, embed it | `st.line_chart(data)` |
| CSS, JavaScript, a design | yours | not really available |
| this application | ~70 lines plus 4 templates | ~90 lines, no templates |

**The heuristic: is the point the data, or the page?** If a colleague needs to explore your
numbers, Streamlit, and it will take an afternoon. If it is a product for people who do not work
with you, Flask or Django — because sooner or later somebody asks for a URL, a login, or a logo
in the corner, and those are the three things Streamlit does not do.

Module 23 is FastAPI, where the type hints you have been writing since module 04 stop being
notation and become the interface.
