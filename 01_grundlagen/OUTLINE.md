# Modul 01 — Python-Grundlagen

**Umfang:** 2 Blöcke à 90 min · **Setzt voraus:** nichts · **Artefakte:** `entdecken.py`,
`entdecken.md`, `folien.md`, `uebungen/`

**Modulcode / Semester / Prüfungsform:** noch nicht festgelegt (siehe
`docs/GRUNDSTRUKTUR-grundkurs.md` Abschnitt 11). Die Lernziele unten sind auf Bloom-Stufe 2–3
formuliert und tragen unter beiden zur Debatte stehenden Lesarten.

## Lernziele

Nach diesem Modul können Sie:

1. einen Projektordner anlegen, eine `.py`-Datei darin speichern und sie mit `uv run`
   **ausführen** — ohne Anleitung;
2. eine Python-Fehlermeldung **lesen** und die verursachende Zeile benennen;
3. für ein gegebenes Codestück mit Variablen, Zahlen und Strings die Ausgabe **vorhersagen**,
   ohne es auszuführen;
4. `int`, `float`, `str`, `bool` und `None` **unterscheiden** und begründen, warum
   `int("3.5")` scheitert, `int(3.5)` aber nicht;
5. eine formatierte Ausgabe mit f-Strings **erzeugen**.

Nicht enthalten: „Python verstehen", „sich mit Datentypen beschäftigen". Wenn Sie eines der
fünf Ziele nicht prüfen können, gehört es hier nicht hin.

## Schnitt in zwei Blöcke

| Block | Folien | Titel |
|---|---|---|
| 1 | 1–12 | Vom leeren Ordner zum laufenden Programm |
| 2 | 13–24 | Datentypen, Ein- und Ausgabe |

**Warum geteilt:** Der Vorgängerstapel hatte ~28 neue Fachbegriffe in einem Block; die
Rastergrenze liegt bei ~15 (Gutachten, Prio A). Gestrichen wurden dabei *Duck Typing* und
*PEP 8* — beides sind ohne Vorwissen leere Vokabeln.

## Nachbereitung — genau eine Sache

**Auftrag:** Schreiben Sie ein Skript `steckbrief.py`, das Ihren Namen, Ihr Geburtsjahr und Ihre
Körpergröße in Variablen ablegt und daraus mit **einem** f-String einen Satz ausgibt.
**Abgabe:** die Datei, im Kursordner, bis zur nächsten Sitzung.
