"""Solution 04 -- A template with a loop and a condition."""

from flask import Flask, render_template_string

from sensorreport import load_readings, summarise

app = Flask(__name__)

TEMPLATE = """
{%- for s in summaries %}
{{ s.location }};{{ s.usable }};
{{- "%.2f"|format(s.mean) if s.mean is not none else "--" }};
{{- "fault" if s.faults else "ok" }}
{%- endfor %}
"""

EMPTY = """
{%- if summaries %}rows{% else %}no rows{% endif %}
"""

with app.app_context():  # render_template_string needs one; a real request has it
    print(render_template_string(TEMPLATE, summaries=summarise(load_readings())).strip())
    print(render_template_string(EMPTY, summaries=[]).strip())
    # `is not none` and not |default: the default filter replaces an UNDEFINED
    # value, and None is defined.
    print(render_template_string("{{ v|default('--') }}", v=None))
    print(render_template_string("{{ v if v is not none else '--' }}", v=None))
