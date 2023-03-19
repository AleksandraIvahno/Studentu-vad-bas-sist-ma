import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

mywindow = tk.Tk()
mywindow.title("Vadība")

mywindow.geometry("660x350")
mywindow.resizable(0, 0)

connection = sqlite3.connect('info.db')

TABLA_VĀRDS = "student_tabla"
STUDENT_ID = "student_id"
STUDENT_VĀRDS = "student_vārds"
STUDENT_SKOLA = "student_skola"
STUDENT_ADRESE = "student_adrese"
STUDENT_TĀLRUNIS = "student_tālrinis"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLA_VĀRDS + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_VĀRDS + " TEXT, " + STUDENT_SKOLA + " TEXT, " +
                   STUDENT_ADRESE + " TEXT, " + STUDENT_TĀLRUNIS + " INTEGER);")

mainLabel = tk.Label(mywindow, text="STUDENTU VADĪBAS SISTĒMA", fg="#555599", width=30)
mainLabel.config(font=("Franklin Gothic Medium", 30))
mainLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))

vārdsLabel = tk.Label(mywindow, text="IEVADIET SAVU VĀRDU", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(50, 0), pady=(30, 0))

skolaLabel = tk.Label(mywindow, text="IESTĀJIETIES SAVĀ SKOLĀ", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(50, 0))

adreseLabel = tk.Label(mywindow, text="IEVADIET SAVU ADRESI", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=3, column=0, padx=(50, 0))

tālrinisLabel = tk.Label(mywindow, text="IEVADIET SAVU TELEFONA NR.", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=4, column=0, padx=(50, 0))

vārdsEntry = tk.Entry(mywindow, width=30)
skolaEntry = tk.Entry(mywindow, width=30)
adreseEntry = tk.Entry(mywindow, width=30)
tālrinisEntry = tk.Entry(mywindow, width=30)

vārdsEntry.grid(row=1, column=1, padx=(0, 40), pady=(30, 10))
skolaEntry.grid(row=2, column=1, padx=(0, 40), pady=10)
adreseEntry.grid(row=3, column=1, padx=(0, 40), pady=10)
tālrinisEntry.grid(row=4, column=1, padx=(0, 40), pady=10)


def takeNameInput():
    username = vārdsEntry.get()
    vārdsEntry.delete(0, tk.END)
    skolaVārds = skolaEntry.get()
    skolaEntry.delete(0, tk.END)
    adrese = adreseEntry.get()
    adreseEntry.delete(0, tk.END)
    tālrinis = int(tālrinisEntry.get())
    tālrinisEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLA_VĀRDS + " ( " + STUDENT_VĀRDS + ", " +
                       STUDENT_SKOLA + ", " + STUDENT_ADRESE + ", " +
                       STUDENT_TĀLRUNIS + " ) VALUES ( '"
                       + username + "', '" + skolaVārds + "', '" +
                       adrese + "', " + str(tālrinis) + " ); ")
    connection.commit()
    messagebox.showinfo("Panākumi", "Dati ir veiksmīgi saglabāti.")


def destroyRootWindow():
    mywindow.destroy()
    secondWindow = tk.Tk()

    # secondWindow.geometry("660x300")
    # secondWindow.resizable(0, 0)

    secondWindow.title("PAŠREIZĒJIE REKSTI")

    appLabel = tk.Label(secondWindow, text="Studentu vadības sistēma      ",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("viens", "divi", "trīs", "četri")

    tree.heading("viens", text="Studenta vārds")
    tree.heading("divi", text="Skolas nosaukums")
    tree.heading("trīs", text="Adrese")
    tree.heading("četri", text="Telefona numurs")

    cursor = connection.execute("SELECT * FROM " + TABLA_VĀRDS + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


button = tk.Button(mywindow, text="IEVIETOT", activebackground="gray", width=20, command=lambda: takeNameInput())
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(mywindow, text="RĀDĪT", activebackground="gray", width=20,
                          command=lambda: destroyRootWindow())
displayButton.grid(row=5, padx=(10, 100), column=1)

mywindow.mainloop()