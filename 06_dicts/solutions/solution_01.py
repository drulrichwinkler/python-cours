"""Solution 01 -- Read a record."""

sensor = {
    "tag": "TH-04",
    "unit": "C",
    "limits": {"low": -20.0, "high": 85.0},
}

print(sensor["tag"])
print(sensor["limits"]["high"])
print("calibrated" in sensor)
print(sensor.get("calibrated", "unknown"))
print(sorted(sensor))
