# import tkinter module and Tk themed widgets(old and new)
from tkinter import *
import tkinter as tk
from tkinter import ttk

# basic window of calculator
calculator = tk.Tk()


# calculator name and size
calculator.title("Raj calculator") # title of the calculator
calculator.geometry("550x550+20+20")

calculator.attributes('-topmost', 1)

# changing the icon
img = PhotoImage(file='/home/rajendiran/codes/logo.png')
calculator.iconphoto(False,img)

# creating label
label_1 = Label(calculator, text = 'please click', fg="white", bg= "green").pack()

ttk.Label(calculator, text = 'raj').pack()

def button_clicked():
    print('rajendiran')

button = ttk.Button(calculator, text='more fun', command=button_clicked)
button.pack()








def select(option):
    print(option)


ttk.Button(calculator, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(calculator, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(calculator, text='Scissors', command=lambda: select('Scissors')).pack()



calculator.mainloop()


