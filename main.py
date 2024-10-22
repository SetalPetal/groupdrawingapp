import tkinter as tk 
from tkinter import Tk, Menu, Frame, Button, Scale, Canvas, Label, StringVar, Entry, Toplevel, messagebox, filedialog
from tkinter.colorchooser import askcolor

class Window:
    def __init__(self, root):
        self.root = root 
        self.root.title("Drawing Application")
        self.root.geometry("1200x900")

        #Tool bar
        self.toolbar = Frame(self.root, bd=1, relief=tk.RAISED, bg='Grey')

        self.toolbar.place(x=0, y=0, width=1200, height=150)

        #Buttons 
        save_button = Button(self.toolbar, text=f"Save")
        save_button.place(x=0, y=0, width=100, height=75)

        load_button = Button(self.toolbar, text=f"Load")
        load_button.place(x=0, y=75, width=100, height=75)

        draw_button = Button(self.toolbar, text=f"Draw")
        draw_button.pack(side=tk.LEFT, padx=2, pady=2)

        eraser_button = Button(self.toolbar, text=f"Eraser")
        eraser_button.pack(side=tk.LEFT, padx=2, pady=2)

        color_button = Button(self.toolbar, text=f"Color")
        color_button.pack(side=tk.LEFT, padx=2, pady=2)

        brushes_button = Button(self.toolbar, text=f"Brushes")
        brushes_button.pack(side=tk.LEFT, padx=2, pady=2)

        shape_button = Button(self.toolbar, text=f"Shapes")
        shape_button.pack(side=tk.LEFT, padx=2, pady=2)

        undo_button = Button(self.toolbar, text=f"Undo")
        undo_button.pack(side=tk.LEFT, padx=2, pady=2)

        redo_button = Button(self.toolbar, text=f"redo")
        redo_button.pack(side=tk.LEFT, padx=2, pady=2)

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
