import tkinter as tk
from tools import FileManager
from tools import UndoRedo
from tools import DrawTool
from tools.color_picker import ColorPicker
from settings.setup import Layout, Theme
from enhancements.zbutton import ZButton
from tools import FileManager
from tools import UndoRedo
from tools import DrawTool
from tools.color_picker import ColorPicker
from tools.shapes_tool import ShapeTool
from tools.draw_tool import Eraser
from tools.brush_tool import BrushTool

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
        self.swatch_btn_imgs = self._get_button_images("color_select")
        self.color_picker_btn_imgs = self._get_button_images("color_picker")
        self._undo_btn_imgs = self._get_button_images("undo")
        self._redo_btn_imgs = self._get_button_images("redo")
        self.square_btn_imgs = self._get_button_images("square")
        self.triangle_btn_imgs = self._get_button_images("triangle")
        self.circle_btn_imgs = self._get_button_images("circle")
        self.star_btn_imgs = self._get_button_images("star")
        self.line_horizontal_btn_imgs = self._get_button_images("line_horizontal")
        self.line_vertical_btn_imgs = self._get_button_images("line_vertical")
        self.line_diagonal_1_btn_imgs = self._get_button_images("line_diagonal_1")
        self.line_diagonal_2_btn_imgs = self._get_button_images("line_diagonal_2")

        # Shape button icons.
        self.shape_icons_button = {
            "square":self.square_btn_imgs,
            "circle":self.circle_btn_imgs,
            "triangle":self.triangle_btn_imgs,
            "star":self.star_btn_imgs
        }
        # Static shape icons.
        self.shape_icons_static =  {
            "square":self.square_btn_imgs["active"],
            "circle":self.circle_btn_imgs["active"],
            "triangle":self.triangle_btn_imgs["active"],
            "star":self.star_btn_imgs["active"],
            "line 1":self.line_horizontal_btn_imgs["active"],
            "line 2":self.line_vertical_btn_imgs["active"],
            "line 3":self.line_diagonal_1_btn_imgs["active"],
            "line 4":self.line_diagonal_2_btn_imgs["active"],
        }       

        # Label images
        self._load_save_bg_img = self._get_component_img("load_save_frame_bg")
        self._undo_redo_bg_img = self._get_component_img("undo_redo_frame_bg")
        self._draw_bg_img = self._get_component_img("draw_frame_bg")
        self._brush_style_bg_img = self._get_component_img("brush_style_frame_bg")
        self._draw_shape_bg_img = self._get_component_img("draw_shape_frame_bg")
        self._slider_bg_img = self._get_component_img("slider_frame_bg")
        self._size_input_output_bg_img = self._get_component_img("size_input_output_frame_bg")
        self._size_label_bg_img = self._get_component_img("plain_square_btn_active")
        self._color_bg_img = self._get_component_img("color_frame_bg")
        self._color_label_bg_img = self._get_component_img("color_label_bg")
        self.brush_style_label_img = self._get_component_img("brush_style_label_bg")
        self.draw_shape_label_img = self._get_component_img("draw_shape_label_bg")        

    def __init__(self, root):

        # Setup imported tools
        self.file_manager = FileManager()
        self.undo_redo = UndoRedo()
        self.action_history = []

        #Load image compoents.
        self._load_img_components()

    # Initialize colors and active swatch
        self.swatch1_color = 'black'
        self.swatch2_color = 'white'
        self.active_color = self.swatch1_color
        self.active_swatch = 1

