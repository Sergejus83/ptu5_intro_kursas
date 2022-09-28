# Label – užrašas (kortelė)
# Button – mygtukas
# Entry – laukelis
# Menu – meniu
# Frame – rėmelis
# Checkbutton – varnelė
# Listbox – sąrašas
# Scrollbar – sąrašo slinkimo juosta

# Grafinių objektų formavimas rėmeliuose (su pack funkcija):

from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y ,YES
langas = Tk()
langas.geometry("400x200")
# freimai
virsutinis = Frame(langas)
apatinis = Frame(langas)
# migtukai
mygtukas1 = Button(virsutinis, text="Pirmas")
mygtukas2 = Button(virsutinis, text="Antras")
mygtukas3 = Button(virsutinis, text="Trecias")
mygtukas4 = Button(apatinis, text="hello > Julija")
#pakuojam
virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM, fill=Y)
# paleidziam
langas.mainloop()