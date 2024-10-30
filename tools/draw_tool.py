class DrawTool:
    def __init__(self, canvas, undo_redo, view):
        self.canvas = canvas
        self.undo_redo = undo_redo
        self.view = view  # Ensures its the view 

    def activate(self):        
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        # Set up drawing events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)
        print("Draw tool activate")

    def start_draw(self, event):
        self.canvas.old_x = event.x
        self.canvas.old_y = event.y
       # start record actions for UndoRedo
        self.undo_redo.start_group()
    
    def draw(self, event):
        if self.canvas.old_x and self.canvas.old_y:
            x, y = event.x, event.y
            fill_color = self.view.active_color  # selected color
            #Record line
            line_id = self.canvas.create_line(
            self.canvas.old_x, 
            self.canvas.old_y, 
            x, 
            y, 
            fill=fill_color, 
            width=2
        )
        # Add recorded line 
        self.undo_redo.add_action({
            'type': 'line',
            'id': line_id,
            'coords': (self.canvas.old_x, self.canvas.old_y, x, y),
            'fill': fill_color,
            'width': 2
        })
        self.canvas.old_x = x
        self.canvas.old_y = y
    
    def end_draw(self, event):
        # end group recording when drawing stops
        self.undo_redo.end_group()
        self.canvas.old_x = None
        self.canvas.old_y = None


class Eraser:
    def __init__(self, canvas):
        self.canvas = canvas
        self.old_x = None
        self.old_y = None
        self.eraser_size = 10

    def activate(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

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
