# Übungen Modul 01

## Überblick

| Datei | Art | worum es geht |
|---|---|---|
| `aufgabe_1.py` | ausfüllen | Sensor-Steckbrief: vier Variablen, vier Ausgaben |
| `aufgabe_2.py` | vorhersagen | Typen — `pruefe()` sagt grün oder rot |
| `aufgabe_3.py` | reparieren | Der Code stürzt ab. Traceback lesen, beheben |
| `aufgabe_4.py` | ausfüllen | Umwandeln zwischen den Typen |
| `aufgabe_5.py` | ausfüllen | Formatierte Messwertzeile mit f-String |
| `aufgabe_6.py` | ausfüllen | Fahrenheit nach Celsius |
| **hier unten** | nachdenken | Aufgabe 7 (Traceback lesen) und 8 (begründen) |
| `aufgabe_9_bonus.py` | ausfüllen | Die Logzeile, die ab Modul 08 wiederkommt |

Jede `.py`-Datei nennt in ihrem Kopf die **erwartete Ausgabe**. Trifft Ihr Programm sie, sind
Sie fertig — Sie müssen niemanden fragen. Ausführen mit:

```bash
uv run 01_grundlagen/uebungen/aufgabe_1.py
```

**Noch nicht erlaubt:** `if`, `else`, Schleifen, eigene Funktionen. Alle Aufgaben kommen ohne aus.

---

## Aufgabe 7 — Traceback lesen

Eine Kollegin schickt Ihnen diese Meldung. Die Datei sehen Sie nicht.

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

> **Hinweis 1:** Lesen Sie von unten nach oben. Die letzte Zeile sagt *was*, die Zeilen darüber
> sagen *wo*.
> **Hinweis 2:** „most recent call last" heißt: Der zuletzt aufgerufene Schritt steht **unten**.
> **Hinweis 3:** Ein `ZeroDivisionError` entsteht bei genau einem Wert des Nenners.

**Selbstkontrolle:** Ihre Antwort zu d) muss erklären, *warum* `anzahl` diesen Wert hatte —
nicht nur, dass er es hatte.

---

## Aufgabe 8 — Begründen

Je zwei bis drei Sätze:

a) Warum liefert `int(3.9)` den Wert `3` und nicht `4`?
b) Warum scheitert `int("3.9")` mit einem `ValueError`, obwohl `int(3.9)` funktioniert?
c) Warum ist `0.1 + 0.2 == 0.3` falsch?

> **Hinweis zu b:** Die eine Fassung bekommt eine *Zahl*, die andere *Text*. Was muss `int()`
> im zweiten Fall zusätzlich tun — und wozu ist es dabei in der Lage?
> **Hinweis zu c:** Denken Sie an ⅓ im Dezimalsystem.

**Selbstkontrolle:** Ihre Antwort zu c) muss das Wort *binär* oder *Zweiersystem* enthalten
und den Vergleich mit ⅓ ziehen.

Beide Antworten stehen ausformuliert in `loesungen.py` — lesen Sie erst, wenn Sie etwas
Eigenes hingeschrieben haben. Auch etwas Falsches.
