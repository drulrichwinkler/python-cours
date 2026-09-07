# Module 10 — Modules, packages and the project

**Assumes:** modules 01–09 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 10_modules` says whether your exercises are done

## What this is about

Everything so far has been one file at a time. This is the module about the second file, and
about what turns a folder of them into something you can install, run by name and hand to
somebody else.

- **A module is a file, and importing it runs it.** Once. Every later import of the same name
  hands back what is already in `sys.modules` — which is why a `print` at the top of a module
  appears exactly one time, and why an import with side effects is a trap.
- **`sys.path` is a list, searched in order.** `import x` is not magic, and "it works here and
  not there" is almost always this list being different.
- **`python file.py` and `python -m package.file` do not put the same thing on that list** —
  the file's own folder in the first case, the current directory in the second. That one
  difference explains most import errors you will meet.
- **`if __name__ == "__main__":`** — because a file is executed when it is imported, and the two
  cases have to be told apart. Java's `public static void main` is a declaration; this is a
  runtime check on a string.
- **A package is a folder**, and `__init__.py` is the file that runs when it is first imported.
  A Java file declares the `package` it belongs to, and that declaration has to match the
  directory; Python has no such line — the position on `sys.path` is the whole truth.
- **A project is a `pyproject.toml`, a `src/` folder and a lock file.** `uv init`, `uv add`,
  `uv sync`, `uv run` — and `[project.scripts]`, which is how a function becomes a command.
- **Dependency groups**, which is the line between what your program needs and what developing
  it needs. `pytest` belongs on one side of it and `requests` on the other.

And two names promised back in module 06: `collections.Counter` and `collections.defaultdict`,
which is where the standard library gets its introduction.

## What you can do afterwards

1. **say** what `import` actually does, and what happens on the second one;
2. **read** an `ImportError` and name which of the two run styles would have avoided it;
3. **write** `if __name__ == "__main__":` and say what it is testing;
4. **split** a script into a package with an `__init__.py`, and say what `__all__` is for;
5. **lay out** a project so that `uv run` finds it, and turn a function into a command.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 10_modules`**
4. **`solutions/`** — last

`sensorlib/` in this folder is a real package, and the exercises import from it.

## The line at the top of the exercises that use `sensorlib`

```python
sys.path.insert(0, str(MODULE))   # so that `import sensorlib` finds it
```

That line is in four of the seven exercises, because they are run as scripts from a folder that
is not the one `sensorlib` lives in. It is also exactly what you should **not** have to write in
a real project — section 7 shows what replaces it, which is an installed package and one entry
in `pyproject.toml`. Seeing the manual version first is the point: section 7 replaces that line,
it does not hide it.
