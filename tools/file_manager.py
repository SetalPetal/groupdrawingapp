from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageGrab
import pyautogui

"""
Class requires pillow module and pyautogui module.
To install pillow:
In VS Code, go to 'View' > Terminal
In the terminal run "pip3 install pillow"
To install pyautogui :
In VS Code, go to 'View' > Terminal
In the terminal run "pip3 install pyautogui"

"""
class FileManager:

    def __init__(self):

        # Specifies file types that can be saved and opened using file dialog.
        self.FILE_TYPES = (('Portable Network Graphic file', '.png'),
                           ('Joint Photographic Experts Group file', '.jpg'),
                           ('Joint Photographic Experts Group file', '.jpeg'),
                           ('Bitmap file', '.bmp'))
        
        # Used to crop canvas when saving drawing
        # self.CROP_OFFSET = 3

    
    def save_file(self, window, canvas):
        # Save function had issues with cropping the screen with Image.grab()
        # This appears to have been fixed by using pyautogui.screenshot()
        
        # get coordinates for canvas top left
        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        # Get coordinates for canvas bottom right.
        x1 = canvas.winfo_width()
        y1=canvas.winfo_height()

        # Screen grab the image.
        img = pyautogui.screenshot(region=(x, y, x1, y1))

        # Get file name with dialog window.
        file_name = filedialog.asksaveasfilename(title="Save Drawing",
                                                 confirmoverwrite=True,
                                                 defaultextension='.png',
                                                 filetypes=self.FILE_TYPES)

        # Only try to save file if a file name was generated.
        if file_name != '':
            # If saving as a jpeg file, convert image to RGB mode.
            # This will allow for the image to be saved as jpeg.
            # if file_name.endswith('jpeg') or file_name.endswith('jpg'):
            #     # Convert the image to RBG image.
            #     img = img.convert('RGB')
            # Save img.
            img.save(file_name)
            # Show message file was saved.
            messagebox.showinfo('File Save', 'File saved!')
        else:
            # Show message file was not saved.
            messagebox.showwarning('File Save', 'File not saved!')

    def load_image(self, canvas):
        # Opens a dialog for user to select file to load.
        image_file = filedialog.askopenfile(title="Open an Image",
                                            filetypes=self.FILE_TYPES)
        # If filedialog was closed before submitting a file, image_file will be empty
        # return if image_file is empty, to prevent errors.
        if image_file == "":
            # Show message file was not loaded.
            messagebox.showwarning('Load Image', 'No image was loaded!')
            return
        # Load image_file into a PIL.Image object
        image = Image.open(image_file.name)
        # Resize image if overlaps canvas.
        image = self.__fit_image_to_canvas(image, canvas)
        # Convert image to a tkinter compatible image object.
        tk_image = ImageTk.PhotoImage(image)
        return tk_image

    def __fit_image_to_canvas(self, image, canvas):
        """
        Detect if image overlaps canvas and resizes the image to fit into the canvas while maintaining image aspect ratio.

        Parameters:
                image (PIL.Image object): Image to to check and resize.
                canvas (tkinter.canvas object): Container that wil hold the image.

        Returns:
                image (PIL.Image object): Resized image or unchanged.
        """
        # Get Canvas Dimensions
        CANVAS_WIDTH = canvas.winfo_width()
        CANVAS_HEIGHT = canvas.winfo_height()
        # Will be used to modify image dimensions
        multiplier = 1

        # get difference between image and canvas dimensions
        x_difference = image.width - CANVAS_WIDTH
        y_difference = image.height - CANVAS_HEIGHT

        # If image width is longer than canvas width, and if image width is longer than image height, \
        # set multiplier proportional to canvas width / image width.
        if x_difference > 0 and x_difference > y_difference:
            multiplier = CANVAS_WIDTH / image.width
            print(f"PASS 01\n X DIF: {x_difference}, Y DIF: {y_difference}")
        # If image height is longer than canvas height, and if image height is longer than image width, \
        # set multiplier proportional to canvas height / image height.
        elif y_difference > 0 and y_difference > x_difference:
            multiplier = CANVAS_HEIGHT / image.height
            print(f"PASS 02\n X DIF: {x_difference}, Y DIF: {y_difference}")
        # If image width longer than canvas width, and if image width is equal to image height, \
        # set multiplier proportional to canvas width / image width.
        elif x_difference > 0 and x_difference == y_difference:
            multiplier = CANVAS_WIDTH / image.width
            print(f"PASS 03\n X DIF: {x_difference}, Y DIF: {y_difference}")
        # Set new lenghts for image dimensions based on multiplier.
        new_width = int(image.width * multiplier)
        new_height = int(image.height * multiplier)
        # Resize image to fit with the canvas.
        image = image.resize((new_width, new_height))

        return image