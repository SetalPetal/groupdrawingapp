from tkinter import messagebox, filedialog
from PIL import Image, ImageGrab
import os

"""
Class requires pillow module.
To install pillow:
In VS Code, go to 'View' > Terminal
In the terminal run "pip3 install pillow"

"""
class FileManager:

    def save_file(self, window, widget):
        
        # Set up rectangle dimensions for ImageGrab
        # Update main window to make sure current info is applied when \
        # getting dimensional info.
        window.update()
        # Needing to crop the ImageGrab rectangle by 3 pixels each side, \
        # as was capturing window border.
        # (this was happening on mac OS, not sure if required for Windows).
        CROP_OFFSET = 3
        # Set point dimensions for ImageGrab rectangle.
        # x and y = top left point of rectangle.
        # x1 and y1 = bottom right point of rectangle.
        x = widget.winfo_rootx() + CROP_OFFSET
        y = widget.winfo_rooty() + CROP_OFFSET
        x1 = x + widget.winfo_width() - (CROP_OFFSET * 2)
        y1 = y + widget.winfo_height() - (CROP_OFFSET * 2)
        # Screen grab the image.
        img = ImageGrab.grab((x, y, x1, y1))

        # Get file name with dialog window.
        file_name = filedialog.asksaveasfilename(confirmoverwrite=True,
                                               defaultextension='.png',
                                               filetypes=[
                                                   ('Portable Network Graphic file', '.png'),
                                                   ('Joint Photographic Experts Group file', '.jpg'),
                                                   ('Joint Photographic Experts Group file', '.jpeg'),
                                                   ('Bitmap file', '.bmp')
                                                ])

        # Only try to save file if a file name was generated.
        if file_name != '':
            # If saving as a jpeg file, convert image to RGB mode.
            # This will allow for the image to be saved as jpeg.
            if file_name.endswith('jpeg') or file_name.endswith('jpg'):
                # Convert the image to RBG image.
                img = img.convert('RGB')
            # Save img.
            img.save(file_name)
            # Show message file was saved.
            messagebox.showinfo('File Save', 'File saved!')
        else:
            # Show message file was not saved.
            messagebox.showwarning('File Save', 'File not saved!')

    def load_image(self, canvas):

        image_file = filedialog.askopenfile(defaultextension='.png',
                                            filetypes=[
                                                ('Portable Network Graphic file', '.png'),
                                                ('Joint Photographic Experts Group file', '.jpg'),
                                                ('Joint Photographic Experts Group file', '.jpeg'),
                                                ('Bitmap file', '.bmp')
                                            ])