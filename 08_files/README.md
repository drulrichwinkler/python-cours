# Module 08 — Files, CSV and JSON

**Assumes:** modules 01–07 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 08_files` says whether your exercises are done

## What this is about

This is where the data stops being written in the source. `data/sensors.csv` and
`data/limits.json` are in this folder, and from here on they are the thread that runs through the
course: tested in module 15, fetched over HTTP in 16, analysed with pandas in 18, stored in
SQLite in 19, and displayed five different ways in modules 21–25.

- **`pathlib.Path` is an object, not a string.** You have been reading `Path(__file__).parent`
  in every test file since module 00; this is where it gets explained. `/` joins parts, and the
  result works on Windows and macOS alike.
- **Naming the encoding is not optional.** `open()` without one asks the operating system, and
  the answer differs between machines. Python will even point at the line for you:
  `python -X warn_default_encoding` turns every unnamed encoding into a warning.
- **The wrong encoding is worse when it does not raise.** `ascii` raises on the first byte it
  cannot handle. `latin-1` never raises — it produces `Â°C` and travels on into your database.
- **CSV is not "split on the comma".** A field may contain the separator, in quotes, and the
  module that reads it is one line longer than doing it by hand and correct on data you did not
  write.
- **JSON is not Python.** The round trip is lossy in ways that are easy to miss: a `tuple` comes
  back a `list`, an `int` key comes back a `str` key, and a `set` does not go out at all.

## `with`, used here and explained in module 09

Every file in this module is opened in a `with` block, because a file that is not closed is a bug
in every language. What `with` actually is — the protocol, and how to write one — is module 09.
Here it is enough that the file is closed when the block ends, including when the block ends
because something raised.

## What you can do afterwards

1. **build** a path from parts and ask it what its name, suffix and parent are;
2. **read and write** a text file with the encoding named, and say what happens when it is not;
3. **tell apart** the encoding error that raises from the one that does not;
4. **read** a CSV with `csv.DictReader`, and say why `newline=""` is in the call;
5. **load and dump** JSON, and name three things the round trip does not preserve.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 08_files`**
4. **`solutions/`** — last

## `bytes`

One section, enough to show that a file is bytes and a `str` is what you get after decoding them.
Module 16 is where it matters, because HTTP hands you bytes with the encoding named somewhere
else entirely — and sometimes wrongly.
