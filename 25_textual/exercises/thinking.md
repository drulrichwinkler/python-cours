# Module 25 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 25_textual`.

---

## Exercise 07 — Four ways to say "call this"

The course has now registered a callback four times, four different ways:

| module | how | what registers it |
| --- | --- | --- |
| 21 Flask | `@app.get("/summary")` | a decorator, run at import |
| 22 Streamlit | nothing | there is no callback; the script re-runs |
| 24 tkinter | `command=self.refresh` | an argument, passed at construction |
| 25 Textual | `def on_button_pressed` | the method's **name** |

Three of the four can fail without saying anything, and each fails somewhere
different. Measured:

```
24  command=self.bump()   ->  the button gets None; Tk accepts None as "no command"
25  def on_button_press   ->  nothing is ever called; no warning
21  @app.get("/summry")   ->  /summry answers 200, /summary answers 404
```

a) For each of those three, say **what** the mistake is a mistake *in* — the value
   passed, the name of the thing, or a string inside it — and why nothing can catch
   it. Then say what makes Streamlit the exception: what did it give up in order to
   have no way of failing like this?
b) Each of the three has something you can ask to find out the truth rather than
   guess. Name it for all three. (Two of them appeared in this module and module 24;
   the third is a Flask attribute you have already used.)
c) Registration by name is a **convention**. Registration by decorator is
   **explicit**. Argue both sides: name one thing the convention buys that the
   decorator cannot, and one thing the decorator buys that the convention cannot.
   Then say which of the two you would want in a codebase eight people work on, and
   why that answer might differ from the one for a codebase you maintain alone.
d) `action_worse` in exercise 09 is found from the string `"worse"` in `BINDINGS`.
   Rename the method and not the binding, and pressing `f` does nothing. Say what
   a linter or a type checker would make of the resulting file, and what that tells
   you about which errors a type checker is able to be useful for at all.

> **Hint on (a):** in one case the mistake is a perfectly valid expression, in one it
> is a perfectly valid method, and in one it is a perfectly valid string.
> **Hint on (b):** `cget`, `handler_name`, `url_map`.
> **Hint on (d):** does `self.limit += 2.0` inside an unreferenced method look wrong
> to anything?

**Check yourself:** your answer to (a) has to explain why Streamlit's freedom from
this class of bug is a *consequence* of something, not a design win it chose.

---

## Exercise 08 — The same bug, the opposite answer

Module 24 and module 25 were handed one identical mistake: a handler that raises
`ValueError`. Measured, both:

| | tkinter (24) | Textual (25) |
| --- | --- | --- |
| the app afterwards | still running | stopped |
| the traceback | stderr, `Exception in Tkinter callback` | propagated, names your frame |
| the caller | `invoke()` returns normally | re-raised on leaving `run_test()` |
| the exit code | **0** | **1** |

a) Neither answer is a bug. Write the one-sentence case for each, in terms of **what
   the toolkit assumes about the process it is running in**. Then say which of the two
   assumptions is true of a program a colleague starts by double-clicking an icon,
   and which is true of one started from a Makefile.
b) You have to ship both kinds. Say what you would add to the tkinter program so its
   failures are as findable as Textual's — and then say what you would deliberately
   *not* copy from Textual, and why.
c) Module 24 had no test client and module 25 has one that works. Both are GUIs.
   Explain the difference in terms of **who owns the screen**, and then extend it: name
   the property a toolkit must have for its input to be simulable, and check Flask,
   Streamlit and FastAPI against it.

### The terminal, and the two you have not been shown

Measured: this module's app runs with `DISPLAY` unset, and `run_test(size=(30, 6))`
produces a screen that is thirty characters by six. The screen is a grid of
characters — which is precisely what fits down an ssh connection, a `docker exec`, or
a serial console.

d) A colleague has to watch a long-running job on a machine they can only reach by
   ssh. Go through all five presentations and say what each would require of that
   machine, and which are therefore out. Be specific about Flask and FastAPI: they do
   not need a display either, so say what they *do* need and why it may not be
   available.
e) There are two more toolkits a dual-study reader will meet and this course does not
   cover: **PyQt6** and **PySide6**. Both wrap the same C++ library, Qt. The
   difference that matters is the licence — PyQt6 is GPL or a paid commercial licence,
   PySide6 is LGPL. Say what that difference means for a program your employer ships
   to a customer, and which of the two you would therefore evaluate first. One
   paragraph; this is not a law exam, and "ask legal" is part of a correct answer as
   long as you can say *what* you would ask them.
f) Finally, the honest question about this module. Textual is a young library and its
   API moves — `.renderable` on a `Static` does not exist in the version this course
   pins, and `reactive(..., init=False)` is a detail you would not guess. Weigh that
   against what it gives you, and say under what circumstances you would choose a
   terminal interface anyway, and under what circumstances that would be the wrong
   call for a program that has to still work in five years.

> **Hint on (d):** one of the five needs a port to be reachable, which is a firewall
> question and not a Python question.
> **Hint on (f):** what does `curses` in the standard library give you, and what does
> it cost?

**Check yourself:** your answer to (d) has to name what each of the five needs, not
just which one wins.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
