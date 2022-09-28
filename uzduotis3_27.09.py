# 3 užduotis
# Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:

# Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
# Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
# Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
# Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys

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

def atkurti():
   l_rezultatas["text"] =paskutinis_rez.get()

def iseiti():
    langas.destroy()
    
def labas(): 
    ivesta = e_zodis.get()
    l_rezultatas["text"] = f"Labas, {ivesta} !"
    paskutinis_rez.set(l_rezultatas["text"])

    
l_zodis = Label(langas, text="Iveskite varda: ")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=labas)
langas.bind("<Return>", lambda event: labas()) # naudojam "ENTER" patvirtinimui

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)



l_rezultatas = Label(langas, text="", anchor=W)

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=N)

langas.mainloop()

