# Kundenverwaltung (Python)

Ein einfaches Kundenverwaltungssystem mit Python und Tkinter.
Das Programm ermöglicht es, Kundenaufträge zu verwalten, zu bearbeiten und zu verfolgen.

# Funktionen

* Kunden hinzufügen
* Kunden bearbeiten
* Kunden löschen
* Statussystem (Offen / In Arbeit / Fertig)
* Kundensuche
* Filter nach Status
* Einnahmenberechnung (nur fertige Aufträge werden gezählt)
* Statistikübersicht
* Automatische Kundennummern (#0001)
* CSV Export der Kundendaten
* Detailanzeige von Kunden
* Sortierte Kundenliste
* Verbesserte Stabilität bei Suche und Filter

# Technologien

* Python
* Tkinter (GUI)
* Lokale Dateispeicherung (.txt)
* CSV Export

# Beschreibung

Dieses Projekt wurde erstellt, um meine Programmierkenntnisse in Python zu verbessern und ein vollständiges kleines Verwaltungssystem mit grafischer Benutzeroberfläche zu entwickeln.

Die Anwendung trennt Frontend (GUI) und Backend (Logik & Datenspeicherung), wodurch der Code übersichtlich und leichter wartbar bleibt.

Zusätzlich können Kundendaten als CSV-Datei exportiert werden, um sie z.B. in Excel weiterzuverwenden.

# Projektstruktur

Kundenverwaltung

* main.py (Frontend / GUI)
* backend.py (Logik und Datenverwaltung)
* Kunden.txt (Speicherung der Kundendaten)
* Kunden_export.csv (Exportierte Kundendaten)

# Starten des Programms

Python muss installiert sein.

Programm starten mit:

python main.py
