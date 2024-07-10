from tkinter import*
import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox  import showinfo

# Creating window
login = tk.Tk()
login.geometry("350x200")
login.resizable(False, False)
login.title("sigin In")

# Store email id and password
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    msg = f'you Entered email {email.get()} and Password {password.get()}'

    showinfo(
        title = "information",
        message = msg
    )
#signin frame
signin = ttk.Frame(login)
signin.pack(padx=10, pady=10, fill="x",expand=True)


# email

email_label = ttk.Label( signin, text= "Email Address:")
email_label.pack(fill="x", expand= True)

email_entry = ttk.Entry( signin, textvariable = email)
email_entry.pack(fill='x', expand=True)

email_entry.focus()

#password
password_label = ttk.Label(signin, text = "password:")
password_label.pack(fill='x', expand=TRUE)

password_Entry = ttk.Entry(signin, textvariable=password,)
password_Entry.pack(fill="x", expand=True)

# login button

login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', pady=15)




login.mainloop()
