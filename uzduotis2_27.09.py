# Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"

from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = e_zodis.get()
    l_rezultatas["text"] = "Labas", ivesta, "!"

l_zodis = Label(langas, text="Iveskite varda: ")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
langas.bind("<Return>", lambda event: spausdinti()) # naudojam "ENTER" patvirtinimui
l_rezultatas = Label(langas, text="", anchor=W)

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=N)

langas.mainloop()