"""A tiny HTTP server, so this module needs no network.

Read this file: a request handler, a dispatch over six routes, and a context
manager. It is the other side of every request you will make here, and module 20
comes back to what a port actually is.

Used as a context manager (module 09), so the server is always shut down:

    with serve() as base:
        response = requests.get(f"{base}/readings.csv", timeout=5)

The routes it answers:

    /readings.csv     200, text/csv; charset=utf-8      the log, correctly labelled
    /unlabelled.csv   200, text/csv                     the same bytes, no charset
    /readings.json    200, application/json             the same data as JSON
    /missing          404
    /broken           500
    /slow             200, after a second
"""

import contextlib
import json
import threading
import time
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, HTTPServer

CSV = "tag;value;unit\nTH-01;21.7;°C\nTH-04;91.0;°C\nTH-09;23.1;°C\n"

PAYLOAD = {
    "station": "Halle 3",
    "readings": [
        {"tag": "TH-01", "value": 21.7},
        {"tag": "TH-04", "value": 91.0},
        {"tag": "TH-09", "value": 23.1},
    ],
}


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, *args: object) -> None:
        pass  # keep the server quiet; it would otherwise log every request

    def _send(self, status: int, body: bytes = b"", content_type: str | None = None) -> None:
        self.send_response(status)
        if content_type is not None:
            self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 -- the name is fixed by http.server
        if self.path == "/readings.csv":
            self._send(200, CSV.encode("utf-8"), "text/csv; charset=utf-8")
        elif self.path == "/unlabelled.csv":
            # The same bytes, and a Content-Type that does not say utf-8.
            self._send(200, CSV.encode("utf-8"), "text/csv")
        elif self.path == "/readings.json":
            self._send(200, json.dumps(PAYLOAD).encode("utf-8"), "application/json")
        elif self.path == "/missing":
            self._send(404)
        elif self.path == "/broken":
            self._send(500)
        elif self.path == "/slow":
            time.sleep(1.0)
            self._send(200, b"eventually\n", "text/plain; charset=utf-8")
        else:
            self._send(404)


@contextlib.contextmanager
def serve() -> Iterator[str]:
    """Start the server on a free port and yield its base URL."""
    # Port 0 means "any free port": no clash if something else is running.
    server = HTTPServer(("127.0.0.1", 0), _Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
