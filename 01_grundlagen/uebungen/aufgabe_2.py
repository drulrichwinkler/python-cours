"""Aufgabe 2 -- Typen vorhersagen.

Tragen Sie unten ein, was die vier print()-Zeilen ausgeben -- BEVOR Sie die Datei
ausfuehren. pruefe() sagt Ihnen, ob es stimmt, ohne die Antwort zu verraten.

Hinweis: Schreiben Sie die Zeile so hin, wie Python sie druckt -- mit spitzen
Klammern und Anfuehrungszeichen.
"""

from kurs import pruefe

# TODO: ersetzen Sie die Punkte durch Ihre Vorhersage
pruefe(
    "...",
    "ec15c2bad4367dd8e12539fc1cc9b70b3e6f04d8c07fad82072a535827db73f1",
    "Es geht um 21.7 -- eine Zahl mit Komma.",
)

# Erst danach ausfuehren:
print(type(21.7))
print(type("21.7"))
print(type(21))
print(type(True))
