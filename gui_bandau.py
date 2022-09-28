# from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y ,YES, TOP, RIGHT, W

from tkinter import *
langas = Tk()
langas.geometry("400x200")
# freimai
virsus = Frame(langas)
apacia = Frame(langas)

mygtukas1 = Button(virsus, text="Spausdinti", anchor=W)
mygtukas2 = Button(virsus, text="Apacia")
mygtukas3 = Button(virsus, text="Galas")

virsus.pack(side=TOP)
apacia.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=RIGHT)

langas.mainloop()