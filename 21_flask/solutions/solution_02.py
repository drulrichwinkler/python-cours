"""Solution 02 -- Predict what Flask does.

content type     is text/html for a returned str and application/json for a
                 returned dict. Flask decides from the type, which is what makes a
                 small JSON endpoint two lines -- and module 23 is what you reach
                 for when the API is the point rather than an afterthought.
<int:number>     converts, so the view receives an int rather than a str. A path
                 that is not digits does not reach the view at all: no route
                 matched, so it is a 404. Better than a ValueError inside a view,
                 and worth choosing deliberately.
query string     is text. 'above=91.5' arrives as the string '91.5', and
                 type=float converts it. A value that will not convert gives None
                 rather than raising -- right for something a person typed, and a
                 case the view has to handle. No parameter at all is None too, so
                 those two look identical from inside.
Jinja2           escapes by default: '<b>x</b>' becomes '&lt;b&gt;x&lt;/b&gt;' and
                 lands in the page as text. |safe turns that off and the browser
                 treats it as markup -- which for anything a user supplied is
                 cross-site scripting, and the same shape as module 19's SQL
                 injection: text from outside became syntax on the inside.
|default('--')   gives 'None', not '--'. The filter replaces an UNDEFINED value,
                 and None is defined. The test that works is
                 {{ v if v is not none else '--' }} -- which matters here, because
                 a mean over no readings is None.
url_for          builds the path from the route, and an argument the route has no
                 placeholder for becomes a query parameter. It takes the name of
                 the VIEW FUNCTION, so the URL is free to change.
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
    assert client.get("/text").headers["Content-Type"].split(";")[0] == "text/html"
    assert client.get("/json").headers["Content-Type"].split(";")[0] == "application/json"

    assert client.get("/reading/5").get_json()["type"] == "int"

    assert client.get("/reading/abc").status_code == 404

    assert client.get("/search?above=91.5").get_json() == {"raw": "91.5", "converted": 91.5}

    assert client.get("/search?above=lots").get_json()["converted"] is None

    assert client.get("/search").get_json()["raw"] is None


with app.app_context():
    assert render_template_string("{{ t }}", t="<b>x</b>") == "&lt;b&gt;x&lt;/b&gt;"
    assert render_template_string("{{ t|safe }}", t="<b>x</b>") == "<b>x</b>"

    assert render_template_string("{{ v|default('--') }}", v=None) == "None"
    assert render_template_string("{{ v if v is not none else '--' }}", v=None) == "--"


with app.test_request_context():
    assert url_for("reading", number=5) == "/reading/5"
    assert url_for("search", above=85) == "/search?above=85"
