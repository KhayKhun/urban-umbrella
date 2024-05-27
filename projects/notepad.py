import tkinter as tk
import datetime

root = tk.Tk()

t = tk.Text(root,height=30, padx=20, pady=20)
def save():
    print(t.get())
date = datetime.datetime.now()
title = tk.Label(text="Happy"+" " +date.strftime("%A")+ "!!")
b = tk.Button(root, text="save", command=save)
t1 = tk.Label(text= date.strftime("%d"+"/"+"%m"+"/"+"%y"))



title.pack()
b.pack()
t.pack()

t1.pack()

root.mainloop()