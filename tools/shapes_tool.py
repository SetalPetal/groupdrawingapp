import tkinter as tk

class ShapeTool:
    def __init__(self, view):
        self.view = view
        self.canvas = view.get_canvas()
        self.undo_redo = view.undo_redo  #get reference to undo_redo from view
        self.old_x = None
        self.old_y = None
        self.color = view.get_swatch_color("swatch_1")
        self.fill_color = view.get_swatch_color("swatch_2")
        self.brush_size = 10
        self.shape = "square"
        self.current_shape = None

        # Bind for mouse events
        self.canvas.bind('<Button-1>', self.button_press)
        self.canvas.bind('<B1-Motion>', self.mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.button_release)
        # Activate mouse events
    def activate(self):
        self.canvas.bind('<Button-1>', self.button_press)
        self.canvas.bind('<B1-Motion>', self.mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.button_release)
        print("ShapeTool activated")

    def square(self):
        self.shape = 'square'

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
            if self.shape == 'circle':
                self.current_shape = self.canvas.create_oval(
                    self.old_x, self.old_y, event.x, event.y,
                    outline=self.color, fill=self.fill_color
                )
            elif self.shape == 'square':
                self.current_shape = self.canvas.create_rectangle(
                    self.old_x, self.old_y, event.x, event.y,
                    outline=self.color, fill=self.fill_color
                )
            elif self.shape == 'star':
                self.current_shape = self.create_star(self.old_x, self.old_y, event.x, event.y)
            elif self.shape == 'triangle':
                self.current_shape = self.create_triangle(self.old_x, self.old_y, event.x, event.y)

    def button_release(self, event):
        if self.shape:
            # Delete the preview shape
            if self.current_shape:
                self.canvas.delete(self.current_shape)
            
            # Create final shape and id
            shape_id = None
            coords = [self.old_x, self.old_y, event.x, event.y]
            
            if self.shape == 'circle':
                shape_id = self.canvas.create_oval(
                    coords[0], coords[1], coords[2], coords[3],
                    outline=self.color, fill=self.fill_color
                )
                shape_type = 'oval'
            elif self.shape == 'square':
                shape_id = self.canvas.create_rectangle(
                    coords[0], coords[1], coords[2], coords[3],
                    outline=self.color, fill=self.fill_color
                )
                shape_type = 'rectangle'
            elif self.shape == 'star':
                points = self._calculate_star_points(coords[0], coords[1], coords[2], coords[3])
                shape_id = self.canvas.create_polygon(
                    points, outline=self.color, fill=self.fill_color
                )
                shape_type = 'polygon'
            elif self.shape == 'triangle':
                points = self._calculate_triangle_points(coords[0], coords[1], coords[2], coords[3])
                shape_id = self.canvas.create_polygon(
                    points, outline=self.color, fill=self.fill_color
                )
                shape_type = 'polygon'

            # Create dictionary for undo/redo
            if shape_id:
                action = {
                    'type': shape_type,
                    'id': shape_id,
                    'coords': coords,
                    'fill': self.fill_color,
                    'outline': self.color
                }
                
                # For polygon shapes (star and triangle), add points
                if shape_type == 'polygon':
                    if self.shape == 'star':
                        action['points'] = points
                    elif self.shape == 'triangle':
                        action['points'] = points

                # Add the action to the undo stack
                self.undo_redo.add_action(action)

            self.current_shape = None
        self.old_x, self.old_y = None, None

    def create_star(self, x1, y1, x2, y2):
        points = self._calculate_star_points(x1, y1, x2, y2)
        return self.canvas.create_polygon(points, outline=self.color, fill=self.fill_color)

    def create_triangle(self, x1, y1, x2, y2):
        points = self._calculate_triangle_points(x1, y1, x2, y2)
        return self.canvas.create_polygon(points, outline=self.color, fill=self.fill_color)
    
    def _calculate_star_points(self, x1, y1, x2, y2):
        return [x1, y2, (x1 + x2) / 2, y1, x2, y2, x1, (y1 + y2) / 2, x2, (y1 + y2) / 2]
    
    def _calculate_triangle_points(self, x1, y1, x2, y2):
        return [x1, y2, (x1 + x2) / 2, y1, x2, y2]
    
    def update_colors(self):
        self.color = self.view.get_swatch_color("swatch_1")
        self.fill_color = self.view.get_swatch_color("swatch_2")