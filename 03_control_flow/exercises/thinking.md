# Module 03 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 03_control_flow`.

---

## Exercise 08 — Translate, then argue

Here is a loop as it would be written in C:

```c
int worst = 0;
for (int i = 0; i < n; i++) {
    if (readings[i] > readings[worst]) {
        worst = i;
    }
}
printf("%d: %f\n", worst, readings[worst]);
```

a) Write it in Python, keeping the index — the literal translation.
b) Write it again without the index, using `enumerate`.
c) Which of the two would you rather find in a code review, and what exactly is
   the argument? "More Pythonic" is not an argument.

> **Hint on (c):** count the places where a wrong index could hide in each
> version. That number is the argument.

**Check yourself:** your answer to (c) has to name something that can go wrong in
one version and cannot in the other.

---

## Exercise 10 — When is `match` worth it?

You have written both an `if`/`elif` chain and a `match` in this module.

a) For `describe(status)` in exercise 07, which of the two would you keep, and why?
b) Name a case where `match` clearly wins over `if`/`elif`.
c) You write `match code:` and inside it `case IDLE:`, meaning to check whether
   `code` equals the constant `IDLE`. Why does that not do what you meant?

> **Hint on (b):** think about what you would have to write by hand to take a
> `("reading", "14:05", 21.7)` tuple apart and check its first element at the
> same time.
> **Hint on (c):** what would `case IDLE:` compare against, if a bare name binds
> rather than compares? Try it with a second `case` after it and read what Python
> says.

**Check yourself:** your answer to (c) has to say what a bare name in a pattern
does *instead* of comparing.

The written-out answers are in `solutions/solution_08.md` and `solution_10.md`.
