import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("My calculator")

bg = tk.PhotoImage(file="cat.jpg")

canvas = tk.Canvas(root, width=400,height=400)
canvas.pack(fill="both",expand=True)

canvas.create_image(0,0, bg, "nw")

f = tk.Frame(root)

def show_info(): messagebox.showinfo("Information", "You're short")
def show_warn(): messagebox.showwarning("Warning", "You're short")
def show_err(): messagebox.showerror("Error", "You're short")
def show_q(): messagebox.askquestion("Question?", "You're short?")

info = tk.Button(f, text = "Info", command=show_info)
warn = tk.Button(f, text = "Warn", command=show_warn)
err = tk.Button(f, text = "Err", command=show_err)
ques = tk.Button(f, text = "Q", command=show_q)

info.grid(row=0, column=0)
warn.grid(row=1, column=0)
err.grid(row=0, column=1)
ques.grid(row=1, column=1)

f.pack()
root.mainloop()