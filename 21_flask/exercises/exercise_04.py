"""Exercise 04 -- A template with a loop and a condition.

Write a Jinja2 template that prints one line per location:
`location;usable;mean;status`, where the mean has two decimal places or `--` when
there is none, and the status is `fault` if the location has any faults and `ok`
otherwise.

Then a second template that prints `rows` or `no rows`, and two one-liners about
`None`.

Expected output:

    Hall;18;22.12;ok
    Office;9;22.34;ok
    Test rig;20;32.83;fault
    no rows
    None
    --

Hint: `{% for %}` / `{% endfor %}`, and `{%-` trims the whitespace before the tag so
the lines come out clean. `{{ "%.2f"|format(x) }}` formats. Lines 5 and 6 are the
point: `|default('--')` replaces an **undefined** value and `None` is defined, so the
test you want is `{{ v if v is not none else '--' }}`.
"""

from flask import Flask, render_template_string

from sensorreport import load_readings, summarise

app = Flask(__name__)

# TODO: the templates, then render them inside `with app.app_context():`
