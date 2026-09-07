# Module 07 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 07_strings`.

---

## Exercise 07 — Why the wrong operator passes the test

```python
a = "TH-04"
b = "TH-04"
a is b          # True

built = "".join(["TH", "-04"])
built is a      # False
built == a      # True
```

a) Say what `is` is actually asking, and why the first answer is `True` without
   anything about strings being special.
b) A colleague writes `if state is "open":` and their unit test passes — the test
   is in its own file, and it still passes. Describe the first situation in
   production where it stops working, and say why no amount of testing with values
   written in the source would have found it. Then say what happens to the same bug
   if the value is spelled `"in-progress"` instead, and why that is worse rather
   than better.
c) `is` is not useless. Name the one comparison where it is the correct operator and
   `==` is not, and say why.

> **Hint on (b):** where do states come from in a program that is actually running?
> And: which characters may appear in a Python identifier?
> **Hint on (c):** there is exactly one of a certain object in a Python process.

**Check yourself:** your answer to (a) has to explain the `True` without using the
word "string" — the rule is about objects.

---

## Exercise 08 — What is the length of a string?

```python
len("TH-04")                    # 5
len("Übergabe")                 # 8
len("Übergabe".encode("utf-8")) # 9
len("👍")                        # 1, and Java's length() says 2
```

a) Name the three different questions those numbers answer. One of them is not about
   the text at all.
b) A file on disk has 9 bytes in it and the program prints a string of length 8.
   Say where the missing byte went, and what had to be known for the conversion to
   work.
c) Java counts UTF-16 code units, so the emoji is 2 there. Name one operation that
   is harder in Java because of that, and one that is harder in Python because a
   code point is still not the same thing as a character on screen.

> **Hint on (c):** think about an accented letter that can be written as one code
> point or as a letter plus a combining mark, and what `len` says about each.

**Check yourself:** your answer to (b) has to name the thing that has no default you
can rely on across systems.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
