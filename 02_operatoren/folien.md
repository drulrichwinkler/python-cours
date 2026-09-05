# Modul 2: Operatoren und Ausdrücke

*Folien 3–7 und 12–13 sind Nachschlagestoff und gehören in die Vorbereitung.
Präsenz: Folien 1–2, 8–11, 14–18.*

---

## Folie 1: Ein Byte, das alles sagt

Ein Temperatursensor meldet seinen Zustand nicht in Worten, sondern in **einem Byte**:

```
0 0 0 0 0 1 1 0
              │ └─ Bit 0: Messung bereit
              └─── Bit 1: Grenzwert überschritten
            └───── Bit 2: Sensorfehler
          └─────── Bit 3: Kalibrierung nötig
```

Dieses Byte ist `6`. **Wie fragen Sie ab, ob der Grenzwert überschritten ist?**

Nicht mit `==`. Am Ende dieser Sitzung mit einer Zeile.

---

## Folie 2: Was ein Operator ist

```python
5 + 3          # + ist der Operator, 5 und 3 sind die Operanden
temperatur > 25
ist_aktiv and nicht_gestoert
```

Vier Familien, in dieser Reihenfolge:

| Familie | Beispiele | ergibt |
|---|---|---|
| arithmetisch | `+ - * / // % **` | eine Zahl |
| vergleichend | `== != < > <= >=` | `True`/`False` |
| logisch | `and or not` | meist `True`/`False` — Folie 11 zeigt die Ausnahme |
| bitweise | `& \| ^ ~ << >>` | eine Zahl |

---

## Folie 3: Arithmetik — die vier bekannten

```python
5 + 3        # 8
5 - 3        # 2
5 * 3        # 15
5 / 3        # 1.6666666666666667
```

**Achtung:** `/` liefert *immer* eine Fließkommazahl, auch wenn es aufgeht:
`6 / 3` ergibt `2.0`, nicht `2`.

---

## Folie 4: Arithmetik — die drei, die man lernen muss

```python
7 // 2       # 3      Ganzzahldivision: teilen und abschneiden
7 % 2        # 1      Modulo: der Rest
2 ** 10      # 1024   Potenz
```

`%` ist der meistunterschätzte Operator der Sprache:

```python
zahl % 2 == 0      # ist die Zahl gerade?
sekunden % 60      # die Sekunden innerhalb der Minute
index % laenge     # bleibt garantiert im Bereich
```

---

## Folie 5: Modulo bei negativen Zahlen

```python
 17 % 5      #  2
-17 % 5      #  3     <- nicht -2!
```

Python garantiert: Das Ergebnis von `%` hat **das Vorzeichen des rechten Operanden**.
In C und Java ist das anders — dort käme `-2` heraus.

> Wenn Sie Code aus einer anderen Sprache übernehmen, ist das eine der Stellen, an denen er
> still etwas anderes tut.

---

## Folie 6: Reihenfolge der Auswertung

Von stark nach schwach:

| | |
|---|---|
| 1. | `**` Potenz |
| 2. | `-x` Vorzeichen |
| 3. | `* / // %` |
| 4. | `+ -` |
| 5. | `< > <= >= == != in is` |
| 6. | `not` → `and` → `or` |

```python
2 + 3 * 4        # 14, nicht 20
```

**Im Zweifel Klammern.** Sie kosten nichts und ersparen Ihnen die Diskussion.

---

## Folie 7: Zwei Fallen in der Reihenfolge

```python
2 ** 3 ** 2      # 512, nicht 64
```
`**` wird von **rechts** ausgewertet: `2 ** (3 ** 2)` = `2 ** 9`.

```python
-3 ** 2          # -9, nicht 9
```
`**` bindet stärker als das Minuszeichen: `-(3 ** 2)`. Wer `9` will, schreibt `(-3) ** 2`.

---

## Folie 8: Vergleiche

```python
5 == 5         # True
5 != 3         # True
5 > 3          # True
5 <= 5         # True
5 == 5.0       # True   -- Wert gleich, Typ egal
"a" == "A"     # False  -- Text ist genau
```

Ein Vergleich liefert **immer** `True` oder `False`. Das ist der Rohstoff für alles, was in
Modul 03 an Verzweigungen kommt.

---

## Folie 9: Die Wahrheitstabellen — vollständig

**`and` — beide müssen wahr sein:**

| A | B | `A and B` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

**`or` — mindestens eines:**

| A | B | `A or B` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

**`not`** dreht um: `not True` ist `False`.

---

## Folie 10: Kurzschlussauswertung

```python
if anzahl != 0 and summe / anzahl > 10:
    ...
```

Warum stürzt das bei `anzahl = 0` **nicht** ab?

**Weil Python aufhört, sobald das Ergebnis feststeht.** Ist der linke Teil von `and` falsch,
wird der rechte gar nicht mehr angesehen. Bei `or` umgekehrt: Ist links wahr, ist Schluss.

Das ist keine Optimierung, sondern eine **Zusage der Sprache** — Sie dürfen sich darauf
verlassen und Ihre Prüfungen in dieser Reihenfolge schreiben.

---

## Folie 11: `and` und `or` geben nicht `True` zurück

```python
0 or "leer"          # 'leer'
"a" and "b"          # 'b'
None or 0 or "x"     # 'x'
```

