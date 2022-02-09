class Alien:

    def __init__(self, spawn_pos=(0, 0)):
        self.coords = spawn_pos
    
    def update(self):
        """Abstract"""
        pass

    def move(self, x, y):
        self.coords = (x, y)
    
    def move_relative(self, x, y):
        self.coords = self.coords[0] + x, self.coords[1] + y
