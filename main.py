import tkinter as tk 
from tkinter import Tk, Menu, Frame, Button, Scale, Canvas, Label, StringVar, Entry, Toplevel, messagebox, filedialog
from tkinter.colorchooser import askcolor
from tools.shapes_tool import ShapesTool

class Window:
    def __init__(self, root):
        self.root = root 
        self.root.title("MEZ. Canvas")
        self.root.geometry("1200x900")

        # Tool bar
        self.toolbar = Frame(self.root, bd=1, relief=tk.RAISED, bg='Grey')
        self.toolbar.place(x=0, y=0, width=1200, height=150)

        # Buttons
        save_button = Button(self.toolbar, text="Save", width=15, height=3)
        save_button.grid(row=0, column=0, rowspan=2, sticky="ew", padx=5)

        load_button = Button(self.toolbar, text="Load", width=15, height=3)
        load_button.grid(row=2, column=0, rowspan=2, sticky="ew", padx=5)

        draw_button = Button(self.toolbar, text="Draw")
        draw_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        eraser_button = Button(self.toolbar, text="Eraser")
        eraser_button.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

        color_button = Button(self.toolbar, text="Color")
        color_button.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

        brushes_button = Button(self.toolbar, text="Brushes")
        brushes_button.grid(row=0, column=4, sticky="ew", padx=5, pady=5)

        shape_button = Button(self.toolbar, text="Shapes")
        shape_button.grid(row=0, column=5, sticky="ew", padx=5, pady=5)

        undo_button = Button(self.toolbar, text="Undo")
        undo_button.grid(row=0, column=6, sticky="ew", padx=5, pady=5)

        redo_button = Button(self.toolbar, text="Redo")
        redo_button.grid(row=0, column=7, sticky="ew", padx=5, pady=5)

        # Configure grid columns to expand evenly
        for i in range(8):
            self.toolbar.grid_columnconfigure(i, weight=1)

        # Canvas
        self.canvas = Canvas(self.root, bg='white')
        self.canvas.place(x=0, y=150, width=1200, height=750)

        #shapes tool class initialzed
        self.shapes_tool = ShapesTool(self.canvas)

        #shape menu 
        self.shapes_menu = Menu(self.root, tearoff=0)
        self.shapes_menu.add_command(label="Rectangle", command=self.use_rectangle)
        self.shapes_menu.add_command(label="Oval", command=self.use_oval)
        self.shapes_menu.add_command(label="Line", command=self.use_line)

        def show_shapes_menu(self, event=None):
            self.shapes_menu.post(self.root.winfo_pointerx(), self.root.winfo_pointery())

        def rectangle(self):
            self.shapes_tool.rectangle()

        def oval(self):
            self.shapes_tool.oval()

        def line(self):
            self.shapes_tool.line()

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
