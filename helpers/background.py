import tkinter as tk

root = tk.Tk()
root.title("Tkinter App with Background Image")

i = tk.PhotoImage(file="paper.png")

l = tk.Label(image=i)
l.place(x=0,y=0)
root.mainloop()