#------ Setup main window.
        self.root = root
        self.root.title("MEZ. Canvas")
        self.root.iconbitmap("data/ui_components/app_icon.ico")
        self.root.geometry(Layout.root["SIZE"])
        self.root.configure(background="black")

        # Setup canvas
        self.canvas = tk.Canvas(self.root, bg=Theme.WHITE)
        self.canvas.place(x=Layout.canvas["X"],
                          y=Layout.canvas["Y"],
                          width=Layout.canvas["WIDTH"],
                          height=Layout.canvas["HEIGHT"])
        self.canvas.old_x = None
        self.canvas.old_y = None

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
                                   highlightthickness = 0, bd = 0,
                                   command=self.save_canvas)
        self.save_button.place(x=Layout.TOOLBAR_PADDING,
                               y=Layout.TOOLBAR_PADDING)
    #-- LOAD BUTTON.
        self.load_button = ZButton(self.load_save_frame,
                                   self._load_btn_imgs,
                                   text="load",
                                   compound="center",
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0,
                                   command=self.load_img_to_canvas)
        self.load_button.place(x=Layout.TOOLBAR_PADDING,
                               y=Layout.TOOLBAR_SECOND_ROW_Y)

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
                                   highlightthickness=0, bd=0,
                                   command=self.use_pencil)
        self.pencil_button.place(x=Layout.TOOLBAR_PADDING,
                               y=Layout.TOOLBAR_PADDING)
    #-- PAINT BUTTON.
        self.paint_button = ZButton(self.draw_frame,
                                   self._paint_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness=0, bd=0,
                                   command=self.use_paint)
        self.paint_button.place(x=Layout.TOOLBAR_PADDING,
                               y=Layout.TOOLBAR_SECOND_ROW_Y)

    #-- ERASER BUTTON.
        self.eraser_button = ZButton(self.draw_frame,
                                   self._eraser_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness =0, bd=0,
                                   command=self.use_eraser)
        self.eraser_button.place(x=Layout.draw["ERASER_BUTTON_X"],
                               y=Layout.TOOLBAR_SECOND_ROW_Y)
        self.eraser_button.config(command=self.use_eraser)
        # Slider background.
        self.slider_bg = tk.Label(self.draw_frame,
                                image=self._slider_bg_img,
                                bg=Theme.WHITE)
        self.slider_bg.place(x=Layout.draw["SLIDER_BG_X"],
                               y=Layout.TOOLBAR_PADDING,
                                width=Layout.draw["SLIDER_BG_WIDTH"],
                                height=Layout.DEFAULT_BUTTON_SIZE)
    #-- Size Slider.
        self.slider_value = tk.StringVar()
        self.size_slider = tk.Scale(self.draw_frame,
                                    from_=1, to=200,
                                    showvalue=False,
                                    orient="horizontal",
                                    variable=self.slider_value,
                                    command=self.size_scale)
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
                           y=Layout.TOOLBAR_SECOND_ROW_Y,
                           width=Layout.draw["SIZE_BG_WIDTH"],
                           height=Layout.DEFAULT_BUTTON_SIZE)
        # Size Label.
        self.size_label = tk.Label(self.draw_frame,
                                   text="Size",
                                   image=self._size_label_bg_img,
                                   compound="center",
                                   bg=Theme.WHITE)
        self.size_label.place(x=Layout.draw["SIZE_BG_X"],
                              y=Layout.TOOLBAR_SECOND_ROW_Y,
                              width=Layout.DEFAULT_BUTTON_SIZE,
                              height=Layout.DEFAULT_BUTTON_SIZE)
    #-- Size text input/output
        self.size_entry_value = tk.StringVar()
        self.size_entry = tk.Entry(self.draw_frame,
                                   textvariable=self.size_entry_value,
                                   validate="key",
                                   validatecommand=(root.register(self._size_entry_validation), "%S"))
        self.size_entry.place(x=Layout.draw["TEXT_BOX_X"],
                                     y=Layout.draw["TEXT_BOX_Y"],
                                     width=Layout.draw["TEXT_BOX_WIDTH"],
                                     height=Layout.draw["TEXT_BOX_HEIGHT"])
        self.size_entry.bind('<FocusOut>', self.size_entry_input)
        self.size_entry.bind('<Return>', self.size_entry_input)
        # testing code.
        self.size_entry.insert(tk. END, "20")

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
        # Add color tool label.
        self.color_label = tk.Label(self.color_frame,
                                    text="color",
                                    image=self._color_label_bg_img,
                                    compound="center",
                                    bg=Theme.BLACK)
        self.color_label.place(x=Layout.color["LABEL_X"],
                               y=Layout.DEFAULT_PADDING,
                               width=Layout.color["FRAME_WIDTH"],
                               height=Layout.color["LABEL_HEIGHT"])
        
        # Swatch Button 1
        self.swatch_1_button = ZButton(
            self.color_frame,
            self.swatch_btn_imgs,
            bg=self.swatch1_color,
            fg=Theme.BLACK,
            highlightthickness=0, bd=0,
            command=self.select_swatch1
        )
        self.swatch_1_button.place(x=Layout.TOOLBAR_PADDING, y=Layout.TOOLBAR_SECOND_ROW_Y)

        # Swatch Button 2
        self.swatch_2_button = ZButton(
            self.color_frame,
            self.swatch_btn_imgs,
            bg=self.swatch2_color,
            fg=Theme.BLACK,
            highlightthickness=0, bd=0,
            command=self.select_swatch2
        )
        self.swatch_2_button.place(x=Layout.color["SWATCH_2_X"], y=Layout.TOOLBAR_SECOND_ROW_Y)

        # Color Picker Button
        self.color_picker_button = ZButton(
            self.color_frame,
            self.color_picker_btn_imgs,
            fg=Theme.BLACK,
            highlightthickness=0, bd=0,
            command=self.change_active_swatch_color
        )
        self.color_picker_button.place(x=Layout.color["PICKER_X"], y=Layout.TOOLBAR_SECOND_ROW_Y)
        
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
        # Add brush style label.
        self.brush_style_label = tk.Label(self.brush_style_frame,
                                          text="Brush Style",
                                          image=self.brush_style_label_img,
                                          compound="center",
                                          bg=Theme.BLACK)
        self.brush_style_label.place(x=Layout.DEFAULT_PADDING,
                                     y=Layout.DEFAULT_PADDING,
                                     width=Layout.brush_style["LABEL_WIDTH"],
                                     height=Layout.brush_style["LABEL_HEIGHT"])
    #-- Add brush style icon.
        self.brush_style_icon = tk.Label(self.brush_style_frame,
                                         image=self.circle_btn_imgs["active"],
                                         bg=Theme.LIGHT_GRAY)
        self.brush_style_icon.place(x=Layout.brush_style["ICON_X"],
                                    y=Layout.brush_style["ICON_Y"],
                                    width=Layout.DEFAULT_BUTTON_SIZE,
                                    height=Layout.DEFAULT_BUTTON_SIZE)
    #-- Add brush style drop down menu.
        self.brush_style_options = ["Circle", "Square", "Triangle", "Star",
                                    "Line 1", "Line 2", "Line 3", "Line 4"]
        self.brush_style_selection = tk.StringVar(self.root)
        self.brush_style_selection.set(self.brush_style_options[0])
        self.brush_style_menu = tk.OptionMenu(self.brush_style_frame,
                                              self.brush_style_selection,
                                              *self.brush_style_options,
                                              command=self.update_brush_style)
        self.brush_style_menu.place(x=Layout.TOOLBAR_PADDING,
                                    y=Layout.TOOLBAR_SECOND_ROW_Y,
                                    width=Layout.brush_style["DROPDOWN_WIDTH"],
                                    height=Layout.brush_style["DROPDOWN_HEIGHT"])

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

        # Add draw shape label.
        self.draw_shape_label = tk.Label(self.draw_shape_frame,
                                    text="Draw Shape",
                                    image=self.draw_shape_label_img,
                                    compound="center",
                                    bg=Theme.BLACK)
        self.draw_shape_label.place(x=Layout.DEFAULT_PADDING,
                                    y=Layout.DEFAULT_PADDING,
                               width=Layout.draw_shape["LABEL_WIDTH"],
                               height=Layout.draw_shape["LABEL_HEIGHT"])
    #-- Add draw shape button.
        self.draw_shape_button = ZButton(self.draw_shape_frame,
                                   self.square_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0,
                                   bg=Theme.LIGHT_GRAY,
                                   command=self.use_draw_shape)
        self.draw_shape_button.place(x=Layout.draw_shape["BUTTON_X"],
                                    y=Layout.draw_shape["BUTTON_Y"],
                                    width=Layout.DEFAULT_BUTTON_SIZE,
                                    height=Layout.DEFAULT_BUTTON_SIZE)
    #-- Add draw shape drop down menu.
        self.draw_shape_options = ["Circle", "Square", "Triangle", "Star"]
        self.draw_shape_selection = tk.StringVar(self.root)
        self.draw_shape_selection.set(self.draw_shape_options[1])
        self.draw_shape_menu = tk.OptionMenu(self.draw_shape_frame,
                                              self.draw_shape_selection,
                                              *self.draw_shape_options,
                                              command=self.select_shape_to_draw)
        self.draw_shape_menu.place(x=Layout.TOOLBAR_PADDING,
                                    y=Layout.TOOLBAR_SECOND_ROW_Y,
                                    width=Layout.draw_shape["DROPDOWN_WIDTH"],
                                    height=Layout.draw_shape["DROPDOWN_HEIGHT"])
        
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
#-------Set up undo and redo buttons using ZButton class - a modified tk.Button class.

        self.undo_button = ZButton(self.undo_redo_frame,
                                   self._undo_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0,
                                   command=self.undo_action)
            
        self.undo_button.place(x=Layout.TOOLBAR_PADDING,
                               y=Layout.TOOLBAR_PADDING)
        # Redo button.
        self.redo_button = ZButton(self.undo_redo_frame,
                                   self._redo_btn_imgs,
                                   fg=Theme.BLACK,
                                   highlightthickness = 0, bd = 0,
                                   command=self.redo_action)
        self.redo_button.place(x=Layout.TOOLBAR_PADDING,
                               y=Layout.TOOLBAR_SECOND_ROW_Y)
        
        # Initialise size variable.
        self._DEFAULT_DRAW_SIZE = 2
        self.draw_size = self._DEFAULT_DRAW_SIZE

        # Initialize tools
        self.shape_tool = ShapeTool(self.canvas)
        self.draw_tool = DrawTool(self.canvas, self.undo_redo, self)
        self.eraser_tool = Eraser(self.canvas)
        self.brush_tool = BrushTool(self.canvas, self)
        print(self.draw_tool)

        
        self.size_scale(self._DEFAULT_DRAW_SIZE)
        # Active Button - Used to teack which tool is active.
        self.active_button = self.pencil_button
        
        
