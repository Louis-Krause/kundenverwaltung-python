import backend
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Schriftart und Farben für das UI (Dark-Design)

Front = ("Segoe UI", 11)
BG_MAIN = "#1e1e1e"        # Hintergrund Hauptfenster
BG_FRAME = "#2a2a2a"       # Hintergrund für Frames
BG_WIDGET = "#333333"      # Hintergrund für Eingabefelder/Listbox
BTN_NORMAL = "#3a3a3a"     # Normaler Button-Hintergrund
BTN_HOVER = "#2e2d2d"      # Button-Hover
TEXT_COLOR = "#ffffff"      # Standard-Textfarbe
ACCENT = "#4c8bf5"          # Auswahlfarbe in der Listbox

# Hauptfenster erstellen und konfigurieren

window = tk.Tk()
window.geometry("500x500")
window.title("Kundenverwaltung v1.0")
window.config(bg=BG_MAIN)

# Layout: linke Spalte (Kundenliste) und rechte Spalte (Details)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)
window.grid_rowconfigure(0, weight=1)

# Popup zum Hinzufügen eines neuen Kunden
def pop_up():
    # Öffnet ein neues Fenster, in dem ein Kunde angelegt werden kann.
    popUp = tk.Toplevel(window)
    popUp.geometry("300x300")
    popUp.resizable(False, False)
    popUp.title = "Kunde Hinzufügen."
    popUp.config(bg=BG_FRAME)

    # Eingabefeld für den Namen
    tk.Label(popUp, text="Name", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_name = tk.Entry(popUp)
    entry_name.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_name.pack()

    # Eingabefeld für das Gerät
    tk.Label(popUp, text="Gerät", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_geraet = tk.Entry(popUp)
    entry_geraet.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_geraet.pack()

    # Eingabefeld für das Problem
    tk.Label(popUp, text="Problem", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_problem = tk.Entry(popUp)
    entry_problem.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_problem.pack()

    # Eingabefeld für den Preis
    tk.Label(popUp, text="Preis", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_preis = tk.Entry(popUp)
    entry_preis.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_preis.pack()

    def hinzuefuegen():
        # Liest die Eingaben aus, validiert sie und fügt den Kunden über das Backend hinzu.
        # Aktuelles Datum für den neuen Kunden
        datum = datetime.now().strftime("%d.%m.%Y")

        name = entry_name.get()
        geraet = entry_geraet.get()
        problem = entry_problem.get()
        preis = entry_preis.get()

        # Prüfen, ob alle Felder ausgefüllt sind
        if not all([name, geraet, problem, preis]):
            messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen.")
            return

        # Preis auf gültige positive Zahl prüfen
        preis_text = entry_preis.get().strip()
        if preis_text == "":
            messagebox.showerror("Fehler", "Bitte Preis eingeben.")
            return
        try:
            preis = float(preis_text)
            if preis < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gib eine gültige positive Zahl für den Preis ein.")
            return

        # Neue Kundennummer vom Backend holen und Kunden hinzufügen
        kundennummer = backend.Kundennummer_rechner()
        backend.hinzuefuegen(name, geraet, problem, preis, datum, kundennummer)
       
        # Daten speichern und Oberfläche aktualisieren
        backend.speichern()

        listbox_update()

        if not listbox.curselection: return

        listbox.select_set(tk.END)

        anzeigen_auto()
        

        # PopUp schliesen
        popUp.destroy()

    # Button zum Absenden im Popup
    add = tk.Button(
        popUp,
        text="Hinzufügen",
        bg=BTN_NORMAL,
        fg="white",
        activebackground=BTN_HOVER,
        relief="flat",
        padx=15,
        pady=8,
        command=hinzuefuegen
    )
    add.pack()

# Popup zum Bearbeiten eines bestehenden Kunden
def pop_upBearbeiten():
    #Öffnet ein Fenster mit den aktuellen Daten des ausgewählten Kunden zum Bearbeiten.
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]
    kunde = backend.Kunden[index]

    popUpB = tk.Toplevel()
    popUpB.geometry("300x300")
    popUpB.resizable(False, False)
    popUpB.config(bg=BG_FRAME)
    popUpB.title = "Kunde bearbeiten"

    # Eingabefeld Name (vorausgefüllt)
    tk.Label(popUpB, text="Name", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_name = tk.Entry(popUpB)
    entry_name.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_name.pack()
    entry_name.insert(0, kunde["Name"])

    # Eingabefeld Gerät (vorausgefüllt)
    tk.Label(popUpB, text="Gerät", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_geraet = tk.Entry(popUpB)
    entry_geraet.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_geraet.pack()
    entry_geraet.insert(0, kunde["Gerät"])

    # Eingabefeld Problem (vorausgefüllt)
    tk.Label(popUpB, text="Problem", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_problem = tk.Entry(popUpB)
    entry_problem.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_problem.pack()
    entry_problem.insert(0, kunde["Problem"])

    # Eingabefeld Preis (vorausgefüllt)
    tk.Label(popUpB, text="Preis", font=Front, bg=BG_WIDGET, fg=TEXT_COLOR).pack()
    entry_preis = tk.Entry(popUpB)
    entry_preis.config(bg=BTN_HOVER, fg=TEXT_COLOR, insertbackground="white")
    entry_preis.pack()
    entry_preis.insert(0, str(kunde["Preis"]))

    def bearbeitenSpeichern():
        fehler = False

        # Prüfen, ob alle Felder ausgefüllt sind
        if not all([entry_name.get(), entry_geraet.get(), entry_problem.get(), entry_preis.get()]):
            messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen.")
            return

        Preis_text = entry_preis.get().strip()

        # Preis auf gültige Zahl prüfen
        try:
            Preis = float(Preis_text)
        except ValueError:
            messagebox.showerror("Preis muss eine Zahl sein.")
            fehler = True
            return

        # Preis auf positiven Wert prüfen
        try:
            preisT = float(entry_preis.get())
            if preisT < 0:
                raise ValueError
        except ValueError:
            fehler = True
            messagebox.showerror("Fehler", "Bitte gib eine gültige positive Zahl für den Preis ein.")
            return

        # Wenn keine Fehler aufgetreten sind, Kundendaten aktualisieren
        if not fehler:
            kunde["Name"] = entry_name.get()
            kunde["Gerät"] = entry_geraet.get()
            kunde["Problem"] = entry_problem.get()
            kunde["Preis"] = float(entry_preis.get())

            # Backend speichern und Oberfläche aktualisieren
            backend.speichern()
            listbox_update()

            listbox.select_set(index)
            
            anzeigen_auto()

            popUpB.destroy()

    # Button zum Speichern der Änderungen
    tk.Button(
        popUpB,
        text="Speichern",
        bg=BTN_NORMAL,
        fg="white",
        activebackground=BTN_HOVER,
        relief="flat",
        padx=15,
        pady=8,
        command=bearbeitenSpeichern
    ).pack()


#Kunden löschen
def loeschen():
    # Löscht den ausgewählten Kunden aus der Liste.
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]
    backend.kunde_loeschen(index)

    Kinfo.delete("1.0", tk.END)
    listbox_update()


# Suchfeld – aktualisiert die Listbox bei Eingabe
def update_search(*args):
    # Wird bei jeder Änderung des Suchtextes aufgerufen und filtert die Liste.
    suchtext = search_var.get()
    gefiltert = backend.kunde_suchen(suchtext)

    listbox.delete(0, tk.END)
    for K in gefiltert:
        listbox.insert(
            tk.END,
            f"#{int(K['Kundennummer']):04} | {K['Status']} | {K['Name']} - {K['Gerät']}"
        )


# Status des ausgewählten Kunden weiterdrehen
def status():
   # Ändert den Status des ausgewählten Kunden: Offen -> In Arbeit -> Fertig -> Offen.
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]
    kunde = backend.Kunden[index]

    if kunde["Status"] == "Offen":
        kunde["Status"] = "In Arbeit"
    elif kunde["Status"] == "In Arbeit":
        kunde["Status"] = "Fertig"
    else:
        kunde["Status"] = "Offen"

    backend.speichern()
    anzeigen_auto()
    listbox_update()


# Filter-Menü anzeigen 
def filterButton(event):
    #Zeigt bei Klick auf den Filter-Button ein Kontextmenü an.
    menu.tk_popup(event.x_root, event.y_root)


# Liste nach Status filtern
def filtern(Stat):
    #Zeigt nur Kunden mit dem übergebenen Status an.
    listbox.delete(0, tk.END)
    for K in sorted(backend.Kunden, key=lambda k: k["Datum"]):
        if K["Status"] == Stat:
            listbox.insert(tk.END, f"#{int(K['Kundennummer']):04} | {K['Status']} | {K['Name']} - {K['Gerät']}")


# Statistik anzeigen
def statistik():
    #Zeigt eine Übersicht über Anzahl offener, in Arbeit und Fertiger Kunden sowie Gesamteinnahmen.
    Kunde = backend.Kunden
    Kinfo.delete("1.0", tk.END)
    Num = 0
    Num2 = 0
    Num3 = 0

    Money = sum(float(k["Preis"]) for k in Kunde if k["Status"] == "Fertig")

    for K in Kunde:
        if K["Status"] == "Offen":
            Num += 1
        elif K["Status"] == "In Arbeit":
            Num2 += 1
        else:
            Num3 += 1

    Kinfo.insert(tk.END, f"""
                Statistik:

                Kunden offen:           {Num}
                Kunden in Arbeit:       {Num2}
                Kunden Fertig:          {Num3}
                Einnahmen:               {Money:.2f}$ """)


# ===== Hover-Effekte für Buttons =====
def on_enter(e):
    e.widget.configure(bg=BTN_HOVER)

def on_leave(e):
    e.widget.configure(bg=BTN_NORMAL)


#  GUI 


# Linker Frame (Kundenliste und Suche)
lFrame = tk.Frame(window)
lFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
lFrame.config(bg=BG_FRAME)
lFrame.grid_rowconfigure(1, weight=1)
lFrame.grid_columnconfigure(0, weight=1)

# Rechter Frame (Detailanzeige)
RFrame = tk.Frame(window)
RFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
RFrame.config(bg=BG_FRAME)
RFrame.grid_rowconfigure(0, weight=1)
RFrame.grid_columnconfigure(0, weight=1)

# Unterer Frame (Buttons)
BFrame = tk.Frame(window)
BFrame.config(bg=BG_MAIN)
BFrame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Suchfeld
search_var = tk.StringVar()
search_entry = tk.Entry(lFrame, textvariable=search_var)
search_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
search_var.trace_add("write", update_search)

# Listbox (Kundenliste)
listbox = tk.Listbox(lFrame, height=50, font="Arial")
listbox.grid(row=1, column=0, sticky="nsew")

# Scrollbar für Listbox
scrollbar = tk.Scrollbar(lFrame, orient="vertical")
scrollbar.grid(row=1, column=1, sticky="nesw")
listbox.config(bg=BG_WIDGET, fg=TEXT_COLOR, selectbackground=ACCENT,
               selectforeground="white", highlightthickness=0, borderwidth=0,
               yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Filter-Button
FilterBTN = tk.Button(
    lFrame,
    text="Filtern",
    bg=BTN_NORMAL,
    fg="white",
    activebackground=BTN_HOVER,
    relief="flat"
)
FilterBTN.grid(row=0, column=2)
FilterBTN.bind("<Enter>", on_enter)
FilterBTN.bind("<Leave>", on_leave)
FilterBTN.bind("<Button-1>", filterButton)

# Textfeld für Kundendetails
Kinfo = tk.Text(RFrame, font=Front)
Kinfo.grid(row=0, column=0, sticky="nsew")
Kinfo.config(bg=BG_WIDGET, fg=TEXT_COLOR, insertbackground="white",
             highlightthickness=0, borderwidth=0)

# Buttons unten
hinzufuegenBTN = tk.Button(
    BFrame,
    text="Kunde Hinzufügen",
    bg=BTN_NORMAL,
    fg="white",
    activebackground=BTN_HOVER,
    relief="flat",
    padx=15,
    pady=8,
    command=pop_up
)
hinzufuegenBTN.grid(row=1, column=0)
hinzufuegenBTN.config(width=20, height=2)
hinzufuegenBTN.bind("<Enter>", on_enter)
hinzufuegenBTN.bind("<Leave>", on_leave)

loeschenBTN = tk.Button(
    BFrame,
    text="Kunde Löschen",
    bg=BTN_NORMAL,
    fg="white",
    activebackground=BTN_HOVER,
    relief="flat",
    padx=15,
    pady=8,
    command=loeschen
)
loeschenBTN.grid(row=1, column=1)
loeschenBTN.config(width=20, height=2)
loeschenBTN.bind("<Enter>", on_enter)
loeschenBTN.bind("<Leave>", on_leave)

bearbeitenBTN = tk.Button(
    BFrame,
    text="Kunde Bearbeiten",
    bg=BTN_NORMAL,
    fg="white",
    activebackground=BTN_HOVER,
    relief="flat",
    padx=15,
    pady=8,
    command=pop_upBearbeiten
)
bearbeitenBTN.grid(row=1, column=2)
bearbeitenBTN.config(width=20, height=2)
bearbeitenBTN.bind("<Enter>", on_enter)
bearbeitenBTN.bind("<Leave>", on_leave)


StatusBTN = tk.Button(
    BFrame,
    text="Status Ändern",
    bg=BTN_NORMAL,
    fg="white",
    activebackground=BTN_HOVER,
    relief="flat",
    padx=15,
    pady=8,
    command=status
)
StatusBTN.grid(row=1, column=3)
StatusBTN.config(width=20, height=2)
StatusBTN.bind("<Enter>", on_enter)
StatusBTN.bind("<Leave>", on_leave)

StatistikBTN = tk.Button(
    BFrame,
    text="Statistik",
    bg=BTN_NORMAL,
    fg="white",
    activebackground=BTN_HOVER,
    relief="flat",
    padx=15,
    pady=8,
    command=statistik
)
StatistikBTN.grid(row=1, column=4)
StatistikBTN.config(width=20, height=2)
StatistikBTN.bind("<Enter>", on_enter)
StatistikBTN.bind("<Leave>", on_leave)


def exportieren():
    backend.export_csv()

exportBTN = tk.Button(
    BFrame,
    text="Export",
    bg=BTN_NORMAL,
    fg="white",
    activebackground=BTN_HOVER,
    relief="flat",
    padx=15,
    pady=8,
    command=exportieren
)
exportBTN.grid(row=1, column=5)
exportBTN.config(width=20, height=2)
exportBTN.bind("<Enter>", on_enter)
exportBTN.bind("<Leave>", on_leave)



# ===== Funktion: Listbox komplett neu aufbauen =====
def listbox_update():
    #Löscht die Listbox und füllt sie mit allen Kundene (sortirt nach Datum).
    listbox.delete(0, tk.END)
    if not backend.Kunden:
        return

    for K in sorted(backend.Kunden, key=lambda k: k["Datum"]):
        listbox.insert(tk.END, f"#{int(K['Kundennummer']):04} | {K['Status']} | {K['Name']} - {K['Gerät']}")


listbox_update()


# Details des ausgewählten Kunden anzeigen
def anzeigen(event):
    Kinfo.delete("1.0", tk.END)
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]
    text = listbox.get(index)

    # Kundennummer aus dem Text holen
    kundennummer = text.split("|")[0].replace("#", "").strip()
    kundennummer = int(kundennummer)

    # richtigen Kunden finden
    kunde = next((k for k in backend.Kunden if int(k["Kundennummer"]) == kundennummer), None)

    if not kunde:
        return

    Kinfo.insert("1.0", f"""
        Kundennummer:   #{int(kunde['Kundennummer']):04}

        Name:           {kunde["Name"]}
        Gerät:          {kunde["Gerät"]}
        Problem:        {kunde["Problem"]}
        Preis:          {kunde["Preis"]}$

        Status:         {kunde["Status"]}
        Datum:          {kunde["Datum"]}
    """)

#  Details automatisch aktualisieren
def anzeigen_auto():
    index = listbox.curselection()[0]
    kunde = backend.Kunden[index]
    Kinfo.delete("1.0", tk.END)
    Kinfo.insert("1.0", f"""
            Kundennummer:   #{int(kunde['Kundennummer']):04}

            Name:           {kunde["Name"]}
            Gerät:          {kunde["Gerät"]}
            Problem:        {kunde["Problem"]}
            Preis:          {kunde["Preis"]}$

            Status:         {kunde["Status"]}
            Datum:          {kunde["Datum"]}
    """)


menu = tk.Menu(window, tearoff=0)
menu.add_command(label="Offen", command=lambda: filtern("Offen"))
menu.add_command(label="In Arbeit", command=lambda: filtern("In Arbeit"))
menu.add_command(label="Fertig", command=lambda: filtern("Fertig"))
menu.add_command(label="Alle", command=listbox_update)

# Event: Wenn in der Listbox ein Eintrag angeklickt wird, Details anzeigen
listbox.bind("<<ListboxSelect>>", anzeigen)

window.mainloop()
