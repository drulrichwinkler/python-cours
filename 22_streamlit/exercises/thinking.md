# Module 22 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 22_streamlit`.

---

## Exercise 07 — The script that runs again

```python
plain = 0
plain += 1
st.write(f"plain={plain}")          # plain=1, three runs in a row

st.session_state.setdefault("kept", 0)
st.session_state["kept"] += 1
st.write(f"kept={st.session_state['kept']}")   # kept=1, then 2, then 3
```

a) Explain both results from the execution model, in a way that does not use the
   phrase "Streamlit is different". What exactly happens between the second and the
   third `st.write`?
b) Module 21's Flask app kept nothing between requests either — a new request ran a
   new view function. So both frameworks start from scratch. Name what is genuinely
   different about where the two put their state, and why Streamlit needs
   `session_state` where Flask did not.
c) A colleague's app has a counter that works for one click and then stops
   increasing. Say what they wrote, and say why the bug is worse than one that never
   works at all.
d) `@st.cache_data` avoids re-reading the file. Name a function in this application
   that must **not** be cached, and say what would go wrong.

> **Hint on (a):** how many times has the file been executed by then, and where did
> `plain` come from on each of those?
> **Hint on (b):** what does Flask's view function do with a value it needs to keep,
> and what does the browser send back next time?
> **Hint on (d):** what does the cache key on, and what does it not notice?

**Check yourself:** your answer to (c) has to say what the user sees on the first
click, and why that is the problem.

---

## Exercise 08 — When you have outgrown it

Streamlit gives up three things: control of the markup, the URL structure, and the
request cycle.

a) For each of the three, name a concrete request from a user or a colleague that you
   could not fulfil, and say what you would have to do about it.
b) The module's heuristic is "is the point the data, or the page?". Apply it to four
   cases and defend each in one sentence:
   1. a dashboard for your team, showing last night's test results;
   2. a public page where customers look up a serial number;
   3. an internal tool where somebody edits the sensor list;
   4. a page you have to embed in the company intranet's existing layout.
c) You have a Streamlit app that three departments use, and now somebody wants a
   login. Say what your options are and which you would take.
d) Streamlit re-runs the script for every interaction. Name the kind of application
   where that is not merely inefficient but *wrong* — where the model itself does not
   fit.

> **Hint on (a):** think about a bookmark, a logo, and a progress bar during a long
> upload.
> **Hint on (d):** what if something has to happen while nobody is interacting?

**Check yourself:** your answer to (d) has to name a requirement that the re-run
model cannot express, not just one it does slowly.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
