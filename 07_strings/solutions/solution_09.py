"""Solution 09 (bonus) -- Parse a log line into a dict."""


def parse(line):
    """Turn 'tag=TH-04; value=91.0; unit=C' into a dict of stripped strings."""
    record = {}
    for field in line.split(";"):
        # maxsplit=1 keeps a value that contains an = sign in one piece.
        key, raw = field.split("=", 1)
        record[key.strip()] = raw.strip()
    return record


line = " tag=TH-04; value=91.0; unit=C "

record = parse(line)
print(record)
print(record["value"], float(record["value"]) > 85)
print(sorted(record))
print(parse("tag=TH-09"))
