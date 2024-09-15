from tkinter import *
import tkinter as tk 
from tkinter import ttk


# main window
window = Tk()
window.title("flipkart.com")
window.geometry("500x600")
window.config(bg="#D2B48C")

#lables

searchbar=Entry()
searchbar.pack(side='left', anchor="n")

mic_image = PhotoImage(file='mic.png')

mic_button = Button(window, image=mic_image, height=40, width=40, cursor='hand2')
mic_button.place(x=400, y=2,height=40, width=40)





home_button = Button(window,text="Home", height=2, width=5, border=0, font=('areial',12,"bold"), cursor='hand2')
home_button.pack(side='left',anchor='sw',padx=15)
                 
explore_buttton = Button(window, text="explore", height=2, border=0, width=5,font=('areial',12,"bold"), cursor='hand2')
explore_buttton.pack(side='left', anchor='sw',padx=15)

account=Button(window, text="Account", height=2, width=5, border=0, font=('areial',12,"bold"), cursor='hand2')
account.pack(side='left',anchor='se',padx=15)

cart_button = Button(window, text="cart", height=2, width=5, border=0, font=('areial',12,"bold"), cursor='hand2')
cart_button.pack(side='left',anchor='se',padx=15)
                     
# footer = tk.Label(window,height=15)
# footer.pack(fill='x')
window.mainloop()
