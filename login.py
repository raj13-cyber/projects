# import tkinter module and Tk themed widgets(old and new)
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox  import showinfo
from tkinter.ttk import*


login_form = tk.Tk()
login_form.title("Login")
login_form.geometry("300x250")


fields = {}

#store email and password 
email= tk.StringVar()
password=tk.StringVar()


def login_clicked():
    msg= f'successful {email.get()}  {password.get()}'

    showinfo(
        title = "Login Info",
        message = msg
    )


# create user name label 
fields['username_label'] = ttk.Label(text="User Name:")
fields['username'] = ttk.Entry()

# create password label 
fields['password_label'] = ttk.Label(text = "Password:") 
fields['password'] = ttk.Entry()

# loop
for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

button=ttk.Button(text="Login", command=login_clicked).pack(anchor=tk.W,padx=10, pady=5)



login_form.mainloop()

