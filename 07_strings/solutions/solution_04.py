"""Solution 04 -- Take a line apart and put it back together."""

line = "  TH-04 ; 91.0 ; C  "

fields = [field.strip() for field in line.split(";")]
print(fields)

tag, value, unit = fields
print(f"{tag} {float(value):.1f} {unit}")

print("|".join(fields))
print(line.split())
