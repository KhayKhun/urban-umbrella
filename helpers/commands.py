import tkinter as tk
from tkinter import messagebox

def save(event):
    print(" ctrl s")

def paste(event):
    print(" ctrl v")

root = tk.Tk()
root.title("Keyboard Shortcuts Example")

root.bind('<Control-s>', save)
root.bind('<Control-v>', paste)

root.mainloop()
