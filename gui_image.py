from tkinter import *
from PIL import ImageTk, Image

langas = Tk()

picture = ImageTk.PhotoImage(Image.open("pictures/picture_kalendorius.png"))
panel = Label(langas, image=picture)
panel.pack(side=BOTTOM, fill=BOTH, expand=YES)
langas.mainloop()

