"""Solution 05 -- Equality, and what it costs."""


class Reading:
    def __init__(self, tag, celsius):
        self.tag = tag
        self.celsius = celsius

    def __repr__(self):
        return f"Reading(tag={self.tag!r}, celsius={self.celsius})"

    def __eq__(self, other):
        # NotImplemented rather than False: it lets the other operand try, and
        # Python falls back to identity if nobody knows.
        if not isinstance(other, Reading):
            return NotImplemented
        return (self.tag, self.celsius) == (other.tag, other.celsius)

    def __hash__(self):
        # Defining __eq__ sets __hash__ to None. Over the same fields, and only
        # because those fields are not meant to change.
        return hash((self.tag, self.celsius))


a = Reading("TH-04", 91.0)
b = Reading("TH-04", 91.0)

print(a == b, a is b)
print(a == "TH-04")
print(len({a, b}))
print(sorted({a, b}, key=lambda r: r.celsius))
