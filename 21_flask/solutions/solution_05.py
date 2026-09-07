"""Solution 05 -- Escaping, and what |safe undoes."""

from flask import Flask, render_template_string

app = Flask(__name__)

HOSTILE = "<script>alert('xss')</script>"

with app.app_context():
    # Jinja2 escapes by default, so the text lands in the page as text.
    print(render_template_string("<p>{{ text }}</p>", text=HOSTILE))
    # |safe says "this is markup and I trust it" -- and here it is a script the
    # browser will run. Text from outside became syntax on the inside, which is
    # module 19's SQL injection in a different language.
    print(render_template_string("<p>{{ text|safe }}</p>", text=HOSTILE))
    print(render_template_string("<p>{{ text }}</p>", text="Müller & Co"))
    print("<" in render_template_string("<p>{{ t }}</p>", text="x", t=HOSTILE)[3:-4])
