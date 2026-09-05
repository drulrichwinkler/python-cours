# Modul 02 — Präsenz-Drehbuch

**Für die Lehrperson.** Ein **halber** Block (~45 min). Die Folien 3–7 und 12–13 sind
Nachschlagestoff und wurden mit `entdecken.py` vorbereitet — sie werden hier **nicht**
durchgegangen. Wer sie doch vorträgt, verbraucht die Zeit für die drei Dinge, die man nicht
nachliest.

---

**Einstieg (3 min) — Hook H2, Folie 1.**
Das Statusbyte an die Wand, ohne Erklärung:

```
0 0 0 0 0 1 1 0
```

„Das meldet ein Sensor. Es heißt: Grenzwert überschritten, Sensorfehler liegt an. Wie fragen Sie
ab, ob der Grenzwert überschritten ist?" Vorschläge sammeln — es kommt zuverlässig `== 2` oder
`== 6`. Beides stehen lassen, nicht bewerten: „Am Ende der Sitzung mit einer Zeile."

**Rückkanal (2 min).** Handzeichen zu Feld 2 (`-17 % 5`) und Feld 5. Wer bei Feld 5 `True`
erwartet hatte, hebt die Hand — das sind erfahrungsgemäß die meisten.

---

**PI-1 (6 min) — `is` gegen `==`, Folien 14–15.**
> ```python
> a = [1, 2]
> b = [1, 2]
> print(a == b, a is b)
> ```
> (A) `True True` (B) `True False` (C) `False True` (D) `False False`

Abstimmen, **nicht** auflösen, Nachbargespräch 90 Sekunden, erneut abstimmen. Antwort **B**.

Danach die Nachfrage, die den Punkt setzt: „Und `a = 1000; b = 1000; a is b`?"
Live vorführen — **einmal in einer Datei** (`True`) und **einmal im REPL, Zeile für Zeile**
(`False`). Dieselbe Frage, zwei Antworten.

Die Auflösung ist nicht das Detail, sondern die Regel: *`is` beantwortet eine Frage, die Sie
fast nie stellen wollen. Für Werte `==`. `is` nur für `None`.*

---

**Live-Demo (8 min) — Kurzschlussauswertung, Folie 10.**
Im REPL vorführen:

```python
anzahl = 0
anzahl != 0 and 10 / anzahl > 1     # False, kein Absturz
10 / anzahl > 1 and anzahl != 0     # ZeroDivisionError
```

Die Reihenfolge entscheidet über Absturz oder nicht. Traceback gemeinsam von unten nach oben
lesen — Rückgriff auf Modul 01.

---

**Bitmasken (12 min) — Folien 16–18, das Herzstück.**
Am offenen Terminal, mitschreiben lassen. `bin()` bei jedem Schritt mitzeigen, damit die Bits
sichtbar bleiben:

```python
status = 0b0110
bin(status & 0b0010)     # Bit lesen
bin(status | 0b0001)     # Bit setzen
bin(status & ~0b0100)    # Bit löschen
```

Dann zurück zu Folie 1: `bool(status & GRENZWERT)`. **Der Hook wird hier eingelöst** — die eine
Zeile, die am Anfang versprochen war.

Wenn Zeit ist, ein echtes Datenblatt zeigen (GPIO-Register, `chmod 755`, TCP-Flags). Im dualen
Studiengang kennt ein Teil der Gruppe das aus dem Betrieb — fragen Sie danach, es kostet zwei
Minuten und bringt einen Praxisbezug, den kein Lehrbuch liefert.

---

**Operator-Ketten (5 min) — Folie 19.**
An die Wand, ohne Vorrede:

```python
3 > 2 > 1        # ?
(3 > 2) > 1      # ?
```

Erst raten lassen, dann ausführen: `True` und `False`. Auflösung: Die Klammern erzwingen, dass
`True` als `1` weitergerechnet wird.

---

**Minutenpapier (3 min).** „Wofür würden Sie in Ihrem Betrieb ein Statusbyte einsetzen?"
Einsammeln — die Antworten sind das Material für die Übungen im Folgejahr.

**Auftrag:** `status.py`, siehe `OUTLINE.md`.

---

## Wenn Zeit fehlt

Streichen: Folie 5 (Modulo negativ), Folie 19 (Ketten). **Nicht** streichen: Folien 14–15
(`is` gegen `==`) und 17–18 (Bitmasken) — das eine ist die häufigste Fehlerquelle, das andere
der einzige Andockpunkt für die Informationstechnik im ganzen Modul.
