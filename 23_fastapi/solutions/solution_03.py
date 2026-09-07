"""Solution 03 -- Repair: parsing by hand."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from sensorreport import load_readings  # noqa: E402

app = FastAPI()


@app.get("/above")
def above(minimum: float = 85.0):
    """Count the readings above `minimum`.

    The annotation replaced the conversion. `minimum` arrives as a float or the
    function is never called -- there is no third case to handle, and therefore no
    `try` block and no error message of my own to write and translate.
    """
    return {"count": sum(1 for r in load_readings() if r.value is not None and r.value > minimum)}


client = TestClient(app)

first = client.get("/above")
print(first.status_code, first.json()["count"])

second = client.get("/above", params={"minimum": "warm"})
problem = second.json()["detail"][0]
print(second.status_code, problem["loc"][0], problem["loc"][1], problem["type"])
