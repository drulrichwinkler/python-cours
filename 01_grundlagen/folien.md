# Modul 1: Python-Grundlagen

*Block 1 — Vom leeren Ordner zum laufenden Programm (Folien 1–12)*

---

## Folie 1: Ein Programm, das es nicht gab

Vor dieser Sitzung existiert auf Ihrem Rechner eine Datei nicht.

Nach dieser Sitzung existiert sie, Sie haben sie geschrieben, und sie tut etwas.

Dazwischen liegen genau vier Handgriffe: **Ordner. Datei. Speichern. Ausführen.**

> Alles andere in diesem Kurs — Webseiten, Datenbanken, Schnittstellen — sind dieselben vier
> Handgriffe mit mehr Zeilen dazwischen.

---

## Folie 2: Was ist Python?

- **Interpretiert:** Sie schreiben Text, ein Programm liest ihn Zeile für Zeile und tut, was
  dort steht. Kein Übersetzungsschritt dazwischen.
- Entwickelt von Guido van Rossum, erste Veröffentlichung **1991**
- Lesbare Syntax — Einrückung statt geschweifter Klammern
- Heute vor allem: Datenauswertung, Automatisierung, Web-Schnittstellen, KI

**Wir benutzen Python 3.12.** Anleitungen im Netz, die `print "Hallo"` ohne Klammern zeigen,
sind Python 2 und über zehn Jahre alt.

---

## Folie 3: Die drei Werkzeuge

| Werkzeug | wofür |
|---|---|
| **VS Code** | der Editor — hier schreiben Sie |
| **Terminal** | hier starten Sie — es ist in VS Code eingebaut |
| **uv** | verwaltet Python und die Pakete — `uv run` startet Ihr Programm |

`uv` holt bei Bedarf auch den Interpreter selbst. Sie müssen Python **nicht** getrennt
installieren.

---

## Folie 4: Die vier Handgriffe

```bash
mkdir mein_erstes_projekt      # 1. Ordner
cd mein_erstes_projekt
uv init                        # legt pyproject.toml an
```

Dann in VS Code eine Datei `hallo.py` anlegen (2.), hineinschreiben:

```python
print("Hallo, Welt!")
```

speichern (3. — `Strg+S`, unter macOS `Cmd+S`) und starten (4.):

```bash
uv run hallo.py
```

---

## Folie 5: print()

```python
print("Hallo, Welt!")
print("Ihr Name", "ist", "wichtig")     # Leerzeichen dazwischen
print("A", "B", "C", sep="-")           # A-B-C
print("ohne Zeilenumbruch", end="")
```

- `print()` gibt aus, was in den Klammern steht
- Mehrere Argumente werden mit Komma getrennt und mit **Leerzeichen** ausgegeben
- `sep=` ändert das Trennzeichen, `end=` das Zeilenende

---

## Folie 6: Der erste Fehler — und wie man ihn liest

Schreiben Sie absichtlich falsch:

```python
print("Hallo)
```

Das Terminal antwortet:

```
  File "hallo.py", line 1
    print("Hallo)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

**Lesen Sie von unten nach oben.**

1. **Letzte Zeile:** *was* ist passiert — `SyntaxError`, ein Anführungszeichen fehlt
2. **Darüber:** *wo* — `hallo.py`, `line 1`
3. Erst dann in den Code schauen

---

## Folie 7: Ein Traceback mit mehreren Zeilen

```
Traceback (most recent call last):
  File "rechnen.py", line 5, in <module>
    print(teile(10, 0))
          ^^^^^^^^^^^^
  File "rechnen.py", line 2, in teile
    return a / b
           ~~^~~
ZeroDivisionError: division by zero
```

- **Unten** steht immer der Fehler selbst
- Darüber der Weg dorthin, **die unterste Datei-Zeile ist die, wo es knallte**
- Die Pfeile `~~^~~` zeigen auf die Stelle in der Zeile

> „Traceback (most recent call last)" heißt: *der zuletzt aufgerufene Schritt steht ganz unten.*

---

## Folie 8: Kommentare

```python
# Diese Zeile ignoriert Python vollständig.
preis = 19.99      # auch am Zeilenende möglich

