# Label – užrašas (kortelė)
# Button – mygtukas
# Entry – laukelis
# Menu – meniu
# Frame – rėmelis
# Checkbutton – varnelė
# Listbox – sąrašas
# Scrollbar – sąrašo slinkimo juosta

# Kaip esant skirtingiems vartotojo veiksmams, paleisti skirtingas funkcijas:

from tkinter import *
langas = Tk()

def spausdinti_su_enter(): # jei nera 'event' reikia aprasyti mygtuke. zr zemiau
    print("spausdina paspausdus ENTER...")

def spausdinti_su_kaire(event):
    print("spausdina paspausdus kaire")

def spausdinti_su_desine(event):
    print("spausdina paspausdus desine")

mygtukas = Button(langas, text="Spausdinti") #, command=spausdinti)
mygtukas.bind("<Button-1>", spausdinti_su_kaire)
mygtukas.bind("<Button-3>", spausdinti_su_desine)
langas.bind("<Return>", lambda event: spausdinti_su_enter()) # jei nera 'event' galima aprasyti cia
mygtukas.pack()
langas.mainloop()



# Paspaustas kairys pelės mygtukas!
# Paspaustas dešinys pelės mygtukas!
# Paspaustas ENTER!