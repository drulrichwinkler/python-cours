# Module 24 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 24_tkinter`.

---

## Exercise 07 — The loop you do not own

Three measurements from this module:

```
root.after(0, f); print(log)      ->  []          nothing ran
root.update();    print(log)      ->  ['one']     one turn of the loop
after(0, slow); after(10, quick)  ->  slow start, slow end, quick
                                      quick was due at 10 ms and did not get its
                                      turn until slow had returned
```

a) In the first line, `f` was scheduled and did not run. Say who was executing code at
   that moment and who was not, and say what `after` actually did with `f`.
b) A callback in this module takes no arguments and returns nothing —
   `def refresh(self) -> None`. Both halves of that follow from one fact. Name the
   fact, and then say separately why there are no arguments and why there is no
   return value.
c) `quick` was due at 10 ms and did not run until `slow` had returned, three
   hundred milliseconds later. Name three things a user notices while that is
   happening. Then: a colleague's window has a button that fetches a file over
   HTTP, which takes thirty seconds. Say what they must not do, and sketch what to do
   instead — in terms of `after`, not in terms of a library you would have to look up.
d) Module 20 said Ctrl+C stops a server, and module 21 and 22 both relied on it. Say
   what stops *this* program, why Ctrl+C is not reliably it, and what that tells you
   about which process is in charge.
e) Every framework in Part 5 calls your code rather than being called by it, and this
   is the fourth one. Put Flask, Streamlit, FastAPI and tkinter in order of **how long
   you hand control away for**, and say what each one hands it back at.

> **Hint on (b):** what does the event loop know about the button that was pressed,
> and where would it put an answer if you gave it one?
> **Hint on (c):** the thing not to do is the thing `slow` did. For the sketch: what
> could the callback do in 50 milliseconds, and how would it arrange to be called
> again?
> **Hint on (d):** which process has the keyboard while a window is focused?

**Check yourself:** your answer to (e) has to name what ends the handover in each of
the four cases, and one of the four does not end until the program does.

---

## Exercise 08 — The exception nobody sees, and the missing test client

Two measurements, and they are related.

**One.** A button whose command raises `ValueError`:

```
before: []
after the bad button: []          the callback did nothing, the program continued
invoke() re-raised: False
$ echo $?
0
```

**Two.** `event_generate("<Return>")`, simulating a keypress, on the same code three
times over: once with the window visible, once with it positioned off-screen, once
withdrawn. Three different answers. Which one you get depends on **which window has
focus**, and focus is the window manager's business, not your program's.

a) The exit code is 0. Name three things that treat 0 as success, and say for each
   what it would conclude about a program whose buttons all raise.
b) Tk catches the exception on purpose. Make the case *for* that design in two
   sentences — what is the alternative, and what would it do to a user with unsaved
   work? Then say what it costs, and what you would put in `logic.py` or around the
   callback so the cost is paid by you rather than by whoever is using the window.
c) Modules 21, 22 and 23 each had a test client: `test_client()`, `AppTest`,
   `TestClient`. Explain from measurement Two why there is no equivalent for tkinter —
   what exactly would have to be faked. Then state the architectural answer this
   module takes instead, and say what it costs: name one thing about `app.py` that its
   tests cannot check at all.
d) `tkinter` failed on this project's toolchain with
   `TclError: Can't find a usable init.tcl in ... /tools/deps/lib/tcl8.6`, a directory
   on the machine that built the interpreter. And Tk is 8.6 on macOS and 9.0 on Linux
   for the same Python version. Say what class of problem that is — one sentence that
   does not use the word "tkinter" — and name one other dependency in this course
   with the same property, and one that cannot have it.
e) Now that all five presentations exist, pick one for each and defend it in a
   sentence:
   1. an operator on the shop floor enters a serial number and gets a verdict;
   2. a colleague explores last night's readings and adjusts a limit;
   3. the test rig's controller reads the current limit every thirty seconds;
   4. you need to watch a long-running job's output over ssh, on a server.

> **Hint on (a):** one of the three is in this repository.
> **Hint on (c):** what does `invoke()` skip that a real click does not?
> **Hint on (d):** what does `import pandas` need from the machine, and what does
> `import csv` need?

**Check yourself:** your answer to (c) has to name something concrete in `app.py` —
a line or a widget — that no test in `tests/` touches.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
