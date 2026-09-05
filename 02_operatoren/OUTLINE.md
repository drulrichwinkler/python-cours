# Modul 02 — Operatoren und Ausdrücke

**Dauer:** etwa 1,5 Stunden · **Setzt voraus:** Modul 01 · **Rückkanal:** `entdecken.ipynb`
sagt grün oder rot, jede Aufgabendatei nennt ihre erwartete Ausgabe

## Worum es geht

Rechnen, vergleichen, verknüpfen. Drei Dinge daraus lohnen mehr Aufmerksamkeit als der Rest:
`is` gegen `==` (die häufigste Verwechslung der Sprache), die Kurzschlussauswertung (sie
entscheidet über Absturz oder nicht) und **Bitmasken** — Ihr erster Berührungspunkt mit der Art,
wie Geräte tatsächlich ihren Zustand melden.

## Was Sie danach können

1. für einen arithmetischen Ausdruck die **Auswertungsreihenfolge** angeben und das Ergebnis
   vorhersagen — einschließlich `**`, `//` und `%`;
2. eine vollständige **Wahrheitstabelle** für `and` und `or` aufstellen;
3. **begründen**, warum `==` und `is` verschiedene Fragen stellen, und angeben, welche der
   beiden man auf Werte anwendet;
4. aus einem Statusbyte mit `&` ein Bit **auslesen** und mit `|` eines **setzen**;
5. eine Bereichsprüfung als **Operator-Kette** schreiben (`1 < x < 10`) und erklären, warum das
   nicht dasselbe ist wie `(1 < x) < 10`.

## Reihenfolge

1. **`entdecken.ipynb`** — acht Vorhersagen, etwa 25 Minuten
2. **`uebungen/`** — sieben Aufgabendateien, eine Denkaufgabe in `aufgaben.md`, ein Bonus
3. **`uebungen/loesungen.py`** — zuletzt

## Noch nicht erlaubt

`if`, `else`, Schleifen, eigene Funktionen. Das gilt hier besonders: Mehrere Aufgaben sehen aus,
als bräuchten sie eine Verzweigung, und lassen sich doch als **ein boolescher Ausdruck**
schreiben. Genau das ist der Punkt des Moduls.
