# Übungen Modul 02

## Überblick

| Datei | Art | worum es geht |
|---|---|---|
| `aufgabe_1.py` | ausfüllen | Grundrechenarten — und der Unterschied zwischen `/` und `//` |
| `aufgabe_2.py` | vorhersagen | Auswertungsreihenfolge, zwei Überraschungen |
| `aufgabe_3.py` | ausfüllen | Wahrheitstabelle, alle acht Zeilen |
| `aufgabe_4.py` | reparieren | Absturz durch Division — ohne `if` beheben |
| `aufgabe_5.py` | ausfüllen | Bereichsprüfung als Operator-Kette |
| `aufgabe_6.py` | ausfüllen | Altersgruppe ohne `if` |
| `aufgabe_7.py` | ausfüllen | Statusbyte auslesen und ein Bit setzen |
| **hier unten** | nachdenken | Aufgabe 8 (begründen) |
| `aufgabe_9_bonus.py` | ausfüllen | Schaltjahr — und eine Klammerfrage |

Jede `.py`-Datei nennt in ihrem Kopf die **erwartete Ausgabe** und einen Hinweis. Ausführen mit:

```bash
uv run 02_operatoren/uebungen/aufgabe_1.py
```

**Noch nicht erlaubt:** `if`, `else`, Schleifen, eigene Funktionen. Mehrere Aufgaben sehen aus,
als bräuchten sie eine Verzweigung — sie brauchen einen booleschen Ausdruck. Das ist der Punkt.

---

## Aufgabe 8 — Begründen

Je zwei bis drei Sätze:

a) Was ist der Unterschied zwischen `==` und `is`? Welchen von beiden nehmen Sie, um zwei
   Messwerte zu vergleichen — und warum?
b) `a = 1000; b = 1000; a is b` liefert in einer Datei `True`, im Notebook Zelle für Zelle
   `False`. Was folgt daraus für Ihren eigenen Code?
c) Warum stürzt `anzahl != 0 and summe / anzahl > 10` bei `anzahl = 0` nicht ab?

> **Hinweis zu a:** Zwei Blätter Papier mit derselben Zahl darauf. Welche der beiden Fragen
> beantwortet man mit „ja", welche mit „nein"?
> **Hinweis zu b:** Die interessante Antwort ist nicht, *warum* sich Python so verhält, sondern
> was Sie daraus für Ihren Code ableiten.
> **Hinweis zu c:** Das Stichwort steht im Hinweis von `aufgabe_4.py`.

**Selbstkontrolle:** Ihre Antwort zu b) muss den Rat enthalten, `is` nicht für Werte zu
verwenden — nicht die Erklärung, wie Python Zahlen zwischenspeichert. Diese Erklärung ist ein
Detail der Umsetzung und darf sich zwischen zwei Python-Versionen ändern. Der Rat nicht.

Die ausformulierten Antworten stehen in `loesungen.py`.
