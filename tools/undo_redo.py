class UndoRedo:
    def __init__(self):
        self.undo_stack = []  # Stack for undo actions
        self.redo_stack = []  # Stack for redo actions
        self.current_group = []  # Temporary storage for current action group
        self.is_recording = False
    
    def start_group(self):
        """Start recording a group of actions"""
        self.is_recording = True
        self.current_group = []
    
    def end_group(self):
        """End recording and save the group"""
        if self.current_group:  # Only add group if it contains actions
            self.undo_stack.append({
                'type': 'group',
                'actions': self.current_group
            })
            self.redo_stack.clear()
        self.current_group = []
        self.is_recording = False
    
    def add_action(self, action):
        """Add an action, either to current group or as standalone"""
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
            # Handle group of actions
            for sub_action in reversed(action['actions']):
                canvas.delete(sub_action['id'])
            self.redo_stack.append(action)
        else:
            # Handle single action
            canvas.delete(action['id'])
            self.redo_stack.append(action)
    
    def redo(self, canvas):
        if not self.redo_stack:
            return
            
        action = self.redo_stack.pop()
        
        if action['type'] == 'group':
            # Recreate group of actions
            new_group = []
            for sub_action in action['actions']:
                new_id = canvas.create_line(
                    sub_action['coords'][0],
                    sub_action['coords'][1],
                    sub_action['coords'][2],
                    sub_action['coords'][3],
                    fill=sub_action['fill'],
                    width=sub_action['width']
                )
                new_group.append({
                    'type': 'line',
                    'id': new_id,
                    'coords': sub_action['coords'],
                    'fill': sub_action['fill'],
                    'width': sub_action['width']
                })
            self.undo_stack.append({
                'type': 'group',
                'actions': new_group
            })
        else:
            # Recreate single action
            new_id = canvas.create_line(
                action['coords'][0],
                action['coords'][1],
                action['coords'][2],
                action['coords'][3],
                fill=action['fill'],
                width=action['width']
            )
            self.undo_stack.append({
                'type': action['type'],
                'id': new_id,
                'coords': action['coords'],
                'fill': action['fill'],
                'width': action['width']
            })
