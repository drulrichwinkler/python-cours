# Solution 08 — Retry, and when not to

**a) Which failures a retry can help**

- **Nobody answered** — `ConnectionError`, `Timeout`. Retrying can help: the network
  may have blipped, the server may have been restarting, the timeout may have been
  unlucky. This is the case the loop was written for.
- **The server answered badly** — `HTTPError`. Retrying almost never helps, and for
  4xx it cannot: the server has told you the request itself is wrong, and sending it
  three more times produces three more of the same answer.

And the case where the loop makes things **actively worse**: a `429 Too Many
Requests`. The server is saying "you are sending too much", and the loop's response is
to send it twice more, immediately, with no delay. That is how a client gets its IP
banned rather than rate-limited. A `503` under load is the same shape — three
immediate retries from every client is the mechanism by which an overloaded service
stays overloaded.

A second, quieter harm: the `except` clause swallows the exception and `continue`s, so
after three attempts the caller gets `RuntimeError("gave up")` and **no information
about why**. The 404 that would have been a one-line fix is now indistinguishable from
a DNS failure. That is module 09's argument against a wide `except` arriving in real
code.

**b) Which codes are worth retrying**

Three, and what they have in common is that **none of them says the request was
wrong**:

- **429 Too Many Requests** — the request was fine, the timing was not.
- **502 Bad Gateway** and **503 Service Unavailable** — the request never reached
  something that could answer it, or that thing is temporarily out.
- (**504 Gateway Timeout** belongs with them, which makes it four if you count it.)

Everything else in 4xx is a statement about the request: 400 malformed, 401 not
authenticated, 403 not allowed, 404 not there. Retrying an unchanged request against
an unchanged server is arithmetic — the answer does not move. The odd one out in 4xx
is 429, because it is the only one that is about *time* rather than about the request.

`500` is the interesting middle case: it means the server broke, which might be
transient or might be a bug your request triggers deterministically. Retry it at most
once, with a delay, and stop.

What the code must do for `429`: **read the `Retry-After` header** and wait that long.
It is either a number of seconds or an HTTP date, and it is the server telling you the
answer. Ignoring it and retrying immediately is worse than not retrying at all. Where
there is no header, back off exponentially with jitter — 1 s, 2 s, 4 s, plus a random
fraction so that a thousand clients do not all return at the same instant.

**c) GET against the database write**

The difference is **idempotence**, which is exactly what module 14's exercise turned
on. A GET is *defined* to be idempotent and safe: RFC 9110 says it must not have
side effects beyond retrieval, so sending it twice leaves the server as it was and the
timeout case — where the first attempt may have succeeded and only the reply was lost —
costs nothing. The database write in module 14 had no such guarantee, which is why
retrying it could insert three rows.

The catch: **that promise is a convention, not a mechanism.** Nothing stops a server
from doing work in a GET handler, and plenty do — a GET that increments a view counter,
records an audit entry, or is wired to `/delete?id=5` because somebody found that
easier. The specification says such a server is wrong; your retry loop is what finds
out.

So the one GET where retrying is still not safe: **one whose URL you did not write.**
If the endpoint came from a config file, a redirect, or a link in somebody's payload,
you do not know what it does, and idempotence is a claim about a well-behaved server
rather than about the request you are sending.
