# Solution 08 — When a protocol is the wrong idea

**a) What structural typing buys**

You can make a type work with `for` without owning it, without inheriting from
anything, and without the type's author having anticipated you. Three concrete cases:

- **Adding behaviour to a class you did not write** — a mixin, a subclass, or a
  wrapper gains `__iter__` and every function that iterates now accepts it. In Java,
  a class that does not declare `implements Iterable` cannot be used in a for-each,
  full stop; you write an adapter.
- **Partial conformance is legal.** A class can support `in` and `len` without being
  a full sequence. Java's interfaces come in fixed sizes: implementing `List` means
  implementing all of it, which is why `UnsupportedOperationException` exists.
- **Two unrelated libraries fit together** without a shared base class to agree on.
  That is the whole reason `with`, `for` and `len` work on types the language has
  never heard of.

**b) What it costs**

**Nothing announces the intent.** A reader has to scan the class body for dunder
methods to discover that it is iterable. There is no line saying so, and no compiler
checking that you meant it.

**Partial implementations fail late and locally.** Write `__iter__` and `__len__` but
not `__contains__`, and `in` still works — it falls back to iterating — so you never
find out. Write `__getitem__` and forget `__len__`, and `for` works while `len()`
raises `TypeError: object of type 'X' has no len()`, at whichever call site happens to
ask first. The failure is not at the class, it is at the use.

`typing.Protocol` puts back the *declaration*: a class can be declared to satisfy a
protocol, and `mypy` will then check that the methods are there and have the right
signatures. What it does not do is check anything at run time, and it does not make
the object announce itself — an object still either has the method or does not.

**c) `log_a + log_b` and sorting logs**

**`__add__` for merging: defensible.** `+` on two containers means concatenation for
`list`, `str` and `tuple`, so a reader arrives with the right expectation, and the
result type is obvious. The conditions: it must return a **new** `Log` rather than
modifying either operand — `+` that mutates would contradict every other `+` in the
language — and merging must have one obvious meaning. If two logs can have different
tags, it does not: what is the tag of the result? At that point the operator is
hiding a decision, and `Log.merge(a, b)` is better because it has room for an
argument.

**`__lt__` sorting by highest reading: not defensible.** `a < b` on two logs does not
suggest "compare their maxima" to anybody. It reads as if logs had a natural order,
and they do not — you could as reasonably sort by tag, by length, or by time. The
reader has to leave the call site and go and read the class to find out which, and
the answer is arbitrary when they get there.

`sorted(logs, key=lambda log: log.highest)` says at the call site exactly what is
being compared, costs one line, and lets a different call sort differently. That is
the version to write.

**What I would do:** implement `__add__` only if all logs in the system share a tag,
otherwise a named `merge`; and never `__lt__`. The rule underneath: implement a
protocol when the meaning is the one a reader already expects from the syntax. Where
you would have to explain it, use a name instead — a name is where an explanation
fits.
