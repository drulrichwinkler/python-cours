"""Test harness for the exercises.

The expected output of an exercise lives in exactly one place: the docstring of
the exercise file, under the line "Expected output:". The tests read it from
there, so the exercise, its solution and its test can never drift apart.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import textwrap
from pathlib import Path
from types import ModuleType

__all__ = ["expected_output", "run_file", "assert_output", "assert_runs", "load_module"]

_MARKER = "Expected output:"


def expected_output(spec_file: Path | str) -> str:
    """Pull the expected output out of an exercise docstring.

    Everything indented below the marker belongs to it; the block ends at the
    first non-indented, non-empty line.
    """
    text = Path(spec_file).read_text(encoding="utf-8")
    if _MARKER not in text:
        raise AssertionError(f"{Path(spec_file).name} has no '{_MARKER}' section in its docstring")

    after = text.split(_MARKER, 1)[1].splitlines()[1:]
    block: list[str] = []
    for line in after:
        if not line.strip():
            block.append("")
            continue
        if not line.startswith((" ", "\t")):
            break
        block.append(line)
    return textwrap.dedent("\n".join(block)).strip()


def run_file(path: Path | str) -> str:
    """Run a file in a fresh interpreter and return what it printed."""
    path = Path(path)
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        cwd=path.parent,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(
            f"{path.name} exited with code {result.returncode}:\n{result.stderr.strip()}"
        )
    return result.stdout.strip()


def assert_output(path: Path | str, spec_file: Path | str | None = None) -> None:
    """Assert that running `path` prints what `spec_file` says it should."""
    expected = expected_output(spec_file if spec_file is not None else path)
    actual = run_file(path)
    if actual != expected:
        raise AssertionError(
            f"{Path(path).name} printed something else.\n\n"
            f"--- expected ---\n{expected}\n\n"
            f"--- actual ---\n{actual}\n"
        )


def assert_runs(path: Path | str) -> None:
    """Assert that a file runs to the end without raising.

    Used for the prediction exercises. They are a series of `assert` statements
    with `...` where the answer goes: unfilled or wrong, the file stops with an
    AssertionError; right, it finishes silently.
    """
    run_file(path)


def load_module(path: Path | str) -> ModuleType:
    """Import a single .py file by path, so a test can call the functions inside it.

    Used from module 00 onwards for exercises that define a function instead of
    printing. Exercises that only print are checked with assert_output above.
    """
    path = Path(path)
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
