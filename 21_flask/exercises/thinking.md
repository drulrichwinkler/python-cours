# Module 21 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 21_flask`.

---

## Exercise 07 — Text from outside, syntax on the inside

Three of these are the same bug in three languages:

```python
connection.execute(f"SELECT * FROM readings WHERE tag = '{tag}'")   # module 19
render_template_string("<p>{{ text|safe }}</p>", text=comment)      # module 21
f"<p>{comment}</p>"                                                 # module 21
```

a) Name what the three have in common, precisely enough that the sentence covers all
   three. Then name the one thing that fixes all three, and say why it is the same
   fix.
b) Jinja2 escapes by default and `|safe` opts out. Say why that default is the right
   way round, and what it would cost to have it the other way.
c) `f"<p>{comment}</p>"` has no `|safe` in it and is just as unsafe. Say why — and
   then say what that implies about building HTML in Python at all.
d) There is a legitimate use for `|safe`. Describe one, and say what has to be true
   about the value for it to be legitimate.

> **Hint on (a):** what happens to the boundary between the thing you wrote and the
> thing somebody sent you?
> **Hint on (b):** which mistake do you want to be the one that requires typing
> something extra?

**Check yourself:** your answer to (a) has to work for the SQL case and the two HTML
cases without changing wording.

---

## Exercise 08 — Flask or Django

Flask gives you routing, templates, request parsing and a development server. That is
the list.

a) Name three things a real application needs that Flask does not include, and say
   what you would use for each.
b) For **this** application — read a CSV, show a table, one search box — Flask is
   about seventy lines including the templates. Say what Django would give you here
   that you do not need, and what it would cost.
c) Now change the application: users log in, there are permissions, somebody
   non-technical has to edit the sensor list, and there are thirty tables. Say which
   you would choose and give the two strongest reasons.
d) State the heuristic in one sentence, in a form somebody could apply without having
   used either framework.

> **Hint on (a):** where does the data live, who is allowed to see it, and how does
> the schema change over time?
> **Hint on (c):** what does "somebody non-technical has to edit it" cost you in
> Flask?

**Check yourself:** your answer to (d) has to be a question about the application, not
a preference about the framework.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
