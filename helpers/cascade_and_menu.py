import tkinter as tk
from tkinter import filedialog, messagebox

def new_file(text_widget):
    if messagebox.askokcancel("New", "Do you want to save the current file before creating a new one?"):
        save_file(text_widget)
    text_widget.delete(1.0, tk.END)

def open_file(text_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, content)

def save_file(text_widget):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get(1.0, tk.END))
        messagebox.showinfo("Save", "File saved successfully")

# Set up the main Tkinter window
root = tk.Tk()
root.title("Text Editor")

# Create a Text widget
text_widget = tk.Text(root, wrap='word')
text_widget.pack(expand=True, fill='both')

# Create a Menu bar
menu_bar = tk.Menu(root)

# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: new_file(text_widget))
file_menu.add_command(label="Open", command=lambda: open_file(text_widget))
file_menu.add_command(label="Save", command=lambda: save_file(text_widget))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Attach the menu bar to the root window
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
