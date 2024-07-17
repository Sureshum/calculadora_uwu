from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="stfu greenfella", message="borrar (b) borrar todo (n)")

window = Tk()

button = Button(window, text="click", command=click)
button.pack()
window.mainloop()
