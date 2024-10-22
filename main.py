from tkinter import Tk, Frame, Button, Scale, Canvas, Label, StringVar, Entry, Toplevel, messagebox, filedialog
from tkinter.colorchooser import askcolor

class Window:
    def __init__(self, root):
        self.root = root 
        self.root.title("Drawing Application")
        self.root.geometry("1200x900")

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