Sie geben **den Operanden zurück**, bei dem die Entscheidung fiel — nicht `True`/`False`.

Daraus wird ein häufiges Muster für Standardwerte:

```python
name = eingabe or "unbekannt"     # nimmt "unbekannt", wenn eingabe leer ist
```

---

## Folie 12: Zuweisungsoperatoren

```python
x = 10
x += 3      # x = x + 3   -> 13
x -= 5      # 8
x *= 2      # 16
x //= 3     # 5
x %= 3      # 2
x **= 4     # 16
```

Reine Schreibabkürzung. `x += 3` und `x = x + 3` tun bei Zahlen dasselbe.

*(Bei Listen tun sie es nicht. Das ist Modul 05.)*

---

## Folie 13: `in` — Enthaltensein

```python
"a" in "Hallo"         # True
"lo" in "Hallo"        # True
5 in [1, 5, 9]         # True
"x" not in "Python"    # True
```

Funktioniert mit allem, was mehrere Dinge enthält: Text, Listen, Tupel, später Dictionaries.

---

## Folie 14: `==` gegen `is` — zwei verschiedene Fragen

```python
a = [1, 2]
b = [1, 2]

a == b       # True   -- "steht dasselbe drin?"
a is b       # False  -- "ist es dasselbe Ding?"
```

| | Frage |
|---|---|
| `==` | Haben beide **denselben Wert**? |
| `is` | Sind beide **dasselbe Objekt** im Speicher? |

Zwei Blätter Papier mit derselben Zahl darauf: `==` ja, `is` nein.

---

## Folie 15: Warum `is` bei Zahlen trügt

```python
a = 1000
b = 1000
a is b
```

**In einer `.py`-Datei: `True`. Zeile für Zeile im REPL: `False`.**

Der Grund ist ein Detail der Umsetzung — beim Übersetzen einer Datei erkennt Python, dass
zweimal dieselbe Zahl im selben Block steht, und legt sie nur einmal ab. Im REPL ist jede Zeile
ein eigener Block.

**Die Lehre ist nicht das Detail, sondern die Regel:**

> `is` beantwortet eine Frage, die Sie fast nie stellen wollen. Für Werte nehmen Sie `==`.
> `is` benutzen Sie für genau einen Fall: `if ergebnis is None`.

---

## Folie 16: Bitweise Operatoren

| | | Beispiel |
|---|---|---|
| `&` | AND | Bit lesen |
| `\|` | OR | Bit setzen |
| `^` | XOR | Bit umschalten |
| `~` | NOT | alle Bits kippen |
| `<<` `>>` | schieben | Bit an die richtige Stelle bringen |

Binärzahlen schreibt man in Python mit `0b`, Unterstriche sind zur Lesbarkeit erlaubt:

```python
0b0000_0110      # 6
bin(6)           # '0b110'
```

---

## Folie 17: Das Statusbyte von Folie 1

```python
BEREIT       = 0b0001    # 1
GRENZWERT    = 0b0010    # 2
FEHLER       = 0b0100    # 4
KALIBRIERUNG = 0b1000    # 8

status = 0b0110          # 6: Grenzwert überschritten UND Sensorfehler
```

**Bit lesen** — mit `&` alles ausblenden außer dem einen Bit:

```python
status & GRENZWERT           # 2  -> ungleich 0, also gesetzt
status & BEREIT              # 0  -> nicht gesetzt
bool(status & GRENZWERT)     # True
```

Das ist die Zeile von Folie 1.

---

## Folie 18: Bits setzen, löschen, umschalten

```python
status | BEREIT         # 0b0111  setzen   (aus 0 wird 1, 1 bleibt 1)
status & ~FEHLER        # 0b0010  löschen  (Maske umdrehen, dann UND)
status ^ KALIBRIERUNG   # 0b1110  umschalten
status >> 1             # 0b11    alles um eine Stelle nach rechts
```

**Wo Ihnen das begegnet:** GPIO-Pins am Mikrocontroller, Statusregister in Datenblättern,
Berechtigungen in Dateisystemen (`chmod 755`), Flags in Netzwerkprotokollen. Überall dort, wo
viele Ja/Nein-Angaben in eine Zahl passen müssen.

---

## Folie 19: Operator-Ketten

```python
1 < x < 10                # pythonisch
x > 1 and x < 10          # dasselbe, umständlicher
```

Python erlaubt Vergleiche zu ketten — und meint damit wirklich beide Vergleiche.
**Das ist nicht dasselbe wie Klammern:**

```python
3 > 2 > 1        # True   -- (3 > 2) und (2 > 1)
(3 > 2) > 1      # False  -- True > 1  ->  1 > 1  ->  False
```

Die zweite Zeile rechnet mit `True` als `1`. In den meisten Sprachen gibt es die erste gar nicht.

---

## Folie 20: Ihr Auftrag

Statusbyte `0b0000_1010`. Schreiben Sie `status.py`, das für alle vier Flags in je einer Zeile
ausgibt, ob sie gesetzt sind:

```
Bereit: False
Grenzwert: True
Fehler: False
Kalibrierung: True
```

**Ohne `if`.** Sie brauchen es nicht — `bool()` und `&` genügen.

> **Nächstes Mal:** Bisher lief jedes Ihrer Programme von oben nach unten durch, immer gleich.
> Ab Modul 03 trifft es Entscheidungen — und macht Dinge mehr als einmal.
