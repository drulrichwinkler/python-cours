# Solution 07 — No checked exceptions

**a) What the compiler does that nothing in Python does**

1. **It proves, before the program runs, that every checked exception is either
   handled or declared.** Not "usually handled" — every path, at compile time. In
   Python there is no such pass; a `FileNotFoundError` from a library you called
   three levels down reaches your `main` and nobody was asked about it.
2. **It puts the answer in the signature**, where the caller reads it. `throws
   IOException` is machine-checked documentation: it cannot be out of date, because
   the code would not compile. A Python docstring saying `Raises: ParseError` is a
   promise nothing verifies, and it goes stale the first time somebody adds a branch.

The honest summary: Java catches a real class of mistake that Python leaves to you.

**b) The case against**

The compiler can insist that you write *something*. It cannot insist that the
something is useful. What gets written under deadline is

```java
try { ... } catch (IOException e) { }             // or e.printStackTrace();
```

which is worse than not catching at all: the exception is now gone, the stack trace
is on somebody's console instead of in the caller's hands, and the program carries on
with whatever state the half-finished operation left. The compiler is satisfied and
the failure is invisible.

The second complaint is about the boundaries. An interface that declares `throws
IOException` has committed every implementation to that vocabulary; a change deep in
one implementation ripples out through every signature that passes the value along.
Lambdas made it sharper still — a checked exception cannot travel out of a
`Function`, so Java code full of streams tends to wrap everything in an unchecked
exception, which is Python's model arrived at by a longer road.

So: it is a real trade, not a mistake in either direction. Java pays with ceremony
and with the empty catch block; Python pays by making "what can this raise" a
question you have to answer with documentation and care.

**c) A library function that reads a config file**

- **Signature:** the types say what comes *back*, and that is all they can do —
  `def load(path: Path) -> Config:`. Resist encoding failure in the return type
  (`Config | None`) unless a missing config is a normal outcome for every caller:
  it moves the handling to a place with no information about what went wrong, and it
  is easy for the caller to ignore.
- **Docstring:** a `Raises:` section naming what a caller can reasonably catch, and
  what each one means. It is not checked, so keep it to the exceptions you deliberately
  raise or deliberately let through — a list of everything possible is noise.
- **Body:** let `FileNotFoundError` through unchanged, and translate the parse
  failures into a `ConfigError` of your own with `from err`. The reasoning: a missing
  file is a fact the caller understands and can act on, and `FileNotFoundError` is
  already the right name for it. A malformed config, on the other hand, arrives as
  `ValueError`, `KeyError` or `UnicodeDecodeError` — implementation detail leaking
  out — and a caller cannot write `except ValueError` around your function without
  catching things you have not thought about. One class of your own turns that into a
  question they can answer.
