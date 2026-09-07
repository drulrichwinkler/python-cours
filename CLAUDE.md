# Arbeitsanweisungen für dieses Repository

## Das Publikum — die wichtigste Tatsache

**Studierende im 5. Semester Informationstechnik an einer dualen Hochschule.**

Sie programmieren seit vier Semestern, in C und/oder Java. Sie arbeiten im Betrieb. Sie
wissen, was eine Variable, ein Typ, eine Funktion, eine Schleife, ein Compiler, ein Fehler,
ein Stacktrace, ein Test und ein Terminal ist.

**Neu ist ihnen Python**, nicht das Programmieren.

Daraus folgt für jeden Text im Kurs:

- **Erkläre die Sache, nicht das Konzept.** „`//` ist Ganzzahldivision" ist Sache.
  „Eine Division teilt eine Zahl durch eine andere" ist Konzept — und beleidigend.
- **Der eigentliche Stoff ist das Delta zu C und Java.** `7 / 2` ist in C ganzzahlig und in
  Python nicht; `-17 % 5` ist dort `-2` und hier `3`; Javas `==` ist Pythons `is`. Solche
  Stellen dürfen ausführlich sein — sie sind der Grund, warum es den Kurs gibt.
- **Keine Ermutigung.** „Fehler sind kein Zeichen, dass Sie etwas falsch gemacht haben"
  unterstellt eine Verunsicherung, die es nicht gibt, und wirkt dadurch herablassend.
- **Siezen**, ausnahmslos — auch in Kommentaren, Aufgabenstellungen und Testnamen.
- **Keine Zeitangaben.** Kein „Dauer: etwa 2 Stunden", kein „About 30 minutes", weder im
  Modul-README noch im Notebook. Solche Zahlen sind geraten, und sie treffen niemanden:
  Wer schneller ist, hält sich für oberflächlich; wer länger braucht, für zu langsam. Im
  Selbststudium ohne Note misst ohnehin niemand mit. Was eine Einheit kostet, steht in
  ihrem Umfang — nicht in einer Behauptung darüber.

Wo eine Python-Eigenheit unerwartet ist, ist eine lange Erklärung richtig. Kurz gehört es
dort, wo nichts Neues passiert.

**Nicht kürzen:** Erklärungen von Python-Mechanik — `__file__`, `Path` und das `/` darauf,
Decorator-Syntax, `-> None`, `assert`, Tuple-Unpacking. Die bleiben, auch wenn sie in
fünfzehn Testdateien gleichlautend stehen: Jede Datei muss für sich lesbar sein, und wer
mit Übung 06 anfängt, hat Übung 01 nicht gelesen. Studierende dürfen überspringen, was sie
schon kennen — dafür braucht es keine Vorkehrung, und ein Verweis auf eine andere Datei
zwingt nur zum Blättern.

## Vor dem Abschluss: Lektorat

**Jedes Dokument, das Studierende zu sehen bekommen, geht durch den Agenten `lektor`**,
bevor es als fertig gilt — neu geschrieben oder geändert, gleichermaßen. Das betrifft:

- `README.md` in der Wurzel und in jedem Modul
- `*/explore.ipynb` (die Markdown-Zellen)
- `*/exercises/*.py` und `*/solutions/*.py` — Docstrings und Kommentare
- `*/tests/*.py` — die erklärenden Kommentare, die Studierende lesen sollen
- `*/exercises/thinking.md`
- `.vscode/settings.json` — die Kommentare darin sind an Studierende gerichtet

Der Agent prüft **nur die Ansprache**: zu vereinfachend, herablassend, geschwätzig — oder
umgekehrt zu knapp. Sein Auftrag steht in `~/.claude/agents/lektor.md`.

Befunde einarbeiten, nicht wegdiskutieren. Wo du widersprichst, sag es dem Nutzer mit
Begründung, statt den Befund stillschweigend zu übergehen.

**Nicht geprüft** werden `docs/` (deutsche Planungsunterlagen), `demos/` (Autorenmaterial)
und `course/` (Infrastruktur) — dort ist der Autor das Publikum.

## Was den Kurs sonst trägt

- **Rückkanal statt Betreuung.** Es gibt keine Präsenz und keine Abgabe. Jede Aufgabe nennt
  ihre erwartete Ausgabe im Docstring, jeder Test prüft genau das, jede Vorhersage im
  Notebook ist ein `assert` mit `...` als Platzhalter. Stille heißt richtig.
- **Keine Lösung im Lesefluss.** Lösungen liegen in `solutions/`, nie unter der Aufgabe.
- **Aufgabentypen, die KI-Assistenten überleben:** Code lesen, Ausgabe vorhersagen,
  kaputten Code reparieren, eine Entscheidung begründen.
- **Werkzeugkette:** `uv` durchgehend. `uv run pytest -m "not your_turn"`, `uv run mypy`,
  `uv run ruff check .`, `uv run ruff format --check .` müssen grün sein.
- **Abhängigkeiten: eine Gruppe, alles drin.** `uv sync` installiert die komplette
  Werkzeugkette *und* jedes Paket, das irgendein Modul braucht — `requests`, `pandas`, die fünf
  Frameworks. Keine Aufteilung in Gruppen: Studierende richten einmal ein und stoßen ab Modul 16
  nicht auf einen zweiten Installationsschritt. Neues Paket für ein neues Modul: in `dev`,
  mit einer Kommentarzeile, welches Modul es braucht.
- **Notebooks laufen top-to-bottom durch.** Zellen, die absichtlich scheitern (Vorhersagen,
  vorgeführte Fehler), tragen das Tag `raises-exception`.
