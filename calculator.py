# import tkinter module and Tk themed widgets(old and new)
from tkinter import *
import tkinter as tk
from tkinter import ttk



calculator = tk.Tk()
calculator.title()
calculator.geometry("500x500+100+100")


mybutton = Button(calculator, text= "1", fg= 'white', bg= 'green')
mybutton.pack()


Entry_box= Entry(calculator)
Entry_box.pack()

Entry_box.insert(0,"enter the proper value")

Frame = ttk.Frame(calculator, padding=10)
Frame.pack()

ttk.Label(Frame, text="Hello world").grid(row=0, column=0)
ttk.Button(Frame, text="quit", command=calculator.destroy).grid(column=1,row=1)



calculator.mainloop()
