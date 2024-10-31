class BrushSize:
    def __init__(self, initial_size=2):
        self.size = initial_size
        self.callbacks = []

    def set_size(self, new_size):
        self.size = new_size
        for callback in self.callbacks:
            callback(new_size)

    def get_size(self):
        return self.size

    def register_callback(self, callback):
        self.callbacks.append(callback)
