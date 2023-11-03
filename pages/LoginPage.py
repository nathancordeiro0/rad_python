import tkinter as tk
from tkinter import messagebox

def verify_fields():
    if entry_a.get() == "":
        messagebox.showinfo("Campo obrigatório", "Campos não podem estar em branco")
        

root = tk.Tk()
width = 600
height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))

frame = tk.Frame(master=root)

label_a = tk.Label(master=frame, text="Usuário")
label_a.pack()
entry_a = tk.Entry(master=frame, width=40)
entry_a.pack(pady=10)

label_b = tk.Label(master=frame, text="Senha")
label_b.pack()
entry_b = tk.Entry(master=frame, width=40)
entry_b.pack()

button = tk.Button(master=frame, text="Login", width=20, bg="blue", fg="white", relief=tk.FLAT, command=verify_fields)
button.pack(pady=10)

frame.pack()

entry_b.bind("<FocusIn>", entry_b.config(show="*"))

root.mainloop()
