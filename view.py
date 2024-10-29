import tkinter as tk
from tools import FileManager
from tools import draw_tool
from settings.setup import Layout, Theme
from enhancements.zbutton import ZButton


class View():

    def _get_component_img(self, file_name):
        # Set path to component image.
        PATH = f"data/ui_components/{file_name}.png"
        # Return loaded image.
        return tk.PhotoImage(file=PATH)

    def _get_button_images(self, component_name):
        # Get images for each button state.
        button_inactive = self._get_component_img(f"{component_name}_btn_inactive")
        button_hover = self._get_component_img(f"{component_name}_btn_hover")
        button_active = self._get_component_img(f"{component_name}_btn_active")
        # Return dictionary with each button state image.
        return {
            "inactive":button_inactive,
            "hover":button_hover,
            "active":button_active
            }

    def _load_img_components(self):
        # Button images
        self._save_btn_imgs = self._get_button_images("plain_rectangle")
        self._load_btn_imgs = self._get_button_images("plain_rectangle")
        self._pencil_btn_imgs = self._get_button_images("pencil")
        self._paint_btn_imgs = self._get_button_images("paint")
        self._eraser_btn_imgs = self._get_button_images("eraser")
        self._undo_btn_imgs = self._get_button_images("undo")
        self._redo_btn_imgs = self._get_button_images("redo")

        # Label images
        self._load_save_bg_img = self._get_component_img("load_save_frame_bg")
        self._undo_redo_bg_img = self._get_component_img("undo_redo_frame_bg")
        self._draw_bg_img = self._get_component_img("draw_frame_bg")
        self._color_bg_img = self._get_component_img("color_frame_bg")
        self._brush_style_bg_img = self._get_component_img("brush_style_frame_bg")
        self._draw_shape_bg_img = self._get_component_img("draw_shape_frame_bg")
        self._slider_bg_img = self._get_component_img("slider_frame_bg")
        self._size_input_output_bg_img = self._get_component_img("size_input_output_frame_bg")
        self._size_label_bg_img = self._get_component_img("plain_square_btn_inactive")

        

        

    def __init__(self, root):

        # Setup imported tools
        self.file_manager = FileManager()

        #Load image compoents.
        self._load_img_components()

#------ Setup main window.
        self.root = root
        self.root.title("MEZ. Canvas")
        self.root.iconbitmap("data/ui_components/app_icon.ico")
        self.root.geometry(Layout.root["SIZE"])
        self.root.configure(background="black")

#------ Setup toolbar frame and add to main window.
        self.toolbar = tk.Frame(self.root,
                                bg=Theme.BLACK)
        self.toolbar.place(x=Layout.toolbar["X"],
                           y=Layout.toolbar["Y"],
                           width=Layout.toolbar["WIDTH"],
                           height=Layout.toolbar["HEIGHT"])           
        
#------ Set up save_load frame and add to toolbar.
        self.load_save_frame = tk.Frame(self.toolbar, bg=Theme.BLACK)
        self.load_save_frame.place(x=Layout.load_save["X"],
                                   y=Layout.load_save["Y"],
                                   width=Layout.load_save["FRAME_WIDTH"],
                                   height=Layout.load_save["FRAME_HEIGHT"])
        # Add background image to the frame.
        self.load_save_bg = tk.Label(self.load_save_frame,
                                     image=self._load_save_bg_img,
                                     bg=Theme.BLACK)
        self.load_save_bg.place(x=Layout.DEFAULT_PADDING,
                                y=Layout.DEFAULT_PADDING,
                                width=Layout.load_save["BG_WIDTH"],
                                height=Layout.load_save["BG_HEIGHT"])        
        # Set up save_load buttons using ZButton class - a modified tk.Button class.
        # Make sure to include img_library argument after root argument.
        # Refer to _load_img_components() for list of image dicts that will be loaded.
    #-- SAVE BUTTON.
        self.save_button = ZButton(self.load_save_frame,
                                   self._save_btn_imgs,
                                   text="Save",
                                   compound="center",
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0)
        self.save_button.place(x=Layout.load_save["BUTTON_PADDING"],
                               y=Layout.load_save["BUTTON_PADDING"])
    #-- LOAD BUTTON.
        self.load_button = ZButton(self.load_save_frame,
                                   self._load_btn_imgs,
                                   text="load",
                                   compound="center",
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0)
        self.load_button.place(x=Layout.load_save["BUTTON_PADDING"],
                               y=Layout.load_save["SECOND_ROW_Y"])

