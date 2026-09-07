# Solution 07 — The encoding that does not raise

**a) What the two mappings do**

An encoding is a mapping between byte sequences and characters. The question is
whether the mapping is defined for every input.

`ascii` defines 128 characters, for byte values 0 to 127. Half of the 256 possible
byte values have no meaning in it at all, so a decoder that meets one has nothing to
return and raises.

`latin-1` defines a character for **all 256** byte values — Python's codec maps byte
`n` to code point `n`, with no gaps. There is no byte sequence it cannot decode, so
it has nothing to raise about. That is not permissiveness, it is completeness: the
mapping is total, and a total function has no error case.

Only in that direction, though. Going the other way there are 256 characters
available and rather more than 256 in Unicode, so `"€".encode("latin-1")` raises
`UnicodeEncodeError`. Reading with the wrong encoding is the silent half; writing
with it is loud.

UTF-8 sits in between: multi-byte sequences have a shape, and a byte that cannot
start or continue one is an error. That is why UTF-8 usually notices when it is
handed something else.

**b) Which failure you want at three in the morning**

The exception. It stops at the line that made the wrong assumption, names the byte
and the position, and nothing downstream ever sees the bad value.

What happens to `Â°C` instead: it is an ordinary `str` and nothing else in the
program can tell it apart from a correct one. It goes into the dict, gets written to
the database, into the report, into the customer's export. The bug is found weeks
later by a human reading a PDF, at which point the wrong data is in the database and
the program that put it there has run five hundred times. The stack trace you would
have got for free is now an afternoon of archaeology.

The general form: **a failure that raises costs you an incident; a failure that
returns a value costs you a data migration.**

**c) What is wrong with `.replace("Â°", "°")`**

Beyond inelegance: it is not one substitution, it is at least 1920 of them. Every code point
that UTF-8 writes in two bytes turns into its own pair of characters — `ä` becomes
`Ã¤`, `ö` becomes `Ã¶`, `ß` becomes `Ã\x9f` — and three-byte characters like `€`
produce three. A `.replace` fixes the one that was noticed and leaves the rest, so
the file looks repaired until the next customer's data arrives.

It is also lossy in one direction that cannot be undone: some of the byte values in
those pairs are control characters, and text that has been through a strip, a
normalisation or a database column with a different collation may no longer contain
what the reverse mapping needs.

The fix belongs at the **only place where bytes become text**: the `encoding=`
argument on the read. Decode once, correctly, at the edge; everything inside the
program is then `str` and nobody has to think about it again.
