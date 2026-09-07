# Solution 07 — Four ways to say "call this"

**a) What each mistake is a mistake in**

- **tkinter, `command=self.bump()`** — a mistake in the **value passed**.
  `self.bump()` is a perfectly valid expression that evaluates to `None`, and `None`
  is a legal thing to pass as `command`: Tk reads it as "this widget has no command",
  which is a state a button is allowed to be in. Nothing can catch it because nothing
  is wrong. The types are compatible, the call succeeds, and the only evidence is that
  the counter is at 1 before anybody pressed anything.
- **Textual, `def on_button_press`** — a mistake in the **name of the thing**.
  `on_button_press` is a perfectly valid method: correct signature, correct body,
  never looked up. Nothing can catch it because Textual does not know what methods you
  *meant* to write. The lookup is `getattr(self, message.handler_name, None)`, and a
  missing handler is the normal case — most messages have no handler on most widgets,
  so an absent one cannot be an error.
- **Flask, `@app.get("/summry")`** — a mistake in **a string inside it**. The
  decorator did its job perfectly and registered the endpoint `summary` at the path
  `/summry`. Nothing can catch it because a path is data: Flask has no way to know
  which URLs you intended, and a URL that nobody requests is not distinguishable from
  a URL that does not exist yet. Measured: `/summry` answers 200, `/summary` answers
  404, and `app.url_map` lists the endpoint under its correct Python name.

The pattern across all three: **the mistake is a valid value in a position where the
framework has no expectations to check it against.** A type checker cannot help
because nothing is mistyped; a linter cannot help because nothing is unused or
unreachable.

**Streamlit is the exception, and it is a consequence.** There is no way to make this
mistake there because there is nothing to register: the script runs top to bottom on
every interaction, and a widget call *returns* the widget's current value. No name is
looked up, no function is stored, no string is matched. But that freedom is not a
design win Streamlit chose — it is what is left over after giving up the request
cycle. Because there is no registration there is also no way to say "run this when
that happens", which is why `st.session_state` had to exist at all and why module 22
listed the three things Streamlit cannot do. **The bug class is absent because the
mechanism is absent.**

**b) What to ask instead of guessing**

- tkinter: **`widget.cget("command")`**. It returns Tk's internal command name, or the
  empty string when there is none. Measured in module 24's notebook: `''` for the
  broken button.
- Textual: **`Button.Pressed.handler_name`** — every message class carries the method
  name it will be delivered to. `'on_button_pressed'`, which is the answer, not a
  recollection of it.
- Flask: **`app.url_map`**, or `[str(r) for r in app.url_map.iter_rules()]`. It lists
  every path the application will actually answer, which is the only place the
  difference between `/summary` and `/summry` is visible.

Worth noticing that all three are *introspection on the running program* rather than a
static check. That is the shape of debugging a registration problem: you cannot read
it off the source, so you ask the object.

**c) Convention against decorator**

**What the convention buys that the decorator cannot:** the handler is discoverable
from the message. Given a `Button.Pressed`, Textual can find its handler on any widget
in the tree without anything having been registered anywhere — which is how a message
can bubble from a button up through its container to the app, with each level free to
handle it or not. A decorator registers *one* function in *one* place at import time,
and cannot express "whoever above me cares about this". Bubbling is the feature, and
it needs the lookup to be by name.

**What the decorator buys that the convention cannot:** the registration is visible in
the diff. `@app.get("/summary")` on a line means that line created a route; a method
named `on_button_pressed` looks exactly like a method named `on_button_press`, and
neither looks like a registration at all. You can also read all of an application's
routes by grepping for the decorator, and you cannot read all of a Textual app's
handlers without knowing every message name in advance.

**In a codebase eight people work on: the decorator.** Not because the convention is
worse, but because the cost of the convention is paid by the reader and the reader is
now seven other people. A convention is a shared secret, and a shared secret across
eight people with different start dates is a source of exactly the bug in (a).

**Alone, the convention is fine** — you hold the naming rules in your head, the
codebase is small enough to grep, and the bubbling is worth having. The honest
generalisation: implicit mechanisms scale with how much context the reader already
has, and a team is defined by not sharing context.

**d) The binding string, and what a type checker can see**

Renaming `action_worse` to `action_higher` while `BINDINGS` still says `"worse"`
produces a file that is **completely clean**. mypy sees a method with correct
annotations that is never called from within the class — which is true of every
handler in every Textual app, so it cannot be an error. `self.limit += 2.0` is a
valid operation on a `float` reactive. Ruff sees no unused import, no undefined name,
no unreachable code. There is nothing to report.

What that tells you about type checkers: **a type checker verifies that the values
flowing through your program fit together. It cannot verify that your program is
connected up**, because connection here is a string matched against an attribute name
at run time, and a string is a value like any other. The moment a framework's wiring
lives in data — a path, a key name, a binding, a template filename, a column name in
a SQL string — the checker is outside the part that can go wrong.

Which is exactly the boundary module 23 drew from the other side. There the
annotations became the parser, so the checker's reach *grew*: `minimum: float` is
verified and enforced. Here the wiring is a string, so the reach ends. Same course,
same tool, and the difference is entirely whether the framework encoded its contract
in types or in text.
