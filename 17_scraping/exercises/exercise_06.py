"""Exercise 06 -- robots.txt, read rather than guessed.

Read the server's `robots.txt` with the standard library and print six lines:

  1-4. for `/readings.html`, `/private/secret`, `/admin` and `/administration`:
       the path padded to 20 characters, then whether `*` may fetch it
  5.   whether `GreedyBot` may fetch `/readings.html`
  6.   the crawl delay for `*`

Expected output:

    /readings.html       True
    /private/secret      False
    /admin               False
    /administration      False
    False
    1

Hint: `RobotFileParser()`, then `set_url(...)`, then `read()`. `can_fetch(agent,
url)` wants a full URL, so `urljoin(base, path)`. Line 4 is the one to look at
twice -- `Disallow: /admin` matched something nobody wrote down.
"""

import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from server import serve  # noqa: E402

# TODO: read the rules inside `with serve() as base:`, then six prints
