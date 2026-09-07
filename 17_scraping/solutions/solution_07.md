# Solution 07 — The repair nobody asked for

**a) What the parser built**

`html.parser` has no rule that closes a `<td>` when the next one opens — it is not a
browser and does not implement HTML5's tag-omission table. So when it meets a second
`<td>` while the first is still open, the only place it can put it is **inside** the
first. Measured on the two-cell case:

```python
soup = BeautifulSoup('<tr class="row"><td class="tag">TH-01<td class="value">21.7', "html.parser")
td = soup.select_one("td")
[c.name for c in td.find_all(True)]      # ['td'] -- the second cell is a CHILD
```

The tree is `td.tag` containing `td.value`, not two siblings. Then two things
compound:

- **`select("td")` matches descendants**, so it finds the outer cell *and* the one
  nested inside it — and on the three-reading page, four levels of nesting, hence four
  matches for two readings.
- **`get_text()` returns all the text below a node**, so the outermost cell's text is
  its own plus everything nested inside it: `TH-01` + `21.7` + `TH-04` + `91.0`.

Which is why the first cell contains every value on the page. Both behaviours are
correct in isolation; the wrong answer comes from the tree, and the tree came from a
guess.

**b) Why a strict parser would be useless**

Because malformed HTML is not the exception, it is the norm. Unclosed `<td>`,
`<li>` and `<p>` are *legal* — HTML5 explicitly permits omitting those end tags — so
"malformed" would have to mean something stricter than the specification. Beyond that,
real pages have unescaped ampersands, attributes without quotes, tags closed in the
wrong order, and stray `</div>`s. A parser that raised would reject a large majority
of the web, which means nobody could use it to read the web, which is the only thing
it is for.

So the library cannot refuse. What follows is that **the problem is yours**: the
parser hands you a tree that is always well formed, whatever it was given, and it
cannot tell you which parts of that tree it invented. Nobody else is in a position to
check that a row has three cells. That is why the one `if` in section 5 is not
defensive programming for its own sake — it is the only place the check can happen.

**c) The failure profile the three share**

All three are **total functions where you wanted a partial one**: for every input they
return a value, and for some inputs that value is wrong.

- `latin-1` decodes all 256 byte values, so it never rejects; it returns `Â°C`.
- A `text/*` response with no charset gets a default rather than a question; it
  returns `Â°C`.
- An HTML parser repairs rather than rejecting; it returns four cells.

In every case the return type is right, the value is plausible, and nothing is
signalled. And the reason that is worse than an exception is **when** the failure is
discovered and **what** is in the discoverer's hands:

| | exception | silent wrong value |
| --- | --- | --- |
| discovered | at the line that caused it | weeks later, by a person reading output |
| by whom | you, while writing it | a customer, or nobody |
| in hand | a traceback naming the line | a database with bad rows in it and no record of when |
| cost | an incident | a data migration |

An exception is expensive for one minute. A silent wrong value is cheap for six weeks
and then expensive for a fortnight — and the version of the code that produced it has
been deployed two hundred times since.

The general rule this course keeps arriving at: **when a tool cannot fail, you have to
supply the failure.** Name the encoding, check the status, verify the shape.
