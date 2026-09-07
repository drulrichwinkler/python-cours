# Module 08 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 08_files`.

---

## Exercise 07 — The encoding that does not raise

```python
data.read_text(encoding="ascii")    # UnicodeDecodeError
data.read_text(encoding="latin-1")  # 'TH-01;21.7;Â°C;Hall'
```

a) Explain, in terms of what an encoding is, why `latin-1` cannot fail and `ascii`
   can. Do not say "latin-1 is more permissive" — say what the mapping does.
b) Which of the two failures would you rather have in a program that reads a
   customer's file at three in the morning, and why? Name what happens to the
   `Â°C` afterwards.
c) A colleague fixes a mojibake bug by calling `.replace("Â°", "°")` on the parsed
   text. Say what is wrong with that beyond inelegance — and where the fix actually
   belongs.

> **Hint on (a):** how many byte values are there, and how many characters does
> each of the two encodings define?
> **Hint on (c):** what other characters does the same broken decoding produce, and
> how many of them are there?

**Check yourself:** your answer to (b) has to name a consequence that shows up
somewhere other than the line that read the file.

---

## Exercise 08 — Why the module and not the split

```python
[line.split(";") for line in text.splitlines()]   # exercise 03, before
csv.reader(fh, delimiter=";")                     # exercise 03, after
```

a) `data/tricky.csv` breaks the first one. Say exactly what the reader has to keep
   track of that a `split` cannot, and why no amount of splitting fixes it.
b) Every call in this module passes `newline=""` to `open` when a CSV is involved.
   The documentation requires it. Say what the file object would otherwise do that
   the `csv` module is already doing — and why the symptom appears on Windows and
   not on your machine.
c) You are handed a 40 GB log file and asked for the average of one column. Say
   which of `read_text`, `splitlines` and iterating the file object you can still
   use, and why.

> **Hint on (a):** what does a quote character mean, and when does it stop meaning
> it?
> **Hint on (c):** which of the three has the whole file in memory at once?

**Check yourself:** your answer to (b) has to describe a *doubled* character, and
say which layer put each part of it there.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
