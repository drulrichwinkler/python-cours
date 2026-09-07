"""Solution 02 -- Predict what pandas does.

dtype            is 'str'. pandas picks a type per column from the data, and one
                 cell reading 'kaputt' in fifty makes the whole column text. It is
                 not in pandas' default NA list, which does include 'n/a', 'NA',
                 'null' and a dozen more.
the arithmetic   is not one behaviour, and that is the lesson. .sum() CONCATENATED
                 the strings and returned a str -- no error, and a result starting
                 '20.722.4...' that is a total of nothing. .max() gave the largest
                 string alphabetically, also a str. .mean() raised TypeError.
                 `> 85` raised TypeError. And `> "85"` compared as TEXT and
                 happily returned a count. Two of the five refuse, three do
                 something else quietly, and there is no rule to remember about
                 which.
describe()       is the cheapest way to notice: on a text column it gives count,
                 unique, top and freq instead of mean and std. Four rows that are
                 not the four rows you were expecting.
na_values        makes the column float64; parse_dates makes `at` a datetime
                 rather than text, which is what lets .dt work later.
len vs count     is 50 against 47. count() skips NaN and len() does not, so a
                 report saying "average of 50 readings" after calling .mean() is
                 wrong by three.
mask             is a Series of dtype bool, one entry per row, and .sum() counts
                 the True ones -- 3.
`and`            raises ValueError: a Series of fifty booleans has no single truth
                 value, which is module 02's `and` returning an operand with no
                 operand to return. Use & and bracket each side.
NaN              is not equal to itself, which is why pd.isna exists and why you
                 never write == None or == NaN.
"""

from pathlib import Path

import pandas as pd

READINGS = Path(__file__).resolve().parent.parent / "data" / "readings.csv"

raw = pd.read_csv(READINGS, sep=";")

assert str(raw["value"].dtype) == "str"


assert type(raw["value"].sum()).__name__ == "str"
assert type(raw["value"].max()).__name__ == "str"

try:
    raw["value"].mean()
    mean_outcome = "worked"
except TypeError:
    mean_outcome = "TypeError"

assert mean_outcome == "TypeError"

try:
    raw["value"] > 85
    compare_outcome = "worked"
except TypeError:
    compare_outcome = "TypeError"

assert compare_outcome == "TypeError"


assert type((raw["value"] > "85").sum()).__name__ in ("int64", "int")


assert raw["value"].describe().index.tolist() == ["count", "unique", "top", "freq"]


clean = pd.read_csv(READINGS, sep=";", na_values=["kaputt"], parse_dates=["at"])

assert str(clean["value"].dtype) == "float64"
assert str(clean["at"].dtype).startswith("datetime64")


assert len(clean) == 50
assert clean["value"].count() == 47


mask = clean["value"] > 85

assert type(mask).__name__ == "Series"
assert str(mask.dtype) == "bool"
assert mask.sum() == 3


try:
    clean[(clean["value"] > 85) and (clean["location"] == "Test rig")]
    joined = "worked"
except ValueError:
    joined = "ValueError"

assert joined == "ValueError"


assert (float("nan") == float("nan")) is False
assert pd.isna(float("nan")) is True
