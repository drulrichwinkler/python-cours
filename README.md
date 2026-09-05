# Python-Grundkurs — Übungsprojekt

**Ein reines Übungsprojekt.** Keine Folien, keine Vorlesung, kein Termin. Sie arbeiten allein,
in Ihrem Tempo, und der Rechner sagt Ihnen, ob es stimmt.

> **Für wen ist das?** Für Menschen, die noch nie programmiert haben. Es beginnt bei
> „Was ist eine Variable?" und endet bei einer Anwendung, die Sie vorzeigen können — Webseite,
> API, Datenauswertung, Fenster. **Wenn Sie schon programmieren können** — C, Java, C++ — und
> nur Python brauchen, sparen Sie hier Wochen: Nehmen Sie stattdessen *Python für Umsteiger*.

---

## Loslegen

Sie brauchen **[uv](https://docs.astral.sh/uv/)** und **[VS Code](https://code.visualstudio.com/)**.
Python holt `uv` selbst.

```bash
git clone <dieses-repository>
cd 2026-python-grundkurs
uv sync
```

Prüfen, ob alles steht:

```bash
uv run python -c "from kurs import pruefe; pruefe('ok', '2689367b205c16ce32ed4200942b8b8b1e262dfc70d9bc9fbc77c49699a4f1df')"
```

Erscheint `✅ Richtig: ok`, kann es losgehen.

## Wie ein Modul funktioniert

Jedes Modul ist ein Ordner mit derselben Struktur:

| Datei | was Sie damit tun |
|---|---|
| `OUTLINE.md` | zuerst lesen — was Sie danach können sollen |
| `entdecken.ipynb` | **Schritt 1:** vorhersagen, prüfen lassen, dann ausführen |
| `uebungen/aufgabe_*.py` | **Schritt 2:** ausfüllen, bis die erwartete Ausgabe erscheint |
| `uebungen/aufgaben.md` | die Aufgaben zum Nachdenken, mit gestuften Hinweisen |
| `uebungen/loesungen.py` | **zuletzt**, zum Vergleichen |

```bash
uv run jupyter lab                          # Notebook öffnen
uv run 01_grundlagen/uebungen/aufgabe_1.py  # Aufgabe ausführen
```

## Woran Sie merken, dass Sie fertig sind

Das ist die Frage, die ein Selbstlernkurs beantworten muss — hier auf drei Wegen:

- **Im Notebook** tragen Sie Ihre Vorhersage ein und `pruefe()` sagt ✅ oder ❌. Die Antwort
  steht nirgends im Klartext, nur als Prüfsumme. Sie können also nicht versehentlich spicken
  und bekommen trotzdem sofort Rückmeldung.
- **In jeder Aufgabendatei** steht im Kopf die **erwartete Ausgabe**. Trifft Ihr Programm sie,
  ist die Aufgabe erledigt.
- **Bei den Denkaufgaben** steht eine Zeile *Selbstkontrolle*: woran eine gute Antwort erkennbar
  ist, ohne sie vorwegzunehmen.

**Raten Sie, statt zu überspringen.** Eine falsche Vorhersage ist der Zweck der Übung — sie
zeigt genau die Stelle, an der Ihre Vorstellung vom Rechner abweicht. Wer erst die Lösung liest,
erlebt Verstehen, ohne etwas zu können.

## Aufbau

| Teil | Module | Inhalt |
|---|---|---|
| 1 | 01–05 | Sprachkern: Variablen, Operatoren, Verzweigungen, Schleifen, Funktionen, Listen |
| 2 | 06–10 | Daten und Robustheit: Dictionaries, Strings, Dateien, Fehler, Module |
| 3 | 11–13 | Objekte: Klassen, Vererbung, Generatoren |
| 4 | 14–19 | Werkzeuge und Daten: Decorators, Testen, HTTP, Scraping, Pandas, SQL |
| 5 | 20–25 | Ausflüge: Flask, Streamlit, FastAPI, Tkinter, Textual |
| 6 | 26 | Abschlussprojekt |

**Ein roter Faden zieht sich durch:** ein Sensor-Logfile. Es wird gelesen (08), getestet (15),
über HTTP geholt (16), mit Pandas ausgewertet (18), in SQLite gespeichert (19) — und dann
fünfmal angezeigt: als Webseite, als Datenapp, als API, als Fenster, als Terminal-Oberfläche.

Die Begründung des Zuschnitts steht in
[`docs/GRUNDSTRUKTUR-grundkurs.md`](docs/GRUNDSTRUKTUR-grundkurs.md). **Achtung:** Dieses
Dokument beschreibt noch den ursprünglichen Plan als Präsenzkurs mit Folien; der Kopf der Datei
sagt, was davon nach dem Umbau zum Übungsprojekt noch gilt.

## Stand

| Modul | Status |
|---|---|
| 01 Grundlagen | ✅ vollständig |
| 02 Operatoren | ✅ vollständig |
| 03–26 | ⬜ geplant |
