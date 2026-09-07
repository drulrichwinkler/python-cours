# Solution 08 — Nothing is private

**a) What each one is for**

- **`_buffer`** is addressed to **people and tools**. It says: not part of the
  interface, may change without notice, do not rely on it. `from x import *` skips
  it, documentation generators hide it, linters and IDEs de-emphasise it. The
  interpreter does nothing at all.
- **`__cache`** is addressed to **the interpreter**, and it does one specific job:
  inside the class body the name is rewritten to `_Sensor__cache`. That means a
  subclass can have its own `__cache` and the two never collide, because each is
  mangled with the class that defined it. It is namespace separation between a class
  and its subclasses, not access control — `sensor._Sensor__cache` reaches it.

**b) Two things that get worse**

1. **Debugging.** The attribute is not called what the source says it is called. In a
   traceback, in `vars(sensor)`, in a debugger watch window, in `getattr`, it is
   `_Sensor__cache`. A colleague searching the codebase for `__cache` finds the
   definition and not the runtime name; a `hasattr(sensor, "__cache")` written in
   good faith is always False.
2. **Subclassing.** A subclass that wants to reuse the parent's buffer cannot: it
   writes `self.__buffer` and gets `_Child__buffer`, a different attribute, silently
   empty. The collision protection that is the feature's purpose becomes an obstacle
   the moment inheritance was intended.

A third, smaller one: anything generic over attributes — serialisation, a `__eq__`
over `vars()`, a repr helper — now sees mangled names and has to know about them.

**c) The argument, and the argument against**

**For:** enforcement buys less than it appears to. In every language that has
`private`, reflection gets past it, and the cases where somebody reaches into your
internals are cases where they had a reason and no alternative. What actually keeps
a codebase honest is that the internal thing is *marked*, so that using it is a visible
decision rather than an accident — and `_name` marks it at every use site, in the
reader's eye, for free. Meanwhile the absence of enforcement makes testing, debugging
and monkey-patching straightforward, which is a daily benefit against a rare harm.

**Against, in a codebase with twenty contributors:** the convention fails
demonstrably when the internal name is *convenient*. Somebody in a hurry writes
`other._buffer` because the public method does not quite do what they need; it works,
it ships, and it is now load-bearing. Six months later the class is refactored, the
buffer becomes a deque, and the breakage is in a module the author never read. Nothing
flagged the coupling when it was created — no compiler error, and a code review that
did not happen to look at that line. With `private` the coupling could not have been
created silently; it would have required a visible act.

The honest position is that Python trades a compile-time guarantee for a
review-time signal, and that the trade gets worse as the number of people who have
not read your class grows. Linters help — several will flag access to a `_name`
belonging to another object — which is the tooling putting back some of what the
language declined to enforce.
