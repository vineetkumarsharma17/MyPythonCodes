from tkinter import *
from PIL import Image,ImageTk
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registrarion form")
        self.root.geometry("1080x720+50+0")
        # bg image========
        self.bg=ImageTk.PhotoImage(file="images/bg.jpg")



root=Tk()
obj=register(root)
root.mainloop()

        