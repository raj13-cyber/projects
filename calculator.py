# import tkinter module and Tk themed widgets(old and new)
from tkinter import *
import tkinter as tk
from tkinter import ttk


login_form = tk.Tk()
login_form.title("Login")
login_form.geometry("300x250")

fields = {}

# create user name label 
fields['username_label'] = ttk.Label(text="User Name")
fields['username'] = ttk.Entry()

# create password label 
fields['password_label'] = ttk.Label(text = "Password")
fields['password'] = ttk.Entry()

# loop
for field in fields.values():
    field.pack()

login_form.mainloop()
