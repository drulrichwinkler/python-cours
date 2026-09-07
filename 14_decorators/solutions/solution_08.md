# Solution 08 — What a decorator costs the reader

**a) What is invisible at the call site**

From `publish(report)`, none of this is visible:

- the call may be **repeated up to three times**, so any side effect in `publish` can
  happen three times;
- it is **timed**, so something is written somewhere — a log line, a metric — on every
  call;
- it is **checked for authorisation**, so it may raise an exception that has nothing to
  do with publishing, from a layer the caller never mentioned;
- the **return value** may not be `publish`'s. `@retry` has to decide what to return on
  the final failure, and `@timed` could plausibly return a `(result, duration)` pair.

To find out, the reader has to open four things: the three decorator definitions —
which may be in three different modules, or in a library — and `publish` itself. The
call site names one of the four.

A traceback shows the cost too. Every layer adds a frame, and unless each wrapper
carries `@functools.wraps`, the frames are called `wrapper`, `wrapper`, `wrapper`.
That is the practical argument for `wraps` restated: without it, the stack trace of a
decorated call names nothing you can search for.

**b) `@retry` on a database write**

The danger: `publish` may not be safe to run twice. If it inserts a row, three
attempts can insert three rows; if it charges a card, three attempts can charge three
times. And a retry fires on *any* failure it is configured to catch — including a
timeout, where the first attempt may well have **succeeded** and only the
acknowledgement was lost. That is the worst case, because the retry is triggered
precisely when the state is unknown.

What the decorator would have to know: whether `publish` is **idempotent** — whether
running it twice with the same argument leaves the system in the same state as running
it once. It cannot know that, and nothing in the signature says so. So the
responsibility sits with whoever writes the `@retry` line, and the honest version of
this decorator retries only on errors that are known not to have taken effect
(connection refused, DNS failure) rather than on everything.

The safe pattern where the operation is not naturally idempotent: give the operation
an identifier the other side deduplicates on, so a repeated attempt is recognised as
the same attempt.

**c) The test to apply**

**Belongs in a decorator:** logging and timing. The caller does not need to know, the
return value is unchanged, and the concern is genuinely orthogonal — the same wrapper
is correct on any function.

**Does not belong:** validating the arguments of one specific function, and anything
that changes the return type. `@repeat(3)` from exercise 04 is the example in this
module: it turns a function returning a string into one returning a list of strings.
Nothing in the signature says so and no type checker sees it, so every call site is
now wrong in a way that only shows up at run time.

The test, in two questions:

1. **Does the caller need to know?** If yes, it does not belong in a decorator,
   because a decorator's job is to be invisible.
2. **Does it change the meaning of the return value or the signature?** If yes, the
   same answer — the decorator is now lying about what the function is.

Why "it is repeated" is not enough: a function is also a way of not repeating
yourself, and it has the advantage of being visible at the call site. Repetition
argues for factoring something out; it does not argue for factoring it out *behind*
the code that uses it. The decorator is right when the repetition is both everywhere
and beside the point — which is why logging qualifies and argument validation does
not.
