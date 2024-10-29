import tkinter as tk

class Eraser:
    def __init__(self, canvas):
        self.canvas = canvas
        self.old_x = None
        self.old_y = None
        self.eraser_size = 10

        # Mouse bindings
        self.canvas.bind('<B1-Motion>', self.erase)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def set_eraser_size(self, size):
        self.eraser_size = size

    def erase(self, event):
        if self.old_x and self.old_y:
            x1, y1 = (event.x - self.eraser_size), (event.y - self.eraser_size)
            x2, y2 = (event.x + self.eraser_size), (event.y + self.eraser_size)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='white')
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None
