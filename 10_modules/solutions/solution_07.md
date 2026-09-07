# Solution 07 — The same file, two ways to start it

**a) What each form puts on the list**

- `python tool/show.py` puts **the folder containing the file** at `sys.path[0]` —
  `tool/`. Python was handed a path and nothing else. It has no idea the file belongs
  to a package, so it makes the file's own directory importable and runs it.
- `python -m tool.show` puts **the current working directory** at `sys.path[0]`.
  Here Python was handed a dotted *name*, which it can only resolve by searching
  `sys.path` — so the directory you are standing in has to be on it, and it is put
  there for you.

The assumption behind each: the first is "this file is a program, run it"; the second
is "this is a module inside a package that is importable from here". That is why only
the second form can do a relative import — a file run by path has no parent package,
and `from ..reader import read` raises `ImportError: attempted relative import with no
known parent package`.

**b) The colleague's script**

Say the project is `proj/`, the package is `proj/tool/`, and the script is
`proj/tool/show.py`, importing `import tool.helpers`.

- **`python -m tool.show` from `proj/`.** `sys.path[0]` is `proj/`. `tool` is a
  folder inside it, so `import tool.helpers` finds it. Works.
- **`python tool/show.py` from `proj/`.** `sys.path[0]` is `proj/tool/` — the file's
  own folder. `proj/` itself is **not on the list at all**. `import tool.helpers`
  looks for a `tool` inside `proj/tool/`, does not find one, and raises
  `ModuleNotFoundError`.

The confusing part is that both commands were run from the same directory. The
current directory is not what matters; what matters is which directory each form puts
on `sys.path`.

**c) Two things wrong with `sys.path.insert`**

1. **It hard-codes a layout into the code.** The line computes a path from
   `__file__` with a fixed number of `.parent`s. Move the file one folder deeper and
   the import breaks in a way that mentions neither the move nor the line.
2. **It is global and it wins.** Inserting at position 0 puts your folder ahead of
   everything, including the standard library. A module of yours named `logging.py`
   or `json.py` then shadows the real one for the whole process, and the error
   arrives somewhere else entirely.

A third, milder one: it only fixes the process that runs that file. Anything else
importing your package still cannot find it.

What replaces it: **an installed package.** A `pyproject.toml`, the code under
`src/`, and `uv sync` — after which the package is in the environment, importable
from anywhere, by every tool, with no line at the top of any file. In this course
that is exactly what `course/` is: `pyproject.toml` lists it, and every test file
writes `from course.checks import assert_output` without touching `sys.path`.
