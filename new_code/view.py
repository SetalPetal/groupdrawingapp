import tkinter as tk
from tools import FileManager
from settings.setup import Layout, Theme


class View():

    def __init__(self, root):

        # Setup imported tools
        self.file_manager = FileManager()


        # Setup main window.
        self.root = root
        self.root.title("MEZ. Canvas")
        # self.root.iconbitmap("dir")
        self.root.geometry(Layout.root["SIZE"])

        # Setup toolbar frame and add to main window.
        self.toolbar = tk.Frame(self.root, bg=Theme.BLACK)
        self.toolbar.place(x=Layout.toolbar["X"],
                           y=Layout.toolbar["Y"],
                           width=Layout.toolbar["WIDTH"],
                           height=Layout.toolbar["HEIGHT"])
        
        
        
        # Set up save_load frame and add to toolbar.
        self.save_load_frame = tk.Frame(self.toolbar, bg=Theme.WHITE)
        self.save_load_frame.place(x=Layout.save_load["X"],
                           y=Layout.save_load["Y"],
                           width=Layout.save_load["WIDTH"],
                           height=Layout.save_load["HEIGHT"])
        
        # Set up save_load buttons
        self.save_button = tk.Button(self.root, text="Save", font="Helvetica", fg="black", borderwidth=0, padx=0, pady=0)
        self.save_button.place(x=10, y=10, width=47, height=25)
        
        # Setup canvas and add to main window.
        self.canvas = tk.Canvas(self.root, bg=Theme.WHITE)
        self.canvas.place(x=Layout.canvas["X"],
                          y=Layout.canvas["Y"],
                          width=Layout.canvas["WIDTH"],
                          height=Layout.canvas["HEIGHT"])





if __name__ == "__main__":
    root = tk.Tk()
    app = View(root)
    root.mainloop()