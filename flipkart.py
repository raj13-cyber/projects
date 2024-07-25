from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter.ttk import*

# create window 
window = tk.Tk()
window.title("Flipkart")
window.geometry("340x480")
window.resizable(True, True)

window.config(bg='#ffe8ca',borderwidth=5)


# icon change
img = PhotoImage(file='/home/rajendiran/projects/codes/flipkart.png')
window.iconphoto(False,img)

# label create 
search_bar = Entry()


search_bar.insert(1, "please Enter url here")
footer=ttk.Frame(window, height=30)

micimage = PhotoImage(file='mic.png')
mic_button =ttk.Button(window,image=micimage,cursor='hand2')



# pack geometry
search_bar.pack(fill='x', ipadx=40, ipady=3, pady=20)
footer.pack(side=BOTTOM, fill='both', ipady=10)
mic_button.pack(side=LEFT,ipadx=10,ipady=10)







window.mainloop()
