"""Exercise 02 -- Predict what exceptions do.

Replace each `...` with the value you expect, then run the file.

    uv run 09_errors/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""


# TODO: which blocks run, and in which order?
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


assert parse("21.7") == ...
assert parse("n/a") == ...


# TODO: finally runs on every way out of the block -- including a return
def sneaky():
    try:
        return "from try"
    finally:
        return "from finally"


assert sneaky() == ...


# TODO: which of these does a bare `except:` catch that `except Exception` does not?
assert issubclass(ValueError, Exception) == ...
assert issubclass(KeyboardInterrupt, Exception) == ...


# TODO: an except clause catches its class and everything below it
try:
    raise FileNotFoundError("gone")
    caught = "nothing"
except OSError as err:
    caught = type(err).__name__

assert caught == ...


# TODO: raising inside an except block -- what does Python keep?
try:
    try:
        float("n/a")
    except ValueError:
        raise RuntimeError("could not parse")
except RuntimeError as err:
    context = type(err.__context__).__name__
    cause = err.__cause__

assert context == ...
assert cause is ...


# TODO: what a truthy __exit__ does to the exception
class Swallow:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return True


reached = False
with Swallow():
    raise ValueError("boom")
    reached = True

assert reached == ...
