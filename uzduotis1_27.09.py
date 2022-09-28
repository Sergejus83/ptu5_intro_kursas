# 1 užduotis
# Sukurti programą su grafine sąsaja, kuri:

# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"


from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = e_zodis.get()
    l_rezultatas["text"] = "Labas", ivesta, "!"
    # e_zodis.delete(0, len(ivesta)) # istrina ivesta teksta, kad netrintu po kiek vieno ivesties

l_zodis = Label(langas, text="Iveskite varda: ")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
# langas.bind("<Return>", lambda event: spausdinti()) # naudojam "ENTER" patvirtinimui
l_rezultatas = Label(langas, text="", anchor=W)

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=N)

langas.mainloop()