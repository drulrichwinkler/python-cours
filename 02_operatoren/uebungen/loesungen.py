"""Loesungen zu Modul 02 -- Operatoren und Ausdruecke.

Ausfuehren mit:  uv run 02_operatoren/uebungen/loesungen.py

Erst lesen, wenn Sie zu jeder Aufgabe etwas Eigenes hingeschrieben haben.
"""

print("=" * 60)
print("Aufgabe 1 -- Grundrechenarten")
print("=" * 60)

print(15 + 27)
print(100 - 43)
print(8 * 7)
print(45 / 6)
print(45 // 6)
print(45 % 6)
print(2**10)

# Beachten Sie Zeile 4: 45 / 6 ergibt 7.5, also einen float.
# 45 // 6 ergibt 7 -- abgeschnitten, nicht gerundet. 45 % 6 ist der Rest, 3.
# 7 * 6 + 3 = 45. So haengen // und % immer zusammen.


print()
print("=" * 60)
print("Aufgabe 2 -- Ausgabe vorhersagen")
print("=" * 60)

print(2 + 3 * 4)  # 14  -- Punkt vor Strich
print((2 + 3) * 4)  # 20  -- Klammern zuerst
print(2**3**2)  # 512 -- ** von rechts: 2 ** (3 ** 2) = 2 ** 9
print(-(3**2))  # -9  -- ** bindet staerker als das Minus: -(3 ** 2)
print(10 - 4 - 3)  # 3   -- Minus von links: (10 - 4) - 3


print()
print("=" * 60)
print("Aufgabe 3 -- Wahrheitstabelle")
print("=" * 60)

print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")


print()
print("=" * 60)
print("Aufgabe 4 -- Kaputten Code reparieren")
print("=" * 60)

# Der Fehler war:  ZeroDivisionError: division by zero
# Reparatur: die Pruefung VOR die Division stellen. Ist der linke Teil von `and`
# falsch, sieht Python den rechten gar nicht mehr an (Kurzschlussauswertung).
# Die Reihenfolge ist hier kein Stil, sondern der ganze Trick.

summe = 0
anzahl = 0
print(anzahl != 0 and summe / anzahl > 10)


print()
print("=" * 60)
print("Aufgabe 5 -- Bereichspruefung")
print("=" * 60)

wert = 21.7
print(f"{wert} plausibel: {-40 <= wert <= 85}")

wert = -55.0
print(f"{wert} plausibel: {-40 <= wert <= 85}")

wert = 85.0
print(f"{wert} plausibel: {-40 <= wert <= 85}")

# Dreimal fast dieselbe Zeile -- das stoert zu Recht. In Modul 03 lernen Sie die
# Schleife, die genau diese Wiederholung beseitigt. Bis dahin schreiben wir sie aus.
# Beachten Sie die Kette: -40 <= wert <= 85 prueft beide Grenzen auf einmal.


print()
print("=" * 60)
print("Aufgabe 6 -- Altersgruppe als boolescher Ausdruck")
print("=" * 60)

alter = 25

print(f"Kind: {alter < 12}")
print(f"Teenager: {12 <= alter <= 17}")
print(f"Erwachsener: {18 <= alter <= 64}")
print(f"Senior: {alter >= 65}")

# Vier Ausgabezeilen, weil vier Fragen gestellt werden. In Modul 03 wird daraus
# EINE Zeile mit if/elif -- und dann lohnt der Vergleich: Was ist besser lesbar?


print()
print("=" * 60)
print("Aufgabe 7 -- Statusbyte auslesen")
print("=" * 60)

BEREIT = 0b0001
GRENZWERT = 0b0010
FEHLER = 0b0100
KALIBRIERUNG = 0b1000

status = 0b1010

print(f"Bereit: {bool(status & BEREIT)}")
print(f"Grenzwert: {bool(status & GRENZWERT)}")
print(f"Fehler: {bool(status & FEHLER)}")
print(f"Kalibrierung: {bool(status & KALIBRIERUNG)}")

neu = status | BEREIT
print(f"Neues Byte: {bin(neu)}")

# bool() ist noetig, weil status & GRENZWERT die Zahl 2 liefert, nicht True.
# Ohne bool() stuende dort "Grenzwert: 2" -- richtig, aber nicht die Antwort
# auf die gestellte Frage.


print()
print("=" * 60)
print("Aufgabe 8 -- Begruenden")
print("=" * 60)

print(
    """
a) == fragt nach dem Wert ("steht dasselbe drin?"), is nach der Identitaet
   ("ist es dasselbe Ding im Speicher?"). Fuer zwei Messwerte nehmen Sie ==:
   Sie wollen wissen, ob dieselbe Temperatur gemeldet wurde, nicht ob es sich um
   dasselbe Objekt handelt.

b) Dass dieselbe Frage je nach Umgebung verschieden beantwortet wird, heisst:
   Verlassen Sie sich nicht darauf. Benutzen Sie is nicht fuer Werte -- nur fuer
   den einen Fall, fuer den es gedacht ist: `if ergebnis is None`.
   Wie das Zwischenspeichern der Zahlen genau funktioniert, muessen Sie nicht wissen.

c) Wegen der Kurzschlussauswertung. Bei `and` prueft Python den linken Teil zuerst;
   ist er falsch, steht das Ergebnis bereits fest und der rechte Teil wird gar nicht
   ausgewertet. anzahl != 0 ist bei anzahl = 0 falsch -- also kommt es nie zur
   Division. Das ist eine Zusage der Sprache, kein Zufall.
""".strip()
)


print()
print("=" * 60)
print("Bonus -- Schaltjahr")
print("=" * 60)

jahr = 2024
print(f"{jahr}: {jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0)}")

jahr = 1900
print(f"{jahr}: {jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0)}")

jahr = 2000
print(f"{jahr}: {jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0)}")

jahr = 2023
print(f"{jahr}: {jahr % 4 == 0 and (jahr % 100 != 0 or jahr % 400 == 0)}")

# Zur Klammerfrage aus dem Aufgabenblatt -- die ehrliche Antwort:
# Ohne Klammern liest Python  (jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0 ,
# weil `and` staerker bindet als `or`. Und dieser Ausdruck liefert fuer JEDE Jahreszahl
# dasselbe Ergebnis wie der geklammerte. Nachgerechnet fuer die Jahre 1 bis 4000:
# null Abweichungen. Der Grund: Wer durch 400 teilbar ist, ist auch durch 4 teilbar --
# der Fall, in dem sich die beiden Formen unterscheiden koennten, existiert nicht.
#
# Warum dann klammern? Weil der Ausdruck die REGEL abbilden soll, nicht nur ihr
# Ergebnis. Die Regel lautet "durch 4 teilbar UND (...)". Wer das ohne Klammern
# hinschreibt, verlaesst sich auf eine Bindungsstaerke und auf eine Zahleneigenschaft,
# die beide nirgends dastehen. Der naechste Leser muss dann beweisen, was er lesen
# koennen sollte.
