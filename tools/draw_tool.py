class DrawTool:
    def __init__(self, canvas, undo_redo):
        self.canvas = canvas
        self.undo_redo = undo_redo
        
    def activate(self):
        # Unbind any existing events
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
        # Start recording a new action group when drawing begins
        self.undo_redo.start_group()
    
    def draw(self, event):
        if self.canvas.old_x and self.canvas.old_y:
            x, y = event.x, event.y
            # Create the line and store its ID
            line_id = self.canvas.create_line(
                self.canvas.old_x, 
                self.canvas.old_y, 
                x, 
                y, 
                fill="black", 
                width=2
            )
            # Add the action to the current group
            self.undo_redo.add_action({
                'type': 'line',
                'id': line_id,
                'coords': (self.canvas.old_x, self.canvas.old_y, x, y),
                'fill': "black",
                'width': 2
            })
            self.canvas.old_x = x
            self.canvas.old_y = y
    
    def end_draw(self, event):
        # End the action group when drawing stops
        self.undo_redo.end_group()
        self.canvas.old_x = None
        self.canvas.old_y = None


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

