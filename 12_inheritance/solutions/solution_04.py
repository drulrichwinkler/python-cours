"""Solution 04 -- A type that works with for, in and len."""


class Log:
    def __init__(self, readings):
        self.readings = readings

    def __len__(self):
        return len(self.readings)

    def __iter__(self):
        return iter(self.readings)

    def __contains__(self, value):
        return value in self.readings

    def __getitem__(self, index):
        return self.readings[index]


log = Log([21.7, 91.0, 23.1])

print(len(log))
print([value for value in log])
print(91.0 in log, 0.0 in log)
print(log[0], log[-1])
print(max(log), sorted(log))
# With no __bool__, an object with __len__ is falsy when the length is zero.
print(bool(log), bool(Log([])))
