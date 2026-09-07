# Module 04 — Functions

**Assumes:** modules 01–03 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 04_functions` says whether your exercises are done

## What this is about

You have written functions for four semesters. This module is the list of things Python does
differently, and one trap that catches everybody once.

- **There is no overloading.** A `def` binds a name the way `=` does; a second one rebinds it and
  the first is gone. The argument machinery is rich because it has to be.
- **Default arguments are evaluated once**, when the `def` runs — so a mutable default is one
  object shared by every call that omits it. C++ re-evaluates on each call, Java has no defaults
  at all, so there is no habit to fall back on.
- **Keyword arguments and keyword-only parameters**, which make a call self-documenting and let
  you forbid the unreadable one.
- **Return several values** as a tuple, with no out-parameters and no wrapper class.
- **Arguments are references.** Mutating what you were handed is visible to the caller; rebinding
  the parameter is not.
- **No block scope, and `nonlocal`.** A closure captures the variable, not its value — Java's
  effectively-final restriction removed. That is what lets a closure accumulate without a wrapper
  object, and what makes closures built in a loop share one variable.
- **Functions are values.** `key=` is the everyday use; decorators in module 14 are the next step.

## What you can do afterwards

1. **say** what a second `def` with the same name does, and why that follows from what `def` is;
2. **explain** why a mutable default accumulates, and write the fix;
3. **write** a signature with defaults, `*args`, `**kwargs` and a keyword-only parameter, and
   **say** when each earns its place;
4. **name** which changes a function makes to its arguments the caller can see;
5. **pass** a function as an argument, and say what a closure captures.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 04_functions`**
4. **`solutions/`** — last

## A thread that runs on

Exercise 02 asks what the caller sees when a function mutates a list it was given. That is `b = a`
from module 01, seen from the other side. Module 05 is where it stops being a curiosity and starts
being the thing you have to hold in your head.
