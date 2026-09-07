"""Exercise 03 -- Repair a comparison.

`is_faulty` is meant to say whether two tags are the same tag. It gets the first
call right and the second one wrong -- and the second one is the realistic case,
because a tag read from a file is assembled while the program runs.

Run it, see which line is wrong, then fix the function. Do not change the calls.

Expected output:

    True
    True
    False

Hint: `is` asks whether two names refer to one object. That is not the question.
"""


def is_faulty(tag, faulty_tag):
    return tag is faulty_tag  # TODO: the bug is in this line


print(is_faulty("TH-04", "TH-04"))
print(is_faulty("".join(["TH", "-04"]), "TH-04"))
print(is_faulty("TH-09", "TH-04"))
