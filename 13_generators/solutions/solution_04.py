"""Solution 04 -- The same iterator, twice over."""


class Countdown:
    """The Java shape: state in attributes, and __next__ raising to stop."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


def countdown(start):
    """The same thing. The state is the paused function."""
    while start > 0:
        yield start
        start -= 1


print(list(Countdown(3)))
print(list(countdown(3)))
print(list(Countdown(3)) == list(countdown(3)))
print(type(countdown(3)).__name__)
