# Label – užrašas (kortelė)
# Button – mygtukas
# Entry – laukelis
# Menu – meniu
# Frame – rėmelis
# Checkbutton – varnelė
# Listbox – sąrašas
# Scrollbar – sąrašo slinkimo juosta

# Kaip per grafinę sąsają nuskaityti ir atspausdinti duomenis

from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = e_zodis.get()
    l_rezultatas["text"] = ivesta
    e_zodis.delete(0, len(ivesta)) # istrina ivesta teksta, kad netrintu po kiek vieno ivesties

l_zodis = Label(langas, text="Įrašykite žodį: ")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
langas.bind("<Return>", lambda event: spausdinti()) # naudojam "ENTER" patvirtinimui
l_rezultatas = Label(langas, text="", bd=5, relief=SUNKEN, anchor=W)

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=W+E)

langas.mainloop()