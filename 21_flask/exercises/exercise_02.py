"""Exercise 02 -- Predict what Flask does.

Replace each `...` with the value you expect, then run the file.

    uv run 21_flask/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

from flask import Flask, render_template_string, request, url_for

app = Flask(__name__)


@app.get("/text")
def as_text():
    return "just words"


@app.get("/json")
def as_json():
    return {"tag": "TH-04"}


@app.get("/reading/<int:number>")
def reading(number):
    return {"type": type(number).__name__}


@app.get("/search")
def search():
    return {
        "raw": request.args.get("above"),
        "converted": request.args.get("above", type=float),
    }


with app.test_client() as client:
    # TODO: what content type does each return value produce?
    assert client.get("/text").headers["Content-Type"].split(";")[0] == ...
    assert client.get("/json").headers["Content-Type"].split(";")[0] == ...

    # TODO: <int:number> converts. To what?
    assert client.get("/reading/5").get_json()["type"] == ...

    # TODO: and a path that does not match the converter
    assert client.get("/reading/abc").status_code == ...

    # TODO: everything from a query string starts as a string
    assert client.get("/search?above=91.5").get_json() == ...

    # TODO: a value that will not convert -- does it raise?
    assert client.get("/search?above=lots").get_json()["converted"] is ...

    # TODO: and no parameter at all
    assert client.get("/search").get_json()["raw"] is ...


with app.app_context():
    # TODO: what Jinja2 does to markup in a variable
    assert render_template_string("{{ t }}", t="<b>x</b>") == ...
    assert render_template_string("{{ t|safe }}", t="<b>x</b>") == ...

    # TODO: the default filter and None
    assert render_template_string("{{ v|default('--') }}", v=None) == ...
    assert render_template_string("{{ v if v is not none else '--' }}", v=None) == ...


with app.test_request_context():
    # TODO: url_for encodes, and puts extras in the query string
    assert url_for("reading", number=5) == ...
    assert url_for("search", above=85) == ...
