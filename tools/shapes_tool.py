import tkinter as tk

class ShapeTool:
    def __init__(self, canvas):
        self.canvas = canvas
        self.old_x = None
        self.old_y = None
        self.color = 'black'
        self.fill_color = 'white'
        self.brush_size = 10
        self.shape = None
        self.current_shape = None

        # Bind for mouse events
        self.canvas.bind('<Button-1>', self.button_press)
        self.canvas.bind('<B1-Motion>', self.mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.button_release)

    def rectangle(self):
        self.shape = 'rectangle'

    def circle(self):
        self.shape = 'circle'

    def star(self):
        self.shape = 'star'

    def triangle(self):
        self.shape = 'triangle'

    def button_press(self, event):
        self.old_x, self.old_y = event.x, event.y
        self.current_shape = None

    def mouse_drag(self, event):
        if self.shape:
            if self.current_shape:
                self.canvas.delete(self.current_shape)
            if self.shape == 'rectangle':
                self.current_shape = self.canvas.create_rectangle(self.old_x, self.old_y, event.x, event.y,
                                                                  outline=self.color, fill=self.fill_color)
            elif self.shape == 'circle':
                self.current_shape = self.canvas.create_oval(self.old_x, self.old_y, event.x, event.y,
                                                             outline=self.color, fill=self.fill_color)
            elif self.shape == 'star':
                self.current_shape = self.create_star(self.old_x, self.old_y, event.x, event.y)
            elif self.shape == 'triangle':
                self.current_shape = self.create_triangle(self.old_x, self.old_y, event.x, event.y)

    def button_release(self, event):
        if self.shape:
            self.mouse_drag(event)
            self.current_shape = None
        self.old_x, self.old_y = None, None
        print("Button released")

    def create_star(self, x1, y1, x2, y2):
        # Custom method to draw a star
        points = [x1, y2, (x1 + x2) / 2, y1, x2, y2, x1, (y1 + y2) / 2, x2, (y1 + y2) / 2]
        return self.canvas.create_polygon(points, outline=self.color, fill=self.fill_color)

    def create_triangle(self, x1, y1, x2, y2):
        # Custom method to draw a triangle
        points = [x1, y2, (x1 + x2) / 2, y1, x2, y2]
        return self.canvas.create_polygon(points, outline=self.color, fill=self.fill_color)
