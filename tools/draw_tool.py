def draw_tool(canvas):
    def start_draw(event):
       #Starting canvas position
        canvas.old_x, canvas.old_y = event.x, event.y

    def draw(event):
        #Create a line from the old position to the new position
        x, y = event.x, event.y
        if canvas.old_x and canvas.old_y:
            # Draw line from old coordinates to the new coordinates
            canvas.create_line(canvas.old_x, canvas.old_y, x, y, fill="black", width=2)
            # Update the coordinates
            canvas.old_x, canvas.old_y = x, y

    # Clear the coordinates on mouse release
    def end_draw(event):
        canvas.old_x, canvas.old_y = None, None

    # User events bindings
    canvas.bind("<Button-1>", start_draw)       
    canvas.bind("<B1-Motion>", draw)            
    canvas.bind("<ButtonRelease-1>", end_draw)  
