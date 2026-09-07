"""Solution 09 (bonus) -- The whole application, tested."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))  # so that `import app` finds it -- module 10

import app as flask_app  # noqa: E402


def describe(client, path):
    """status, content type and whether a marker is in the body."""
    response = client.get(path)
    return response.status_code, response.headers["Content-Type"].split(";")[0]


with flask_app.app.test_client() as client:
    for path in ("/", "/location/Hall", "/location/Nowhere", "/search?above=85", "/api/summary"):
        status, kind = describe(client, path)
        print(f"{path:22}{status:>5} {kind}")

    print()
    body = client.get("/").get_data(as_text=True)
    # The summary page links to each location by url_for, so the href is in the HTML.
    print("Test%20rig" in body, "Nowhere" in body)

    payload = client.get("/api/summary").get_json()
    print(payload["limit"], len(payload["locations"]))
    print([e["faults"] for e in payload["locations"]])
