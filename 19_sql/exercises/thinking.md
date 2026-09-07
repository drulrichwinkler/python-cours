# Module 19 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 19_sql`. Run `uv run 19_sql/build_db.py` first if you have not.

---

## Exercise 07 — The clause the data rewrote

```python
tag = "TH-04' OR '1'='1"

connection.execute("SELECT COUNT(*) FROM readings WHERE tag = ?", (tag,))   # 0
connection.execute(f"SELECT COUNT(*) FROM readings WHERE tag = '{tag}'")    # 50
```

a) Write out the SQL that SQLite actually parsed in the second case, and say which
   part of it made every row match. Then say what the placeholder did differently —
   not "it escaped the quotes", but what was sent to SQLite and when.
b) The example above reads too much. Give a value for `tag` that would do something
   worse, and say what stops it in the placeholder version.
c) A colleague says they will be safe because they escape the input: they replace
   every `'` with `''` before pasting it in. Give two reasons that is not a fix.
d) A placeholder cannot stand in for a column name — `SELECT ? FROM readings`
   selects the string. So how do you write a query whose sort column comes from a
   user's dropdown? Say what you would do and what could go wrong with the obvious
   shortcut.

> **Hint on (a):** at what point does the query text stop being text?
> **Hint on (c):** what about a value that is a number rather than a string? And who
> has to remember to call the escaping function?
> **Hint on (d):** the set of legal column names is known to you and finite.

**Check yourself:** your answer to (a) has to describe two things travelling
separately, and say what each one is.

---

## Exercise 08 — Where the work happens

Module 18 grouped fifty readings in pandas. This module grouped the same fifty in
SQL. Both gave three rows.

a) Now make it ten million readings on a laptop with 8 GB of memory. Say what happens
   to each of the two, concretely, and name the quantity that decides it.
b) `pd.read_sql_query("SELECT * FROM readings", connection)` and
   `pd.read_sql_query("SELECT location, AVG(value) ... GROUP BY location", connection)`
   both end with a DataFrame. Say what is different about the two programs, in terms
   of what crosses the boundary between the database and your process.
c) Name one job where pandas is clearly right even though the data is in a database,
   and one where SQL is clearly right even though the data would fit in memory.
d) The course has now said "let SQL reduce, let pandas explore". Give the case where
   that advice is wrong — a job where doing the reduction in SQL costs you something
   real.

> **Hint on (a):** what has to fit in memory at once for each approach?
> **Hint on (c):** think about a plot, and think about several processes writing at
> once.
> **Hint on (d):** what do you have to know before you can write the query, and what
> if you do not know it yet?

**Check yourself:** your answer to (d) has to name something you cannot do once the
reduction has happened.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