#------ Set up footer and add to main window.
        # Footer may be used in future development for app info and zoom in/out feature.
        self.footer = tk.Frame(self.root, bg=Theme.MID_GRAY)
        self.footer.place(x=Layout.footer["X"],
                          y=Layout.footer["Y"],
                          width=Layout.footer["WIDTH"],
                          height=Layout.footer["HEIGHT"]) 

    def toggle_active_button(self, button_id):
        # Set active button that matches button ID.
        if button_id.lower() == "pencil":
            self.active_button = self.pencil_button
        elif button_id.lower() == "paint":
            self.active_button = self.paint_button
        elif button_id.lower() == "eraser":
            self.active_button = self.eraser_button
        elif button_id.lower() == "shape":
            self.active_button = self.draw_shape_button
        else:
            raise ValueError("Input was not a valid button ID.")
        # Set all tool buttons back to inactive state.
        self.pencil_button.update_state("inactive")
        self.paint_button.update_state("inactive")
        self.eraser_button.update_state("inactive")
        self.draw_shape_button.update_state("inactive")
        # Set active button state to active.
        self.active_button.update_state("active")


    def undo_action(self):
        self.undo_redo.undo(self.canvas)
    
    def redo_action(self):
        self.undo_redo.redo(self.canvas)

    def save_canvas(self):
        self.save_button.update_state("active")
        self.file_manager.save_file(self.root, self.canvas)
        self.save_button.update_state("inactive")

    def load_img_to_canvas(self):
        self.load_button.update_state("active")
        self.canvas_image = self.file_manager.load_image(self.canvas)
        self.canvas.create_image(0, 0, anchor='nw', image=self.canvas_image)
        self.load_button.update_state("inactive")

    def update_brush_style(self, selection):
        self.brush_style_icon.config(image=self.shape_icons_static[selection.lower()])
        self.brush_tool.set_brush_style(selection.lower())
        # Activate the brush tool.
        self.use_paint()

    def select_shape_to_draw(self, selection):
        # Update draw shape button to refelct selected shape.
        self.draw_shape_button.update_image_library(self.shape_icons_button[selection.lower()])
        # Set shape for the shape tool.
        if selection == "Circle":
            self.shape_tool.shape = 'circle'
        elif selection == "Square":
            self.shape_tool.shape = 'square'
        elif selection == "Triangle":
            self.shape_tool.shape = 'triangle'
        elif selection == "Star":
            self.shape_tool.shape = 'star'
        # Activate the shape tool.
        self.use_draw_shape()

    def select_swatch1(self):
        self.active_color = self.swatch1_color
        self.active_swatch = 1
        self.swatch_1_button.update_state("active")
        self.swatch_2_button.update_state("inactive")

    def select_swatch2(self):
        self.active_color = self.swatch2_color
        self.active_swatch = 2
        self.swatch_1_button.update_state("inactive")
        self.swatch_2_button.update_state("active")

    def change_active_swatch_color(self):
        self.color_picker_button.update_state("active")
        new_color = ColorPicker(self.root).get_color()
        self.color_picker_button.update_state("inactive")
        if new_color:
            if self.active_swatch == 1:
                self.swatch1_color = new_color
                self.active_color = new_color
                self.swatch_1_button.config(bg=self.swatch1_color)
                self.swatch_1_button.update("active")
            else:
                self.swatch2_color = new_color
                self.active_color = new_color
                self.swatch_2_button.config(bg=self.swatch2_color)

    def size_scale(self, size):
        # Clear size entry and insert size from the scale slider.
        self.size_entry.delete(0, "end")
        self.size_entry.insert(0, size)
        # set draw size for class.
        self.draw_size = size
        # update size for tools.
        self.update_tool_size(self.draw_size)

    def size_entry_input(self, event):
        # get text from size entry variable and convert to int.
        size = int(self.size_entry_value.get())
        # Set scale slider to match value of size entry.
        self.size_slider.set(size)
        # set draw size for class.
        self.draw_size = size
        # update size for tools.
        self.update_tool_size(size)
        # Return focus to main window (root)
        root.focus()

    # Used for size entry validation to ensure only decimal characters are entered.
    def _size_entry_validation(self, text):
        # Return true/false if text contains only decimal characters.
        return text.isdecimal()
    
    def get_draw_size(self):
        return self.draw_size

    def update_tool_size(self, size):
        self.draw_tool.update_size(size)
        
    
    def use_pencil(self):
        # Toggle pencil button to active state
        self.toggle_active_button("pencil")
        # Change size scale.
        self.size_slider.config(to=self.draw_tool.MAX_SIZE)
        # Re-adjust size scale to match new range.
        self.size_scale(self.draw_size)
        # Set draw size.
        self.draw_tool.update_size(self.draw_size)
        # Activate draw (pencil) tool.
        self.draw_tool.activate()

    def use_paint(self):
        # Toggle paint button to active state
        self.toggle_active_button("paint")
        # Activate brush tool.
        self.brush_tool.activate()
        

    def use_eraser(self):
        # Toggle eraser button to active state
        self.toggle_active_button("eraser")
        # Activate eraser tool.
        self.eraser_tool.activate()

    def use_draw_shape(self):
        # Toggle draw shape button to active state
        self.toggle_active_button("shape")
        # Activate the shape tool.
        self.shape_tool.activate()

    

if __name__ == "__main__":
    root = tk.Tk()
    app = View(root)
    root.mainloop()