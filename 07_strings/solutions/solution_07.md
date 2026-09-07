# Solution 07 — Why the wrong operator passes the test

**a) What `is` asks**

`a is b` asks whether the two names refer to **one object**. Nothing about strings.

The first answer is `True` because the compiler saw both literals in the source,
kept a single object for them and bound both names to it. The same thing happens to
any repeated constant in a code object. Change nothing about the comparison and
build the value at runtime instead, and there are two objects — so `is` is `False`
while `==` is still `True`, because `==` asks about content.

The reason this is a trap and not a fact to memorise: the answer depends on how the
value was made, which is not visible at the line where you compare it.

**b) The first situation in production**

The first tag that is not written in the source. A line read from a file, a field
out of a CSV, a query parameter, a JSON value, a name typed by a user — all of them
are built while the program runs, so `tag is "TH-04"` is `False` and the branch
never fires. Nothing raises: the sensor is simply never recognised as faulty.

Testing cannot find it, because a test that writes `is_faulty("TH-04")` puts the
literal in the source and gets the interned object back. The test and the bug
disagree precisely on the thing the test does not vary. The only test that would
have caught it builds the string the way production does — which is what
`exercise_03.py` does with `"".join(["TH", "-04"])`.

**c) Where `is` is right**

`x is None`. There is exactly one `None` object in a process, so identity is the
question, and `==` would be the wrong operator: a class can define `__eq__` and
make `x == None` answer anything it likes, while `is None` cannot be intercepted.

The same argument applies to the other singletons — `is True`, `is False` where you
really mean the object and not the truthiness — and to any deliberate identity
question, such as `new_list is original` in module 05.
