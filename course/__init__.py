"""Helpers for the Python course.

There is no classroom and nothing to hand in. Your feedback loop is this package:
it tells you green or red without ever spelling out the answer.

    from course import check

    prediction = "..."
    check(prediction, "3a7bd3e2...")
"""

from __future__ import annotations

import hashlib
import re

__all__ = ["check", "hint", "answer_hash"]

_PLACEHOLDERS = ("", "...", "your answer here", "type here")


def _normalise(text: object) -> str:
    """Make answers comparable without being pedantic.

    Lowercase, collapse whitespace, drop surrounding quotes. So "  True " and
    "true" count as the same answer.
    """
    s = str(text).strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip("\"'")


def answer_hash(answer: object) -> str:
    """For authors: the checksum of an answer."""
    return hashlib.sha256(_normalise(answer).encode("utf-8")).hexdigest()


def check(prediction: object, expected_hash: str, nudge: str = "") -> bool:
    """Compare your prediction against the stored answer.

    The answer is not in this file -- only its checksum. So you cannot peek by
    accident, and you still get an immediate verdict.
    """
    if _normalise(prediction) in _PLACEHOLDERS:
        print("[ ] Nothing filled in yet. Write down your prediction --")
        print("    even one you are unsure about. Guessing is the point.")
        return False

    if answer_hash(prediction) == expected_hash:
        print(f"[OK] Correct: {prediction}")
        return True

    print(f"[X] Not yet. You said: {prediction!r}")
    if nudge:
        print(f"    Nudge: {nudge}")
    print("    Run the next cell to see what actually happens.")
    return False


def hint(text: str) -> None:
    """Print a hint that does not give the answer away."""
    print(f"[hint] {text}")
