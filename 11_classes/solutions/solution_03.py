"""Solution 03 -- Repair a shared class attribute."""


class Logbook:
    def __init__(self, owner):
        self.owner = owner
        # The list belonged to the class, so every logbook appended to the same
        # one. Built here instead, each object gets its own.
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)


first = Logbook("TH-04")
second = Logbook("TH-09")

first.add("91.0")
second.add("23.1")

print(first.entries)
print(second.entries)
print(first.entries is second.entries)
