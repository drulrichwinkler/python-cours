"""Solution 02 -- Predict what HTTP does.

encoding         is 'utf-8' where the header says charset=utf-8 and 'ISO-8859-1'
                 where it says only text/csv -- for the same bytes. requests
                 follows a rule from an obsolete specification: a text/* response
                 with no charset is Latin-1. Which, as module 08 established,
                 decodes any byte sequence and therefore never fails, so .text
                 gives 'TH-01;21.7;Â°C' and nothing raises.
missing.ok       is False and the status is 404 -- but get() did not raise. A
                 status code IS an answer; the request succeeded. Only
                 raise_for_status() turns 4xx and 5xx into an HTTPError, and it
                 has to be called.
.json() on CSV   raises JSONDecodeError. The usual cause is a server that returned
                 an error page and a caller who did not look at the status first --
                 which is why raise_for_status belongs BEFORE the parse.
payload          is a dict, and the value inside is a float. JSON carries types
                 where a CSV carries text, which is the practical reason an API
                 speaks JSON and a file does not.
headers          are case-insensitive: response.headers is a CaseInsensitiveDict,
                 because HTTP header names are.
port 1           gives ConnectionError -- nobody answered. That is the other kind
                 of failure, and it is a RequestException like HTTPError is, so
                 one except clause can catch both if that is what you want.
"""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    labelled = requests.get(f"{base}/readings.csv", timeout=5)
    unlabelled = requests.get(f"{base}/unlabelled.csv", timeout=5)

    assert (labelled.content == unlabelled.content) is True
    assert labelled.encoding == "utf-8"
    assert unlabelled.encoding == "ISO-8859-1"

    assert unlabelled.text.splitlines()[1] == "TH-01;21.7;Â°C"

    missing = requests.get(f"{base}/missing", timeout=5)

    assert missing.status_code == 404
    assert missing.ok is False

    try:
        missing.raise_for_status()
        raised = "nothing"
    except Exception as err:
        raised = type(err).__name__

    assert raised == "HTTPError"

    csv_response = requests.get(f"{base}/readings.csv", timeout=5)
    try:
        csv_response.json()
        parsed = "parsed"
    except Exception as err:
        parsed = type(err).__name__

    assert parsed == "JSONDecodeError"

    payload = requests.get(f"{base}/readings.json", timeout=5).json()

    assert type(payload).__name__ == "dict"
    assert type(payload["readings"][0]["value"]).__name__ == "float"

    assert (labelled.headers["content-type"] == labelled.headers["Content-Type"]) is True


try:
    requests.get("http://127.0.0.1:1/nothing", timeout=0.5)
    reached = "answered"
except requests.RequestException as err:
    reached = type(err).__name__

assert reached == "ConnectionError"
