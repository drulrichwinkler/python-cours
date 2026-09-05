"""Aufgabe 7 -- Statusbyte auslesen.

Geben Sie fuer jedes der vier Flags aus, ob es in `status` gesetzt ist.
Setzen Sie danach BEREIT und geben Sie das neue Byte binaer aus.

Erwartete Ausgabe:

    Bereit: False
    Grenzwert: True
    Fehler: False
    Kalibrierung: True
    Neues Byte: 0b1011

Hinweis 1: status & MASKE liefert eine ZAHL, nicht True/False. Ohne bool()
stuende dort "Grenzwert: 2" -- richtig, aber nicht die Antwort auf die Frage.
Hinweis 2: Ein Bit setzen heisst ODER. Binaer ausgeben: bin().
"""

BEREIT = 0b0001
GRENZWERT = 0b0010
FEHLER = 0b0100
KALIBRIERUNG = 0b1000

status = 0b1010

# TODO: vier Zeilen


# TODO: BEREIT setzen und binaer ausgeben
