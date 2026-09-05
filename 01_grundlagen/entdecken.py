"""Modul 01 — Vorbereitung: Python-Grundlagen.

So arbeiten Sie mit dieser Datei:

  1. Drucken Sie `entdecken.md` aus oder legen Sie ihn neben sich.
  2. Lesen Sie einen Abschnitt und schreiben Sie Ihre Vorhersage in das passende Feld.
     Erst hinschreiben, dann weiterlesen. Auch wenn Sie unsicher sind -- besonders dann.
  3. Wenn alle acht Felder ausgefuellt sind: `uv run 01_grundlagen/entdecken.py`
  4. Vergleichen Sie. Jede falsche Vorhersage ist eine Stelle, an der Sie etwas gelernt haben.

Dauer: etwa 30 Minuten.
"""

print("=== 1. print() mit mehreren Argumenten ===")
# VORHERSAGE (Feld 1): Was steht in den beiden Zeilen -- genau, mit allen Zeichen?
print("Sensor", "Temperatur", "OK")
print("Sensor", "Temperatur", "OK", sep=" | ")

print()
print("=== 2. Zuweisung ist keine Gleichung ===")
# VORHERSAGE (Feld 2): Welche Zahl wird ausgegeben?
a = 5
b = a
a = 10
print(b)

print()
print("=== 3. Zwei Arten zu teilen ===")
# VORHERSAGE (Feld 3): Drei Werte. Welche?
print(7 / 2)
print(7 // 2)
print(7 % 2)

print()
print("=== 4. Der Typ haengt am Wert ===")
# VORHERSAGE (Feld 4): Was gibt type() jeweils aus?
print(type(42))
print(type("42"))
print(type(42.0))

print()
print("=== 5. Umwandeln -- und was dabei verloren geht ===")
# VORHERSAGE (Feld 5): Wird 3.9 zu 3 oder zu 4?
print(int(3.9))
print(float("3.14"))
print(str(42) + "!")

print()
print("=== 6. f-Strings ===")
# VORHERSAGE (Feld 6): Beide Zeilen genau hinschreiben.
temperatur = 23.456
print(f"Es sind {temperatur} Grad.")
print(f"Es sind {temperatur:.1f} Grad.")
print(f"{temperatur=}")

print()
print("=== 7. Wahr und falsch -- die Falle ===")
# VORHERSAGE (Feld 7): Vier Werte. Achtung bei der letzten Zeile.
print(bool(0))
print(bool(""))
print(bool("0"))
print(bool("False"))

print()
print("=== 8. Die beruehmteste Ueberraschung ===")
# VORHERSAGE (Feld 8): Was ist 0.1 + 0.2? Schreiben Sie es GENAU hin.
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

print()
print("-- Ende von entdecken.py --")