#------ Set up draw frame and add to toolbar.
        self.draw_frame = tk.Frame(self.toolbar, bg=Theme.BLACK)
        self.draw_frame.place(x=Layout.draw["X"],
                                   y=Layout.draw["Y"],
                                   width=Layout.draw["FRAME_WIDTH"],
                                   height=Layout.draw["FRAME_HEIGHT"])
        # Add background image to the frame.
        self.draw_bg = tk.Label(self.draw_frame,
                                image=self._draw_bg_img,
                                bg=Theme.BLACK)
        self.draw_bg.place(x=Layout.DEFAULT_PADDING,
                                y=Layout.DEFAULT_PADDING,
                                width=Layout.draw["BG_WIDTH"],
                                height=Layout.draw["BG_HEIGHT"])
        # Create and add buttons.
    #-- PENCIL BUTTON.
        self.pencil_button = ZButton(self.draw_frame,
                                   self._pencil_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0,
                                   )
        self.pencil_button.place(x=Layout.draw["BUTTON_PADDING"],
                               y=Layout.draw["BUTTON_PADDING"])
    #-- PAINT BUTTON.
        self.paint_button = ZButton(self.draw_frame,
                                   self._paint_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0)
        self.paint_button.place(x=Layout.draw["BUTTON_PADDING"],
                               y=Layout.draw["SECOND_ROW_Y"])

    #-- ERASER BUTTON.
        self.eraser_button = ZButton(self.draw_frame,
                                   self._eraser_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0)
        self.eraser_button.place(x=Layout.draw["ERASER_BUTTON_X"],
                               y=Layout.draw["SECOND_ROW_Y"])
        # Slider background.
        self.slider_bg = tk.Label(self.draw_frame,
                                image=self._slider_bg_img,
                                bg=Theme.WHITE)
        self.slider_bg.place(x=Layout.draw["SLIDER_BG_X"],
                               y=Layout.draw["BUTTON_PADDING"],
                                width=Layout.draw["SLIDER_BG_WIDTH"],
                                height=Layout.DEFAULT_BUTTON_HEIGHT)
    #-- Size Slider.
        self.size_slider = tk.Scale(self.draw_frame, from_=0, to=200, showvalue=False,orient="horizontal")
        self.size_slider.place(x=Layout.draw["SIZE_SLIDER_X"],
                               y=Layout.draw["SIZE_SLIDER_Y"],
                               width=Layout.draw["SIZE_SLIDER_WIDTH"],
                               height=Layout.draw["SIZE_SLIDER_HEIGHT"],
                               )
        # Size background.
        self.size_bg = tk.Label(self.draw_frame,
                                image=self._size_input_output_bg_img,
                                bg=Theme.WHITE)
        self.size_bg.place(x=Layout.draw["SIZE_BG_X"],
                           y=Layout.draw["SECOND_ROW_Y"],
                           width=Layout.draw["SIZE_BG_WIDTH"],
                           height=Layout.DEFAULT_BUTTON_HEIGHT)
        # Size Label.
        self.size_label = tk.Label(self.draw_frame,
                                   text="Size",
                                   image=self._size_label_bg_img,
                                   compound="center",
                                   bg=Theme.WHITE)
        self.size_label.place(x=Layout.draw["SIZE_BG_X"],
                              y=Layout.draw["SECOND_ROW_Y"],
                              width=Layout.DEFAULT_BUTTON_HEIGHT,
                              height=Layout.DEFAULT_BUTTON_HEIGHT)
    #-- Size text input/output.
        self.size_input_output = tk.Text(self.draw_frame)
        self.size_input_output.place(x=Layout.draw["TEXT_BOX_X"],
                                     y=Layout.draw["TEXT_BOX_Y"],
                                     width=Layout.draw["TEXT_BOX_WIDTH"],
                                     height=Layout.draw["TEXT_BOX_HEIGHT"])
        # testing code.
        self.size_input_output.insert(tk. END, "20")




#------ Set up color frame and add to toolbar.
        self.color_frame = tk.Frame(self.toolbar, bg=Theme.BLACK)
        self.color_frame.place(x=Layout.color["X"],
                                   y=Layout.color["Y"],
                                   width=Layout.color["FRAME_WIDTH"],
                                   height=Layout.color["FRAME_HEIGHT"])
        # Add background image to the frame.
        self.color_bg = tk.Label(self.color_frame,
                                image=self._color_bg_img,
                                bg=Theme.BLACK)
        self.color_bg.place(x=Layout.DEFAULT_PADDING,
                            y=Layout.DEFAULT_PADDING,
                            width=Layout.color["BG_WIDTH"],
                            height=Layout.color["BG_HEIGHT"])

