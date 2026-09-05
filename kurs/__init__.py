"""Hilfsfunktionen fuer den Python-Grundkurs.

Der Kurs hat keine Praesenz und keine Abgabe. Der Rueckkanal ist diese Datei:
Sie sagt Ihnen gruen oder rot, ohne die Antwort zu verraten.

    from kurs import pruefe, tipp

    vorhersage = "..."
    pruefe(vorhersage, "3a7bd3e2...")
"""

from __future__ import annotations

import hashlib
import re

__all__ = ["pruefe", "tipp", "loesung_von"]


def _normieren(text: object) -> str:
    """Vergleichbar machen, ohne pedantisch zu sein.

    Kleinschreibung, Leerzeichen zusammenziehen, aeussere Anfuehrungszeichen weg.
    "  True " und "true" gelten damit als dieselbe Antwort.
    """
    s = str(text).strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip("\"'")


def _hash(text: object) -> str:
    return hashlib.sha256(_normieren(text).encode("utf-8")).hexdigest()


def pruefe(vorhersage: object, erwartet_hash: str, hinweis: str = "") -> bool:
    """Vergleicht Ihre Vorhersage mit der hinterlegten Antwort.

    Die Antwort steht nicht im Klartext in dieser Datei -- nur ihre Pruefsumme.
    Sie koennen also nicht versehentlich spicken, und Sie bekommen trotzdem
    sofort eine Rueckmeldung.
    """
    if _normieren(vorhersage) in ("", "...", "hier eintragen"):
        print("⬜ Noch nichts eingetragen. Schreiben Sie Ihre Vorhersage hin --")
        print("   auch eine unsichere. Raten ist der Zweck der Uebung.")
        return False

    if _hash(vorhersage) == erwartet_hash:
        print(f"✅ Richtig: {vorhersage}")
        return True

    print(f"❌ Noch nicht. Sie hatten: {vorhersage!r}")
    if hinweis:
        print(f"   Hinweis: {hinweis}")
    print("   Fuehren Sie die naechste Zelle aus -- dann sehen Sie, was wirklich herauskommt.")
    return False


def tipp(text: str) -> None:
    """Gibt einen Hinweis aus, der die Antwort nicht verraet."""
    print(f"💡 {text}")


def loesung_von(antwort: object) -> str:
    """Nur fuer Autoren: erzeugt die Pruefsumme zu einer Antwort."""
    return _hash(antwort)
