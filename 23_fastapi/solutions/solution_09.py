"""Solution 09 -- One route, everything at once."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI, HTTPException, Query  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from sensorreport import load_readings  # noqa: E402

app = FastAPI()


class LocationOut(BaseModel):
    """What one location's answer looks like on the wire."""

    name: str
    above: int
    worst: float | None


@app.get("/location/{name}")
def location(
    name: str,
    minimum: float = Query(default=85.0, ge=-50),
) -> LocationOut:
    """One location, counted against a limit the caller may choose."""
    here = [r for r in load_readings() if r.location == name]
    if not here:
        raise HTTPException(status_code=404, detail=f"no location {name!r}")

    usable = [r.value for r in here if r.value is not None]
    return LocationOut(
        name=name,
        above=sum(1 for v in usable if v > minimum),
        # max() over an empty sequence raises, so the empty case is decided first.
        worst=max(usable) if usable else None,
    )


client = TestClient(app)

for path, params in [
    ("/location/Test rig", None),
    ("/location/Test rig", {"minimum": 0}),
    ("/location/Hall", None),
    ("/location/Keller", None),
    ("/location/Hall", {"minimum": -99}),
]:
    r = client.get(path, params=params)
    if r.status_code == 200:
        body = r.json()
        print(r.status_code, f"{body['name']} above={body['above']} worst={body['worst']}")
    elif r.status_code == 404:
        print(r.status_code, r.json()["detail"])
    else:
        print(r.status_code, r.json()["detail"][0]["type"])
