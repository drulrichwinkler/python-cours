# Solution 07 — Dict or class?

**a) What the class gives you**

1. **The field names are checked before the program runs.** `sensor.untit` is a name
   the editor and `mypy` can see is wrong; `sensor["untit"]` is a string, and a
   string is not wrong until it is looked up.
2. **The shape is written down in one place.** With the dict, the answer to "what
   keys does a sensor have" is whatever every writer happened to put in. With the
   class, it is the `__init__` signature, and a missing argument is an error at the
   call.
3. **Behaviour can live with the data** — `sensor.is_above_limit(reading)` belongs to
   the type, rather than being a free function that has to re-derive which keys it
   may assume.

Two more that are worth having: types on the fields, so `high` is a `float` and not
sometimes the string `"85.0"`; and a `repr` that identifies the object in a
traceback.

**b) Where the dict is right**

- **The keys are data, not design.** A JSON response, a config file, a CSV header, a
  database row: you do not know the keys while you are writing the code, and a class
  would only be a second copy of a shape that lives somewhere else.
- **The set of keys varies from record to record**, and code that asks `if "unit" in
  record` is saying something true about the data rather than working around a
  missing field.

A third, weaker one: at the edge of the program — parsing, transport — the data is a
dict anyway. Turning it into a class at the boundary is a decision worth making
deliberately, in one place, which is what `@dataclass` and module 12 are for.

**c) When each fails**

`sensor.untit` fails **when the file is read** — by the editor as you type, by
`mypy` in the build, and at import time in the sense that the attribute simply is not
there on a class that declares its fields. `sensor["untit"]` fails **when that line
runs**, which may be the error branch that fires once a week.

On a program running for a week, that is the whole difference. The dict version puts
the mistake in the one code path nobody exercised, at 3 a.m., in a `KeyError` whose
message is a misspelled string. A tool that never runs the program finds the first
kind and, for a plain dict, has nothing to look at in the second but a string.

One qualification, because it is the answer to "then why not always a class":
`typing.TypedDict` declares which keys a dict has, and `mypy` then reports
`sensor["untit"]` as `TypedDict "Sensor" has no key "untit"` — a dict at runtime, a
checked shape at build time. It is the right tool where the data has to stay a dict
(JSON in, JSON out) and the shape is nevertheless known. It changes the answer to
(a)(1), not the answer to (b).
