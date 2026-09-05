"""Aufgabe 3 -- Kaputten Code reparieren.

Dieses Programm stuerzt ab. Fuehren Sie es aus, LESEN SIE DEN TRACEBACK und
reparieren Sie es.

Der Messwert kommt als Text aus einer Datei -- an der ersten Zeile duerfen Sie
nichts aendern.

Erwartete Ausgabe (nach der Reparatur):

    Abstand zum Grenzwert: 3.3000000000000007

Ja, wirklich. Warum, steht in Abschnitt 8 von entdecken.ipynb.

Notieren Sie fuer sich: Welchen Fehlertyp meldet Python, und welche Zeile?
"""

messwert = "21.7"  # <- nicht aendern
grenzwert = 25

abstand = grenzwert - messwert  # TODO: hier ist der Fehler
print(f"Abstand zum Grenzwert: {abstand}")
