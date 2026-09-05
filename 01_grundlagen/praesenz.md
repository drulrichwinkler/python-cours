# Modul 01 — Präsenz-Drehbuch

**Für die Lehrperson.** Zwei Blöcke à 90 min. Die Folien tragen den Inhalt; hier steht, was
*getan* wird. ~45 aktive Minuten je Block, den Rest füllt Ihre Erfahrung.

---

## Block 1 — Vom leeren Ordner zum laufenden Programm

**Einstieg (3 min) — Hook statt Gliederung.**
Wortlos ein leeres Terminal öffnen, `mkdir demo`, `cd demo`, eine Datei anlegen,
`print("Hallo")` tippen, `uv run hallo.py`. Dann: „Das waren zwölf Sekunden. Alles, was wir in
diesem Kurs noch machen, sind dieselben vier Handgriffe mit mehr Zeilen dazwischen."
*Keine Gliederungsfolie.*

**Rückkanal (2 min).** Handzeichen: Wer hat den Vorhersagezettel dabei? Wer ist bei Feld 8
danebengelegen? Das ist der Aufhänger für Block 2 — nicht jetzt auflösen.

**PI-1 (6 min) — Folie 12.**
> `a = 5` · `b = a` · `a = 10` · `print(b)` — was kommt heraus?
> (A) 5 (B) 10 (C) Fehler

Abstimmen lassen, **nicht** auflösen. Nachbargespräch 90 Sekunden, erneut abstimmen, dann
auflösen: **5.** Anschließend der Satz, der zählt: „Merken Sie sich Ihre Begründung. In Modul 05
stellen wir dieselbe Frage mit einer Liste, und dann ist die Antwort eine andere."

**Live-Demo (8 min) — Traceback, Folien 6–7.**
Absichtlich drei Fehler produzieren und **jedes Mal von unten nach oben vorlesen**:
`print("Hallo)` · `print(x)` bei undefiniertem `x` · `print("x" + 1)`.
Bei jedem: erst die letzte Zeile, dann die Zeilennummer, dann erst in den Code sehen.
Geeignet für `/autodemo` (Baustein D1).

**Fehlersuche in Partnerarbeit (15 min).**
Vier kaputte Zeilen an die Wand, Papier, keine Rechner:

```python
2wert = 10
print("Hallo)
Print("Welt")
name = Max
```

Je Zeile: Welcher Fehlertyp, welche Zeile meldet Python? Auflösen lassen, nicht selbst auflösen.

**Minutenpapier (3 min).** „Was war heute die überraschendste Zeile?" Einsammeln.

---

## Block 2 — Datentypen, Ein- und Ausgabe

**Einstieg (3 min) — Hook H1.**
„Schreiben Sie auf ein Blatt, was `0.1 + 0.2` ergibt." Sammeln lassen (fast alle: 0.3), dann im
REPL vorführen: `0.30000000000000004`. Erst danach Folie 14. Der Hook lebt davon, dass die
Antwort *vorher* auf Papier steht.

**Retrieval aus Block 1 (2 min), keine Wiederholungsfolie.**
Drei Fragen ins Plenum: Wo steht im Traceback der Fehler? Was macht `sep=`? Was ist an
`Name` und `name` verschieden?

**PI-2 (6 min) — Folie 20.**
> Was gibt `bool("False")` aus? (A) True (B) False (C) Fehler

Antwort **A**. Fast alle tippen B. Auflösung: `bool()` fragt nicht, *was* dort steht, sondern
*ob etwas* dort steht. `"False"` ist ein nicht leerer Text.

**Live-Demo (8 min) — `input()` liefert immer Text, Folie 21.**
`alter = input("Ihr Alter: ")`, `42` eintippen, `print(alter + 1)` → `TypeError`. Traceback
gemeinsam lesen (Rückgriff auf Block 1), dann `int(alter) + 1`. Danach `f"{alter=}"` zeigen —
der Trick von Folie 23 löst genau dieses Rätsel.

**Übung (15 min).** `uebungen/aufgaben.md`, Aufgaben 1–4. Jede hat eine Zeile
**Erwartete Ausgabe** — wer die trifft, ist fertig und geht weiter.

**Abschluss (3 min) — Cliffhanger statt „Best Practices".**
An die Wand: `5 == 5` und `1000 is 1000`. „Eine dieser Antworten wird Sie überraschen.
Nächstes Mal." Nicht auflösen.

**Auftrag:** `steckbrief.py`, siehe `OUTLINE.md`.

---

## Wenn Zeit fehlt

Zuerst kürzen: Folie 2 (Geschichte), Folie 11 (Namen, die etwas sagen), Folie 17 (`None`).
**Nicht** kürzen: Folien 6–7 (Traceback) und Folie 20 (`bool`) — beide sind Prio-A-Inhalte
und tragen den Rest des Kurses.
