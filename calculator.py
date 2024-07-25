import tkinter as tk

root = tk.Tk()
root.title("Microphone Symbol")

# Create a label with the microphone symbol
microphone_label = tk.Label(root, text="\U0001F3A4", font=("Arial", 50))
microphone_label.pack()

root.mainloop()

