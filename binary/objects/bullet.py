from binary.interfaces.moveable import Moveable
from binary.interfaces.renderable import Renderable

import pygame


class Bullet(Moveable, Renderable):

    texture_path = "./resource/image/dynamic/yellow_bullet.png"
    size = (5, 20)

    vertical_speed = 2
    horizontal_speed = 0

    def __init__(self, spawn_pos=(0, 0), screen=None):
        Moveable.__init__(self, spawn_pos)
        Renderable.__init__(self, screen)

        self.set_start_direction()

    def set_start_direction(self):
        self.direction = [0, -1]
    
    def update(self):
        self.moving()
        self.render()
    
    def moving(self):
        self.move_by_direction()
