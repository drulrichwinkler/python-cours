# Solution 08 — Where to bind, and what `debug=True` gives away

**a) The three arguments, and the combination**

- **`host="0.0.0.0"`** — listen on every network interface, not just the loopback. The
  server becomes reachable from any machine that can route to yours: the office
  network, the coffee shop wifi, and on a badly configured network the internet.
- **`port=5000`** — the number clients connect to. Not secret, and easy to find:
  scanning the common ones takes seconds.
- **`debug=True`** — the reloader plus the interactive debugger. On an unhandled
  exception, Flask returns a traceback page **with an interactive Python console in
  it**.

Together they make an **unauthenticated remote Python shell**, running as your user,
on your machine, for anybody who can reach port 5000. Not "insecure" in the abstract:
that specific thing.

**b) The sequence**

What `debug=True` buys, and it is genuinely a lot: the server restarts when you save a
file, and a traceback comes back in the browser with local variables at every frame
and a console you can type into. While you are writing an application that is the
difference between a minute and ten.

How somebody on the same wifi turns it into running code:

1. **Find the port.** `nmap` across the subnet, or simply try 5000 on each address.
   Werkzeug's page announces itself.
2. **Make it raise.** Any URL that hits an unhandled exception — a malformed
   parameter, a missing record, a wrong type. On a half-written application this is
   not hard, and `debug=True` exists because it happens often.
3. **Get the traceback page.** It lists every frame with a console icon beside it.
4. **Open the console** and type. It evaluates in that frame's namespace, so
   `__import__("os").listdir("/")` works, as does reading your files, your
   environment — which is where API keys usually are — and anything the process can
   do.

Modern Werkzeug puts a **PIN** in front of the console, which is printed on the
server's own console at startup. That is a real obstacle and not a defence: the PIN is
derived from machine details, has been reconstructible in the past, and is worth
nothing if the attacker can read one file or one log. It buys time. It does not change
the answer.

The rule that follows: **`debug=True` is a development setting**, and it belongs behind
`127.0.0.1`. The two together are the mistake.

**c) Why the advice inverts in a container**

Because it is not the same `127.0.0.1`. A container has its own network namespace, so
its loopback interface is **the container's own** — reachable from inside that
container and from nowhere else, not even from the host.

So a service that binds `127.0.0.1` in a container is unreachable, including by
`docker run -p 8000:8000`, which forwards the host's port to the *container's
interface* rather than to its loopback. Binding `0.0.0.0` inside a container means
"every interface **of this container**", which is one interface on a private network.

What does the isolating is then the container's network and the port mapping: nothing
is published unless somebody wrote `-p`. The advice did not invert — **the boundary
moved.** In both cases the rule is the same: listen on everything inside your
isolation boundary, and be deliberate about what crosses it.

**d) Five minutes for a colleague**

**Two ways:**

1. **Bind `0.0.0.0` and give them your address** — `http://192.168.1.42:5000`. Works
   immediately, needs no tools, and exposes the port to the whole network for as long
   as it runs.
2. **Leave the bind alone and forward the port over SSH**, from their machine:
   `ssh -L 5000:localhost:5000 you@your-machine`. Your server stays on `127.0.0.1`;
   the tunnel is authenticated and encrypted, and it goes away when they close it.

**I would take (1)** — with `debug=False`, and I would stop the server afterwards. For
five minutes on a trusted office network, against a colleague at the next desk, the
tunnel is ceremony: it needs SSH access to your machine, which is a bigger thing to
arrange than the problem being solved.

What makes that answer defensible rather than lazy is the condition attached: it is a
short-lived, known network, and **the debugger is off**. Change any of those and the
answer changes — an untrusted network, or a demo left running overnight, is what (2)
is for. The two mistakes to avoid are treating the tunnel as always necessary, and
treating `0.0.0.0` as free.
