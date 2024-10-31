import tkinter as tk

class BrushTool:
    MIN_SIZE = 1
    MAX_SIZE = 200

    def __init__(self, view):
        self.view = view    #for referencing view canvas
        self.canvas = view.get_canvas()
        self.undo_redo = view.undo_redo  #get reference to undo_redo from view
        self.brush_style = 'line 1'
        self.size = view.get_draw_size()
        self.current_shape = None  #set variable for current shape

    def activate(self):
        #unbind any previous bindings
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        
        # Set up drawing events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def start_draw(self, event):
        self.canvas.old_x = event.x
        self.canvas.old_y = event.y
        self.undo_redo.start_group() #start group recording

    def draw(self, event):
        if self.canvas.old_x and self.canvas.old_y:
            x, y = event.x, event.y
            fill_color = self.view.active_color 
            
            #shapes for brush styles
            if self.brush_style == 'line 1':
                shape_id = self.canvas.create_line(
                    x - (self.size / 2), y,
                    x + (self.size / 2), y,
                    fill=fill_color, width=int(self.size * 0.1)
                )
                #add to undo stack
                self.undo_redo.add_action({
                    'type': 'line',
                    'id': shape_id,
                    'coords': [x - (self.size / 2), y, x + (self.size / 2), y],
                    'fill': fill_color,
                    'width': int(self.size * 0.1)
                })
            
            elif self.brush_style == 'line 2':
                shape_id = self.canvas.create_line(
                    x, y - self.size,
                    x, y + self.size,
                    fill=fill_color, width=int(self.size * 0.2)
                )
                self.undo_redo.add_action({
                    'type': 'line',
                    'id': shape_id,
                    'coords': [x, y - self.size, x, y + self.size],
                    'fill': fill_color,
                    'width': int(self.size * 0.2)
                })

            elif self.brush_style == 'line 3':
                shape_id = self.canvas.create_line(
                    x - self.size, y + self.size,
                    x + self.size, y - self.size,
                    fill=fill_color, width=int(self.size * 0.2)
                )
                self.undo_redo.add_action({
                    'type': 'line',
                    'id': shape_id,
                    'coords': [x - self.size, y + self.size, x + self.size, y - self.size],
                    'fill': fill_color,
                    'width': int(self.size * 0.2)
                })

            elif self.brush_style == 'line 4':
                shape_id = self.canvas.create_line(
                    x - self.size, y - self.size,
                    x + self.size, y + self.size,
                    fill=fill_color, width=int(self.size * 0.2)
                )
                self.undo_redo.add_action({
                    'type': 'line',
                    'id': shape_id,
                    'coords': [x - self.size, y - self.size, x + self.size, y + self.size],
                    'fill': fill_color,
                    'width': int(self.size * 0.2)
                })

            elif self.brush_style == 'circle':
                shape_id = self.canvas.create_oval(
                    x - (self.size / 2), y - (self.size / 2),
                    x + (self.size / 2), y + (self.size / 2),
                    outline=fill_color, fill=fill_color
                )
                self.undo_redo.add_action({
                    'type': 'oval',
                    'id': shape_id,
                    'coords': [x - (self.size / 2), y - (self.size / 2), 
                             x + (self.size / 2), y + (self.size / 2)],
                    'fill': fill_color,
                    'outline': fill_color
                })

            elif self.brush_style == 'square':
                shape_id = self.canvas.create_rectangle(
                    x - (self.size / 2), y - (self.size / 2),
                    x + (self.size / 2), y + (self.size / 2),
                    outline=fill_color, fill=fill_color
                )
                self.undo_redo.add_action({
                    'type': 'rectangle',
                    'id': shape_id,
                    'coords': [x - (self.size / 2), y - (self.size / 2),
                             x + (self.size / 2), y + (self.size / 2)],
                    'fill': fill_color,
                    'outline': fill_color
                })

            elif self.brush_style == 'triangle':
                points = [x, y - (self.size / 5 * 3),
                         x + (self.size / 5 * 3), y + (self.size / 5 * 2),
                         x - (self.size / 5 * 3), y + (self.size / 5 * 2)]
                shape_id = self.canvas.create_polygon(points, outline=fill_color, fill=fill_color)
                self.undo_redo.add_action({
                    'type': 'polygon',
                    'id': shape_id,
                    'points': points,
                    'fill': fill_color,
                    'outline': fill_color
                })

            elif self.brush_style == 'star':
                points = [x, y - (self.size * 0.617),
                         x + (self.size * 0.12), y - (self.size * 0.234),
                         x + (self.size * 0.5), y - (self.size * 0.234),
                         x + (self.size * 0.2), y,
                         x + (self.size * 0.3), y + (self.size * 0.383),
                         x, y + (self.size * 0.149),
                         x - (self.size * 0.3), y + (self.size * 0.383),
                         x - (self.size * 0.2), y,
                         x - (self.size * 0.5), y - (self.size * 0.234),
                         x - (self.size * 0.12), y - (self.size * 0.234)]
                shape_id = self.canvas.create_polygon(points, outline=fill_color, fill=fill_color)
                self.undo_redo.add_action({
                    'type': 'polygon',
                    'id': shape_id,
                    'points': points,
                    'fill': fill_color,
                    'outline': fill_color
                })

            self.canvas.old_x = x
            self.canvas.old_y = y

    def end_draw(self, event):
        self.canvas.old_x = None
        self.canvas.old_y = None
        #end group recording
        self.undo_redo.end_group()

    def set_brush_style(self, style):
        self.brush_style = style

    def update_size(self, size):
        self.size = int(size)