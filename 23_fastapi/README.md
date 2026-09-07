# Module 23 — FastAPI

**Assumes:** modules 01–22 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 23_fastapi` says whether your exercises are done

## What this is about

The same numbers as modules 21 and 22, served to a **program** rather than to a person. There is
no HTML in this module and no widget: `app.py` answers with JSON, and the caller is code.

```console
uv run uvicorn 23_fastapi.app:app --reload
```

Then <http://127.0.0.1:8000/docs> — a page nobody in this repository wrote. Ctrl+C stops it,
module 20.

The reason this module exists is one sentence:

> **Your type hints stop being notation and become the program.**

In module 04 an annotation was documentation that mypy read; deleting it changed nothing about
what ran. Here `minimum: float` is the code that parses the query string, `body: LimitIn` is the
code that validates the request body, and `-> SummaryOut` is the code that decides what leaves
the process. Measured on one unchanged function body:

| return annotation | what the client got |
| --- | --- |
| `-> Out` | `{'tag': 'TH-04', 'value': 93.5}` |
| `-> dict[str, Any]` | `{'tag': 'TH-04', 'value': 93.5, 'secret': 'internal note'}` |
| none | the same three keys, and the documented schema is `{}` |

An annotation you can widen without thinking is now a data leak you can ship in a one-line diff.

## The first tool in this course that refuses

Five times already a tool has answered rather than fail:

| module | the tool | what it does instead of failing |
| --- | --- | --- |
| 08 | `latin-1` | decodes any bytes; gives you `Â°C` |
| 16 | `requests` with no charset | falls back to Latin-1; the same `Â°C` |
| 17 | `html.parser` | repairs; four cells where there are two |
| 18 | `read_csv` | picks a type from the data; `.sum()` concatenates |
| 19 | SQLite | stores what it was given; `REAL` holds `'kaputt'` |

This is the other case, and it closes the theme:

```console
GET /faults?minimum=85.5   ->  200, three readings
GET /faults?minimum=warm   ->  422, {"type": "float_parsing", "loc": ["query", "minimum"]}
```

Note that it did convert `"85.5"`, which arrived as text on the wire. So the rule is not "it
refuses anything unfamiliar" — it converts where the whole string has exactly one reading, and
refuses where it would have to choose. `"85,5"` is refused; a human reads it as eighty-five and a
half, and guessing between `.` and `,` is the mistake the other five rows made.

**The refusal happens before your function.** `fault_list` was never entered, so inside it
`minimum` is a float and there is no second case — no `try`, no `isinstance`, no default on
failure, and no error message of your own to write and keep in step with a front end.

## Where the schemas live, and where they do not

The Pydantic models sit in `app.py`, next to the routes, and not in `sensorreport`. A schema
belongs at the **boundary** of a program, and `sensorreport` has no boundary: it is the analysis,
and modules 24 and 25 have to keep using it from a window and a terminal, neither of which has a
request body. That is also why `sensorreport` does not import pydantic — a dependency added there
would be inherited by all five modules of Part 5 for the benefit of one.

## Two checkers, and what each of them catches

Both mypy and Pydantic read the same annotation, at different times, and they do not agree:

| | mypy, before running | Pydantic, per request |
| --- | --- | --- |
| a route returning a `dict` where `-> Out` is annotated | **error** | passes; the dict is validated and filtered |
| a request with `minimum=warm` | cannot see it | **422**, field named |
| a response missing a field of its model | error, if the dict is literal | **500** `ResponseValidationError` |
| `-> Any` anywhere | silent by construction | nothing left to check |

The last row is the one to remember: `Any` switches off both of them at once.

## Bad input and bad output are not symmetric

- a bad **request** → **422**, with `loc` naming `query`/`path`/`body` and the field. The client
  can act on it, so it is told everything.
- a bad **response** → **500 Internal Server Error**, and nothing else. Measured. The client
  cannot act on it — it cannot supply your missing field — and the shape of your models is not
  its business. The traceback goes to your log, where it belongs.

Detail in an error message is not politeness. It is a function of who can fix the thing.

## Testing without a server

`TestClient` calls the application in this process. No port, no `uvicorn`, no waiting:

```python
from fastapi.testclient import TestClient

client = TestClient(app)
client.get("/summary/Hall").json()                  # {'location': 'Hall', ...}
client.post("/limit", json={"celsius": 90}).json()  # {'faults_at_this_limit': 2, ...}
```

Same shape as Flask's `test_client()` in module 21 and `AppTest` in module 22, for the same
reason: a test that needs a port fails when the port is busy.

One detail that matters when a route of yours raises: **`TestClient` re-raises the exception**
rather than turning it into a 500, so a test shows you the traceback.
`TestClient(app, raise_server_exceptions=False)` gives you the response a browser would get.
Both appear in exercise 04.

`import fastapi.testclient` prints a `StarletteDeprecationWarning` about `httpx`. It is
starlette's own note about its own dependency, it goes to stderr, and it changes nothing here.
The notebook silences it in its first cell so the output stays readable; the exercise files do
not, because reflexively silencing a warning you have not read is a worse habit than seeing one.

## What you can do afterwards

1. **say** what a `float` annotation on a query parameter actually does, and when in the request
   it does it;
2. **read** a 422 body — `loc`, `type`, `msg` — and say which of those a front end should use;
3. **write** a Pydantic model with bounds, and say what happens to a body that breaks one;
4. **say** what a return annotation does to a response, and what `Any` there costs;
5. **read** `/openapi.json`, and name two things it cannot tell you about this application;
6. **test** an application without starting a server, including a route that raises.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 23_fastapi`**
4. **`solutions/`** — last

## Flask, Streamlit or FastAPI

| | Flask (21) | Streamlit (22) | FastAPI (23) |
| --- | --- | --- | --- |
| the caller | a browser | a browser | a program |
| what comes out | your HTML | Streamlit's page | JSON against a schema |
| bad input | your `if`, your message | there is no input to be bad | 422, field named, before your code |
| the annotations | ignored | ignored | are the parser and the filter |
| documentation | you write it | not applicable | generated, at `/docs` |
| this application | ~70 lines plus 4 templates | ~90 lines, no templates | ~150 lines, no templates |

**The heuristic: who is the caller?** A person needs a page, and the page is the work. A program
needs a contract, and the contract is the work — which is why the module that serves programs is
the one where the type hints became load-bearing.

Module 24 leaves the web entirely. A tkinter program does not answer requests; it **waits**, in a
loop it does not own, and that is the whole difficulty.
