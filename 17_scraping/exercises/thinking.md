# Module 17 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 17_scraping`.

---

## Exercise 07 — The repair nobody asked for

The same three readings, once with closing tags and once without:

```python
[c.get_text(strip=True) for c in good_row.select("td")]
# ['TH-01', '21.7', '°C']

[c.get_text(strip=True) for c in sloppy_row.select("td")]
# ['TH-0121.7TH-0491.0', '21.7TH-0491.0', 'TH-0491.0', '91.0']
```

a) Explain what the parser did, in terms of the tree it built. Why four cells, and
   why does the first one contain every value on the page?
b) A parser that raised on malformed HTML would be correct and useless. Say why
   useless — what fraction of the web would it reject, and what would that mean for
   the library's users? Then say what that implies about who owns the problem.
c) This is the third time in this course that a tool has guessed rather than failed:
   `latin-1` in module 08, the missing charset in module 16, and this. Name what the
   three have in common as a **failure profile**, and say why that profile is worse
   than an exception even though it looks friendlier.

> **Hint on (a):** if `<td>` is never closed, where can the next `<td>` go? Is it a
> sibling or a child?
> **Hint on (c):** at what point does somebody find out, and what is in their hands
> when they do?

**Check yourself:** your answer to (c) has to name the cost in terms of *when* the
failure is discovered, not just that it is silent.

---

## Exercise 08 — When scraping is the wrong tool

You are asked to collect the readings from a page every hour.

a) Before writing a scraper, three things are worth checking. Name them, in the order
   you would check them, and say what each one would save you.
b) The page turns out to load its table with JavaScript, so the value is not in
   `response.text`. Name the three options from section 6 and say which you would
   take and why. Then say what you would do if the network tab shows the page
   fetching `/api/readings.json` — and what that means for `robots.txt`.
c) Your scraper works for six weeks and then returns empty lists every hour, silently.
   Name the two most likely causes, and say what one line in the scraper would have
   turned this into a message on week one instead of a gap in your data.

> **Hint on (a):** one of the three is a question about the page, one is a question
> about the site, and one is a question you can only answer by asking somebody.
> **Hint on (c):** what does `select_one` return when the page has been redesigned?

**Check yourself:** your answer to (c) has to name the line, and it is a line this
module has already written twice.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
