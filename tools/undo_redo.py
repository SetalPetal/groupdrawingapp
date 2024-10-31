class UndoRedo:
    def __init__(self):
        self.undo_stack = []  #stack for undo actions
        self.redo_stack = []  #stack for redo actions
        self.current_group = []  #temporary stack for action group
        self.is_recording = False

    #recreate different tool shapes
    def _recreate_shape(self, canvas, action):
        if action['type'] == 'line':
            return canvas.create_line(
                action['coords'][0], action['coords'][1],
                action['coords'][2], action['coords'][3],
                fill=action['fill'],
                width=action['width']
            )
        elif action['type'] == 'oval':
            return canvas.create_oval(
                action['coords'][0], action['coords'][1],
                action['coords'][2], action['coords'][3],
                fill=action['fill'],
                outline=action['outline']
            )
        elif action['type'] == 'rectangle':
            return canvas.create_rectangle(
                action['coords'][0], action['coords'][1],
                action['coords'][2], action['coords'][3],
                fill=action['fill'],
                outline=action['outline']
            )
        elif action['type'] == 'polygon':
            return canvas.create_polygon(
                action['points'],
                fill=action['fill'],
                outline=action['outline']
            )
        
    #start recording actions
    def start_group(self):
        self.is_recording = True
        self.current_group = []
    
    #end recording actions
    def end_group(self):
        """End recording and save the group"""
        if self.current_group:  #only add group if it contains actions
            self.undo_stack.append({
                'type': 'group',
                'actions': self.current_group
            })
            self.redo_stack.clear()
        self.current_group = []
        self.is_recording = False
    
    def add_action(self, action):
        if self.is_recording:
            self.current_group.append(action)
        else:
            self.undo_stack.append(action)
            self.redo_stack.clear()
    
    def undo(self, canvas):
        if not self.undo_stack:
            return
            
        action = self.undo_stack.pop()
        
        if action['type'] == 'group':
            for sub_action in reversed(action['actions']):
                canvas.delete(sub_action['id'])
            self.redo_stack.append(action)
        else:
            canvas.delete(action['id'])
            self.redo_stack.append(action)
    
    def redo(self, canvas):
        if not self.redo_stack:
            return
            
        action = self.redo_stack.pop()
        
        if action['type'] == 'group':
            #recreate group 
            new_group = []
            for sub_action in action['actions']:
                new_id = self._recreate_shape(canvas, sub_action)
                new_action = sub_action.copy()
                new_action['id'] = new_id
                new_group.append(new_action)
            self.undo_stack.append({
                'type': 'group',
                'actions': new_group
            })
        else:
            #single action
            new_id = self._recreate_shape(canvas, action)
            new_action = action.copy()
            new_action['id'] = new_id
            self.undo_stack.append(new_action)

    