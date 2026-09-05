# Solution 07 — Reading a traceback

**a) Which line did the error occur on?**
Line 7. In a traceback the *last* file-and-line entry is the innermost frame —
where it actually blew up.

**b) Which line called the function?**
Line 12. That is the outer frame, listed first.

**c) What was the value of `anzahl` / `count`?**
Zero. `ZeroDivisionError` happens for exactly one value of the divisor.

**d) What probably happened?**
The list `werte` was empty, so `count` was `0`. The function computed a sum over
nothing and then divided by a count of nothing. The interesting part is not that
`count` was zero but *why*: nobody checked whether the list contained anything
before dividing by its length.

---

**The habit worth keeping:** read a traceback bottom-up.

1. Last line — *what* happened (the exception type and message)
2. The block above it — *where*, innermost frame last
3. Only then open the file

"Traceback (most recent call last)" is Python telling you exactly this: the most
recent call is at the bottom.
