import tkinter as tk

class BrushTool:

    MIN_SIZE = 1
    MAX_SIZE = 200

    def __init__(self, view):
        self.view = view
        self.canvas = view.get_canvas()
        self.brush_style = 'line 1'
        self.size = view.get_draw_size() 

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
                self.canvas.create_line(x - (self.size / 2), y,
                                        x + (self.size / 2), y,
                                        fill=fill_color, width=int(self.size * 0.1))
            elif self.brush_style == 'line 2':
                self.canvas.create_line(x, y - self.size,
                                        x, y + self.size,
                                        fill=fill_color, width=int(self.size * 0.2))
            elif self.brush_style == 'line 3':
                self.canvas.create_line(x - self.size, y + self.size,
                                        x + self.size, y - self.size,
                                        fill=fill_color, width=int(self.size * 0.2))
            elif self.brush_style == 'line 4':
                self.canvas.create_line(x - self.size, y - self.size,
                                        x + self.size, y + self.size,
                                        fill=fill_color, width=int(self.size * 0.2))
            elif self.brush_style == 'circle':
                self.canvas.create_oval(x - (self.size / 2), y - (self.size / 2),
                                        x + (self.size / 2), y + (self.size / 2),
                                        outline=fill_color, fill=fill_color)
            elif self.brush_style == 'square':
                self.canvas.create_rectangle(x - (self.size / 2), y - (self.size / 2),
                                             x + (self.size / 2), y + (self.size / 2),
                                             outline=fill_color, fill=fill_color)
            elif self.brush_style == 'triangle':
                points = [x, y - (self.size / 5 * 3),
                          x + (self.size / 5 * 3), y + (self.size / 5 * 2),
                          x - (self.size / 5 * 3), y + (self.size / 5 * 2)]
                self.canvas.create_polygon(points, outline=fill_color, fill=fill_color)
            elif self.brush_style == 'star':
                points = [x, y - (self.size * 0.617),
                          x + (self.size * 0.12), y -(self.size * 0.234),
                          x + (self.size * 0.5), y - (self.size * 0.234),
                          x + (self.size * 0.2), y,
                          x + (self.size * 0.3), y + (self.size * 0.383),
                          x, y + (self.size * 0.149),
                          x - (self.size * 0.3), y + (self.size * 0.383),
                          x - (self.size * 0.2), y,
                          x - (self.size * 0.5), y - (self.size * 0.234),
                          x - (self.size * 0.12), y - (self.size * 0.234)]
                self.canvas.create_polygon(points, outline=fill_color, fill=fill_color)
            self.canvas.old_x = x
            self.canvas.old_y = y

        #end drawing 
    def end_draw(self, event):
        self.canvas.old_x = None
        self.canvas.old_y = None

    def set_brush_style(self, style):
        self.brush_style = style

    def update_size(self, size):
        self.size = int(size)
