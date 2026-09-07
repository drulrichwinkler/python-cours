"""Exercise 03 -- Repair a shared class attribute.

Two logbooks, one entry each. Run it: both contain both entries, and the last line
says they are the same list.

Find the line that made one list instead of two, and fix it.

Expected output:

    ['91.0']
    ['23.1']
    False

Hint: a name assigned in the class body belongs to the class, and there is one of it.
A name assigned in `__init__` belongs to the object, and there is one per object.
"""


class Logbook:
    entries = []  # TODO: the bug is in this line

    def __init__(self, owner):
        self.owner = owner

    def add(self, entry):
        self.entries.append(entry)


first = Logbook("TH-04")
second = Logbook("TH-09")

first.add("91.0")
second.add("23.1")

print(first.entries)
print(second.entries)
print(first.entries is second.entries)
