"""Exercise 02 -- Predict what HTTP does.

Replace each `...` with the value you expect, then run the file.

    uv run 16_http/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    # TODO: the same bytes on two routes. What does each one claim its encoding is?
    labelled = requests.get(f"{base}/readings.csv", timeout=5)
    unlabelled = requests.get(f"{base}/unlabelled.csv", timeout=5)

    assert (labelled.content == unlabelled.content) == ...
    assert labelled.encoding == ...
    assert unlabelled.encoding == ...

    # TODO: and what comes out of .text on the unlabelled one?
    assert unlabelled.text.splitlines()[1] == ...

    # TODO: does a 404 raise?
    missing = requests.get(f"{base}/missing", timeout=5)

    assert missing.status_code == ...
    assert missing.ok == ...

    # TODO: what turns it into an exception, and which one?
    try:
        missing.raise_for_status()
        raised = "nothing"
    except Exception as err:
        raised = type(err).__name__

    assert raised == ...

    # TODO: .json() on a body that is not JSON
    csv_response = requests.get(f"{base}/readings.csv", timeout=5)
    try:
        csv_response.json()
        parsed = "parsed"
    except Exception as err:
        parsed = type(err).__name__

    assert parsed == ...

    # TODO: JSON carries types; a CSV does not
    payload = requests.get(f"{base}/readings.json", timeout=5).json()

    assert type(payload).__name__ == ...
    assert type(payload["readings"][0]["value"]).__name__ == ...

    # TODO: headers are looked up without regard to case
    assert (labelled.headers["content-type"] == labelled.headers["Content-Type"]) == ...


# TODO: nobody listening on port 1
try:
    requests.get("http://127.0.0.1:1/nothing", timeout=0.5)
    reached = "answered"
except requests.RequestException as err:
    reached = type(err).__name__

assert reached == ...
