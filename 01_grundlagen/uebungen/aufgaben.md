# Übungen Modul 01 — Python-Grundlagen

**Regel für alle Aufgaben:** Unter jeder steht eine Zeile **Erwartete Ausgabe**. Wenn Ihr
Programm genau das ausgibt, sind Sie fertig — Sie müssen niemanden fragen.

Die Lösungen liegen in `loesungen.py`. Schauen Sie erst hinein, wenn Sie eine eigene Antwort
hingeschrieben haben — auch eine falsche.

**Noch nicht erlaubt:** `if`, `else`, Schleifen. Die kommen in Modul 03. Alle Aufgaben hier
lassen sich ohne sie lösen.

---

## Aufgabe 1 — Sensor-Steckbrief *(schreiben)*

Ein Temperatursensor in einer Werkshalle. Legen Sie vier Variablen an:

- die Kennung `"TH-04"`
- den Aufstellort `"Halle 2"`
- den letzten Messwert `21.7`
- ob der Sensor gerade aktiv ist (`True`)

Geben Sie jede in einer eigenen Zeile aus, im Format `Kennung: TH-04`.

**Erwartete Ausgabe:**
```
Kennung: TH-04
Ort: Halle 2
Messwert: 21.7
Aktiv: True
```

---

## Aufgabe 2 — Typen vorhersagen *(vorhersagen)*

Schreiben Sie **auf Papier**, was diese vier Zeilen ausgeben. Erst danach ausführen.

```python
print(type(21.7))
print(type("21.7"))
print(type(21))
print(type(True))
```

**Erwartete Ausgabe:**
```
<class 'float'>
<class 'str'>
<class 'int'>
<class 'bool'>
```

---

## Aufgabe 3 — Kaputten Code reparieren *(reparieren)*

Dieses Programm stürzt ab. Führen Sie es aus, **lesen Sie den Traceback** und reparieren Sie es.
Der Messwert kommt als Text aus einer Datei — daran dürfen Sie nichts ändern.

```python
messwert = "21.7"
grenzwert = 25
abstand = grenzwert - messwert
print(f"Abstand zum Grenzwert: {abstand}")
```

Notieren Sie zusätzlich: **Welchen Fehlertyp** meldet Python, und **welche Zeile**?

**Erwartete Ausgabe (nach der Reparatur):**
```
Abstand zum Grenzwert: 3.3000000000000007
```

*Ja, wirklich. Aufgabe 8 erklärt, warum.*

---

## Aufgabe 4 — Umwandeln *(schreiben)*

Wandeln Sie um und geben Sie jeweils Wert und Typ aus:

- den Text `"42"` in eine ganze Zahl
- die ganze Zahl `10` in eine Fließkommazahl
- die Fließkommazahl `3.7` in eine ganze Zahl
- die ganze Zahl `0` in einen Wahrheitswert

**Erwartete Ausgabe:**
```
42 <class 'int'>
10.0 <class 'float'>
3 <class 'int'>
False <class 'bool'>
```

---

## Aufgabe 5 — Formatierte Messwertzeile *(schreiben)*

Der Sensor liefert `22.83333`. Geben Sie mit **einem** f-String aus:

```
TH-04 meldet 22.8 Grad.
```

Die Kennung steht in einer Variablen, der Messwert ebenfalls. Runden Sie auf **eine**
Nachkommastelle — im f-String, nicht mit `round()`.

**Erwartete Ausgabe:**
```
TH-04 meldet 22.8 Grad.
```

---

## Aufgabe 6 — Umrechnung *(schreiben)*

Ein Gerät aus den USA meldet Fahrenheit. Rechnen Sie `71.6` in Celsius um:

> Celsius = (Fahrenheit − 32) × 5 / 9

Geben Sie beide Werte in einer Zeile aus, Celsius auf eine Nachkommastelle.

**Erwartete Ausgabe:**
```
71.6 Grad Fahrenheit sind 22.0 Grad Celsius.
```

---

## Aufgabe 7 — Traceback lesen *(lesen)*

Sie bekommen diese Meldung von einer Kollegin geschickt. Die Datei sehen Sie nicht.

```
Traceback (most recent call last):
  File "auswertung.py", line 12, in <module>
    print(mittelwert(werte))
          ^^^^^^^^^^^^^^^^^
  File "auswertung.py", line 7, in mittelwert
    return summe / anzahl
           ~~~~~~^~~~~~~~
ZeroDivisionError: division by zero
```

Beantworten Sie in je einem Satz:

a) In welcher **Zeile** ist der Fehler aufgetreten?
b) In welcher Zeile wurde die Funktion **aufgerufen**?
c) Welchen Wert hatte `anzahl`?
d) Was ist vermutlich passiert?

**Erwartete Antwort:** a) Zeile 7 · b) Zeile 12 · c) 0 · d) Die Liste `werte` war leer,
deshalb war `anzahl` null.

---

## Aufgabe 8 — Begründen *(begründen)*

Schreiben Sie je zwei bis drei Sätze:

a) Warum liefert `int(3.9)` den Wert `3` und nicht `4`?
b) Warum scheitert `int("3.9")` mit einem `ValueError`, obwohl `int(3.9)` funktioniert?
c) Warum ist `0.1 + 0.2 == 0.3` falsch?

**Selbstkontrolle:** Ihre Antwort zu c) muss das Wort *binär* oder *Zweiersystem* enthalten und
erklären, warum das mit ⅓ im Dezimalsystem vergleichbar ist.

---

## Bonus — Die Sensor-Zeile

Bauen Sie aus drei Variablen (`kennung = "TH-04"`, `zeit = "14:05"`, `wert = 22.83333`) mit
**einem einzigen** `print()` diese Zeile:

```
14:05 | TH-04 | 22.8 C
```

Zwei Wege führen zum Ziel: über `sep=` oder über einen f-String. Bauen Sie **beide** und
entscheiden Sie, welcher besser lesbar ist. Diese Zeile ist übrigens genau das Format, das uns
ab Modul 08 als Logfile wieder begegnet.

**Erwartete Ausgabe:**
```
14:05 | TH-04 | 22.8 C
```