#------ Set up brush style frame and add to toolbar.
        self.brush_style_frame = tk.Frame(self.toolbar, bg=Theme.BLACK)
        self.brush_style_frame.place(x=Layout.brush_style["X"],
                                     y=Layout.brush_style["Y"],
                                     width=Layout.brush_style["FRAME_WIDTH"],
                                     height=Layout.brush_style["FRAME_HEIGHT"])
        # Add background image to the frame.
        self.brush_style_bg = tk.Label(self.brush_style_frame,
                                       image=self._brush_style_bg_img,
                                       bg=Theme.BLACK)
        self.brush_style_bg.place(x=Layout.DEFAULT_PADDING,
                               y=Layout.DEFAULT_PADDING,
                               width=Layout.brush_style["BG_WIDTH"],
                               height=Layout.brush_style["BG_HEIGHT"])

#------ Set up draw shape frame and add to toolbar.
        self.draw_shape_frame = tk.Frame(self.toolbar, bg=Theme.BLACK)
        self.draw_shape_frame.place(x=Layout.draw_shape["X"],
                                     y=Layout.draw_shape["Y"],
                                     width=Layout.draw_shape["FRAME_WIDTH"],
                                     height=Layout.draw_shape["FRAME_HEIGHT"])
        # Add background image to the frame.
        self.draw_shape_bg = tk.Label(self.draw_shape_frame,
                                       image=self._draw_shape_bg_img,
                                       bg=Theme.BLACK)
        self.draw_shape_bg.place(x=Layout.DEFAULT_PADDING,
                               y=Layout.DEFAULT_PADDING,
                               width=Layout.draw_shape["BG_WIDTH"],
                               height=Layout.draw_shape["BG_HEIGHT"])
        
#------ Set up undo_redo frame and add to toolbar.
        self.undo_redo_frame = tk.Frame(self.toolbar, bg=Theme.BLACK)
        self.undo_redo_frame.place(x=Layout.undo_redo["X"],
                                   y=Layout.undo_redo["Y"],
                                   width=Layout.undo_redo["FRAME_WIDTH"],
                                   height=Layout.undo_redo["FRAME_HEIGHT"])
        # Add background image to the frame.
        self.undo_redo_bg = tk.Label(self.undo_redo_frame,
                                     image=self._undo_redo_bg_img,
                                     bg=Theme.BLACK)
        self.undo_redo_bg.place(x=Layout.DEFAULT_PADDING,
                                y=Layout.DEFAULT_PADDING,
                                width=Layout.undo_redo["BG_WIDTH"],
                                height=Layout.undo_redo["BG_HEIGHT"])        
        # Set up undo and redo buttons using ZButton class - a modified tk.Button class.
        self.undo_button = ZButton(self.undo_redo_frame,
                                   self._undo_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0)
        self.undo_button.place(x=Layout.undo_redo["BUTTON_PADDING"],
                               y=Layout.undo_redo["BUTTON_PADDING"])
        # Redo button.
        self.redo_button = ZButton(self.undo_redo_frame,
                                   self._redo_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0)
        self.redo_button.place(x=Layout.undo_redo["BUTTON_PADDING"],
                               y=Layout.undo_redo["SECOND_ROW_Y"])

        
#------ Setup canvas and add to main window.
        self.canvas = tk.Canvas(self.root, bg=Theme.WHITE)
        #self.canvas.grid(row=2, column=0, columnspan=6, sticky="n")
        self.canvas.place(x=Layout.canvas["X"],
                          y=Layout.canvas["Y"],
                          width=Layout.canvas["WIDTH"],
                          height=Layout.canvas["HEIGHT"])

        #Fleshed out pencil button linked to draw_tool def
        self.pencil_button = ZButton(self.draw_frame,
                                     self._pencil_btn_imgs,
                                     fg=Theme.BLACK,
                                     highlightthickness=0, bd=0,
                                     command=draw_tool(self.canvas))  

        self.pencil_button.place(x=Layout.draw["BUTTON_PADDING"],
                                 y=Layout.draw["BUTTON_PADDING"])
#------ Set up footer and add to main window.
        # Footer may be used in future development for app info and zoom in/out feature.
        self.footer = tk.Frame(self.root, bg=Theme.MID_GRAY)
        self.footer.place(x=Layout.footer["X"],
                          y=Layout.footer["Y"],
                          width=Layout.footer["WIDTH"],
                          height=Layout.footer["HEIGHT"])

        

        






if __name__ == "__main__":
    root = tk.Tk()
    app = View(root)
    root.mainloop()