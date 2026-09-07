"""Exercise 03 -- Repair three views.

Run it. Two of the three raise, and the third returns 200 for something that does not
exist.

Expected output:

    {'number': 5, 'type': 'int'}
    404
    {'above': None, 'found': 0}
    {'above': 85.0, 'found': 3}
    {'above': None, 'found': 0}
    200 404

Hint: `<int:number>` has already converted, so calling `int()` on it says the
opposite of what the route does. `request.args.get(..., type=float)` gives `None`
rather than raising, so the view has to handle `None` -- that is the 500 on
`/search`. And a view that cannot answer says so: `abort(404)` raises, so nothing
after it runs.
"""

from flask import Flask, request

from sensorreport import load_readings, summarise

app = Flask(__name__)


@app.get("/reading/<int:number>")
def reading(number):
    return {"number": int(number), "type": "str"}  # TODO: two things wrong here


@app.get("/search")
def search():
    above = request.args.get("above", type=float)
    # TODO: what if `above` is None?
    readings = [r for r in load_readings() if r.value is not None and r.value > above]
    return {"above": above, "found": len(readings)}


@app.get("/location/<name>")
def location(name):
    known = {s.location for s in summarise(load_readings())}
    # TODO: an unknown location should not be a 200
    return {"location": name}


with app.test_client() as client:
    print(client.get("/reading/5").get_json())
    print(client.get("/reading/abc").status_code)
    print(client.get("/search").get_json())
    print(client.get("/search?above=85").get_json())
    print(client.get("/search?above=lots").get_json())
    print(client.get("/location/Hall").status_code, client.get("/location/Nowhere").status_code)
