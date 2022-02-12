import pygame


class Moveable:

    def __init__(self, spawn_pos=(0, 0)):
        self.coords = spawn_pos

        self.direction = (0, 0)
        self.horizontal_speed = getattr(self, "horizontal_speed", 1)
        self.vertical_speed = getattr(self, "vertical_speed", 1)

    def transform_position(self, x, y):
        self.coords = (x, y)
    
    def move_relative(self, x, y):
        self.transform_position(self.coords[0] + x, self.coords[1] + y)
    
    def move_by_direction(self):
        self.move_relative(self.direction[0] * self.horizontal_speed,
                           self.direction[1] * self.vertical_speed)
        

class MoveableByInput(Moveable):

    def move(self):
        self.set_direction()
        self.move_by_direction()
    
    def set_direction(self):
        x = y = 0 
        keys = self.get_keys()
        if keys[pygame.K_UP]:
            y = -1
        if keys[pygame.K_DOWN]:
            y = 1
        if keys[pygame.K_LEFT]:
            x = -1
        if keys[pygame.K_RIGHT]:
            x = 1
        
        self.direction = (x, y)
    
    def get_keys(self):
        return pygame.key.get_pressed()
