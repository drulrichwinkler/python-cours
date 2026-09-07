# Solution 07 — The script that runs again

**a) Both results, from the model**

By the third `st.write` the file has been **executed three times**, as three separate
top-to-bottom runs of the same script.

- `plain` is created by the line `plain = 0` on every one of those runs. It is an
  ordinary local variable in an ordinary module-level namespace that is built fresh
  each time, so `plain += 1` always turns 0 into 1. Nothing is being forgotten: the
  value was never asked to last, and the statement that would have preserved it is the
  one that resets it.
- `st.session_state` is not part of that namespace. It belongs to the **browser
  session** — Streamlit holds it between runs and hands the same dict back — so
  `setdefault` does nothing after the first run and `+= 1` accumulates.

What happens between the second and third `st.write`: nothing at all, within one run.
The interesting thing happens *between runs* — the script ends, the namespace is
discarded, the user clicks, and the file starts again at line 1 with a `session_state`
that survived.

**b) Flask kept nothing either. What is different**

Both start from scratch, and the difference is **what "scratch" means and who holds
what is kept.**

In Flask, one request runs one view function. Anything to keep goes somewhere explicit
and external: a cookie signed by the server (`session`), a row in a database, or a
cache. The browser then sends the cookie back with the next request, and the server
looks the state up. The state lives *outside the process's memory for that request*, by
construction, and it is your decision where.

In Streamlit there is no request to hang state off. There is one long-lived server
process, one connection per browser tab, and a script that runs over and over inside
it. `session_state` is Streamlit's answer: a dict in the server's memory, keyed by that
connection.

Which is why Flask did not need it. Flask's model already forced you to be explicit
about persistence, because nothing could possibly survive a request. Streamlit's model
looks as though variables should survive — the script reads like a program, not like a
handler — and `session_state` exists to give the one place where they do.

The consequence worth carrying: `session_state` is **server memory**, so it is lost
when the server restarts and it is per-tab, not per-user. For anything that has to
outlive either, you are back to Flask's answer — a database.

**c) The counter that works once**

They wrote this:

```python
clicks = 0
if st.button("count"):
    clicks += 1
st.write(f"clicks={clicks}")
```

The first click shows `clicks=1`, because the click and the display happen in the same
run: the button returns True, the variable goes to 1, and the page is written. Every
click after that shows `clicks=1` again.

Why that is worse than never working: **the first test passes.** Somebody clicks once,
sees 1, and concludes the feature is done. A counter that always showed 0 would have
been fixed in the same minute. This one ships, and is found by a user who clicked
twice — which is every user.

That is the same failure profile the course has met five times in a row (modules 08,
16, 17, 18, 19): the version that is wrong in a way that looks right first.

**d) A function that must not be cached**

The one in `app.py` that reads the log is cached, and correctly — the file does not
change while the app runs.

What must not be: **anything whose answer depends on something the cache does not
key on.** Two concrete cases in this application:

- **A function taking no arguments that reads a file that *does* change.**
  `@st.cache_data` keys on the arguments, so a no-argument function is computed once
  and never again. If the sensor log were being appended to, the app would show the
  first version of it for as long as the server ran, with nothing wrong on screen.
- **Anything with a side effect** — writing a row, sending a mail, appending to a
  log. A cached call happens once and then silently does not happen, so the second
  fault is never reported.

And the one that is a category error rather than a bug: **`st.cache_data` on something
holding a resource**, like a database connection. `cache_data` returns a *copy* of its
value, so every caller gets a copy of the connection object. `st.cache_resource` is
the one that returns the same object, and choosing wrongly between them is the
distinction worth remembering.

The general rule, which is module 14's rule about `functools.cache` word for word: a
cached function must be pure. `ttl=` and the "Clear cache" menu item are both
admissions that a particular one was not.
