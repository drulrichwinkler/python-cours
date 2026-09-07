"""Solution 06 -- url_for, and never joining strings."""

from flask import Flask, url_for

app = Flask(__name__)


@app.get("/location/<name>")
def location(name):
    return name


@app.get("/search")
def search():
    return "search"


with app.test_request_context():
    # url_for names the VIEW FUNCTION, so the path is free to change.
    print(url_for("location", name="Hall"))
    print(url_for("location", name="Test rig"))  # the space is encoded for you
    # An argument the route has no placeholder for becomes a query parameter.
    print(url_for("search", above=85))
    print(url_for("search", above=85, unit="C"))
