import tkinter as tk

class DrawTool:

    MIN_SIZE = 1
    MAX_SIZE = 50

    def __init__(self, view, undo_redo):
        self.canvas = view.get_canvas()
        self.undo_redo = undo_redo
        self.view = view  # Ensures it's the view
        self.size = view.get_draw_size()
        self.current_objects = []

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
        # Start recording actions for UndoRedo
        self.undo_redo.start_group()
        self.current_objects = []

        # Draw initial oval to start the stroke
        fill_color = self.view.active_color
        width = self.size
        radius = width / 2
        oval_id = self.canvas.create_oval(
            event.x - radius, event.y - radius, event.x + radius, event.y + radius,
            fill=fill_color, outline=fill_color
        )
        self.current_objects.append(oval_id)

    def draw(self, event):
        if self.canvas.old_x and self.canvas.old_y:
            x1, y1 = self.canvas.old_x, self.canvas.old_y
            x2, y2 = event.x, event.y
            fill_color = self.view.active_color
            width = self.size

            # Draw line segment
            line_id = self.canvas.create_line(
                x1, y1, x2, y2,
                fill=fill_color,
                width=width,
                capstyle=tk.ROUND,
                smooth=True
            )
            self.current_objects.append(line_id)

            # Draw oval at the current position to fill gaps
            radius = width / 2
            oval_id = self.canvas.create_oval(
                x2 - radius, y2 - radius, x2 + radius, y2 + radius,
                fill=fill_color, outline=fill_color
            )
            self.current_objects.append(oval_id)

            # Record action for UndoRedo
            self.undo_redo.add_action({
                'type': 'item',
                'id': line_id,
            })
            self.undo_redo.add_action({
                'type': 'item',
                'id': oval_id,
            })

            self.canvas.old_x = x2
            self.canvas.old_y = y2

    def end_draw(self, event):
        # End group recording when drawing stops
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

        # Draw initial oval to start the erase action
        width = self.size
        radius = width / 2
        self.canvas.create_oval(
            event.x - radius, event.y - radius, event.x + radius, event.y + radius,
            fill='white', outline='white'
        )

    def erase(self, event):
        if self.old_x and self.old_y:
            x1, y1 = self.old_x, self.old_y
            x2, y2 = event.x, event.y
            width = self.size

            # Erase line segment
            self.canvas.create_line(
                x1, y1, x2, y2,
                fill='white',
                width=width,
                capstyle=tk.ROUND,
                smooth=True
            )

            # Draw oval at the current position to fill gaps
            radius = width / 2
            self.canvas.create_oval(
                x2 - radius, y2 - radius, x2 + radius, y2 + radius,
                fill='white', outline='white'
            )

            self.old_x = x2
            self.old_y = y2

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def update_size(self, size):
        self.size = int(size)
