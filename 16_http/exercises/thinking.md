# Module 16 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 16_http`.

---

## Exercise 07 — The guess nobody asked for

The same bytes, two routes:

```python
requests.get(f"{base}/readings.csv").encoding      # 'utf-8'
requests.get(f"{base}/unlabelled.csv").encoding    # 'ISO-8859-1'
requests.get(f"{base}/unlabelled.csv").text        # 'TH-01;21.7;Â°C'
```

a) Explain the second line: where did `ISO-8859-1` come from, given that nobody sent
   it? Then say why the third line does not raise, using what module 08 established
   about that encoding.
b) `requests` could have done three other things here: raise, use UTF-8, or run its
   detector. Give the argument for each, and say which you would have chosen for a
   library used by millions of programs — and what the cost of changing it now would
   be.
c) `response.encoding = "utf-8"` and `response.content.decode("utf-8")` produce the
   same string. Name a situation where they are **not** interchangeable.

> **Hint on (a):** how many byte values does Latin-1 define, and how many are there?
> **Hint on (c):** what if the body is not text at all? What if part of it is not
> valid UTF-8?

**Check yourself:** your answer to (b) has to name who would break if the default
changed, not just say it would be nicer.

---

## Exercise 08 — Retry, and when not to

A colleague wraps every request in this:

```python
for attempt in range(3):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        continue
raise RuntimeError("gave up")
```

a) The `except` clause catches both kinds of failure from section 5. For each kind,
   say whether retrying could help, and why.
b) Three of the status codes in the table are worth retrying and most are not. Name
   which, and say what distinguishes them. What extra thing should the code do for
   `429`?
c) This is module 14's `@retry` exercise arriving for real. Say what makes a GET
   different from the database write in that exercise, and then name the one GET where
   retrying is still not safe.

> **Hint on (b):** what does 4xx mean about whose fault it is? Which single 4xx is
> about time rather than about the request?
> **Hint on (c):** what does GET promise about its effect on the server — and is that
> promise enforced?

**Check yourself:** your answer to (a) has to name at least one failure where the
retry loop makes things actively worse.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
