import tkinter as tk
import datetime
from tkinter import filedialog
import os
root = tk.Tk()

t = tk.Text(root,height=30, padx=20, pady=20)
def save():
    
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text", "*.txt"),
            ("Python", "*.py"),
        ]
    )
    print(path)
    if (os.path.exists(path)):
        existed_file = open(path, "w")
        existed_file.write(t.get("1.0",tk.END))
        existed_file.close()
    else:
        created_file = open(path, "x") # create
        created_file.close()

        existed_file = open(path, "w")
        existed_file.write(t.get("1.0",tk.END))
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
        t.delete(1.0, tk.END)
        for line in lines:
            t.insert(tk.END, line)
date = datetime.datetime.now()
title = tk.Label(text="Happy"+" " +date.strftime("%A")+ "!!")
b = tk.Button(root, text="save", command=save)
t1 = tk.Label(text= date.strftime("%d"+"/"+"%m"+"/"+"%y"))
b1 = tk.Button(root, text="open", command=open_file)


title.pack()
b.pack()
b1.pack()
t.pack()

t1.pack()

root.mainloop()