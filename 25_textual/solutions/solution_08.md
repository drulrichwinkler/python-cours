# Solution 08 — The same bug, the opposite answer

**a) The case for each, and what it assumes**

- **tkinter keeps running** because it assumes the process exists to serve **a person
  who is present and has state in it**. One broken button must not take away a window
  someone has been typing into for twenty minutes.
- **Textual stops** because it assumes the process is **an interface it is responsible
  for the correctness of**. Once a handler has raised, the screen no longer reflects
  what the program thinks is true, and continuing to draw it is worse than stopping.

Which assumption is right depends on how the program was started, and both are right
somewhere:

- **Started by double-clicking an icon:** tkinter's assumption. There is nobody
  watching stderr, there may not be a stderr, and there is no supervisor to restart
  anything. A window that survives is the difference between a bad afternoon and a
  lost afternoon.
- **Started from a Makefile:** Textual's assumption. Something is reading the exit
  code and deciding what happens next, and "the interface silently stopped working"
  needs to become "this step failed" or the pipeline continues on a lie.

Note that neither toolkit knows which case it is in. You do.

**b) Shipping both**

**What I would add to the tkinter program:** the two things Textual gets for free.

1. **A place for the traceback that outlives the terminal.** `logging` with a
   `FileHandler` (module 09), configured before the window opens, and the `guarded`
   decorator from module 24's notebook on every callback so `logging.exception` runs
   where Tk would otherwise have printed to nowhere.
2. **A non-zero exit code when something has gone wrong.** Keep a flag — the decorator
   sets it — and `sys.exit(1)` after `mainloop()` returns if it is set. Cheap, and it
   is the difference between a CI job that can tell you something and one that cannot.

**What I would deliberately not copy:** the **tearing down of the window.** Textual is
right to exit and tkinter would be wrong to, for exactly the reason in (a) — the
program with a person's unsaved work in it is the one that must not vanish. The goal
is to make the failure *findable*, not to make it *fatal*. Those are separate
properties and it is worth being explicit about wanting one without the other: log
it, mark it, tell the user in the status bar, exit non-zero at the end — and keep the
window.

**c) Who owns the screen**

**tkinter does not own the screen. The window manager does.** Tk asks for a rectangle
and is told where it is, whether it is visible, whether it has focus, and what the
user did. Every one of those is an answer from another process, and a test would have
to impersonate that process.

**Textual owns the screen completely.** It is a grid of characters that Textual
allocates, fills and hands to stdout; nothing else has an opinion about it. Measured:
`run_test(size=(30, 6))` produces a screen that is thirty by six, because the size is
Textual's to decide. So `Pilot` can inject an event and know it arrived, and the test
is about the app rather than about the environment.

**The property a toolkit needs for its input to be simulable:** its input must be
**data the toolkit itself defines, not a report from another process.** Nothing about
being a GUI or not is the deciding factor — ownership of the boundary is.

Checking the other three:

- **Flask** — input is an HTTP request, a byte string defined by a specification. Fully
  constructible; `test_client()` builds one. Passes.
- **FastAPI** — the same, and it goes further: the request is parsed against
  annotations the application declares, so a test can construct the input *and* know
  what the framework will make of it. Passes.
- **Streamlit** — input is a widget value, defined by Streamlit. `AppTest`'s
  `set_value` writes it directly. Passes — with the wrinkle module 22 measured, that
  the re-run is on a wall clock, hence `default_timeout=30`.

So four of the five pass, and the one that fails is the one whose input crosses an
operating-system boundary. That is the general rule and it holds outside GUIs too: a
program that reads the system clock, the network or a real serial port has the same
problem, and the same architectural answer — put the boundary behind something you can
substitute.

### The terminal, and the two you have not been shown

**d) The machine at the far end of an ssh connection**

| | what it needs of that machine | reachable over ssh? |
| --- | --- | --- |
| tkinter (24) | a graphical session and the Tk libraries | **no** |
| Textual (25) | a terminal, and nothing else | **yes** |
| Streamlit (22) | a listening port, and a browser on your side | only with tunnelling |
| Flask (21) | a listening port, and a browser on your side | only with tunnelling |
| FastAPI (23) | a listening port, and a client that speaks JSON | only with tunnelling |

**tkinter is out** for the reason module 24 measured: no display, `TclError`, and
`ssh -X` is a workaround that needs an X server on your machine and forwards every
redraw over the link.

**Flask, Streamlit and FastAPI do not need a display** — that is right, and it is why
the row says something else. They need **a port that you can reach**, and that is
where they fail in practice: the port is bound on the server, and between you and it
there is a firewall, a security group, or a policy that says nothing but 22 is open.
`ssh -L 8501:localhost:8501` solves it and is a second thing to set up, to explain to
a colleague, and to redo after every reconnection. Add that all three then need a
browser pointed at a forwarded port, and that FastAPI needs you to be a program rather
than a person.

**Textual needs a terminal, and you already have one** — it is the thing you typed
`ssh` into. Nothing to install, nothing to forward, nothing to open. That is the whole
argument, and it is why it is the only one of the five that is genuinely available
here.

**e) PyQt6 and PySide6**

Both are Python bindings for the same C++ library, so the code you write is nearly
identical and the choice is a licensing one. **PyQt6 is GPL or a paid commercial
licence. PySide6 is LGPL** (it is the Qt Company's own binding).

What that means for a program your employer ships to a customer: under the GPL, if you
distribute a program that links PyQt6, you have to offer the recipient the complete
corresponding source of the whole work under the GPL as well. For an internal tool
nobody outside the company receives, that obligation is not triggered and PyQt6 is
free to use. For something that leaves the building, it is either "publish our
source" or "buy the commercial licence". The LGPL asks much less: you must allow the
recipient to replace the LGPL'd library, which for a dynamically-linked Python
dependency you are doing anyway, and your own code stays yours.

**So PySide6 is the one to evaluate first** for anything shipped, and it is also the
one with the shorter conversation attached to it. And "ask legal" is the right instinct
— the useful version of it is being able to say *what* you are asking: does this
program get distributed outside the company, in what form, and does anyone receive a
copy of the binary? Those three answers decide it, and they are answers you have and
legal does not.

**f) A young library, honestly weighed**

The cost is real. `.renderable` on a `Static` does not exist in the version this course
pins, `reactive(..., init=False)` is not guessable, and the fix in both cases came from
running the thing rather than from reading about it. A library at this stage means
your code is pinned to a version, upgrades are a task rather than a formality, and
answers you find online may describe a different API.

**When I would choose a terminal interface anyway:** when the interface is the point
and the machine is not mine. An operator on a build server, a colleague on ssh, a tool
inside a container — cases where a browser and a display are the things I cannot
assume and a terminal is the thing I am already in. And when the alternative is a
CLI with fifteen flags, where a table you can scroll is worth an afternoon.

**When it would be the wrong call for something that has to work in five years:**
when nobody is going to touch the program in those five years. A young library's cost
is paid at upgrade time, and a program that is never upgraded eventually cannot be —
the pinned version stops building on a new Python, and the person who has to fix it
is not you. For that case the standard library is the conservative answer:
**`curses`** is in Python itself, it will still be there, and its API has not moved in
decades. What it costs is everything Textual gives you — no CSS, no widgets, no
message system, no test client, and a layout you compute in character coordinates by
hand. That is a real trade, and the deciding question is not which library is better
but **who maintains this in year three**.
