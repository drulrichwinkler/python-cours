# Solution 08 — Why the module and not the split

**a) What the reader keeps track of**

State: whether it is currently inside a quoted field. A `split` has none — it looks
at each separator in isolation and cannot know that this particular `;` is inside
quotes and therefore data rather than a boundary.

The reader also has to know that a doubled quote inside a quoted field means one
literal quote, that a quoted field may contain a line ending (so a record is not
always a line), and that the quotes are syntax and must not appear in the value.

No amount of splitting fixes it because splitting is stateless by construction. You
would have to walk the line character by character, remembering whether you are
inside quotes — which is what `csv.reader` is. Once you have written that, you have
written the module, only with fewer tests.

**b) `newline=""`**

Without it, a file opened in text mode does **newline translation**: on writing it
turns each `\n` into the platform's line ending, and on reading it turns line
endings into `\n`.

The `csv` module does its own line-ending handling, because a quoted field may
contain one and only the reader knows whether a given line ending ends the record.
So both layers act, and their work is applied twice.

On Windows the symptom is a doubled character: the writer emits `\r\n`, the text
layer then translates the `\n` in that pair into `\r\n` as well, and the file gets
`\r\r\n` — one `\r` from the csv module, one `\r\n` from the file object. Files
written that way open with a blank line between every row in some tools.

It does not show on macOS or Linux because the platform line ending is `\n` there
and the translation on writing is a no-op. Which makes this exactly the class of bug
that passes every test you run and fails at the customer: the platform is the input
you did not vary. The `\r\n` is visible on any machine, though —
`explore.ipynb` prints the raw bytes of a file the csv writer wrote.

**c) 40 GB**

- `read_text` — no. It builds one `str` holding the whole file. 40 GB of file needs
  at least 40 GB of memory, and more while decoding.
- `.splitlines()` — no, twice over: it needs the whole text to have been read
  already, and it then builds a list of every line on top of it.
- **Iterating the file object — yes.** It reads a buffer at a time and hands you one
  line, and the previous line is free to be collected. Memory stays flat regardless
  of the file size, which is the only property that matters here.

`csv.reader` takes any iterable of lines, so it inherits that: reading a 40 GB CSV
row by row is the same three lines as reading a small one. Keep an accumulator and a
count in the loop, not a list of rows — the moment you write `rows = list(...)` you
are back to holding the file in memory.
