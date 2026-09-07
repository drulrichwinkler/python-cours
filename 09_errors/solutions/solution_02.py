"""Solution 02 -- Predict what exceptions do.

parse("21.7")    is ['try', 'else', 'finally']: nothing raised, so `except` is
                 skipped and `else` runs. parse("n/a") is ['try', 'except',
                 'finally'] -- `else` runs only when the try completed.
sneaky()         is 'from finally'. A return in `finally` replaces the one from the
                 `try`, and would swallow an exception on its way past. Legal,
                 almost never wanted, and Java does the same thing.
issubclass       ValueError is an Exception; KeyboardInterrupt is not -- it comes
                 straight off BaseException, along with SystemExit. That is what
                 the difference between `except Exception` and a bare `except:`
                 amounts to in practice, and it is why the bare form can stop
                 Ctrl-C from working.
caught           is 'FileNotFoundError'. An except clause catches its class and
                 every subclass, and FileNotFoundError is an OSError. The name of
                 the class you catch decides how much you took responsibility for.
context          is 'ValueError' and cause is None. Raising inside an except block
                 keeps the original in __context__ automatically; __cause__ stays
                 None unless you wrote `from err`. The traceback shows both either
                 way, with different wording.
reached          is False -- but not because the exception was swallowed early. The
                 raise ends the block, so the line after it never runs; the truthy
                 __exit__ then stops the exception at the `with`, which is why the
                 program reaches the assert at all.
"""


def parse(raw):
    order = []
    try:
        order.append("try")
        float(raw)
    except ValueError:
        order.append("except")
    else:
        order.append("else")
    finally:
        order.append("finally")
    return order


assert parse("21.7") == ["try", "else", "finally"]
assert parse("n/a") == ["try", "except", "finally"]


def sneaky():
    try:
        return "from try"
    finally:
        return "from finally"


assert sneaky() == "from finally"


assert issubclass(ValueError, Exception) is True
assert issubclass(KeyboardInterrupt, Exception) is False


try:
    raise FileNotFoundError("gone")
    caught = "nothing"
except OSError as err:
    caught = type(err).__name__

assert caught == "FileNotFoundError"


try:
    try:
        float("n/a")
    except ValueError:
        raise RuntimeError("could not parse")
except RuntimeError as err:
    context = type(err.__context__).__name__
    cause = err.__cause__

assert context == "ValueError"
assert cause is None


class Swallow:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return True


reached = False
with Swallow():
    raise ValueError("boom")
    reached = True

assert reached is False
