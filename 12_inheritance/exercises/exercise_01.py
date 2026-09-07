"""Exercise 01 -- Inheritance, and the call that is not automatic.

`Sensor` extends `Device` with a unit. Write both classes so that `Sensor` sets the
tag through its parent rather than by assigning it again, and so that its `describe`
adds to the parent's result rather than repeating it.

Expected output:

    device TH-04 (C)
    ['tag', 'unit']
    True True
    device TH-09

Hint: `super().__init__(tag)` in `Sensor.__init__`, and `super().describe()` inside
`Sensor.describe()`. The second line of the output is `sorted(vars(sensor))` -- it
shows that both attributes really are on the object.
"""


# TODO: Device, then Sensor

sensor = Sensor("TH-04", "C")

print(sensor.describe())
print(sorted(vars(sensor)))
print(isinstance(sensor, Device), issubclass(Sensor, Device))
print(Device("TH-09").describe())
