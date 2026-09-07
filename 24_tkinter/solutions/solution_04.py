"""Solution 04 -- A StringVar is not a str."""

import sys
from pathlib import Path

MODULE = Path(__file__).resolve().parent.parent
sys.path.append(str(MODULE))

from display import use_bundled_tcl  # noqa: E402

# Has to run before the first Tk() -- see display.py for why.
use_bundled_tcl()

import tkinter  # noqa: E402

root = tkinter.Tk()
root.withdraw()

var = tkinter.StringVar(value="85.0")
seen: list[str] = []

# Tk hands the callback three arguments -- the internal variable name, an index and
# the operation. None of them is useful here, and `*_` is how you say so.
var.trace_add("write", lambda *_: seen.append(var.get()))

entry = tkinter.Entry(root, textvariable=var)
entry.pack()
root.update()

print("var starts:", var.get())
print("entry shows:", entry.get())

var.set("90.0")
root.update()
print("after set, entry shows:", entry.get())

# Two operations, so two writes -- and the first of them leaves the variable empty.
# A listener that converted on every write would meet float("") here.
entry.delete(0, "end")
entry.insert(0, "42")
root.update()
print("after editing, var says:", var.get())

print("trace fired for:", seen)

root.destroy()
