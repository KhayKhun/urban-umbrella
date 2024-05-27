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
            ("Txt file tway pr", "*.txt"),
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

date = datetime.datetime.now()
title = tk.Label(text="Happy"+" " +date.strftime("%A")+ "!!")
b = tk.Button(root, text="save", command=save)
t1 = tk.Label(text= date.strftime("%d"+"/"+"%m"+"/"+"%y"))



title.pack()
b.pack()
t.pack()

t1.pack()

root.mainloop()