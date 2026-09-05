"""Aufgabe 2 -- Auswertungsreihenfolge vorhersagen.

Tragen Sie unten Ihre Vorhersagen ein, BEVOR Sie die Datei ausfuehren.

Hinweis: Zwei der fuenf Zeilen ueberraschen fast jeden. Bei ** lohnt die Frage,
von welcher Seite Python liest -- und wie stark ein Minuszeichen bindet.
"""

from kurs import pruefe

# TODO: Was ergibt  2 ** 3 ** 2 ?
pruefe(
    "...",
    "94f8607915dff25f013e45fc0642fb9830b0fb25ab0ab46d477eaf1061def379",
    "Nicht (2**3)**2. Andersherum.",
)

# TODO: Was ergibt  -3 ** 2 ?
pruefe(
    "...",
    "d5c534fde62beb89c745a59952c8efed8b7523cbd047e682782e4367de9ea3bf",
    "Die Potenz kommt zuerst, das Minus danach.",
)

# Erst danach ausfuehren:
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)  # fmt: skip
print(-3 ** 2)  # fmt: skip
print(10 - 4 - 3)
