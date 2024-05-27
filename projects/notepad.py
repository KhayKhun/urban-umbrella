import tkinter as tk
import datetime

root = tk.Tk()

t = tk.Text(root,height=30, padx=20, pady=20)
date = datetime.datetime.now()
title = tk.Label(text="Happy"+" " +date.strftime("%A")+ "!!")

t1 = tk.Label(text= date.strftime("%d"+"/"+"%m"+"/"+"%y"))

















title.pack()
t.pack()

t1.pack()

root.mainloop()