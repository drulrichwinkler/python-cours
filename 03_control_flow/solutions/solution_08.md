# Solution 08 — Translate, then argue

**a) With the index**

```python
worst = 0
for i in range(len(readings)):
    if readings[i] > readings[worst]:
        worst = i
print(f"{worst}: {readings[worst]}")
```

**b) With `enumerate`**

```python
worst_index, worst_value = 0, readings[0]
for i, value in enumerate(readings):
    if value > worst_value:
        worst_index, worst_value = i, value
print(f"{worst_index}: {worst_value}")
```

**c) The argument**

Count the subscripts. Version (a) has three — `readings[i]`, `readings[worst]`
twice — and every one of them is a place where a wrong index reads the wrong
element or raises `IndexError`. Version (b) has one, in the initialisation, and
the loop body has none at all.

That is the argument, and it is not about taste: (b) removes a class of mistake
rather than making a different-looking mistake less likely.

Two things worth noticing about (a):

- `for i in range(len(readings))` is the tell-tale of a translated loop. When you
  see it, the question is always whether the index is needed at all.
- Neither version handles an empty list. (a) prints `readings[0]` and raises;
  (b) raises on the initialisation. Python's own answer is
  `max(enumerate(readings), key=lambda pair: pair[1])`, which raises
  `ValueError: max() iterable argument is empty` — an error message that names
  the problem instead of the symptom.
