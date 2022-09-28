# Label – užrašas (kortelė)
# Button – mygtukas
# Entry – laukelis
# Menu – meniu
# Frame – rėmelis
# Checkbutton – varnelė
# Listbox – sąrašas
# Scrollbar – sąrašo slinkimo juosta

#Kaip sukurti meniu:

from tkinter import *
import webbrowser

langas = Tk()
langas.geometry("300x100")

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
submeniu2 = Menu(meniu, tearoff = 0)
submeniu3 = Menu(meniu, tearoff = 0)

def pirmas():
    label_pasirinkta["text"] = "Pirmas!"

def antras():
    label_pasirinkta["text"] = "Antras"

def trecias():
    label_pasirinkta["text"] = "Trecias"

def tell_a_joke():
    label_pasirinkta["text"] = "not funny"

def fart():
    label_pasirinkta["text"] = "pirst..."

def callback(url):
    webbrowser.open_new(url)

def lounch_url(event):
    url = entry_url.get()
    callback(url)
    label_pasirinkta["text"] = f"paleidom brauzeri su {url}"


meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Pirmas", command=pirmas)
submeniu.add_command(label="Antras", command=antras)
submeniu.add_separator()
submeniu.add_command(label="Trecias!", command=trecias)

meniu.add_cascade(label='fun', menu=submeniu2)
submeniu2.add_command(label="tell a joke", command=tell_a_joke)
submeniu2.add_command(label="fart!", command=fart)

meniu.add_cascade(label="settings", menu=submeniu3)
submeniu3.add_radiobutton(label="setting-1")
submeniu3.add_radiobutton(label="setting-2")

lable_iveskite_adresa = Label(langas, text="Enter URL: ")
entry_url = Entry(langas)
langas.bind("<Return>", lounch_url)

label_pasirinkta = Label(langas, text="kolkas nieko", bd=10, relief=SUNKEN, anchor=N) # bd - border/igilinimas ,  relief - idubimas, w-west  i kaire, N-north
label_pasirinkta.pack(side=BOTTOM, fill=X)

lable_iveskite_adresa.pack(side=TOP)
entry_url.pack(side=TOP)

langas.mainloop()


