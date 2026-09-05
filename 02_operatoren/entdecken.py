"""Modul 02 -- Vorbereitung: Operatoren und Ausdruecke.

So arbeiten Sie mit dieser Datei:

  1. `entdecken.md` danebenlegen.
  2. Abschnitt lesen, Vorhersage ins Feld schreiben. Erst danach weiterlesen.
  3. Wenn alle sieben Felder gefuellt sind: `uv run 02_operatoren/entdecken.py`
  4. Vergleichen. Wo Sie danebenlagen, notieren Sie in einem Satz, was Sie erwartet hatten.

Dauer: etwa 25 Minuten. Voraussetzung: Modul 01.
"""

print("=== 1. Drei Arten zu teilen ===")
# VORHERSAGE (Feld 1): Vier Werte. Achten Sie beim ersten auf den Typ.
print(6 / 3)
print(7 // 2)
print(7 % 2)
print(17 % 5)

print()
print("=== 2. Modulo mit negativer Zahl ===")
# VORHERSAGE (Feld 2): Wenn Sie C oder Java kennen, raten Sie zweimal.
print(-17 % 5)

print()
print("=== 3. Wer bindet staerker? ===")
# VORHERSAGE (Feld 3): Drei Werte. Keiner davon ist offensichtlich.
print(2 + 3 * 4)
print(2**3**2)
print(-(3**2))

print()
print("=== 4. Vergleiche ===")
# VORHERSAGE (Feld 4): Vier Wahrheitswerte.
print(5 == 5.0)
print("a" == "A")
print(1 < 5 < 10)
print(True + True)

print()
print("=== 5. Was `and` und `or` wirklich zurueckgeben ===")
# VORHERSAGE (Feld 5): Drei Werte -- und es sind nicht True/False.
print(0 or "leer")
print("a" and "b")
print(None or 0 or "x")

print()
print("=== 6. Ein Statusbyte auslesen ===")
# VORHERSAGE (Feld 6): status ist 0b0110. Welche vier Werte kommen heraus?
BEREIT = 0b0001
GRENZWERT = 0b0010
FEHLER = 0b0100
KALIBRIERUNG = 0b1000
status = 0b0110

print(status)
print(status & GRENZWERT)
print(status & BEREIT)
print(bool(status & FEHLER))

print()
print("=== 7. Gleich, oder dasselbe? ===")
# VORHERSAGE (Feld 7): Vier Wahrheitswerte. Der dritte ist die Falle.
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)
print(3 > 2 > 1)
print((3 > 2) > 1)

print()
print("-- Ende von entdecken.py --")
