# 5 užduotis (papildoma)
# Perdaryti bet kurią ankstesnėse pamokose sukurtą arba savo programą, kurioje vartotojas turėjo įvesti duomenis,
#  į programą su grafine sąsaja. Pvz., tą, kuri atrenka keliamuosius metus, skaičiuoja laiką nuo praeitos datos, 
#  pateikia informaciją apie įvestą eilutę ar pan.

from datetime import datetime, date, timedelta

from tkinter import *
langas = Tk()
paskutinis_rez = StringVar()
today = date.today()
print(today)
e_zodis = 1983
e_zodis = timedelta
print(e_zodis)

def iseiti():
    langas.destroy()
    
def skaiciuoti_metus(): 
    ivesta = int(e_zodis.get())
    l_rezultatas["text"] = today - ivesta
    paskutinis_rez.set(l_rezultatas["text"])
    l_statusas["text"] = "Sukurta"
    
l_zodis = Label(langas, text = "gimimo metus: ")
e_zodis = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=skaiciuoti_metus)
langas.bind("<Return>", lambda event: skaiciuoti_metus()) # naudojam "ENTER" patvirtinimui
langas.bind("<Escape>", lambda event: iseiti())

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Išvalyti", command=isvalyti)
# submeniu.add_command(label="Atkurti", command=atkurti)
# submeniu.add_separator()
# submeniu.add_command(label="Išeiti", command=iseiti)

l_rezultatas = Label(langas, text="", anchor=W)
l_statusas = Label(langas, text="", anchor=N) 

l_zodis.grid(row=0, column=0)
e_zodis.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
l_rezultatas.grid(row=1, columnspan=3, sticky=N)
l_statusas.grid(row=2, columnspan=3, sticky=N)

langas.mainloop()

