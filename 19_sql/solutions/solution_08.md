# Solution 08 — Where the work happens

**a) Ten million readings, 8 GB of memory**

- **pandas:** `read_csv` (or `read_sql_query("SELECT * ...")`) builds the whole table
  in memory first. Ten million rows with five columns is on the order of a gigabyte
  for the numbers alone, more with strings, and pandas needs working room on top of
  that for the groupby. It may fit; it may swap; it may die with a `MemoryError`
  after four minutes of nothing. And it does the same thing again for the next
  question.
- **SQLite:** the `GROUP BY` runs in the database, which reads the file in pages and
  keeps one accumulator per group. Three groups means three accumulators. Memory is
  flat and unrelated to the row count, and what crosses into your process is **three
  rows**.

The quantity that decides it: **how much has to be in memory at once.** For pandas
that is the whole selected table; for SQL it is the result. When the result is small
and the table is large, the ratio is the entire argument — and it is the same argument
module 13 made for a generator over a file.

**b) What crosses the boundary**

Both end with a DataFrame, and that is the only thing they have in common.

- `SELECT * FROM readings` — **ten million rows** are serialised by SQLite, sent over
  the connection, and rebuilt as Python objects and then as arrays. The grouping then
  happens in your process. Everything the database is good at was declined.
- `SELECT location, AVG(value) ... GROUP BY location` — **three rows** cross. The
  scan, the arithmetic and the grouping happened where the data already was.

The programs differ in where the work is and in what the connection carries. The
second is not merely faster: it is a different program, in which the database is a
database rather than a file format.

Module 19's own exercise 09 does this deliberately — `WHERE r.value IS NOT NULL` in
the query means the DataFrame has 47 rows and no NaN, so there is nothing to explain
on the pandas side.

**c) One each**

**pandas, even though the data is in a database: a plot.** Or anything iterative —
try a histogram, change the bin width, add a rolling mean, look again. SQL returns
tables and cannot draw; and the loop of "look, adjust, look again" is module 18's
notebook argument, which needs the data in the process rather than behind a query.
Reduce in SQL first, then plot the result.

**SQL, even though the data would fit in memory: several processes at once.** Two
scripts appending readings while a third reads them. SQLite handles the locking; a
DataFrame in each process handles nothing, and the second writer overwrites the
first's file. The other clear case is **the query as the record** — a stored query is
a reproducible statement of what a number means, which module 18 section 8 said a
notebook is not.

**d) Where "let SQL reduce" is wrong**

**When you do not yet know what to reduce to.** A reduction is a decision, and the
query has to contain it: you have to know which columns matter, which rows to drop
and what to group by *before* you can write it. Exploration is precisely the situation
where you do not.

Concretely: you are looking for outliers and you do not yet know what an outlier is
here. `SELECT location, AVG(value) GROUP BY location` gives you three numbers and has
**thrown away every individual reading** — so the question you think of next, "was it
one sensor or all of them", cannot be asked of what you have. You would go back to the
database, write another query, and pay another round trip, for every question. In a
notebook with the rows in memory, that question costs 0.2 seconds.

So the honest form of the advice: **reduce in SQL once you know what you are reducing
to.** While you are finding out, pull a sample — `LIMIT 10000`, or one location, or one
day — into pandas and explore there. Then write the query.

That also names what you cannot do once the reduction has happened: **ask a question
the reduction did not anticipate.** An aggregate is not invertible, and a mean does not
remember the rows it came from.
