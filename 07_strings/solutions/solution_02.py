"""Solution 02 -- Predict what strings do.

name is ...      is True against the other literal: the compiler keeps one object
                 per literal, so two literals that read the same are one object.
                 `built` is assembled at runtime and is a different object, so
                 `is` is False there -- while `==` is True either way, because ==
                 looks at content.
tag.strip()      hands back the same object when there is nothing to strip; an
                 optimisation you are not meant to notice, and one more reason
                 `is` is the wrong question for strings. .upper() builds a new
                 object even when the text is already upper case.
line.split()     splits on runs of whitespace and drops the empties, giving
                 ['a', 'b', 'c']. line.split(" ") treats every single space as a
                 separator and keeps what is between two of them: nine pieces,
                 six of them empty.
join             raises TypeError. It concatenates strings and converts nothing.
len              counts code points: 8 for "Übergabe". .encode("utf-8") makes
                 bytes, and "Ü" needs two of them, so 9.
"TH-04"[:]       is the same object -- a string cannot change, so there is nothing
                 to protect. values[:] is a copy, because a list can.
"""

name = "TH-04"
from_source = "TH-04"
built = "".join(["TH", "-04"])

assert (name is from_source) is True
assert (name is built) is False
assert (name == built) is True


tag = "TH-04"

assert (tag.strip() is tag) is True
assert (tag.upper() is tag) is False


line = "  a b   c  "

assert line.split() == ["a", "b", "c"]
assert len(line.split(" ")) == 9


try:
    ";".join(["a", 1])
    outcome = "worked"
except Exception as err:
    outcome = type(err).__name__

assert outcome == "TypeError"


word = "Übergabe"

assert len(word) == 8
assert len(word.encode("utf-8")) == 9


text = "TH-04"
values = [1, 2]

assert (text[:] is text) is True
assert (values[:] is values) is False
