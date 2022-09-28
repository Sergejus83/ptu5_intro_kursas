# Label – užrašas (kortelė)
# Button – mygtukas
# Entry – laukelis
# Menu – meniu
# Frame – rėmelis
# Checkbutton – varnelė
# Listbox – sąrašas
# Scrollbar – sąrašo slinkimo juosta

#Grafinių objektų formavimas lentelėje (su grid funkcija):

from tkinter import *

langas = Tk()

l_vardas = Label(langas, text="Vardas")
e_vardas = Entry(langas)
l_pavarde = Label(langas, text="Pavardė")
e_pavarde = Entry(langas)

# varnele = Checkbutton(langas, text="Pažymėk varnelę")

l_vardas.grid(row=0, column=0, sticky=E)
e_vardas.grid(row=0, column=1)
l_pavarde.grid(row=1, column=0, sticky=E)
e_pavarde.grid(row=1, column=1)
# varnele.grid(row=2, columnspan=2)

langas.mainloop()