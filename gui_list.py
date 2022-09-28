# Label – užrašas (kortelė)
# Button – mygtukas
# Entry – laukelis
# Menu – meniu
# Frame – rėmelis
# Checkbutton – varnelė
# Listbox – sąrašas
# Scrollbar – sąrašo slinkimo juosta

# Kaip sukurti atvaizduojamą sąrašą:

from tkinter import *

langas = Tk()

def spausdinti():
    try:
        pasirinkta = sarasas[dezute.curselection()[0]]
    except IndexError:
        label_pasirinkta["text"] = "Nieko!"
    else:
        label_pasirinkta["text"] = pasirinkta

# meta klaida
    # if dezute.curselection()[0] > -1:
    #     pasirinkta = sarasas[dezute.curselection()[0]]
    #     label_pasirinkta["text"] = pasirinkta
    # else:
    #     label_pasirinkta["text"] = "nieko"

dezute_scroll = Scrollbar(langas)
# listbox'ui priskiriam scrollbar'a
dezute = Listbox(langas, yscrollcommand=dezute_scroll.set, width=20) # width - saraso plotis per simboliu vnt
# scrollbaro pozicija atsinaujis, prastumus listboxa kitais budais (ne nu scrollbaru)
dezute_scroll.config(command=dezute.yview)
sarasas = range(1983, 2023)
dezute.insert(END, *sarasas)
# dezute.insert(0, *sarasas[:10]) # nuo/iki tikros vietos
# dezute.insert(0, *sarasas[10:])# nuo/iki tikros vietos
label_pasirinkta = Label(langas, text="Pasirinkite!")
button_pasirinkti = Button(langas, text="rinkite!", command = spausdinti)
# pack and go
dezute.pack(side=LEFT, fill=Y)
dezute_scroll.pack(side=RIGHT,fill=Y)
button_pasirinkti.pack()
label_pasirinkta.pack()

langas.mainloop()