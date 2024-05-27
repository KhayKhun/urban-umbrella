import tkinter as tk
from tkinter import filedialog
def selectfolder():
    path = filedialog.askdirectory() # folder choose

    path = filedialog.askopenfilename() # open a file
   
    path = filedialog.asksaveasfilename( # save a file
        filetypes=[("Text files","*.txt"),("All files","*.*")] # accept file types
    )

    print(path)      

root = tk.Tk()
b = tk.Button(root, text="click", command=selectfolder)
b.pack()

root.mainloop()