# Module 16 — Data over HTTP

**Assumes:** modules 01–15 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 16_http` says whether your exercises are done

## What this is about

The same sensor log as module 08, arriving over a socket instead of off a disk. One thing
changes, and it is the thing this module is for: **on disk you decide the encoding, over HTTP
somebody else claims it** — and when nobody does, `requests` falls back to ISO-8859-1 and hands
you `Â°C` without a word. Module 08's silent failure, from a different direction.

- **A response is a status code, some headers, and a body that is bytes.** `.content` is what
  arrived, `.text` is that decoded, `.json()` is that parsed. Three steps, three ways to fail.
- **A 404 does not raise.** A status code *is* an answer, so the request succeeded.
  `raise_for_status()` is the line that turns 4xx and 5xx into an `HTTPError`, and it belongs
  **before** you parse the body — otherwise a 500 that returns an error page gives you a
  traceback about JSON.
- **`timeout=` is not optional.** Leave it out and there is no timeout at all: the call waits as
  long as the other side keeps the socket open. A program that hangs with no traceback is worse
  to debug than one that crashes, and this is the usual way to write one.
- **Two kinds of failure.** The server answered badly (`HTTPError`, and only if you asked), or
  nobody answered (`ConnectionError`, `Timeout` — those raise by themselves). Retrying helps for
  the second, and for exactly three status codes of the first.
- **`params=` encodes for you**, and reading what it produced is instructive: a space becomes
  `+`, `°` becomes `%C2%B0`, an `&` in a value becomes `%26`. Every one of those is a rule you
  would get wrong by hand.

## No network

`server.py` in this folder answers every request in the module. It is a context manager — module
09 — that starts an HTTP server on a free port and shuts it down afterwards:

```python
with serve() as base:
    response = requests.get(f"{base}/readings.csv", timeout=5)
```

Read it. It is a request handler, a six-route dispatch and a context manager, and it is the
other side of every request you make here; the routes are listed in its docstring. Two of them serve **the same bytes** with different
`Content-Type` headers, which is what section 3 is built on. Module 20 comes back to what a port
actually is.

## What you can do afterwards

1. **make** a GET request and read the status, the headers and the body;
2. **say** why a 404 does not raise, and write the line that makes it;
3. **name** where a response's encoding comes from, and what to do when the header is silent;
4. **tell apart** a failure the server reported from a failure of the request itself;
5. **build** a URL with parameters without concatenating strings.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 16_http`**
4. **`solutions/`** — last

## The thread

`bytes` → `str` → `dict` is modules 07, 08 and 16 in one expression, and exercise 09 writes it
out. From here the same log gets scraped off a page (17), analysed with pandas (18), stored in
SQLite (19), and served back over HTTP by your own code in modules 21 to 23 — where you are on
the other end of everything in this module.
