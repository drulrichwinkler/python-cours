# Module 21 — Flask

**Assumes:** modules 01–20 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 21_flask` says whether your exercises are done

## What this is about

The first of five presentations of the same data. `app.py` in this folder is the finished
application; the notebook builds it up a piece at a time.

```console
uv run flask --app 21_flask/app run --debug
```

Then <http://127.0.0.1:5000/>. Ctrl+C stops it — module 20.

- **A route is a decorated function.** `@app.get("/")` registers it and hands it back
  unchanged, which is module 14 arriving where it was promised. Nothing about it is magic and
  you have already read the mechanism.
- **You do not need a server to test it.** `app.test_client()` sends requests straight into the
  application — no socket, no port, no process. Every cell in the notebook and every exercise
  uses it, which is also how Flask applications are actually tested.
- **The return value decides the response.** A `str` becomes `text/html`, a `dict` becomes
  `application/json`, a tuple is `(body, status)`.
- **Everything from a URL is text.** `<int:number>` converts, and a path that does not match the
  converter is a 404 rather than an error in your view. `request.args.get("above", type=float)`
  gives **`None`** on a value that will not convert, so the view has to handle it — and
  forgetting to is how a search page returns 500 to somebody who typed a word.
- **Jinja2 escapes by default**, so `<script>` in a variable lands in the page as text. `|safe`
  turns that off, and on anything a user supplied it is cross-site scripting — module 19's SQL
  injection in another language: text from outside became syntax on the inside.
- **`url_for` names the view function**, not the path, so renaming the URL does not break the
  links. It also encodes for you: `Test rig` comes out `Test%20rig`.

## One measured trap

`{{ v|default('--') }}` does **not** replace `None`. It replaces an *undefined* value, and `None`
is perfectly defined — so it prints the word `None` into your page. The test that works is:

```jinja
{{ v if v is not none else "--" }}
```

Which matters here, because a mean over no readings is `None`.

## What you can do afterwards

1. **map** a URL to a function, and read a piece of the path and a query parameter;
2. **test** a route without starting anything;
3. **render** a template with a loop and a condition, and handle a `None`;
4. **say** what Jinja2 does to markup in a variable and what `|safe` undoes;
5. **build** a link with `url_for`, and say why not with `+`;
6. **answer** with a status code, using `abort`.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 21_flask`**
4. **`solutions/`** — last

## What this module contributed to the answer

None of the numbers. `app.py` is one import and four view functions; every figure on the page
comes from `sensorreport`, unchanged since module 20 — which is what makes the comparison with
modules 22 to 25 a comparison of frameworks rather than of analyses.

Module 22 is Streamlit: the same figures with no routes, no templates and no HTML.
