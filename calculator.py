# import tkinter module and Tk themed widgets(old and new)
from tkinter import *
import tkinter as tk
from tkinter import ttk



calculator = tk.Tk()

calculator.title()
calculator.geometry("500x500+100+100")


def button_clicked():
    print('raj has clicked the button')

def select(option):
    print(option)


ttk.Button(calculator, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(calculator, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(calculator, text='Scissors', command=lambda: select('Scissors')).pack()


mybutton = Button(calculator, text= "1", fg= 'white', bg= 'green', command=button_clicked)
mybutton.pack()


Entry_box= Entry(calculator)
Entry_box.pack()

Entry_box.insert(0,"enter the proper value")

Frame = ttk.Frame(calculator, padding=10)
Frame.pack()

ttk.Label(Frame, text="Hello world").grid(row=0, column=0)
ttk.Button(Frame, text="quit", command=calculator.destroy).grid(column=1,row=1)

label_1 = Label(calculator,text="python framework").pack()
calculator.attributes('-topmost',1)                                        

image = PhotoImage(file='/home/rajendiran/codes/logo.png')
calculator.iconphoto(False,image)

ttk.Label(calculator, text= 'hi programmer').pack()


label = ttk.Label(calculator)
label['text'] = 'linux os'
label.pack()



calculator.mainloop()
