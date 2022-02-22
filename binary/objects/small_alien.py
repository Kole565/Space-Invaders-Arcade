from binary.interfaces.moveable import Moveable
from binary.interfaces.renderable import Renderable
from binary.interfaces.collisionable import Collisionable


class SmallAlien(Moveable, Renderable, Collisionable):

    texture_path = "./resource/image/dynamic/SmallAlien.png"
    size = (40, 40)
    rotation = 180

    vertical_speed = 1
    horizontal_speed = 1
    row_step = 20

    def __init__(self, screen, spawn_pos=(0, 0)):
        Moveable.__init__(self, spawn_pos)
        Renderable.__init__(self, screen)
        Collisionable.__init__(self, screen)

        self.set_borders(0, screen.get_width())
        self.set_start_direction_and_aim()
    
    def collision_check(self, collisionables):
        pass
    
    def set_borders(self, left, right):
        self.left_border = left
        self.right_border = right
    
    def set_start_direction_and_aim(self):
        self.direction = [1, 0]
        self.vertical_aim = 9**9

    def update(self):
        self.moving()
        self.render()
    
    def moving(self):
        self.set_direction()
        self.move_by_direction()
    
    def set_direction(self):
        if self.direction[0] != 0 and self.is_beyond_horizontal_borders():
            self.set_down_direction()
            self.set_vertical_aim()
        
        elif self.is_beyond_vertical_aim():
            self.set_left_or_right_direction_by_distance()
            self.set_vertical_aim()
    
    def is_beyond_horizontal_borders(self):
        if self.is_beyond_left_border() or self.is_beyond_right_border():
            return True
    
    def is_beyond_right_border(self):
        if self.coords[0] >= self.right_border - self.size[0]:
            return True
    
    def is_beyond_left_border(self):
        if self.coords[0] <= self.left_border:
            return True
    
    def is_beyond_vertical_aim(self):
        if self.coords[1] >= self.vertical_aim:
            return True
    
    def set_down_direction(self):
        self.direction[0] = 0
        self.direction[1] = 1
    
    def set_left_or_right_direction_by_distance(self):
        if (abs(self.coords[0] - self.left_border) <
            abs(self.coords[0] - self.right_border)):
            self.direction[0] = 1
        else:
            self.direction[0] = -1

        self.direction[1] = 0
    
    def set_vertical_aim(self):
        self.vertical_aim = self.coords[1] + self.row_step
        