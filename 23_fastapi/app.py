"""The FastAPI application this module builds up to.

Run it:

    uv run uvicorn 23_fastapi.app:app --reload

Then open <http://127.0.0.1:8000/docs> in a browser. Ctrl+C stops it -- module 20.

Everything it knows about sensors comes from `sensorreport`, the package all five
modules of Part 5 share, so the comparison with modules 21, 22, 24 and 25 is about
the frameworks and nothing else.

What is different here is where the type hints end up. In module 04 an annotation
was documentation that mypy read. In this file `minimum: float` is the code that
parses the query string, `body: LimitIn` is the code that validates the request
body, and `-> Summary` is the code that decides what goes out. Delete an
annotation and the behaviour changes.
"""

from dataclasses import asdict

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from sensorreport import LIMIT, faults, load_readings, summarise

app = FastAPI(
    title="Sensor readings",
    # This description is what shows up at the top of /docs. FastAPI builds that
    # page out of this file; there is no second document to keep in step.
    description="The readings of module 08, served as JSON.",
)


# ---------------------------------------------------------------------------
# The schemas. They live here, next to the routes, and not in `sensorreport`:
# a schema belongs at the boundary of the program, and `sensorreport` has no
# boundary -- it is the analysis, and it must stay usable from a window (24)
# and a terminal (25), neither of which has a request body.
# ---------------------------------------------------------------------------


class SummaryOut(BaseModel):
    """One location's numbers, as they go over the wire."""

    location: str
    readings: int
    usable: int
    mean: float | None
    highest: float | None
    faults: int


class ReadingOut(BaseModel):
    """One measurement, as it goes over the wire."""

    tag: str
    value: float | None
    location: str
    at: str


class LimitIn(BaseModel):
    """A proposed fault limit. `Field` is where the bounds go.

    `gt` and `lt` are not documentation. A body with `celsius: 500` never reaches
    the function below -- the client gets a 422 naming the field.
    """

    celsius: float = Field(gt=-50, lt=200, description="the new fault limit")
    note: str = "no reason given"


class LimitOut(BaseModel):
    """What accepting a limit answers with."""

    celsius: float
    note: str
    faults_at_this_limit: int


@app.get("/")
def index() -> dict[str, object]:
    """What this service offers. The locations come from the data, not a constant."""
    return {
        "limit": LIMIT,
        "locations": sorted({s.location for s in summarise(load_readings())}),
        "docs": "/docs",
    }


@app.get("/summary")
def all_summaries() -> list[SummaryOut]:
    """Every location, one entry each.

    The return annotation is the response schema. FastAPI reads `list[SummaryOut]`,
    validates what this function returns against it, and puts the schema in
    /openapi.json. There is no `response_model=` argument needed -- the annotation
    already said it.
    """
    # asdict, not vars: `Summary` is a slots dataclass (module 12), so it has no
    # __dict__ for vars() to return. asdict walks the declared fields instead.
    return [SummaryOut(**asdict(s)) for s in summarise(load_readings())]


@app.get("/summary/{location}")
def one_summary(location: str) -> SummaryOut:
    """One location. 404 when there is no such location.

    `location: str` names a segment of the path. The name in the decorator and the
    name of the parameter have to match -- that is how FastAPI connects them.
    """
    for summary in summarise(load_readings()):
        if summary.location == location:
            return SummaryOut(**asdict(summary))
    # HTTPException raises, so nothing below it runs, and FastAPI turns it into a
    # response with this status and body rather than a traceback -- module 21's
    # `abort`, with a message.
    raise HTTPException(status_code=404, detail=f"no location {location!r}")


@app.get("/faults")
def fault_list(
    minimum: float = Query(default=LIMIT, ge=-50, le=200, description="only readings above this"),
) -> list[ReadingOut]:
    """The readings above `minimum`, worst first.

    `minimum: float` with a default makes it an optional query parameter:
    /faults and /faults?minimum=20 both work, /faults?minimum=warm does not.

    `Query(...)` sits where the default goes, and it is not one. It is a metadata
    object FastAPI reads while it builds the route and then removes -- the actual
    default is the `default=` inside it. In this body `minimum` is a float, never a
    `Query`.
    """
    above = [r for r in load_readings() if r.value is not None and r.value > minimum]
    above.sort(key=lambda r: r.value or 0.0, reverse=True)
    return [ReadingOut(tag=r.tag, value=r.value, location=r.location, at=r.at) for r in above]


@app.post("/limit")
def propose_limit(body: LimitIn) -> LimitOut:
    """Count the faults a proposed limit would produce.

    A parameter annotated with a Pydantic model is the request body. Nothing else
    in the signature says so -- the type does.
    """
    above = [r for r in load_readings() if r.value is not None and r.value > body.celsius]
    return LimitOut(celsius=body.celsius, note=body.note, faults_at_this_limit=len(above))


@app.get("/current-faults")
def current_faults() -> list[ReadingOut]:
    """The faults at the limit `sensorreport` ships with -- the same three as module 21."""
    return [
        ReadingOut(tag=r.tag, value=r.value, location=r.location, at=r.at)
        for r in faults(load_readings())
    ]
