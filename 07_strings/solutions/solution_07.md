# Solution 07 — Why the wrong operator passes the test

**a) What `is` asks**

`a is b` asks whether the two names refer to **one object**. Nothing about strings.

The first answer is `True` because the compiler saw both literals **in the same
file**, kept a single object for the constant and bound both names to it. The same
thing happens to any repeated constant in one code object. Build the value at
runtime instead and there are two objects — so `is` is `False` while `==` is still
`True`, because `==` asks about content.

The reason this is a trap and not a fact to memorise: the answer depends on how and
where the value was made, none of which is visible at the line where you compare it.
Three things move it, and you chose none of them deliberately:

- **Which file.** Two literals in two modules are two objects. A notebook cell is
  compiled on its own, so two cells behave like two files.
- **How it is spelled.** A literal that reads like an identifier — letters, digits,
  underscores — is interned for the whole process. `"open"` is one object everywhere;
  `"in-progress"` is not.
- **How it was built.** `"TH" + "-04"` is folded by the compiler and stays one
  object; `"".join(["TH", "-04"])` is not.

**b) The first situation in production**

The first state that is not written in the source. A line read from a file, a field
out of a CSV, a query parameter, a JSON value, a word typed by a user — all of them
are built while the program runs, so `state is "open"` is `False` and the branch
never fires. Nothing raises: the order is simply never treated as open.

Testing does not find it, because every value a test writes is a literal. `"open"`
reads like an identifier, so it is interned process-wide and the comparison is
`True` even when the test lives in its own file. The test and the bug disagree
precisely on the one thing the test does not vary: where the string came from. The
test that would have caught it builds the value the way production does — which is
what `exercise_03.py` does with `"".join(["TH", "-04"])`.

**And `"in-progress"` is worse, not better.** That literal is not interned across
files, so the same comparison is already `False` between a test file and the module
under test — the test goes red, and it goes red for a reason that has nothing to do
with the logic. Two spellings of the same idea, two different wrong behaviours, and
the operator is wrong in both. That is the argument for not learning when interning
happens: what you learn is not to ask.

**c) Where `is` is right**

`x is None`. There is exactly one `None` object in a process, so identity is the
question, and `==` would be the wrong operator: a class can define `__eq__` and
make `x == None` answer anything it likes, while `is None` cannot be intercepted.

The same argument applies to the other singletons — `is True`, `is False` where you
really mean the object and not the truthiness — and to any deliberate identity
question, such as `new_list is original` in module 05.
