from tkinter import colorchooser

class ColorPicker:
    def __init__(self, root):
        self.root = root

    def get_color(self):
        color = colorchooser.askcolor(title="Choose color")
        if color[1]:
            return color[1]
        else:
            return None
