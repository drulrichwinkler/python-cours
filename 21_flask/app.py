"""The Flask application this module builds up to.

Run it:

    uv run flask --app 21_flask/app run --debug

Then open http://127.0.0.1:5000/ in a browser. Ctrl+C stops it -- module 20.

Everything it knows about sensors comes from `sensorreport`, the package all five
modules of Part 5 share. This file is presentation and nothing else, which is what
makes the comparison with modules 22 to 25 mean anything.
"""

from flask import Flask, abort, render_template, request

from sensorreport import LIMIT, faults, load_readings, summarise

app = Flask(__name__)


@app.get("/")
def index():
    """The summary table, one row per location."""
    readings = load_readings()
    return render_template(
        "index.html",
        summaries=summarise(readings),
        faults=faults(readings),
        limit=LIMIT,
    )


@app.get("/location/<name>")
def location(name):
    """One location's readings. 404 when there is no such location."""
    readings = [r for r in load_readings() if r.location == name]
    if not readings:
        # abort raises, so nothing below it runs -- and Flask turns it into a
        # proper 404 response rather than a traceback.
        abort(404)
    return render_template("location.html", name=name, readings=readings, limit=LIMIT)


@app.get("/search")
def search():
    """Readings above a limit given in the query string."""
    # type=float converts and gives None rather than raising on nonsense, which is
    # the behaviour you want for something a user typed.
    above = request.args.get("above", type=float)
    readings = load_readings()
    if above is None:
        selected = []
    else:
        selected = [r for r in readings if r.value is not None and r.value > above]
    return render_template("search.html", above=above, readings=selected)


@app.get("/api/summary")
def api_summary():
    """The same numbers as JSON. A dict return becomes an application/json response."""
    return {
        "limit": LIMIT,
        "locations": [
            {
                "location": s.location,
                "readings": s.readings,
                "usable": s.usable,
                "mean": s.mean,
                "highest": s.highest,
                "faults": s.faults,
            }
            for s in summarise(load_readings())
        ],
    }
