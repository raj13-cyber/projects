from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter.ttk import*

# create window 
window = tk.Tk()
window.title("Flipkart")
window.geometry("340x480")
window.resizable(False, False)





# icon change
img = PhotoImage(file='/home/rajendiran/projects/codes/flipkart.png')
window.iconphoto(False,img)

# label create 
search_bar = Entry().pack(ipadx=40, ipady=3, pady=20)








window.mainloop()
