"""Solution 09 (bonus) -- The whole application, tested."""

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().parent.parent / "app.py"


def run_with(above):
    """Run the app, move the slider, and return the three metrics."""
    app = AppTest.from_file(str(APP), default_timeout=30)
    app.run()
    if above is not None:
        app.slider[0].set_value(above).run()
    return app


app = run_with(None)

print([e.value for e in app.exception] or "none")
print(app.title[0].value)
print([(m.label, m.value) for m in app.metric])
print(len(app.dataframe[0].value), sorted(app.multiselect[0].value))

# Only the third metric depends on the slider: the other two are facts about the
# file rather than about the question being asked.
for above in (20.0, 100.0):
    moved = run_with(above)
    print(above, [m.value for m in moved.metric])
