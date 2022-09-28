import tkinter as tk

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.b_naujas_langas = tk.Button(self.master, text = '\U0001F680 Naujas langas', width = 40, command = self.new_window)  # siimbolius - U+8 simboliai
        self.b_naujas_langas.pack()

    def new_window(self):
        self.vidinis = tk.Toplevel(self.master)
        self.app = Vidinis(self.vidinis)

class Vidinis:
    def __init__(self, master):
        self.master = master
        self.b_uzdaryti = tk.Button(self.master, text = '\u274C Uzdaryti', width = 25, command = self.close_window) # siimbolius - u+4 simboliai
        self.b_uzdaryti.pack()

    def close_window(self):
        self.master.destroy()

langas = tk.Tk()
programa = Pagrindinis(langas)
langas.mainloop()
