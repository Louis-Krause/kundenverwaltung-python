import tkinter as tk
from tkinter import messagebox

# Liste in der alle Kunden gespeichert werden
Kunden = []

def laden():
    try:
        # Öffnet die Datei im Lesemodus
        with open("Kunden.txt", "r") as datei:

            # Jede Zeile wird als ein Kunde eingelesen
            for zeile in datei:

                # Zerlegt die Zeile anhand des Trennzeichens ***
                teile = zeile.strip().split("***")

                # Prüft ob die Zeile alle benötigten Daten enthält
                if len(teile) == 7:

                    # Erstellt ein Kunden-Dictionary
                    kunde = {
                        "Name": teile[0],
                        "Gerät": teile[1],
                        "Problem": teile[2],
                        "Preis": teile[3],
                        "Status": teile[4],
                        "Datum": teile[5],
                        "Kundennummer": teile[6]
                    }

                    # Kunde wird der Kundenliste hinzugefügt
                    Kunden.append(kunde)

    # Falls die Datei noch nicht existiert
    except FileNotFoundError:
        print("Keine Kundendatei gefunden. Es wird eine neue erstellt.")

        # Neue leere Datei erstellen
        with open("Kunden.txt", "w") as datei:
            pass

laden()


def speichern():

    # Öffnet Datei im Schreibmodus (überschreibt alte Daten)
    with open("Kunden.txt", "w") as datei:

        # Jeder Kunde wird als eine Zeile gespeichert
        for K in Kunden:

            # Daten werden mit *** getrennt gespeichert
            zeile = f'{K["Name"]}***{K["Gerät"]}***{K["Problem"]}***{K["Preis"]}***{K["Status"]}***{K["Datum"]}***{K["Kundennummer"]}'

            # Zeile wird in Datei geschrieben
            datei.write(zeile + "\n")

            print(zeile)


def Kundennummer_rechner():

    # Wenn noch keine Kunden existieren
    if not Kunden:
        print("Keine Kunden")
        return 1

    # Sucht die größte vorhandene Kundennummer
    groesteId = max(int(k["Kundennummer"]) for k in Kunden)

    # Neue ID = größte ID + 1
    NewId = groesteId + 1

    return NewId


def hinzuefuegen(name, gereat, problem, preis, datum, kundennummer):

    # Erstellt ein neues Kunden-Dictionary
    kunde = {
        "Name": name,
        "Gerät": gereat,
        "Problem": problem,
        "Preis": preis,
        "Status": "Offen",
        "Datum": datum,
        "Kundennummer": kundennummer
    }

    # Kunde wird zur Liste hinzugefügt
    Kunden.append(kunde)

    print(kunde)



# =========================
# Kunden löschen
# =========================
def kunde_loeschen(index):

    # Holt den Kunden anhand seines Index
    kunde = Kunden[index]

    # Sicherheitsabfrage bevor gelöscht wird
    antwort = messagebox.askyesno(
        "Bestätigung",
        f"Willst du '{kunde['Name']}' wirklich löschen?"
    )

    # Wenn Nutzer "Nein" klickt
    if antwort == False:
        return

    # Kunde wird aus der Liste gelöscht
    del Kunden[index]

    # Änderungen werden gespeichert
    speichern()


def kunde_suchen(suchtext):

    # Wenn kein Suchtext eingegeben wurde → alle Kunden anzeigen
    if not suchtext:
        return Kunden

    # Durchsucht Name, Problem und Kundennummer
    return [
        k for k in Kunden
        if suchtext.lower() in k["Name"].lower()
        or suchtext.lower() in k["Problem"].lower()
        or suchtext in str(k["Kundennummer"])
    ]
