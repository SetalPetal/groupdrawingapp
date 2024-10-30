import tkinter as tk

class BrushTool:
    def __init__(self, canvas, view):
        self.canvas = canvas
        self.view = view
        self.brush_style = 'line 1'  

    def activate(self):
        # Unbind any previous bindings
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        
        # Set up drawing events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

        #start drawing
    def start_draw(self, event):
        self.canvas.old_x = event.x
        self.canvas.old_y = event.y

        #draw class used to set the brush style
    def draw(self, event):
        if self.canvas.old_x and self.canvas.old_y:
            x, y = event.x, event.y
            fill_color = self.view.active_color 
            if self.brush_style == 'line 1':
                self.canvas.create_line(self.canvas.old_x, self.canvas.old_y, x, y, fill=fill_color, width=4)
            elif self.brush_style == 'line 2':
                self.canvas.create_line(self.canvas.old_x, self.canvas.old_y, x, y, fill=fill_color, width=8)
            elif self.brush_style == 'line 3':
                self.canvas.create_line(self.canvas.old_x, self.canvas.old_y, x, y, fill=fill_color, width=16)
            elif self.brush_style == 'line 4':
                self.canvas.create_line(self.canvas.old_x, self.canvas.old_y, x, y, fill=fill_color, width=32)
            elif self.brush_style == 'circle':
                self.canvas.create_oval(self.canvas.old_x, self.canvas.old_y, x, y, outline=fill_color, fill=fill_color)
            elif self.brush_style == 'square':
                self.canvas.create_rectangle(self.canvas.old_x, self.canvas.old_y, x, y, outline=fill_color, fill=fill_color)
            elif self.brush_style == 'triangle':
                points = [self.canvas.old_x, y, (self.canvas.old_x + x) / 2, self.canvas.old_y, x, y]
                self.canvas.create_polygon(points, outline=fill_color, fill=fill_color)
            elif self.brush_style == 'star':
                points = [self.canvas.old_x, y, (self.canvas.old_x + x) / 2, self.canvas.old_y, x, y, self.canvas.old_x, (self.canvas.old_y + y) / 2, x, (self.canvas.old_y + y) / 2]
                self.canvas.create_polygon(points, outline=fill_color, fill=fill_color)
            self.canvas.old_x = x
            self.canvas.old_y = y

        #end drawing 
    def end_draw(self, event):
        self.canvas.old_x = None
        self.canvas.old_y = None

    def set_brush_style(self, style):
        self.brush_style = style
