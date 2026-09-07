# Solution 08 — The mean of what, exactly

**a) Four correct numbers, one answer**

| | answers |
| --- | --- |
| `len(frame)` = **50** | how many rows the file has |
| `count()` = **47** | how many rows have a readable value |
| `mean()` = **26.721** | the average of the 47 readings that exist |
| `fillna(0).mean()` = **25.118** | the average of 47 readings and three invented zeroes |

The one that answers "what is the average reading" is **26.721** — `mean()`, which
skips the missing values. The fourth is not an average of anything that happened: it
is the average of a dataset that includes three thermometers at exactly freezing
point, which no thermometer reported.

**b) The report sentence**

> "average temperature across 50 readings: 26.7 °C"

Two things wrong:

1. **It was not 50 readings.** It was 47. `mean()` skipped three and the sentence
   counted them.
2. **"average temperature" is doing a lot of work.** The 47 readings come from three
   locations, one of which is a test rig that spent two hours above 91 °C. The mean
   over all of them is a number without a referent — it is not the temperature of
   anywhere. The per-location means (22.12, 22.34, 32.83) are three facts; their
   pooled average is not a fourth.

The sentence that is right:

> "Average of 47 usable readings from 50 recorded, 1 March 2026: Hall 22.1 °C,
> Office 22.3 °C, test rig 32.8 °C. Three values could not be read."

Longer, and every clause is defensible.

**c) Where `fillna(0)` is right**

A column where **zero is what the absence means**. For example a `faults` count per
hour, where a missing row means no fault was recorded — the event did not happen, and
"did not happen" is zero. Or `items_sold` for a day with no transactions, or
`rainfall_mm` from a gauge that only reports when it is wet.

What distinguishes those from a temperature: **whether the absence is itself
information about the value.** For a fault count, "nothing was written" means "there
were none" — the absence carries the value. For a temperature, "nothing was written"
means the sensor failed or the cell was unreadable; the true value existed and is
unknown, and it was certainly not 0 °C.

The general rule: **`fillna(x)` is a claim about the world, and it needs the same
justification as any other claim.** The question to ask is not "what number keeps the
code running" but "what do I know about the value that is not there". Where the answer
is "nothing", the honest fill is no fill — `dropna()` and a count of what was dropped.

**d) The three unreadable values, in a report you sign**

Report them. Concretely, three things:

1. **State the count in the output**, next to the number they affect: "47 of 50
   readings usable". `size` against `count` in exercise 09's summary does exactly this,
   per location, which is why the report has both columns.
2. **Say what they were.** Two were spelled `n/a` and one `kaputt` — that is not noise,
   it is a fact about the recording process, and the `kaputt` one suggests a different
   cause from the other two. Somebody who maintains that sensor would want to know.
3. **Do not fill them.** See (c).

Why "drop them" is a decision rather than a default: dropping changes what the number
is the average *of*, and it does so silently. If the three missing values were all
from the test rig at its hottest, dropping them would lower the reported mean and hide
the event the report exists to describe.

Here they are not. Checked:

```
TH-07;n/a;°C;Office;2026-03-01T10:00
TH-01;n/a;°C;Hall;2026-03-01T14:00
TH-09;kaputt;°C;Hall;2026-03-01T16:00
```

Three different sensors, two locations, none of them the test rig and none of them
during the fault. So dropping is defensible — but that had to be **looked at**, and
the looking is the decision. A default cannot make it, because a default does not know
which rows are missing.
