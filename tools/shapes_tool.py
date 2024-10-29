import tkinter as tk 

class ShapeTool:
    def __init__(self, canvas):
        self.canvas = canvas
        self.old_x = None
        self.old_y = None
        self.color = 'black'
        self.brush_size = 10
        self.shape = None
        self.current_shape = None

        #bind for mouse events
        self.canvas.bind('<Button-1>', self.button_press)
        self.canvas.bind('<B1-Motion>', self.mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.button_release)

        def rectangle(self):
            self.shape = 'rectangle'
        def oval(self):
            self.shape = 'oval'
        def line(self):
            self.shape = 'line'

        def button_press(self, event):
            self.old_x, self.old_y = event.x, event.y
            self.current_shape = None

        def mouse_drag(self, event):
            if self.shape:
                if self.current_shape:
                    self.canvas.delete(self.current_shape)
                if self.shape == 'rectangle':
                    self.current_shape = self.canvas.create_rectangle(self.old_x, self.old_y, event.x, event.y)
                elif self.shape == 'oval':
                    self.current_shape = self.canvas.create_oval(self.old_x, self.old_y, event.x, event.y)
                elif self.shape == 'line':
                    self.current_shape = self.canvas.create_line(self.old_x, self.old_y, event.x, event.y)

        def button_release(self, event):
            if self.shape:
                self.mouse_drag(event)
                self.current_shape = None
            self.old_x, self.old_y = None, None

