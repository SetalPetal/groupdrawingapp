from tkinter import Tk, Frame, Button, Scale, Canvas, Label, StringVar, Entry, Toplevel, messagebox, filedialog
from tkinter.colorchooser import askcolor
from PIL import Image, ImageGrab # No longer using Pillow modules in this file.
import os
from file_manager import FileManager

"""
!!! This code was derived from a tutorial to make a paint program.
Source: https://youtu.be/XNf8W0kf3XQ?si=m3HJQyuLGMEyd8WX
!!! This code is not to be incorporated into our project and is for research and testing only.

Please note, if you get "ModuleNotFoundError" when trying to run the program,
you will need to clone the github project in VS Code into a local folder on your computer
and open the folder location in VS Code.
IT TOOK ME HOURS TO FIGURE THAT OUT!!!
To clone the repository in VS Code, select 'View' > 'Command Palette' and enter 'gitcl'.
For some reason, VS Code was having a path issue with the remote github server when Python was trying to locate local modules.

For some reason, when trying to add commits from the clone I downloaded,
VS Code prompted to set user.name and user.email with git.
To do this, presuming you have installed git, open a terminal/command prompt on your computer and enter the following commands:
    git config --global user.name "github username"
    git config --global user.email johndoe@example.com
"""

class FilenamePopup: # This class is no longer used in this file.
    def __init__(self, master):
        top = self.top = Toplevel(master)
        self.lbl = Label(top, text='Choose a file name:')
        self.lbl.pack()
        self.ent_filename = Entry(top)
        self.ent_filename.pack()
        self.btn_ok = Button(top, text='OK', command=self.cleanup)
        self.btn_ok.pack()

    def cleanup(self):
        self.filename = self.ent_filename.get()
        self.top.destroy()

class Paint(object):
    DEFAULT_PEN_SIZE = 6.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1200x700")

        self.toolbar = Frame(self.root)
        self.toolbar.pack()
        # self.canvas_frame = Frame(self.root)
        # self.canvas_frame.pack()

        self.pen_button = Button(self.toolbar, text='Pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0, sticky='ew')

        self.brush_button = Button(self.toolbar, text='Brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1, sticky='ew')

        self.color_button = Button(self.toolbar, text='Colour', command=self.choose_color)
        self.color_button.grid(row=0, column=2, sticky='ew')

        self.eraser_button = Button(self.toolbar, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3, sticky='ew')

        self.size_scale = Scale(self.toolbar, from_=1, to=10, orient='horizontal')
        self.size_scale.grid(row=0, column=4, sticky='ew')

        self.line_button = Button(self.toolbar, text='Line', command=self.use_line)
        self.line_button.grid(row=1, column=0, sticky='ew')

        self.poly_button = Button(self.toolbar, text='Polygon', command=self.use_poly)
        self.poly_button.grid(row=1, column=1, sticky='ew')

        self.clear_button = Button(self.toolbar, text='Clear', command=lambda: self.c.delete('all'))
        self.clear_button.grid(row=1, column=2, sticky='ew')

        self.load_button = Button(self.toolbar, text='Load', command=self.load_image)
        self.load_button.grid(row=1, column=3, sticky='ew')

        self.save_button = Button(self.toolbar, text='Save', command=self.save_file)
        self.save_button.grid(row=1, column=4, sticky='ew')

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.pack()

        self.var_status = StringVar(value='Selected: Pen')
        self.lbl_status = Label(self.toolbar, textvariable=self.var_status)
        self.lbl_status.grid(row=3, column=4, rowspan=3)

        self.setup()
        

        self.root.mainloop()

    def setup(self):
        self.old_x, self.old_y = None, None
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = None
        self.size_multiplier = 1
        
        self.activate_button(self.pen_button)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.c.bind('<Button-1>', self.point)
        self.root.bind('<Escape>', self.line_reset)
        self.line_start = (None, None)

        self.canvas_image = None
        self.file_manager = FileManager()

    def use_pen(self):
        self.activate_button(self.pen_button)
        self.size_multiplier = 1

    def use_brush(self):
        self.activate_button(self.brush_button)
        self.size_multiplier = 2.5

    def use_line(self):
        self.activate_button(self.line_button)

    def use_poly(self):
        self.activate_button(self.poly_button)

    def choose_color(self):
        self.eraser_on = False
        color = askcolor(color = self.color)[1]

        if color is not None:
            self.color = color

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        # self.set_status()

        if self.active_button:
            self.active_button.config(relief='raised')

        some_button.config(relief='sunken')
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.set_status(event.x, event.y)
        line_width = self.size_scale.get() * self.size_multiplier
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=line_width, fill=paint_color, capstyle='round', smooth=True, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def line(self, x, y):
        line_width = self.size_scale.get() * self.size_multiplier
        paint_color = 'white' if self.eraser_on else self.color
        self.c.create_line(self.old_x,
                               self.line_start[0],
                               self.line_start[1],
                               x,
                               y,
                               width=line_width,
                               fill=paint_color,
                               capstyle='round',
                               smooth=True,
                               splinesteps=36)
        
    def point(self, event):
        self.set_status(event.x, event.y)
        btn = self.active_button['text']
        if btn in ('Line', 'Polygon'):
            self.size_multiplier = 1
            if any(self.line_start):
                self.line(event.x, event.y)
                self.line_start = ((None, None) if btn == 'Line' else (event.x, event.y))
            else:
                self.line_start = (event.x, event.y)

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def line_reset(self, event):
        self.line_start = (None, None)

    def color_default(self):
        self.color = self.DEFAULT_COLOR

    def set_status(self, x=None, y=None):
        if self.active_button:
            btn = self.active_button['text']
            oldxy = (self.line_start if btn in ('Line', 'Polygon') else (self.old_x, self.old_y))

            self.var_status.set(f'Selected: {btn}\n' + ((f'Old (x, y): {oldxy}\n(x, y: {x}, {y})') if x is not None and y is not None else ''))

    # def save_file(self):
    #     self.popup = FilenamePopup(self.root)
    #     self.save_button['state'] = 'disabled'
    #     self.root.wait_window(self.popup.top)

    #     filepng = self.popup.filename = ' .png'
    #     print(filepng)

    #     if not os.path.exists(filepng) or messagebox.askyesno('File already exists', 'Overwrite?'):
    #         fileps = self.popup.filename + '.eps'

    #         self.c.postscript(file=fileps)
    #         img = Image.open(fileps)
    #         img.save(filepng, 'png')
    #         os.remove(fileps)

    #         self.save_button['state'] = 'normal'

    #         messagebox.showinfo('File Save', 'File saved!')
    #     else:
    #         messagebox.showwarning('File Save', 'File not saved!')

    #     self.save_button['state'] = 'normal'

    def save_file(self):
        self.file_manager.save_file(self.root, self.c)

    def load_image(self):
        print(f"Window Width: {self.root.winfo_width()}\n Window Height: {self.root.winfo_height()}")
        self.canvas_image = self.file_manager.load_image(self.c)
        self.c.create_image(0, 0, anchor='nw', image=self.canvas_image)

        

    


if __name__ == '__main__':
    Paint()

