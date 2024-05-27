import tkinter as tk
from tkinter import filedialog
def selectfolder():
    path = filedialog.askdirectory()
    print(path)    

root = tk.Tk()
b = tk.Button(root, text="click", command=selectfolder)
b.pack()

root.mainloop()
