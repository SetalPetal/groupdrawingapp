import tkinter as tk 
from tkinter import Tk, Menu, Frame, Button, Scale, Canvas, Label, StringVar, Entry, Toplevel, messagebox, filedialog
from tkinter.colorchooser import askcolor

class Window:
    def __init__(self, root):
        self.root = root 
        self.root.title("Drawing Application")
        self.root.geometry("1200x900")

        #Tool bar
        self.toolbar = Frame(self.root, bd=1)

        #Buttons 
        button = Button(self.toolbar, text=f"Save")
        button.pack(side=tk.LEFT, padx=2, pady=2)

        self.toolbar.pack(side=tk.TOP, fill=tk.X)

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
