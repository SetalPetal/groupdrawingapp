import tkinter as tk 

class Eraser:
    def __init__(self, canvas):
        self.canvas = canvas
        self.old_x = None
        self.old_y = None
        self.eraser_size = 10

        #Mouse bindings 
        self.canvas.bind('<B1-Motion>', self.erase)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def set_eraser_size(self, size):
        self.eraser_size = size

    def erase(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.eraser_size, fill='white',
                                    capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None