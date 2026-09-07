"""Solution 03 -- Repair three views."""

from flask import Flask, abort, request

from sensorreport import load_readings, summarise

app = Flask(__name__)


@app.get("/reading/<int:number>")
def reading(number):
    # <int:number> converts, so `number` is already an int. int(number) worked but
    # said the opposite of what the route does; and a path that is not digits never
    # reaches the view at all -- it is a 404, because no route matched.
    return {"number": number, "type": type(number).__name__}


@app.get("/search")
def search():
    # type=float gives None rather than raising on something a person typed, so the
    # view has to handle None. Without that, /search with no argument was a 500.
    above = request.args.get("above", type=float)
    if above is None:
        return {"above": None, "found": 0}
    readings = [r for r in load_readings() if r.value is not None and r.value > above]
    return {"above": above, "found": len(readings)}


@app.get("/location/<name>")
def location(name):
    known = {s.location for s in summarise(load_readings())}
    if name not in known:
        # abort raises, so nothing below runs, and Flask makes a real 404 out of it
        # instead of returning an empty page with status 200.
        abort(404)
    return {"location": name}


with app.test_client() as client:
    print(client.get("/reading/5").get_json())
    print(client.get("/reading/abc").status_code)
    print(client.get("/search").get_json())
    print(client.get("/search?above=85").get_json())
    print(client.get("/search?above=lots").get_json())
    print(client.get("/location/Hall").status_code, client.get("/location/Nowhere").status_code)
