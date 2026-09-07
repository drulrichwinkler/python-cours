"""Solution 01 -- A route is a decorated function."""

from flask import Flask

app = Flask(__name__)


# @app.get is a decorator: it registers the function and hands it back unchanged.
# Module 14, in the place it was promised.
@app.get("/")
def index():
    return "<h1>Sensors</h1>"


@app.get("/json")
def as_json():
    return {"tag": "TH-04", "value": 91.0}  # a dict becomes application/json


@app.get("/created")
def with_status():
    return "made it", 201  # a tuple is body and status code


with app.test_client() as client:  # no port, no process, no app.run()
    for path in ("/", "/json", "/created"):
        response = client.get(path)
        print(response.status_code, response.headers["Content-Type"].split(";")[0])

    print(client.get("/").get_data(as_text=True))
    print(client.get("/json").get_json())
    print(client.get("/nowhere").status_code)
