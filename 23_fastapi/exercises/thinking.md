# Module 23 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 23_fastapi`.

---

## Exercise 07 — The first tool that refuses

Five times in this course a tool has done something rather than fail:

| module | the tool | what it does instead of failing |
| --- | --- | --- |
| 08 | `latin-1` | decodes any bytes; gives you `Â°C` |
| 16 | `requests` with no charset | falls back to Latin-1; the same `Â°C` |
| 17 | `html.parser` | repairs; four cells where there are two |
| 18 | `read_csv` | picks a type from the data; `.sum()` concatenates |
| 19 | SQLite | stores what it was given; `REAL` holds `'kaputt'` |

This module is the other case. Two measurements from `app.py`:

```console
GET /faults?minimum=85.5   ->  200, three readings
GET /faults?minimum=warm   ->  422, {"type": "float_parsing", "loc": ["query", "minimum"]}
```

a) `"85.5"` is a string on the wire, and it came out as the float `85.5`. `"warm"` is
   also a string, and it was refused. State the rule that distinguishes the two cases
   precisely enough that somebody could implement it. "It converts when it can" is
   not precise enough — say what "can" means here.
b) In the 422 case, `fault_list` never ran. Say where the refusal happened relative to
   your function, and what that buys you inside the function body.
c) A 422 is not a 400 and not a 500. All three mean "this did not work". Say what
   each of the three tells the client about *whose* problem it is and what to do next,
   and place these four events in the right one:
   1. `minimum=warm`;
   2. a location that does not exist;
   3. the readings file has been deleted;
   4. a valid request that your function answers with a field missing from the
      response model.
d) A colleague finds the 422 responses inconvenient, because their front end has to
   handle them. So they change the parameter to `minimum: str` and write
   `float(minimum) if minimum.replace(".", "").isdigit() else 85.0`. Name three
   separate things that are now worse, and say which of the three you would raise
   first in a review.

> **Hint on (a):** what would `float("85,5")` do, and what would a client that sent
> that be entitled to assume?
> **Hint on (c):** measured — case 4 gives the client `500 Internal Server Error` and
> nothing else. Why is that the correct amount of information to hand out?
> **Hint on (d):** one of the three is about the client, one about the code, and one
> about the document in exercise 06.

**Check yourself:** your answer to (a) has to name a string that is a valid number for
a human and not for this parameter.

---

## Exercise 08 — The document, and where it stops

Exercise 06 read `/openapi.json` and found that `GET /summary/{location}` documents a
200 and a 422 — and not the 404 that `one_summary` raises three lines further down.

a) Say why the 404 is missing, in terms of what FastAPI can and cannot see when it
   builds the document. Then say why the 422 *is* there without anybody writing it.
b) `responses={404: {"description": "no such location"}}` on the decorator puts it in
   (measured: the statuses become `['200', '404', '422']`). So the gap is closable by
   hand. Name what is now true of that 404 that was not true of the 422, and say what
   that means for a document that is half generated and half written.
c) A generated document cannot fall behind the code. Name two ways it can still be
   wrong, and give a concrete example of each from this application.
d) Three measurements of the same route, differing only in the return annotation:

   | annotation | what came out |
   | --- | --- |
   | `-> Out` | `{'tag': 'TH-04', 'value': 93.5}` |
   | `-> dict[str, Any]` | `{'tag': 'TH-04', 'value': 93.5, 'secret': 'internal note'}` |
   | none at all | the same three keys, and the documented schema is `{}` |

   Until this module an annotation could be deleted without changing what the program
   did. Say what has changed about that, and what it means for the habit of writing
   `Any` to make a type checker stop complaining.
e) Pick between Flask (21), Streamlit (22) and FastAPI (23) for each, one sentence of
   defence each:
   1. the test rig's controller has to fetch the current limit every thirty seconds;
   2. your team wants to look at last night's readings and change the limit;
   3. a customer's purchasing system needs to read your fault list;
   4. a colleague in another department wants a page they can bookmark and show their
      manager.

> **Hint on (c):** one of the two ways involves a route that does something the
> annotations do not describe; the other involves a schema that is accurate about
> types and wrong about meaning.
> **Hint on (d):** which of the three annotations would mypy have accepted without a
> word?

**Check yourself:** your answer to (e) has to pick FastAPI exactly once, and the
sentence has to say what the *caller* is.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
