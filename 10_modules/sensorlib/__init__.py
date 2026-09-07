"""A tiny package, so that this module has something real to import.

A folder with an __init__.py is a package. This file runs once, the first time
anything under `sensorlib` is imported -- which makes it the place for the few
names the package wants to offer directly.
"""

from sensorlib.parsing import ParseError, to_reading

VERSION = "1.0"

# __all__ names what `from sensorlib import *` should hand out. Without it, the
# star form takes every name that does not begin with an underscore -- including
# the modules and imports that happen to be here.
__all__ = ["ParseError", "VERSION", "to_reading"]
