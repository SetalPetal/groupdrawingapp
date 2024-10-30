from tkinter import Button, PhotoImage
from settings.setup import Theme

class ZButton(Button):


    def __init__(self, root, img_library, *args, **kwargs):       
            super().__init__(root, *args, **kwargs)

            # Image dict contains 3 tk.PhotoImage objects - "inactive", "hover" and "active".
            self.img_library = img_library
            # state can be either "inactive" or "active"
            self.state = "inactive"
            # Set button image to "inactive" image.
            self['image'] = self.img_library[self.state]
            # bind events.
            self.bind('<Enter>', self.enter)
            self.bind('<Leave>', self.leave)
        
    def enter(self, event):
        # Change button to "hover" image and text colour to white.
        if self.state != "active":
            self.config(image=self.img_library["hover"])
            self.config(fg=Theme.WHITE)

    def leave(self, event):
        # CHange button to back to current state and text color to black.
        if self.state != "active":
            self.config(image=self.img_library[self.state])
            self.config(fg=Theme.BLACK)

    def update_state(self, state):
        # Raise error if invalid value is provided to change button state to.
        if state != "inactive" and state != "active":
            raise ValueError("Invalid value to change button state. State can only be a string: \"active\" or \"inactive\".")
        # Update state and button image.
        self.state = state
        self.config(image=self.img_library[self.state])
        self.config(fg=Theme.BLACK)

    def update_image_library(self, image_library):
         self.img_library = image_library
         self.config(image=self.img_library[self.state])
