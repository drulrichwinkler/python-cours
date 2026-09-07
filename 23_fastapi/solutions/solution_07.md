# Solution 07 — The first tool that refuses

**a) The rule that separates `"85.5"` from `"warm"`**

There are **two** checks, in order, and only the first is a conversion. Measured
against `/faults?minimum=...`:

| sent | result |
| --- | --- |
| `85.5` | 200 |
| `1e2`, `85.`, `+85.5`, `-20` | 200 — same as `float()` |
| `" 85.5 "` (with spaces) | 200 — surrounding whitespace is stripped |
| `85.5 C` | 422 `float_parsing` |
| `85,5` | 422 `float_parsing` |
| `8.5.3`, `0x50`, `""` | 422 `float_parsing` |
| `inf`, `nan` | 422 **`less_than_equal`** |

**The conversion rule:** the text is accepted when, after stripping surrounding
whitespace, **the whole of it is a Python float literal** — and refused otherwise.
Two halves matter, and both are load-bearing:

- *the whole of it.* Not a prefix. `"85.5 C"` is refused, even though a lenient parser
  could take the 85.5 and drop the ` C`. There is no partial success, which is why
  `"8.5.3"` is refused rather than read as 8.5.
- *by float syntax, not by locale.* `"85,5"` is refused. A German-speaking colleague
  reads that string as eighty-five and a half; this parameter will not, because a
  parser that guessed which of `.` and `,` was the decimal separator would silently
  turn `85,5` into either 85.5 or 855 depending on a setting nobody set.

The distinguishing property is therefore not "it converts when it can" but
**a single unambiguous reading of the entire string**. Where two readings exist, or
where something would have to be discarded, it refuses. That is the criterion the five
rows of the table failed: `latin-1` had a reading for every byte sequence, so it never
refused; `read_csv` had a reading for a column containing `n/a`, so it picked `str` and
moved on. Having *a* reading is not the same as having *one*.

**The second check is the bound, and `inf` shows it is separate.** `"inf"` and `"nan"`
are valid float literals — `float("inf")` works — so the conversion succeeds and they
are stopped by `le=200` instead. You can see it in the `type` field: `less_than_equal`,
not `float_parsing`. Note which value that catches: `nan`, the one module 18 warned
about, where `nan == nan` is false and every comparison against it is false. It is
refused here for exactly that reason — `nan <= 200` is false — and a route that took
`minimum: float` with no bound at all would have accepted it and then counted zero
faults out of fifty, quietly.

**b) Where the refusal happened**

Before the function. FastAPI resolves and validates every parameter first, and calls
`fault_list` only if all of them came out. In the 422 case the body of the function
was never entered — which is why the log has no traceback from it and why nothing
half-happened.

What that buys inside the body: **`minimum` is a float, and there is no other case.**
No `try`, no `isinstance`, no default-on-failure branch, no error message of my own to
write, translate and keep in step with the front end. The first line of the function
can be the actual work. That is the difference between validating at the boundary and
validating everywhere, and it is why the boundary is worth having a schema at.

**c) 422, 400 and 500**

- **422** — *your request was understood and is not acceptable.* The syntax parsed,
  the semantics did not. Whose problem: the client's. What to do: fix the named field
  and send it again. It is safe to retry after a change, and pointless to retry
  unchanged.
- **400** — *your request was not understood.* Malformed at a lower level: broken
  JSON, a header that is not a header. Whose problem: the client's, again, but there
  is no field to name because parsing did not get that far.
- **500** — *the request was fine and I failed.* Whose problem: the server's. What to
  do: nothing the client can do; retry later at most, and tell somebody.

Placing the four:

1. `minimum=warm` → **422**. Well-formed HTTP, well-formed query string, a value the
   schema rejects, and the response names the field.
2. a location that does not exist → **404**, not any of the three. The request is
   valid and the server worked correctly; the thing asked for is not there. That is
   why it is `HTTPException(404)` in the code and not a validation error: no
   annotation could have known which locations exist.
3. the readings file has been deleted → **500**. `load_readings` raises,
   the client did nothing wrong, and there is nothing it can change.
4. a response missing a field of its model → **500**. Measured: the client gets
   `500 Internal Server Error` and no detail at all.

On the hint for (c): that is the right amount of information because the client has no
move. It cannot add the missing field. Naming which field of which internal model was
absent would tell a stranger the shape of your models and nothing they could act on —
the traceback belongs in your log, and it is there. Note the asymmetry that follows:
**the 422 is detailed because the client can act on it, and the 500 is silent because
it cannot.** Detail in an error message is not politeness; it is a function of who can
fix the thing.

**d) The colleague's `minimum: str` and the hand-written guard**

Three separate things are worse:

1. **The client is now lied to.** `minimum=warm` gets a 200 and a fault count computed
   against 85.0 — a plausible answer to a question nobody asked. The front end no
   longer has to handle a 422, which was the goal; it also can no longer tell a typo
   from a real result. This is exactly the failure mode of the five rows in the table,
   reintroduced by hand.
2. **The guard is wrong in both directions, and measured.**
   `minimum.replace(".", "").isdigit()` is `True` for `"8.5.3"` and for `"85."`, and
   `False` for `"-20"` and for `"1e2"`. So it rejects valid input — a negative limit
   is legitimate here, the bound in `app.py` is `ge=-50` — and it admits `"8.5.3"`,
   on which the `float()` behind it raises. The guard does not even prevent the 500 it
   was written to prevent; it only narrows the set of inputs that cause one, which is
   the worst of the three possible outcomes because it makes the bug rare instead of
   absent. And nothing here checks the bounds at all, so `nan` now gets through.
3. **The document now describes something else.** `/openapi.json` says `minimum` is a
   string with no constraints. Anybody generating a client from it — which is the
   reason to have the document — generates one that sends strings and never learns
   about the bounds. The one artefact that could not fall behind the code has been
   made accurate about a signature that no longer means what it says.

Which to raise first in a review: **the first.** Two and three are costs paid by
developers, and a developer can read the code. One is paid by whoever gets a wrong
number and does not know it — and unlike the other two, it produces no symptom at the
moment it goes wrong. A branch that is subtly incorrect gets found; an answer that is
confidently wrong does not.
