"""A tiny HTTP server that serves HTML, so this module needs no network.

The same shape as module 16's server -- a context manager that starts on a free
port and shuts down afterwards -- with pages instead of data files.

    with serve() as base:
        html = requests.get(f"{base}/readings.html", timeout=5).text

The routes:

    /robots.txt        the rules a polite client reads first
    /readings.html     the table, well formed
    /page2.html        the second page, linked from the first
    /sloppy.html       the same table with unclosed tags -- section 5
    /private/secret    exists, and robots.txt says not to fetch it
"""

import contextlib
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, HTTPServer

ROBOTS = """User-agent: *
Crawl-delay: 1
Disallow: /private/
Disallow: /admin

User-agent: GreedyBot
Disallow: /
"""

READINGS = """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Sensors &mdash; Halle 3</title></head>
<body>
  <h1>Station Halle 3</h1>
  <table id="readings" class="data">
    <tr><th>Tag</th><th>Value</th><th>Unit</th></tr>
    <tr class="row"><td class="tag">TH-01</td><td class="value">21.7</td><td>&deg;C</td></tr>
    <tr class="row fault"><td class="tag">TH-04</td><td class="value">91.0</td><td>&deg;C</td></tr>
    <tr class="row"><td class="tag">TH-09</td><td class="value">23.1</td><td>&deg;C</td></tr>
  </table>
  <a class="next" href="/page2.html">next page</a>
</body>
</html>
"""

PAGE2 = """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Sensors &mdash; Halle 4</title></head>
<body>
  <h1>Station Halle 4</h1>
  <table id="readings" class="data">
    <tr><th>Tag</th><th>Value</th><th>Unit</th></tr>
    <tr class="row fault"><td class="tag">TH-02</td><td class="value">88.4</td><td>&deg;C</td></tr>
    <tr class="row"><td class="tag">TH-07</td><td class="value">22.8</td><td>&deg;C</td></tr>
  </table>
</body>
</html>
"""

# The same three readings, with the closing tags left out -- which is legal HTML and
# is what a great many real pages look like. Section 5 is about what the parser makes
# of it, and the answer is not what you would hope.
SLOPPY = """<!doctype html>
<html><body>
<table id="readings">
  <tr><th>Tag<th>Value
  <tr class="row"><td class="tag">TH-01<td class="value">21.7
  <tr class="row"><td class="tag">TH-04<td class="value">91.0
</table>
</body></html>
"""


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, *args: object) -> None:
        pass

    def _send(
        self, status: int, body: str = "", content_type: str = "text/html; charset=utf-8"
    ) -> None:
        raw = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:  # noqa: N802 -- the name is fixed by http.server
        if self.path == "/robots.txt":
            self._send(200, ROBOTS, "text/plain; charset=utf-8")
        elif self.path in ("/", "/readings.html"):
            self._send(200, READINGS)
        elif self.path == "/page2.html":
            self._send(200, PAGE2)
        elif self.path == "/sloppy.html":
            self._send(200, SLOPPY)
        elif self.path == "/private/secret":
            self._send(200, "<p>You were asked not to fetch this.</p>")
        else:
            self._send(404, "<p>not found</p>")


@contextlib.contextmanager
def serve() -> Iterator[str]:
    """Start the server on a free port and yield its base URL."""
    server = HTTPServer(("127.0.0.1", 0), _Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
