import tkinter as tk
import datetime
from tkinter import filedialog
import os
root = tk.Tk()

date = datetime.datetime.now()
root.title("Happy " + date.strftime("%A")+ "!!")

menu_bar= tk.Menu(root)
text_box = tk.Text(root,height=30, padx=20, pady=20)
clock = tk.Label(text= date.strftime("%d"+"/"+"%m"+"/"+"%y"))

def save():  
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text", "*.txt"),
            ("Python", "*.py"),
        ]
    )
    if (os.path.exists(path)):
        existed_file = open(path, "w")
        existed_file.write(text_box.get("1.0",tk.END))
        existed_file.close()
    else:
        created_file = open(path, "x") # create
        created_file.close()

        existed_file = open(path, "w")
        existed_file.write(text_box.get("1.0",tk.END))
        existed_file.close()
def open_file():
    path = filedialog.askopenfilename(
        filetypes=[
            ("Text", "*.txt"),
            ("Python", "*.py"),
        ]
    )
    if path:
        with open(path, 'r') as file:
            lines = file.readlines()
        text_box.delete(1.0, tk.END)
        for line in lines:
            text_box.insert(tk.END, line)

menu_bar.add_command(label="save",command=save)
menu_bar.add_command(label="open",command=open_file)

root.config(menu=menu_bar)
text_box.pack()
clock.pack()

root.mainloop()