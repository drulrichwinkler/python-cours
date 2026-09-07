"""Exercise 09 (bonus) -- Parse a log line into a dict.

Write `parse(line)` turning

    tag=TH-04; value=91.0; unit=C

into `{"tag": "TH-04", "value": "91.0", "unit": "C"}`. Keys and values are stripped
of their spaces; the values stay strings -- converting is the caller's business.

Expected output:

    {'tag': 'TH-04', 'value': '91.0', 'unit': 'C'}
    91.0 True
    ['tag', 'unit', 'value']
    {'tag': 'TH-09'}

Hint: split on ";" for the fields, then split each field on "=" -- with maxsplit=1,
so that a value containing an = sign survives in one piece. The dict work is module
06.
"""


# TODO: write the function

line = " tag=TH-04; value=91.0; unit=C "

record = parse(line)
print(record)
print(record["value"], float(record["value"]) > 85)
print(sorted(record))
print(parse("tag=TH-09"))
