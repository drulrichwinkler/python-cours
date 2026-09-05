# Python-Grundkurs

**Von Null bis zur eigenen Anwendung.** 26 Module in sechs Teilen — vom ersten `print()` bis zu
einer Webseite, einer API und einem Fenster, die dieselben Messdaten anzeigen.

> **Für wen ist dieser Kurs?** Für Menschen, die noch nie programmiert haben. Er beginnt bei
> „Was ist eine Variable?" und endet bei einer Anwendung, die Sie vorzeigen können — Webseite,
> API, Datenauswertung, Fenster. **Wenn Sie schon programmieren können** — C, Java, C++ — und
> nur Python brauchen, sparen Sie hier Wochen: Nehmen Sie stattdessen *Python für Umsteiger*.

---

## Loslegen

Sie brauchen zwei Dinge: **[uv](https://docs.astral.sh/uv/)** und **[VS Code](https://code.visualstudio.com/)**.

```bash
git clone <dieses-repository>
cd 2026-python-grundkurs
uv sync
uv run 01_grundlagen/entdecken.py
```

Läuft das durch und endet mit `-- Ende von entdecken.py --`, ist Ihre Umgebung in Ordnung.
Wenn nicht: Modul 01, Folie 6 erklärt, wie man die Fehlermeldung liest.

## Wie Sie mit einem Modul arbeiten

Jedes Modul ist ein Ordner. Die Reihenfolge ist gedacht als:

| | Datei | wann |
|---|---|---|
| 1 | `entdecken.md` | **vor** der Sitzung ausdrucken — der Vorhersagezettel |
| 2 | `entdecken.py` | erst die Vorhersagen hinschreiben, **dann** `uv run` |
| 3 | `folien.md` | in der Sitzung |
| 4 | `uebungen/aufgaben.md` | danach, selbst |
| 5 | `uebungen/loesungen.py` | **zuletzt**, zum Vergleichen |

`OUTLINE.md` sagt, was Sie nach dem Modul können sollen. `praesenz.md` ist für die Lehrperson.

**Die Reihenfolge ist der Punkt.** Wer erst die Lösung liest, erlebt Verstehen, ohne etwas zu
können. Schreiben Sie jede Vorhersage hin, bevor Sie ausführen — auch wenn Sie sich unsicher sind.
Besonders dann.

## Aufbau

| Teil | Module | Inhalt |
|---|---|---|
| 1 | 01–05 | Sprachkern: Variablen, Operatoren, Verzweigungen, Schleifen, Funktionen, Listen |
| 2 | 06–10 | Daten und Robustheit: Dictionaries, Strings, Dateien, Fehler, Module |
| 3 | 11–13 | Objekte: Klassen, Vererbung, Generatoren |
| 4 | 14–19 | Werkzeuge und Daten: Decorators, Testen, HTTP, Scraping, Pandas, SQL |
| 5 | 20–25 | Ausflüge: Flask, Streamlit, FastAPI, Tkinter, Textual |
| 6 | 26 | Abschlussprojekt |

Teil 1–3 bilden den **Grundkurs**, Teil 4–6 den **Aufbaukurs**. Der vollständige Zuschnitt mit
Begründungen steht in [`docs/GRUNDSTRUKTUR-grundkurs.md`](docs/GRUNDSTRUKTUR-grundkurs.md).

**Ein roter Faden zieht sich durch:** ein Sensor-Logfile. Es wird gelesen (08), getestet (15),
über HTTP geholt (16), mit Pandas ausgewertet (18), in SQLite gespeichert (19) — und dann fünfmal
angezeigt: als Webseite, als Datenapp, als API, als Fenster, als Terminal-Oberfläche.

## Umgebung

**Editor und Terminal**, nicht Notebook. Jupyter kommt in Modul 18 dazu, wo es zum ersten Mal
etwas nützt — bei einem Datensatz, dessen Einlesen 40 Sekunden dauert und den man danach
hundertmal befragt. Im ganzen Kurs gibt es genau zwei Notebooks: Modul 18 und Modul 19.

Ab Modul 15 ist `uv run pytest` der Rückkanal. Davor steht unter jeder Aufgabe eine Zeile
**Erwartete Ausgabe** — damit Sie ohne Nachfrage wissen, ob Sie fertig sind.

## Stand

| Modul | Status |
|---|---|
| 01 Grundlagen | ✅ vollständig |
| 02 Operatoren | ✅ vollständig |
| 03–26 | ⬜ geplant, siehe `docs/GRUNDSTRUKTUR-grundkurs.md` Abschnitt 10 |
