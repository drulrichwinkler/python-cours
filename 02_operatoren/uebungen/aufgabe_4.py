"""Aufgabe 4 -- Kaputten Code reparieren.

Das stuerzt ab. Reparieren Sie es OHNE ein if und ohne den Wert von `anzahl`
zu aendern.

Erwartete Ausgabe (nach der Reparatur):

    False

Hinweis: Bei `and` prueft Python den linken Teil zuerst -- und wenn dort bereits
feststeht, dass das Ganze falsch ist, sieht es den rechten gar nicht mehr an.
Die Reihenfolge ist hier kein Stil, sondern der ganze Trick.

Notieren Sie fuer sich: Welchen Fehlertyp meldet Python?
"""

summe = 0
anzahl = 0

print(summe / anzahl > 10)  # TODO: hier ist der Fehler
