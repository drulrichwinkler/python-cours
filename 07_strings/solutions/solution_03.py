"""Solution 03 -- Repair a comparison."""


def is_faulty(tag, faulty_tag):
    # `is` asks whether the two names refer to one object. It happens to say True
    # for two literals in the source and False for anything built at runtime,
    # which is why the second call was wrong. == compares content.
    return tag == faulty_tag


print(is_faulty("TH-04", "TH-04"))
print(is_faulty("".join(["TH", "-04"]), "TH-04"))
print(is_faulty("TH-09", "TH-04"))