"""
Mehrere Zeilen. Streng genommen ein String, der nirgends
hingeht — als Kommentar aber üblich.
"""
```

- Kommentare erklären **warum**, nicht *was*
- `# addiere 1 zu x` unter `x = x + 1` ist wertlos
- `# Sensor zählt ab 0, Anzeige ab 1` ist Gold

---

## Folie 9: Variablen

```python
name = "Max"
alter = 25
groesse = 1.85
ist_student = True
```

- Ein **Name**, ein Gleichheitszeichen, ein **Wert**
- Keine Typangabe nötig — Python sieht dem Wert an, was er ist
- Das `=` ist **keine** Gleichung, sondern eine Anweisung: *„lege das da hinein"*

---

## Folie 10: Namen — die Regeln

| erlaubt | nicht erlaubt |
|---|---|
| `name`, `mein_name`, `wert2` | `2wert` (Ziffer am Anfang) |
| `_intern` | `mein-name` (Bindestrich) |
| `groesse` | `größe` — läuft, aber vermeiden Sie Umlaute |
| | `class`, `if`, `for` (Schlüsselwörter) |

- **Groß- und Kleinschreibung zählt:** `name` und `Name` sind zwei verschiedene Variablen
- Üblich in Python: `klein_mit_unterstrich` (*snake_case*)
- Konstanten, die sich nie ändern: `MAX_TEMPERATUR = 80`

---

## Folie 11: Namen, die etwas sagen

```python
# schlecht
x = 23.5
y = x * 1.8 + 32

# gut
temperatur_celsius = 23.5
temperatur_fahrenheit = temperatur_celsius * 1.8 + 32
```

Sie schreiben Code einmal und lesen ihn zehnmal. Meistens sind Sie selbst der Leser —
drei Monate später und ohne Erinnerung.

---

## Folie 12: Vorhersage vor der Pause

```python
a = 5
b = a
a = 10
print(b)
```

**Was wird ausgegeben?** Schreiben Sie die Zahl auf, bevor Sie umblättern.

*(In Modul 05 stellen wir dieselbe Frage noch einmal — mit einer Liste statt einer Zahl.
Die Antwort ist dann eine andere. Das ist kein Zufall.)*

---

*Block 2 — Datentypen, Ein- und Ausgabe (Folien 13–24)*

---

## Folie 13: Ganze Zahlen (`int`)

```python
anzahl = 42
minus = -17
gross = 100_000_000        # Unterstriche als Tausendertrennung
```

- Ganze Zahlen, **beliebig groß** — kein Überlauf wie in C oder Java
- `2 ** 100` rechnet Python ohne Murren aus
- Operationen: `+`, `-`, `*`, `//` (ganzzahlig), `%` (Rest), `**` (Potenz)

---

## Folie 14: Fließkommazahlen (`float`) — und ihre Falle

```python
groesse = 1.85
klein = 1e-5           # 0.00001

print(0.1 + 0.2)
```

Ausgabe:

```
0.30000000000000004
```

**Das ist kein Fehler in Python.** `0.1` lässt sich im Binärsystem nicht exakt darstellen,
so wie ⅓ im Dezimalsystem nicht exakt darstellbar ist. Jede Sprache mit `float` hat das.

→ Geldbeträge niemals in `float` vergleichen.

---

## Folie 15: Text (`str`)

```python
gruss = "Hallo"
name  = 'Python'           # einfache Anführungszeichen sind gleichwertig
zitat = "Sie sagte: \"Ja\""
lang  = """Erste Zeile
Zweite Zeile"""
```

- Zeichenketten, in Anführungszeichen
- `"` oder `'` — Hauptsache dasselbe am Anfang und Ende
- Dreifache Anführungszeichen für mehrzeiligen Text

