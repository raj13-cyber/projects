from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter.ttk import*




# create window 
window = tk.Tk()
window.title("Flipkart")
window.geometry("340x480")
window.resizable(True,True)

window.config(bg='#ffe8ca',borderwidth=5)


# icon change
img = PhotoImage(file='/home/rajendiran/projects/codes/flipkart.png')
window.iconphoto(False,img)

# label create 
search_bar = Entry()
search_bar.insert(1, "please Enter url here")
footer=ttk.Frame(window, height=30)

# images
mic_image = PhotoImage(file='mic.png')
camera_image = PhotoImage(file='camera.png')
home_image = PhotoImage(file='account.png')
                                      
                    
# #Buttons
mic_button = tk.Button(window, width=100, height=100, image=mic_image, cursor='hand2')
camera_button = tk.Button(window, width=100, height=100, image=camera_image,  cursor='hand2')
home_button = tk.Button(window,width=100, height=100, image=home_image, cursor='hand2')

# pack geometry
search_bar.pack(fill='x', ipadx=40, ipady=3, pady=20)
footer.pack(side=BOTTOM, fill='both', ipady=10)

mic_button.pack(ipadx=200, ipady=200)
camera_button.pack(ipadx=200,ipady=200)
home_button.pack(ipadx=2,ipady=200)







window.mainloop()
