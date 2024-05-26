# gui - graphical user interface
# cli - command line interface
import tkinter as tk

root = tk.Tk()
# decalre section
title1 = tk.Label(root, text="Smart Calculator", padx=10,pady=40) # decalre
input1 = tk.Entry(root)
input2 = tk.Entry(root)
answer = tk.Label(root, text="Your answer will be displayed here.")

def clickLikB1():
    answer.config(text=str(int(input1.get())+int(input2.get())))
def clickLikB2():
    answer.configure(text=str(int(input1.get())-int(input2.get())))
def clickLikB3():
    answer.configure(text=str(int(input1.get())*int(input2.get())))
def clickLikB4():
    answer.configure(text=(str(int(input1.get())//int(input2.get()))+" "+"modulus is" + " "+str(int(input1.get())%int(input2.get()))))
    

btn1 = tk.Button(root, text="Add", command=clickLikB1)
btn2 = tk.Button(root, text="Substitude", command=clickLikB2)
btn3 = tk.Button(root, text="Multiply", command=clickLikB3)
btn4 = tk.Button(root, text="Divide", command=clickLikB4)
# pack section
title1.pack() # use
input1.pack()
input2.pack()
answer.pack()


btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()


root.mainloop()