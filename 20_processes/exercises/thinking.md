# Module 20 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 20_processes`.

---

## Exercise 07 — The program that cannot be stopped

```python
while True:
    try:
        do_one_batch()
    except:          # module 09 said not to write this
        pass
```

a) Say precisely what happens when somebody presses Ctrl+C on this. Walk through
   the signal, the exception, the clause, and the next iteration.
b) Module 09 gave the rule; this module gives the symptom. Say what a user does
   after the third Ctrl+C, and what it costs them.
c) `kill -9` cannot be caught. Say why that is both the reason it works and the
   reason it is a last resort, and name one thing a server should have done before
   dying that it now cannot.
d) Rewrite the loop so that Ctrl+C stops it tidily and everything else is still
   handled.

> **Hint on (a):** which class does `KeyboardInterrupt` inherit from, and does a
> bare `except:` catch it?
> **Hint on (c):** what is in memory that is not yet on disk?

**Check yourself:** your answer to (d) has to keep handling the ordinary failures —
"remove the try" is not the answer.

---

## Exercise 08 — Where to bind, and what `debug=True` gives away

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

a) Name what each of the three arguments does, and then say what the combination
   makes possible for anybody on the same network.
b) `debug=True` is genuinely useful. Say what it gives you, and describe the exact
   sequence by which someone on the same wifi turns it into running code on your
   machine.
c) In a Docker container the advice inverts: services there **do** bind `0.0.0.0`.
   Explain why that is not a contradiction — what is different about the container's
   `127.0.0.1`?
d) You need a colleague at the next desk to see your Flask app for five minutes.
   Give two ways to do it and say which you would choose.

> **Hint on (b):** what is on the page when a request raises an exception, and what
> can be typed into it?
> **Hint on (c):** whose loopback interface is it?
> **Hint on (d):** one way changes the bind address; the other does not.

**Check yourself:** your answer to (b) has to describe steps somebody could actually
follow, not just say it is insecure.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
