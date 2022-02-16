from binary.interfaces.moveable import Moveable
from binary.interfaces.renderable import Renderable
from binary.objects.bullet import Bullet

import pygame
from time import time


class Gun(Moveable):

    def __init__(self, screen, parent):
        self.screen = screen
        self.parent = parent

        Moveable.__init__(self)

        self.last_shoot = time()
        self.set_mount_offset()

    def set_mount_offset(self):
        offset = [0, 0]
        offset[0] = self.parent.size[0] / 2

        self.mount_offset = offset

    def update(self):
        self.moving()

    def moving(self):
        x = self.parent.coords[0] + self.mount_offset[0]
        y = self.parent.coords[1] + self.mount_offset[1]

        self.coords = (x, y)
        
    def shooting(self):
        """Abstract"""
    
    def is_can_shoot(self):
        if time() - self.last_shoot > self.shoot_delay:
            return True
    
    def shoot(self):
        self.last_shoot = time()


class UserGun(Gun):

    def update(self):
        super().update()

        self.shooting()

    def shooting(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.is_can_shoot():
            self.shoot()


class BulletGun(UserGun):

    shoot_delay = 0.25

    def __init__(self, screen, parent):
        super().__init__(screen, parent)

        self.bullets = []
    
    def update(self):
        super().update()

        self.update_bullets()
    
    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
    
    def shoot(self):
        super().shoot()

        self.bullets.append(Bullet(self.screen, self.coords))
        