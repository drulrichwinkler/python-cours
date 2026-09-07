"""Solution 04 -- The encoding nobody declared."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

import requests  # noqa: E402
from server import serve  # noqa: E402

with serve() as base:
    labelled = requests.get(f"{base}/readings.csv", timeout=5)
    unlabelled = requests.get(f"{base}/unlabelled.csv", timeout=5)

    # The same bytes on both paths.
    print(labelled.content == unlabelled.content)
    print(labelled.encoding, unlabelled.encoding)
    print(repr(unlabelled.text.splitlines()[1]))

    # Saying it yourself, before .text is read.
    unlabelled.encoding = "utf-8"
    print(repr(unlabelled.text.splitlines()[1]))

    # Or skipping .text entirely, which is the honest version of the same thing.
    print(repr(unlabelled.content.decode("utf-8").splitlines()[1]))
