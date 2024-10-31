import tkinter as tk

class DrawTool:
    MIN_SIZE = 1
    MAX_SIZE = 50

    def __init__(self, view, undo_redo):
        self.canvas = view.get_canvas()
        self.undo_redo = undo_redo
        self.view = view
        self.size = view.get_draw_size()
        self.current_objects = []

    def activate(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        #Set up drawing events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        print("Draw tool activated")

    def start_draw(self, event):
        self.canvas.old_x = event.x
        self.canvas.old_y = event.y
        #Start recording for UndoRedo
        self.undo_redo.start_group()
        self.current_objects = []

        #draw initial oval to start the drawing
        fill_color = self.view.active_color
        width = self.size
        radius = width / 2
        oval_id = self.canvas.create_oval(
            event.x - radius, event.y - radius, 
            event.x + radius, event.y + radius,
            fill=fill_color, outline=fill_color
        )
        self.current_objects.append(oval_id)
        
        #record the initial state for undo/redo
        self.undo_redo.add_action({
            'type': 'oval',
            'id': oval_id,
            'coords': [event.x - radius, event.y - radius, 
                      event.x + radius, event.y + radius],
            'fill': fill_color,
            'outline': fill_color
        })
    #start drawing segment
    def draw(self, event):
        if self.canvas.old_x and self.canvas.old_y:
            x1, y1 = self.canvas.old_x, self.canvas.old_y
            x2, y2 = event.x, event.y
            fill_color = self.view.active_color
            width = self.size

            
            line_id = self.canvas.create_line(
                x1, y1, x2, y2,
                fill=fill_color,
                width=width,
                capstyle='round',
                smooth=True
            )
            self.current_objects.append(line_id)

            #draw oval at the current position to fill gaps
            radius = width / 2
            oval_id = self.canvas.create_oval(
                x2 - radius, y2 - radius, 
                x2 + radius, y2 + radius,
                fill=fill_color, outline=fill_color
            )
            self.current_objects.append(oval_id)

            #record actions for UndoRedo with a dictionary
            self.undo_redo.add_action({
                'type': 'line',
                'id': line_id,
                'coords': [x1, y1, x2, y2],
                'fill': fill_color,
                'width': width
            })
            
            self.undo_redo.add_action({
                'type': 'oval',
                'id': oval_id,
                'coords': [x2 - radius, y2 - radius, 
                          x2 + radius, y2 + radius],
                'fill': fill_color,
                'outline': fill_color
            })

            self.canvas.old_x = x2
            self.canvas.old_y = y2

    def end_draw(self, event):
        #end group recording for UndoRedo
        self.undo_redo.end_group()
        self.canvas.old_x = None
        self.canvas.old_y = None
        self.current_objects = []

    def update_size(self, size):
        self.size = int(size)

class Eraser:
    MIN_SIZE = 1
    MAX_SIZE = 200

    def __init__(self, view):
        self.view = view
        self.canvas = view.get_canvas()
        self.old_x = None
        self.old_y = None
        self.size = view.get_draw_size()
        self.undo_redo = view.undo_redo
        self.current_shape_ids = []  #shape id for eraser movement

    def activate(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        self.canvas.bind('<Button-1>', self.start_erase)
        self.canvas.bind('<B1-Motion>', self.erase)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def start_erase(self, event):
        self.old_x = event.x
        self.old_y = event.y
        self.current_shape_ids = []  #reset shape IDs on new stroke
        
        #start recording group for undo/redo
        self.undo_redo.start_group()

        #draw initial oval to start the erase action
        width = self.size
        radius = width / 2
        shape_id = self.canvas.create_oval(
            event.x - radius, event.y - radius, event.x + radius, event.y + radius,
            fill='white', outline='white'
        )
        
        #add to undo stack
        self.current_shape_ids.append(shape_id)
        self.undo_redo.add_action({
            'type': 'oval',
            'coords': [event.x - radius, event.y - radius, event.x + radius, event.y + radius],
            'fill': 'white',
            'outline': 'white',
            'id': shape_id
        })

    def erase(self, event):
        if self.old_x and self.old_y:
            x1, y1 = self.old_x, self.old_y
            x2, y2 = event.x, event.y
            width = self.size

            #erase line segment
            line_id = self.canvas.create_line(
                x1, y1, x2, y2,
                fill='white',
                width=width,
                capstyle=tk.ROUND,
                smooth=True
            )
            
            #add to undo stack
            self.current_shape_ids.append(line_id)
            self.undo_redo.add_action({
                'type': 'line',
                'coords': [x1, y1, x2, y2],
                'fill': 'white',
                'width': width,
                'id': line_id
            })

            radius = width / 2  #draw in gaps
            oval_id = self.canvas.create_oval(
                x2 - radius, y2 - radius, x2 + radius, y2 + radius,
                fill='white', outline='white'
            )
            
            #add to undo stack
            self.current_shape_ids.append(oval_id)
            self.undo_redo.add_action({
                'type': 'oval',
                'coords': [x2 - radius, y2 - radius, x2 + radius, y2 + radius],
                'fill': 'white',
                'outline': 'white',
                'id': oval_id
            })

            self.old_x = x2
            self.old_y = y2

    def reset(self, event):
        #wnd group recording for undoredo
        self.undo_redo.end_group()
        
        self.old_x = None
        self.old_y = None
        self.current_shape_ids = []

    def update_size(self, size):
        self.size = int(size)