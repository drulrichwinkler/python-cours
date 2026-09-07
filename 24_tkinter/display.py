"""Making tkinter start under this project's toolchain.

This module exists because of one detail of how `uv` installs Python, because it is
the kind of problem a GUI toolkit produces and a pure-Python
library never does.

`tkinter` is not Python. It is a thin wrapper around **Tcl/Tk**, a C library with its
own script files -- `init.tcl` and about a thousand others. The wrapper finds those
files by looking in `<sys.prefix>/lib/tcl8.6`, and `sys.prefix` inside a virtual
environment is the virtual environment. `uv sync` did not put Tcl there; the Tcl that
came with the interpreter sits next to the **base** interpreter, at
`<sys.base_prefix>/lib/tcl8.6`. So the search fails and the error reads:

    _tkinter.TclError: Can't find a usable init.tcl in the following directories:
        /tools/deps/lib/tcl8.6 .../.venv/lib/tcl8.6 ...

`/tools/deps/lib/tcl8.6` is a path on the machine that *built* the interpreter, months
ago, on somebody else's disk. That is the giveaway: this is a compiled dependency
looking for files by absolute path, not a Python import.

`use_bundled_tcl()` below points the two environment variables at the copy that is
actually on disk. It has to run before the first `Tk()`, which is why every file in
this module imports it first.
"""

from __future__ import annotations

import functools
import os
import sys
from pathlib import Path


def use_bundled_tcl() -> None:
    """Point TCL_LIBRARY and TK_LIBRARY at the Tcl that shipped with this interpreter.

    Does nothing if the variables are already set -- somebody who has arranged their
    own Tcl keeps it -- and nothing if this interpreter is not in a virtual
    environment, where the default search already works.
    """
    base = Path(sys.base_prefix) / "lib"
    # The glob is version-agnostic on purpose. Measured: macOS gets Tk 8.6 and needs
    # this; Linux gets Tk 9.0, finds its own files, and the loop below sets nothing.
    # Same Python, two different C libraries -- which is the point of the module.
    for variable, pattern, marker in (
        ("TCL_LIBRARY", "tcl[0-9]*.*", "init.tcl"),
        ("TK_LIBRARY", "tk[0-9]*.*", "tk.tcl"),
    ):
        if variable in os.environ:
            continue
        for candidate in sorted(base.glob(pattern)):
            if (candidate / marker).exists():
                os.environ[variable] = str(candidate)
                break


@functools.cache
def has_display() -> bool:
    """Whether a window can actually be opened here.

    There is no way to ask this other than to try. A machine with no graphical session
    -- a server, a container, a continuous-integration runner -- has a working
    `tkinter` module and no screen to put a window on, and the failure comes from Tcl
    as a `TclError` rather than from Python as an `ImportError`. Both are caught here,
    because a machine can also be missing the binding itself: measured on
    ubuntu-latest, `import tkinter` raises until `python3-tk` is installed.

    `functools.cache` because the answer cannot change while the process runs, and
    finding it out costs a real window.
    """
    use_bundled_tcl()
    try:
        import tkinter
    except ImportError:
        return False
    try:
        root = tkinter.Tk()
    except tkinter.TclError:
        return False
    root.destroy()
    return True
