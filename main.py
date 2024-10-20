import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Window")

# Set the window size
root.geometry("400x300")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Create a button widget
button = tk.Button(root, text="Click Me", font=("Arial", 14), command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)

# Run the application
root.mainloop()
