# Solution 08 — The document, and where it stops

**a) Why the 404 is absent and the 422 is present**

FastAPI builds `/openapi.json` by **inspecting the signature** of every route
function — the parameter names, their annotations, their defaults, and the return
annotation. That is a static reading of the interface. It never runs the function and
it does not read its body.

- The **422 is there** because it follows from the signature alone. `location: str`
  is a path parameter and `minimum: float` a query parameter, and any parameter that
  has to be parsed from text is a parameter that can fail to parse. FastAPI knows it
  will answer a parse failure with a 422, so it documents one. Nobody wrote it because
  nobody had to: it is a consequence of the annotations, and it is right for every
  route that has parameters.
- The **404 is absent** because it is `raise HTTPException(status_code=404, ...)`
  inside the function body, reached by a `for` loop over data that is read at request
  time. Nothing in the signature implies it. To know that this route can 404, FastAPI
  would have to read and understand the body — and if it could do that, it could also
  be wrong about it.

The honest summary: the generated part of the document covers exactly what the type
system knows. Everything the program decides at runtime is outside it.

**b) What is now true of the hand-written 404**

It **can fall behind the code.** The 422 cannot: it is derived from the same
annotations that produce the behaviour, so if the annotation changes the documentation
changes with it, in the same commit, without anybody remembering. The 404 in
`responses={...}` is a second statement of the same fact, and two statements of one
fact can disagree. Delete the `raise` and the document still promises a 404. Add a 409
next year and the document will not mention it.

What that means for a half-generated document: **the generated half is a
specification and the written half is a comment.** They look identical to a reader and
to a code generator, which is the trap — a client generated from this document treats
both with the same confidence. So the written half needs what any comment needs: a
test that fails when it goes stale. Here that means a test asserting the route really
does answer 404 for an unknown location, which is a thing you should have anyway, and
which is what makes the `responses={...}` entry safe to trust.

**c) Two ways a generated document can still be wrong**

1. **It is silent about what the annotations do not describe.** The 404 above is the
   small case. The larger one in this application: `POST /limit` is documented as
   taking a number between -50 and 200 and answering with a count. Nothing says
   whether it *changes* anything. It does not — it only counts — but a caller reading
   the document cannot tell that from a route that would, and `POST` suggests it
   might. Rate limits, authentication, ordering guarantees and idempotence all live in
   the same blind spot.
2. **It is accurate about types and wrong about meaning.** `SummaryOut.mean` is
   documented as `number | null`, which is true. It does not say that `null` means
   "no usable reading here", nor that the mean is over the usable readings only and
   not over `readings`. A client that divides by `readings` gets a number that is
   wrong and validates perfectly. The schema constrains the shape of the value; the
   meaning of the value is not a thing a schema can hold, and `description=` is
   where it has to go instead.

**d) The annotation is now load-bearing**

Until this module, deleting an annotation changed nothing at runtime: the program ran
identically, and only mypy noticed. `-> Out` broke that. The three measurements show
it plainly — the same function body, three annotations, and `secret` reaches the
client in two of the three cases. The annotation is not a description of what the
function returns; **it is the code that decides what leaves the process.**

Two consequences.

First, the review question changes. A widened annotation used to be a documentation
defect. Here `-> dict[str, Any]` is a data leak with a plausible cover story, and it
is invisible in a diff that touches one line of a signature. Second — from the
hint — **mypy would have accepted all three without a word.** `Any` is accepted
everywhere by construction; that is what it is for. So the type checker is no longer a
guard on this property, and writing `Any` to silence mypy silences the one tool that
was watching while also switching off the filter. The habit was always a bad trade; in
this file it is a security bug.

The rule that follows: on a route, the return annotation is production code. Change it
the way you would change a `SELECT` list, not the way you would change a docstring.

**e) Flask, Streamlit or FastAPI**

1. **the test rig's controller fetches the limit every thirty seconds** →
   **FastAPI.** The caller is a program. It wants JSON, a schema it can generate a
   client from, and a status code it can branch on; it has no use for HTML and no
   browser to render it.
2. **your team looks at last night's readings and changes the limit** →
   **Streamlit.** The caller is a colleague sitting next to you, the point is the
   data, and a slider and a table are the whole requirement. An afternoon's work.
3. **a customer's purchasing system reads your fault list** → **FastAPI** would be the
   reflex, and this is where the rule "pick FastAPI exactly once" bites: it is the
   same shape as case 1, so one of the two has to go elsewhere, and the honest
   distinction is not the format but the audience. An external customer needs
   versioning, authentication, a stable contract and a document you are willing to be
   held to — that is a product, and Flask (or FastAPI behind a gateway that provides
   those) is where it belongs. Case 1 is an internal caller on your own network, which
   is the plain FastAPI case.
4. **a colleague in another department wants a page to bookmark and show their
   manager** → **Flask.** "Bookmark" is a URL and "show their manager" is a layout,
   and those are precisely the two things module 22 named as Streamlit's limits.

The point of the exercise is not the four answers. It is that **the caller decides**,
and the caller is a person in two of these and a program in the other two.
