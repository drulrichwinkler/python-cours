# Modul 01 — Python-Grundlagen

**Dauer:** etwa 2 Stunden · **Setzt voraus:** nichts · **Rückkanal:** `entdecken.ipynb` sagt
grün oder rot, jede Aufgabendatei nennt ihre erwartete Ausgabe

## Worum es geht

Variablen, die vier Grundtypen, Ein- und Ausgabe — und die zwei Fallen, über die jeder stolpert:
`bool("False")` und `0.1 + 0.2`. Dazu die Fertigkeit, die im Rest des Kurses am meisten trägt:
**eine Fehlermeldung lesen**.

## Was Sie danach können

1. eine `.py`-Datei anlegen und mit `uv run` **ausführen**;
2. eine Python-Fehlermeldung **lesen** und die verursachende Zeile benennen;
3. für ein Codestück mit Variablen, Zahlen und Strings die Ausgabe **vorhersagen**,
   ohne es auszuführen;
4. `int`, `float`, `str`, `bool` und `None` **unterscheiden** und begründen, warum
   `int("3.5")` scheitert, `int(3.5)` aber nicht;
5. eine formatierte Ausgabe mit f-Strings **erzeugen**.

Wenn Sie eines davon nicht an einer Aufgabe zeigen können, ist das Modul nicht fertig.

## Reihenfolge

1. **`entdecken.ipynb`** — acht Vorhersagen, etwa 30 Minuten. Öffnen mit
   `uv run jupyter lab` (oder in VS Code direkt anklicken).
2. **`uebungen/`** — sechs Aufgabendateien zum Ausfüllen, zwei zum Nachdenken in
   `aufgaben.md`, ein Bonus.
3. **`uebungen/loesungen.py`** — zuletzt, zum Vergleichen.

## Noch nicht erlaubt

`if`, `else`, Schleifen und eigene Funktionen. Die kommen in Modul 03 und 04. Alle Aufgaben hier
lassen sich ohne sie lösen — wenn Sie das Gefühl haben, ein `if` zu brauchen, fehlt Ihnen ein
Ausdruck, kein Sprachmittel.
