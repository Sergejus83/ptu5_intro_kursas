# Label – užrašas (kortelė)
# Button – mygtukas
# Entry – laukelis
# Menu – meniu
# Frame – rėmelis
# Checkbutton – varnelė
# Listbox – sąrašas
# Scrollbar – sąrašo slinkimo juosta

#Kaip sukurti grafinę vartotojo sąsają (su Tkinter)

from tkinter import Tk, Label, Button

#sukuriam lango objekta pagal Tk() klase
langas = Tk()
# nustatom lango dydi
langas.geometry("500x300")
# i langa sukuriam 'uzrasas' objekta pagal label klase, su tekstu
uzrasas = Label(langas, text="Sveiki, Studentai")
uzrasas2 = Label(langas, text="Sveias, antradieni!")
#s supakuojam zrasas
uzrasas.pack()
uzrasas2.pack(side='Button')

# paleidziam lango programa
langas.mainloop()
