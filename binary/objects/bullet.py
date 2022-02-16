from binary.interfaces.moveable import Moveable
from binary.interfaces.renderable import Renderable
from binary.interfaces.collisionable import Collisionable

import pygame


class Bullet(Moveable, Renderable, Collisionable):

    texture_path = "./resource/image/dynamic/yellow_bullet.png"
    size = (5, 20)

    vertical_speed = 2
    horizontal_speed = 0

    def __init__(self, screen, spawn_pos=(0, 0)):
        Moveable.__init__(self, spawn_pos)
        Renderable.__init__(self, screen)
        Collisionable.__init__(self, screen)

        self.set_start_direction()

    def set_start_direction(self):
        self.direction = [0, -1]
    
    def update(self):
        self.moving()
        self.render()
    
    def moving(self):
        self.move_by_direction()
    
    def collision_check(self, objects):
        if self in objects:
            objects.remove(self)

        for object in objects:
            if self.rect.colliderect(object.rect):
                print("{1} collide with {0}".format(self, object))
            
