"""Solution 06 -- Two days of tags."""

today = {"TH-01", "TH-04", "TH-09", "TH-12"}
yesterday = {"TH-04", "TH-09", "TH-11"}

print(sorted(today & yesterday))
print(sorted(today - yesterday))
print(sorted(today ^ yesterday))
print(len(today | yesterday))
print(today <= yesterday)
