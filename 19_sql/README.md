# Module 19 — SQL with SQLite

**Assumes:** modules 01–18 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 19_sql` says whether your exercises are done

## Before you start

```bash
uv run 19_sql/build_db.py
```

That builds `data/readings.db` from the two CSV files next to it. The `.db` file is gitignored:
**a database is a build artefact**, the CSVs are the source, and deleting the file and running
the script again is always safe.

## What this is about

The same fifty readings as module 18, in a database — plus a second table saying where each
sensor is. `sqlite3` is in the standard library: nothing to install, no server, and the whole
database is one file.

**Never build a query out of strings.** The same value through a placeholder and through an
f-string, measured:

```python
tag = "TH-04' OR '1'='1"

connection.execute("SELECT COUNT(*) FROM readings WHERE tag = ?", (tag,))   # 0
connection.execute(f"SELECT COUNT(*) FROM readings WHERE tag = '{tag}'")    # 50
```

The placeholder found nothing, which is the truth — there is no such sensor. The f-string
returned every row in the table, because what SQLite parsed was `WHERE tag = 'TH-04' OR '1'='1'`.
**The WHERE clause was rewritten by the data.** That is SQL injection, and this is its mild
form — it reads too much. The same hole on a `DELETE ... WHERE tag = '...'` deletes **all fifty
rows** with one statement, measured; and a `UNION` in the same position reads a table the query
never mentioned.

(The textbook payload `'; DROP TABLE readings; --` does *not* work through `execute`, which
refuses more than one statement: `ProgrammingError: You can only execute one statement at a
time`. It works through `executescript`, which is why you never hand that foreign text. But note
what the measurements above show: one statement is quite enough.)

**And a `REAL` column will accept the string `"kaputt"`.** `typeof(value)` then says `text`. A
declared type in SQLite is an *affinity* — a preference for how to convert what it can convert —
not a constraint. `STRICT` after the closing bracket of a `CREATE TABLE` turns it into one, and
is one word.

That is the fifth time this course meets the same shape:

| module | the tool | what it does instead of failing |
| --- | --- | --- |
| 08 | `latin-1` | decodes any bytes; gives you `Â°C` |
| 16 | `requests` with no charset | falls back to Latin-1; the same `Â°C` |
| 17 | `html.parser` | repairs; four cells where there are two |
| 18 | `read_csv` | picks a type from the data; `.sum()` concatenates |
| 19 | SQLite | stores what it was given; `REAL` holds `'kaputt'` |

## Three more things that are quiet rather than loud

- **A plain `JOIN` drops rows that do not match**, silently, from a query that succeeded. `LEFT
  JOIN ... WHERE s.tag IS NULL` is how you find those rows instead of losing them.
- **Foreign keys are off by default.** The `REFERENCES sensors(tag)` in the schema is
  documentation until you write `PRAGMA foreign_keys = ON` — once per connection.
- **`NULL = NULL` is not true.** So `WHERE value = NULL` matches nothing, ever, and finds none of
  the three rows that are NULL. `IS NULL` is the operator, and module 18 said the same about
  `NaN == NaN`.

## `with` on a connection is not a close

The trap for everybody who has read module 09:

```python
with sqlite3.connect(path) as connection:                        # a TRANSACTION
    ...                                                          # and a leaked connection

with contextlib.closing(sqlite3.connect(path)) as connection:    # this closes it
    with connection:                                             # this commits or rolls back
        ...
```

`with` on a connection commits at the end of the block and rolls back if the block raised — which
is the property worth having: either all of it happened or none of it did. It does not close
anything.

## What you can do afterwards

1. **write** a SELECT with WHERE, ORDER BY and LIMIT, and read the rows by column name;
2. **say** why a query is never built with an f-string, and what a placeholder cannot stand in for;
3. **join** two tables, and name the rows a plain JOIN drops;
4. **group** in SQL, and say what `COUNT(*)` counts that `COUNT(column)` does not;
5. **say** what SQLite does with a string in a REAL column, and the one word that stops it;
6. **choose** between SQL and pandas for a given job.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 19_sql`**
4. **`solutions/`** — last

## SQL or pandas

You will have written the same summary twice by the end of this module. The pattern that follows
is **let SQL reduce, and let pandas explore**: select the rows and columns you need with a query —
possibly three rows out of ten million — and hand those to pandas with `pd.read_sql_query`.
Reading ten million rows into a DataFrame in order to keep three is the mistake the comparison in
section 9 exists to prevent.
