# Solution 07 — The clause the data rewrote

**a) What SQLite parsed, and what the placeholder did instead**

With the value pasted in, the query text became:

```sql
SELECT COUNT(*) FROM readings WHERE tag = 'TH-04' OR '1'='1'
```

The `'` in the value closed the string literal early. Everything after it — `OR
'1'='1'` — stopped being data and became **part of the query**. `'1'='1'` is true
regardless of the row, and `X OR true` is true, so the `WHERE` clause matches every
row. The trailing `'` from the original query is what the value's final quote pairs
with.

What the placeholder did differently: **two things travelled separately.**

1. The **query text**, with a `?` where the value goes, is sent to SQLite and
   compiled into a prepared statement. At that moment the shape of the query is
   fixed: one comparison, on one column, against one value that is not yet known.
2. The **value** is sent afterwards, as a value, and bound into the compiled
   statement's parameter slot.

So the value is never text that a parser looks at. There is no point at which it
could become syntax, because by the time it arrives the parsing has already happened.
That is the whole mechanism, and it is why the protection is complete rather than
best-effort.

**b) A value that does something worse**

Measured, on this database:

- `x' OR '1'='1` in a `DELETE FROM readings WHERE tag = '...'` — **deletes all fifty
  rows.** One statement, and `rowcount` says 50.
- `x' UNION SELECT tag, location, installed FROM sensors --` in the `SELECT` —
  returns rows from `sensors`, a table the query never named. On a real system that is
  how the password column of another table ends up in a page of search results.

What stops both in the placeholder version: the same thing as in (a). The compiled
statement has one comparison in it. There is no way to add a `UNION` to a statement
that has already been compiled, because the value arrives after the compiling.

Worth knowing: the textbook payload `'; DROP TABLE readings; --` does **not** work
through `sqlite3`'s `execute`, which raises `ProgrammingError: You can only execute
one statement at a time`. It works through `executescript`. That is a small mercy and
not a defence — (b)'s two examples need only one statement each.

**c) Why escaping quotes is not a fix**

Two reasons, and the second is the one that matters.

**It does not cover numbers.** Measured: `WHERE value > 0 OR 1=1` pasted into an
f-string returns all fifty rows, and there is not a single quote character anywhere
in it. Replacing `'` with `''` changes nothing, because the injection never used a
quote. Any numeric or unquoted position — a `LIMIT`, an `OFFSET`, a comparison — is
wide open to an escaping function that only looks at quotes.

**It has to be remembered, every time, by everybody.** A placeholder is safe because
of what it *is*; escaping is safe because of what somebody *did*. There will be a
query written at five o'clock on a Friday that skips it, and nothing will fail — the
code will work perfectly on every input anybody tries. That is the difference between
a property and a practice, and it is why the rule is "always a placeholder" rather
than "escape carefully".

(A third, for completeness: correct escaping is dialect-specific. Backslashes,
`E''` strings, `NO_BACKSLASH_ESCAPES` — the rules differ per database and per setting,
and the driver already knows them.)

**d) A sort column from a dropdown**

The set of sortable columns is **known to you and finite**, so check against it:

```python
SORTABLE = {"tag", "value", "at"}          # a set, written by you

def readings_sorted_by(connection, column):
    if column not in SORTABLE:
        raise ValueError(f"cannot sort by {column!r}")
    # Safe because `column` is now one of three strings this file contains.
    return connection.execute(f"SELECT tag, value FROM readings ORDER BY {column}")  # noqa: S608
```

The check is what makes the f-string acceptable: after it, the interpolated text
cannot be anything a user chose. Note that it is an **allow-list** — a check for
characters you dislike is the same mistake as escaping, one blocklist to keep
complete.

The obvious shortcut and what goes wrong with it: taking the value straight from the
form because "it comes from my own dropdown". A dropdown is HTML; the request is not
obliged to resemble it, and anybody can send `ORDER BY value; --` or a `UNION` in that
field with the browser's developer tools open. **The form is not the boundary — the
handler is.**