---

## Folie 16: Wahrheitswerte (`bool`)

```python
ist_aktiv = True
ist_fertig = False
```

- Genau **zwei** Werte: `True` und `False`
- **Großgeschrieben** — `true` ist ein Fehler
- Jeder Vergleich liefert einen davon: `5 > 3` ist `True`

---

## Folie 17: `None` — das ausdrückliche Nichts

```python
ergebnis = None
```

- Steht für „hier ist noch nichts" oder „es gibt keine Antwort"
- **Nicht** dasselbe wie `0`, `""` oder `False`
- Häufigster Einsatz: der Startwert, bevor ein Wert bekannt ist

```python
print(None == 0)        # False
print(None == False)    # False
```

---

## Folie 18: Welchen Typ hat das? — `type()`

```python
print(type(42))         # <class 'int'>
print(type(1.85))       # <class 'float'>
print(type("42"))       # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>
```

Der Typ hängt am **Wert**, nicht am Namen. Dieselbe Variable darf später etwas anderes
enthalten:

```python
x = 5          # int
x = "fünf"     # jetzt str — erlaubt, aber selten eine gute Idee
```

---

## Folie 19: Typ-Konvertierung

```python
int("42")        # 42
float("3.14")    # 3.14
str(42)          # "42"

int(3.9)         # 3   -- schneidet ab, rundet nicht!
int("3.9")       # ValueError
```

**Warum scheitert das letzte?** `int()` kann eine *Zahl* abschneiden, aber es kann keinen
*Text* interpretieren, der keine ganze Zahl ist. Umweg: `int(float("3.9"))`.

---

## Folie 20: `bool()` — die zweite Falle

```python
bool(0)          # False
bool(1)          # True
bool("")         # False   -- leerer Text
bool("False")    # True    -- nicht leerer Text!
bool([])         # False   -- leere Liste
```

**Merksatz:** Leer ist falsch, alles andere ist wahr. Der Text `"False"` ist nicht leer.

---

## Folie 21: Eingabe mit `input()`

```python
name = input("Ihr Name: ")
print("Hallo,", name)
```

- `input()` hält das Programm an und wartet
- Der Text in den Klammern wird vorher ausgegeben
- **`input()` liefert immer einen String** — auch wenn Sie `42` tippen

```python
alter = input("Ihr Alter: ")
print(alter + 1)        # TypeError!
print(int(alter) + 1)   # so geht es
```

---

## Folie 22: f-Strings

```python
name = "Max"
alter = 25

print(f"{name} ist {alter} Jahre alt.")
print(f"Nächstes Jahr: {alter + 1}")
print(f"Pi ungefähr: {3.14159:.2f}")     # Pi ungefähr: 3.14
```

- **f** vor dem Anführungszeichen
- In geschweiften Klammern steht ein Ausdruck, nicht nur ein Name
- `:.2f` heißt „als Fließkommazahl mit zwei Nachkommastellen"

---

## Folie 23: Der Debug-Trick, den kaum jemand kennt

```python
temperatur = 23.5
print(f"{temperatur=}")
```

Ausgabe:

```
temperatur=23.5
```

Das Gleichheitszeichen **in** der Klammer druckt Name *und* Wert. Wenn Sie wissen wollen,
was in einer Variablen steckt, ist das die kürzeste Frage, die Sie stellen können.

---

## Folie 24: Ihr Auftrag

Schreiben Sie `steckbrief.py`:

- drei Variablen: Ihr Name, Ihr Geburtsjahr, Ihre Körpergröße in Metern
- **eine** Ausgabezeile, mit **einem** f-String, die alle drei enthält
- die Körpergröße auf zwei Nachkommastellen

**Abgabe:** die Datei, bis zur nächsten Sitzung.

> **Nächstes Mal:** `5 == 5` ist `True`. Und `5 is 5`? Und `1000 is 1000`?
> Eine dieser beiden Antworten wird Sie überraschen.
