"""Solution 06 -- robots.txt, read rather than guessed."""

import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from server import serve  # noqa: E402

with serve() as base:
    rules = RobotFileParser()
    rules.set_url(f"{base}/robots.txt")
    rules.read()

    for path in ("/readings.html", "/private/secret", "/admin", "/administration"):
        # Disallow matches by PREFIX, not by path segment, so /administration is
        # forbidden by a rule that says /admin.
        print(f"{path:20} {rules.can_fetch('*', urljoin(base, path))}")

    print(rules.can_fetch("GreedyBot", urljoin(base, "/readings.html")))
    print(rules.crawl_delay("*"))
