"""Loesungen zu Modul 01 -- Python-Grundlagen.

Ausfuehren mit:  uv run 01_grundlagen/uebungen/loesungen.py

Lesen Sie diese Datei erst, wenn Sie zu jeder Aufgabe etwas Eigenes hingeschrieben haben.
Auch etwas Falsches. Wer die Loesung zuerst liest, erlebt Verstehen, ohne etwas zu koennen.
"""

print("=" * 60)
print("Aufgabe 1 -- Sensor-Steckbrief")
print("=" * 60)

kennung = "TH-04"
ort = "Halle 2"
messwert = 21.7
ist_aktiv = True

print(f"Kennung: {kennung}")
print(f"Ort: {ort}")
print(f"Messwert: {messwert}")
print(f"Aktiv: {ist_aktiv}")


print()
print("=" * 60)
print("Aufgabe 2 -- Typen vorhersagen")
print("=" * 60)

print(type(21.7))
print(type("21.7"))
print(type(21))
print(type(True))

# Zur letzten Zeile: bool ist in Python ein Sonderfall von int.
# True verhaelt sich in einer Rechnung wie 1, False wie 0. Das braucht man selten --
# aber es erklaert, warum True + True den Wert 2 ergibt.


print()
print("=" * 60)
print("Aufgabe 3 -- Kaputten Code reparieren")
print("=" * 60)

# Der Fehler war:  TypeError: unsupported operand type(s) for -: 'int' and 'str'
# gemeldet in Zeile 3 des Aufgabencodes.
# Grund: `messwert` ist Text, keine Zahl. Rechnen kann man damit nicht.
# Reparatur: einmal umwandeln. Der Text bleibt unveraendert, wie verlangt.

messwert = "21.7"
grenzwert = 25
abstand = grenzwert - float(messwert)
print(f"Abstand zum Grenzwert: {abstand}")

# Die vielen Neunen am Ende sind kein Fehler -- siehe Aufgabe 8c.


print()
print("=" * 60)
print("Aufgabe 4 -- Umwandeln")
print("=" * 60)

a = int("42")
b = float(10)
c = int(3.7)
d = bool(0)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))


print()
print("=" * 60)
print("Aufgabe 5 -- Formatierte Messwertzeile")
print("=" * 60)

kennung = "TH-04"
messwert = 22.83333

print(f"{kennung} meldet {messwert:.1f} Grad.")

# `:.1f` rundet nur fuer die Ausgabe. Die Variable `messwert` bleibt 22.83333 --
# das ist der Unterschied zu round(), das einen neuen Wert erzeugt.


print()
print("=" * 60)
print("Aufgabe 6 -- Umrechnung")
print("=" * 60)

fahrenheit = 71.6
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} Grad Fahrenheit sind {celsius:.1f} Grad Celsius.")

# Ohne Formatierung stuende hier 21.999999999999996. Auch das ist Aufgabe 8c.


print()
print("=" * 60)
print("Aufgabe 7 -- Traceback lesen")
print("=" * 60)

print("a) Zeile 7 -- die unterste Datei-Zeile im Traceback ist die, wo es knallte.")
print("b) Zeile 12 -- dort steht der Aufruf print(mittelwert(werte)).")
print("c) anzahl war 0 -- nur dann wirft eine Division ZeroDivisionError.")
print("d) Die Liste `werte` war leer, deshalb war anzahl null.")


print()
print("=" * 60)
print("Aufgabe 8 -- Begruenden")
print("=" * 60)

print(
    """
a) int(3.9) ergibt 3, weil int() abschneidet statt zu runden: Es wirft alles hinter dem
   Komma weg. Wer runden will, nimmt round(3.9) -- das ergibt 4.

b) int(3.9) bekommt eine Zahl und darf sie abschneiden. int("3.9") bekommt Text und muss
   ihn zuerst deuten -- und int() kann ausschliesslich Text deuten, der eine ganze Zahl
   darstellt. "3.9" ist keine. Der Umweg lautet int(float("3.9")).

c) 0.1 laesst sich im Zweiersystem nicht exakt darstellen, genauso wenig wie 1/3 im
   Dezimalsystem exakt darstellbar ist (0.3333... hoert nie auf). Der Rechner speichert
   deshalb einen winzig danebenliegenden Wert, und beim Addieren wird die Abweichung
   sichtbar: 0.30000000000000004. Das hat jede Programmiersprache mit Fliesskommazahlen.
   Deshalb vergleicht man Fliesskommazahlen nie mit == -- und Geldbetraege gar nicht.
""".strip()
)


print()
print("=" * 60)
print("Bonus -- Die Sensor-Zeile")
print("=" * 60)

kennung = "TH-04"
zeit = "14:05"
wert = 22.83333

# Weg 1: ueber sep=
print(zeit, kennung, f"{wert:.1f} C", sep=" | ")

# Weg 2: als f-String
print(f"{zeit} | {kennung} | {wert:.1f} C")

# Welcher ist besser lesbar? Der f-String -- weil die Zeile dort so aussieht,
# wie sie spaeter ausgegeben wird. Bei sep= muss man sich das Ergebnis zusammendenken.
# Ab Modul 08 lesen wir genau dieses Format wieder ein.
