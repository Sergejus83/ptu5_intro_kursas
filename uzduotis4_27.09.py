# Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:

# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą

from tkinter import *
langas = Tk()
paskutinis_rez = StringVar()

meniu = Menu(langas)
langas.config(menu=meniu) #
submeniu = Menu(meniu, tearoff = 0)
submeniu2 = Menu(meniu, tearoff = 0)
submeniu3 = Menu(meniu, tearoff = 0)

def isvalyti():
   l_rezultatas["text"] = ""
   l_statusas["text"] = "Išvalyta"

def atkurti():
   l_rezultatas["text"] =paskutinis_rez.get()
   l_statusas["text"] = "Atkurta"

def iseiti():
    langas.destroy()
    
def labas(): 
    ivesta = e_zodis.get()
    l_rezultatas["text"] = f"Labas, {ivesta} !"
    paskutinis_rez.set(l_rezultatas["text"])
    l_statusas["text"] = "Sukurta"

    
l_zodis = Label(langas, text="iveskite varda: ")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=labas)
langas.bind("<Return>", lambda event: labas()) # naudojam "ENTER" patvirtinimui
langas.bind("<Escape>", lambda event: iseiti())

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

l_rezultatas = Label(langas, text="", anchor=W)
l_statusas = Label(langas, text="", anchor=N) 

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=N)
l_statusas.grid(row=2, columnspan=3, sticky=N)

langas.mainloop()

