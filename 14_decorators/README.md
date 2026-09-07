# Module 14 — Decorators

**Assumes:** modules 01–13 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 14_decorators` says whether your exercises are done

## What this is about

You have been reading `@` since module 00 — `@pytest.mark.your_turn` in every test file, then
`@property`, `@classmethod` and `@staticmethod` in module 11, `@dataclass` in module 12,
`@contextlib.contextmanager` in module 09. This is the module that explains it, and there turns
out to be one idea underneath: **a function is a value.**

- **`@thing` is an assignment.** `@loud` above `def add` means `add = loud(add)`. Nothing more —
  and once you read it that way, every decorator in this course becomes ordinary.
- **Java annotations are not this.** `@Override` is metadata the compiler checks. A Python
  decorator *runs* when the `def` is executed, and what it returns is bound to the name — it may
  replace the function (`@loud`) or register it and hand it back unchanged (`@app.route("/")` in
  module 21). Either way it has run, which is what an annotation does not do.
- **The wrapper loses the name, the docstring and the signature** — so every traceback in the
  program says `wrapper`. `@functools.wraps` is the one line that fixes it, and it belongs on
  every wrapper you write.
- **A decorator with an argument is a call that returns a decorator**, which is why there are
  three levels of nesting and why the brackets in `@repeat(3)` are not decoration.
- **Stacked decorators apply bottom up.** The one nearest the `def` ends up innermost.

## What you can do afterwards

1. **say** what `@thing` does, in terms of assignment;
2. **write** a decorator that runs code before and after, and passes arguments and the return
   value straight through;
3. **name** what a wrapper loses and write the line that restores it;
4. **write** a decorator that takes an argument of its own;
5. **say** in which order stacked decorators apply, and what `@functools.cache` is wrong for.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 14_decorators`**
4. **`solutions/`** — last

## What this unlocks

Every framework in Part 5 registers your functions with a decorator: `@app.route` in Flask,
`@app.get` in FastAPI, `@st.cache_data` in Streamlit, `@on` in Textual. After this module those
are not syntax to memorise — they are functions that were handed your function and gave back
something else.
