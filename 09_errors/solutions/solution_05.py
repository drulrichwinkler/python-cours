"""Solution 05 -- A context manager as a class."""


class Section:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"-> {self.name}")
        return self  # what `as` binds

    def __exit__(self, exc_type, exc, traceback):
        # The three arguments are None when the block ended normally. Returning a
        # false value lets the exception carry on; returning True would swallow it.
        raised = exc_type.__name__ if exc_type else "nothing"
        print(f"<- {self.name} ({raised})")
        return False


with Section("reading") as section:
    print("   in", section.name)

try:
    with Section("parsing"):
        raise ValueError("bad line")
except ValueError as err:
    print("caught:", err)
