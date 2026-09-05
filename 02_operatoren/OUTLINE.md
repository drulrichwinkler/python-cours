# Modul 02 — Operatoren und Ausdrücke

**Umfang:** ½ Block Präsenz (~45 min) · **Setzt voraus:** Modul 01 · **Artefakte:**
`entdecken.py`, `entdecken.md`, `folien.md`, `uebungen/`

**Warum nur ein halber Block:** Die Syntaxlisten (Folien 3–7, 12–13) sind rein nachschlagbar und
gehören in die Vorbereitung. Präsenz bleibt für die drei Dinge, die man nicht nachliest:
`is` gegen `==`, Kurzschlussauswertung und Bitmasken.

## Lernziele

Nach diesem Modul können Sie:

1. für einen gegebenen arithmetischen Ausdruck die **Auswertungsreihenfolge** angeben und das
   Ergebnis vorhersagen — einschließlich `**`, `//` und `%`;
2. eine vollständige **Wahrheitstabelle** für `and`, `or` und `not` aufstellen;
3. **begründen**, warum `==` und `is` verschiedene Fragen stellen, und angeben, welche der
   beiden man auf Werte anwendet;
4. aus einem Statusbyte mit `&` ein einzelnes Bit **auslesen** und mit `|` eines **setzen**;
5. eine Bereichsprüfung als **Operator-Kette** schreiben (`1 < x < 10`) und erklären, warum
   das nicht dasselbe ist wie `(1 < x) < 10`.

## Was hier *nicht* mehr steht

Die frühere Übung 8 („Altersgruppe: Kind / Teenager / Erwachsener / Senior") ist nach **Modul 03**
gewandert. Sie verlangt `if`/`elif` — Kontrollstrukturen, die es hier noch nicht gibt. An ihre
Stelle tritt Aufgabe 6, dieselbe Fragestellung als reiner boolescher Ausdruck.

## Nachbereitung — genau eine Sache

**Auftrag:** Nehmen Sie das Statusbyte `0b0000_1010` und schreiben Sie ein Skript
`status.py`, das für alle vier Flags in je einer Zeile ausgibt, ob sie gesetzt sind — ohne `if`.
**Abgabe:** die Datei, bis zur nächsten Sitzung.
