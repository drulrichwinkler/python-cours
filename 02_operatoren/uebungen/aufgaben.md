# Übungen Modul 02 — Operatoren und Ausdrücke

Unter jeder Aufgabe steht eine Zeile **Erwartete Ausgabe**. Trifft Ihr Programm sie, sind Sie
fertig.

**Noch nicht erlaubt:** `if`, `else`, Schleifen — das ist Modul 03. Jede Aufgabe hier kommt ohne
sie aus. Wenn Sie das Gefühl haben, ein `if` zu brauchen, fehlt Ihnen ein boolescher Ausdruck.

---

## Aufgabe 1 — Grundrechenarten *(schreiben)*

Berechnen und ausgeben, jeweils in einer Zeile:
`15 + 27`, `100 - 43`, `8 * 7`, `45 / 6`, `45 // 6`, `45 % 6`, `2 ** 10`

**Erwartete Ausgabe:**
```
42
57
56
7.5
7
3
1024
```

---

## Aufgabe 2 — Ausgabe vorhersagen *(vorhersagen)*

Schreiben Sie **auf Papier**, was herauskommt. Erst dann ausführen.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)
print(-3 ** 2)
print(10 - 4 - 3)
```

**Erwartete Ausgabe:**
```
14
20
512
-9
3
```

Wenn Sie bei Zeile 3 oder 4 danebenlagen: Folie 7 erklärt beide.

---

## Aufgabe 3 — Wahrheitstabelle vervollständigen *(schreiben)*

Geben Sie **alle vier** Zeilen der `and`-Tabelle und **alle vier** der `or`-Tabelle aus,
jeweils im Format `True and False = False`.

**Erwartete Ausgabe:**
```
True and True = True
True and False = False
False and True = False
False and False = False
True or True = True
True or False = True
False or True = True
False or False = False
```

---

## Aufgabe 4 — Kaputten Code reparieren *(reparieren)*

Das stürzt ab. Reparieren Sie es, **ohne** ein `if` und ohne den Wert von `anzahl` zu ändern.
Tipp: Folie 10.

```python
summe = 0
anzahl = 0
print(summe / anzahl > 10)
```

Notieren Sie zusätzlich, **welchen Fehlertyp** Python meldet.

**Erwartete Ausgabe (nach der Reparatur):**
```
False
```

---

## Aufgabe 5 — Bereichsprüfung *(schreiben)*

Ein Messwert gilt als plausibel, wenn er zwischen −40 und 85 Grad liegt (jeweils
einschließlich). Prüfen Sie die Werte `21.7`, `-55.0` und `85.0` — je eine Ausgabezeile,
**als Operator-Kette**, nicht mit `and`.

**Erwartete Ausgabe:**
```
21.7 plausibel: True
-55.0 plausibel: False
85.0 plausibel: True
```

---

## Aufgabe 6 — Altersgruppe als boolescher Ausdruck *(schreiben)*

Für `alter = 25`: Geben Sie für jede der vier Gruppen aus, ob sie zutrifft.

- Kind: unter 12
- Teenager: 12 bis einschließlich 17
- Erwachsener: 18 bis einschließlich 64
- Senior: ab 65

**Ohne `if`.** Jede Zeile ist ein Vergleich oder eine Kette.

**Erwartete Ausgabe:**
```
Kind: False
Teenager: False
Erwachsener: True
Senior: False
```

*(Dieselbe Aufgabe mit `if`/`elif` — also mit **einer** Ausgabezeile statt vier — kommt in
Modul 03 wieder. Vergleichen Sie dann die beiden Lösungen.)*

---

## Aufgabe 7 — Statusbyte auslesen *(schreiben)*

```python
BEREIT       = 0b0001
GRENZWERT    = 0b0010
FEHLER       = 0b0100
KALIBRIERUNG = 0b1000

status = 0b1010
```

Geben Sie für jedes der vier Flags aus, ob es gesetzt ist. Danach: Setzen Sie `BEREIT` und geben
Sie das neue Byte binär aus (`bin()`).

**Erwartete Ausgabe:**
```
Bereit: False
Grenzwert: True
Fehler: False
Kalibrierung: True
Neues Byte: 0b1011
```

---

## Aufgabe 8 — Begründen *(begründen)*

Je zwei bis drei Sätze:

a) Was ist der Unterschied zwischen `==` und `is`? Welchen von beiden nehmen Sie, um zwei
   Messwerte zu vergleichen — und warum?
b) `a = 1000; b = 1000; a is b` liefert in einer Datei `True`, im REPL `False`.
   Was folgt daraus für Ihren eigenen Code?
c) Warum stürzt `anzahl != 0 and summe / anzahl > 10` bei `anzahl = 0` nicht ab?

**Selbstkontrolle:** Ihre Antwort zu b) muss den Rat enthalten, `is` nicht für Werte zu
verwenden — nicht die Erklärung, wie das Zwischenspeichern funktioniert.

---

## Bonus — Schaltjahr

Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist **und** (nicht durch 100 teilbar
**oder** durch 400 teilbar).

Schreiben Sie **einen** booleschen Ausdruck und prüfen Sie damit 2024, 1900, 2000 und 2023.

**Erwartete Ausgabe:**
```
2024: True
1900: False
2000: True
2023: False
```

**Zusatzfrage:** Lassen Sie die Klammern weg und prüfen Sie dieselben vier Jahre. Kommt etwas
anderes heraus? Und wenn nicht — wozu dann die Klammern? Die Antwort steht in `loesungen.py`,
aber überlegen Sie erst selbst.
