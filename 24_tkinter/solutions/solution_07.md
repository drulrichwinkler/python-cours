# Solution 07 — The loop you do not own

**a) Who was executing what**

At the moment of `print(log)`, **this script** was executing. `root.after(0, f)` is an
ordinary function call that returns immediately: it puts `f` on Tk's queue of pending
work, with a due time of now, and hands back an identifier. Nothing calls `f`.

The thing that would have called it — Tk's event loop — was not running, because there
is one thread and the script had it. `root.update()` is that loop, run once by hand:
it takes what is due off the queue, calls it, and returns. `root.mainloop()` is the
same loop with no way out until the window is destroyed.

So `after` does not mean "in n milliseconds". It means "not before n milliseconds, and
then whenever the loop is free", which is precisely what measurement three shows.

**b) No arguments and no return value**

The fact both follow from: **you do not call this function. The event loop does.**

- *No arguments*, because the loop has nothing to pass. It knows an event happened and
  which callback was registered for it; it does not know what your function would want.
  Anything the callback needs it has to fetch itself, which is why the state lives on
  `self` and why the module uses a class at all: `refresh` runs long after `__init__`
  returned and still has to find the listbox.
- *No return value*, because the loop has nowhere to put one. There is no caller
  waiting for an answer — the call came from a queue. A callback that computed
  something and returned it would be throwing the result away. So the result has to go
  somewhere a widget is watching: `self.status.set(...)`, `self.listing.insert(...)`.

This is inversion of control, and it is the same shape as a Flask view function or a
FastAPI route. What is different is the arguments: Flask hands a view the request, and
FastAPI hands a route its parsed parameters. Tk hands a callback nothing.

**c) The turn that came last**

What a user notices while a callback holds the loop:

1. **The window does not repaint.** Not "does not update its data" — it does not
   redraw at all. Drag another window across it and the uncovered part stays blank,
   because the redraw is an event and events are not being processed.
2. **Clicks are not refused, they are held.** A click is delivered to the program by
   the windowing system, which keeps unread input in a queue; a program that is not
   reading its queue is not told about anything and is not told that it was not told.
   So the button that "did nothing" is pressed again, and again, and the presses are
   still there when the loop comes back to them.

   Worth knowing if you try to check this yourself: **`event_generate` is not a model
   for a real click.** Measured — four `event_generate("<Button-1>")` calls made from
   inside a blocking callback fired their bindings immediately, all four of them,
   before the callback returned. It dispatches directly rather than going through the
   queue, which is the same reason it is no basis for a test (exercise 08).
3. **The operating system marks the program as not responding** — the spinning cursor
   on macOS, the greyed title on Windows — and offers to kill it.

The colleague's thirty-second HTTP fetch: **they must not do it in the callback.**
That is what `slow` did, and thirty seconds of it means half a minute of a window the
user is entitled to think is broken.

What to do instead, in this module's vocabulary: the callback starts the work and
returns immediately, and `after` is what gets you back. Put the fetch in a thread or a
subprocess (module 20), have it write its result somewhere the main thread can read —
a `queue.Queue` — and have the callback schedule a poller:

```python
def start(self):
    self.button.config(state="disabled")     # so it cannot be pressed twice
    threading.Thread(target=self.fetch, daemon=True).start()
    self.root.after(50, self.check)

def check(self):
    if self.results.empty():
        self.root.after(50, self.check)      # not done: ask again in 50 ms
        return
    self.show(self.results.get())
    self.button.config(state="normal")
```

Each turn of `check` costs a fraction of a millisecond, so the loop stays free and the
window stays alive. Note that the callback *reschedules itself* — that is the shape of
every periodic job in a GUI, and it is why `after` exists.

**d) What stops this program**

**Destroying the window.** `mainloop()` returns when the window it belongs to is gone,
and the exercises destroy it explicitly (`root.after(100, root.destroy)`) precisely
because there is no other way out.

Ctrl+C is not reliably it, because Ctrl+C is a signal sent by the **terminal** to the
process in its foreground process group — and while a window has focus, the terminal
is not what you are typing into. The keystroke goes to the window manager, which hands
it to Tk, which looks for a binding and finds none. The terminal never sees it.

Even with the terminal focused, it is unreliable: Tk's loop spends its time inside C
code waiting for events, and Python only runs a signal handler between bytecodes. The
handler can sit unrun until the next event arrives — which on an idle window may be
never.

What that tells you: **the window is in charge, not the terminal.** In modules 21, 22
and 23 the terminal owned the process and the browser was a client of it. Here the
relationship is reversed, and the terminal is a place where a traceback happens to
appear.

**e) How long you hand control away for**

Shortest handover first:

1. **FastAPI** — one route call. The framework parses the parameters, calls your
   function, takes the return value, and you are done. It ends at `return`.
2. **Flask** — one view call, the same length, ending at the returned response. It is
   after FastAPI only because the view also renders the template, so slightly more of
   the request is yours.
3. **Streamlit** — one whole script, top to bottom. Longer than a function call by an
   order of magnitude, and it ends when the script reaches its last line. Then the
   namespace is discarded and the next interaction starts a new one.
4. **tkinter** — **once, for the life of the program.** `mainloop()` is entered at
   startup and returns when the window is destroyed. There is no line after it that
   runs while the program is on screen.

The fourth is the one that does not hand control back until the program ends, and that
is why it is the only one of the four where the code is organised as callbacks rather
than as a sequence of statements.
