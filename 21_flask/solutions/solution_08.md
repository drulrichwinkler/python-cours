# Solution 08 — Flask or Django

**a) Three things Flask does not include**

| what | what you would use |
| --- | --- |
| **a database layer** — models, a query API, connection handling | SQLAlchemy, or module 19's `sqlite3` directly for something this size |
| **users, login, sessions, permissions** | Flask-Login for the mechanics; the policy is yours to write |
| **schema migrations** — changing a table that already has data in it | Alembic |

Three more that come up as soon as an application is real: forms with validation
(WTForms), an admin interface (there is nothing — you write it), and a settings and
deployment story (yours to assemble).

None of that is a criticism. "Micro" is a description of scope, and the scope is
honest: Flask does routing, templates, request parsing and a development server, and
says so.

**b) What Django would give this application that it does not need**

Everything in the list above, plus a project layout with `settings.py`,
`urls.py`, an app directory and a `manage.py`; an ORM in front of a CSV file that has
no database; a migrations framework for a schema that does not exist; a user model,
sessions, CSRF middleware and an admin site for an application with no users and no
forms that write anything.

What it costs, concretely:

- **Reading the application takes longer.** This Flask app is one file of four
  functions and four templates, and there is nothing in it that was not chosen. The
  Django equivalent is a dozen files, most of them generated, and a reader has to know
  which parts matter.
- **You inherit conventions you did not need.** `settings.py` is the obvious one:
  fifty lines of configuration for features that are switched on.
- **The framework's answer is now in your way** in the one place you do something
  unusual — reading a CSV rather than a table.

For this application Flask is the better answer, and the reason is not that it is
smaller. It is that **there is nothing to explain**: seventy lines, all of them about
sensors.

**c) Users, permissions, a non-technical editor, thirty tables**

**Django**, and the two strongest reasons:

1. **The admin interface.** "Somebody non-technical has to edit the sensor list" is a
   whole application in Flask: list, create, edit, delete, validation, pagination,
   permissions — for every one of thirty tables. In Django it is a few lines per model
   and it exists. That is not a small convenience; it is the difference between a week
   of work and an afternoon, repeated thirty times.
2. **Thirty tables means the schema will change**, and changing a table that has data
   in it is a migrations problem. Django ships migrations that are generated from the
   models and applied in order; in Flask you assemble SQLAlchemy plus Alembic and own
   the wiring. Both work. One of them you did not have to decide.

The third reason, if a third is wanted: users and permissions are a solved problem
that is easy to get subtly wrong, and Django's version has been attacked for twenty
years.

**d) The heuristic**

> **Can you name everything this application needs? Then Flask. Would you rather not
> have to? Then Django.**

It is a question about the application rather than a preference about the framework,
and it is answerable before you have used either: write down what the thing must do.
If the list is short and specific, a framework that gives you exactly that is an
advantage. If the list is "the usual things a business application needs, and probably
some more later", the framework that already has them is worth the ceremony.

The failure mode in each direction is worth knowing too. Flask chosen for the second
kind of application becomes Django, badly, assembled by you over two years. Django
chosen for the first kind is a lot of scaffolding around four functions — annoying,
but not a trap.
