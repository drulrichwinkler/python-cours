"""Exercise 05 -- Escaping, and what |safe undoes.

Render the hostile string four ways and print what comes out:

  1. `<p>{{ text }}</p>` with `text=HOSTILE`
  2. `<p>{{ text|safe }}</p>` with the same
  3. `<p>{{ text }}</p>` with `text="Müller & Co"`
  4. whether a `<` survives inside the escaped body of `<p>{{ t }}</p>` with
     `t=HOSTILE` -- as True or False

Expected output:

    <p>&lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt;</p>
    <p><script>alert('xss')</script></p>
    <p>Müller &amp; Co</p>
    False

Hint: line 2 is a script the browser would run -- text from outside became syntax on
the inside, which is module 19's SQL injection in a different language. For line 4,
slice the `<p>` and `</p>` off the result and ask whether `<` is in what is left.
"""

from flask import Flask, render_template_string

app = Flask(__name__)

HOSTILE = "<script>alert('xss')</script>"

# TODO: four prints inside `with app.app_context():`
