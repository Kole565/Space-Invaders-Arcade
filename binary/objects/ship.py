from binary.interfaces.moveable import MoveableByInput
from binary.interfaces.renderable import Renderable
from binary.interfaces.collisionable import Collisionable
from binary.objects.gun import BulletGun


class Ship(MoveableByInput, Renderable, Collisionable):

    texture_path = "./resource/image/dynamic/ship/ship.png"
    size = (50, 50)

    vertical_speed = 1
    horizontal_speed = 1

    def __init__(self, screen, spawn_pos=(0, 0)):
        Renderable.__init__(self, screen)
        MoveableByInput.__init__(self, spawn_pos)
        Collisionable.__init__(self, screen)

    def update(self):
        self.move()
        self.render()


class Attacker(Ship):
    
    size = (30, 30)

    vertical_speed = 2
    horizontal_speed = 2

    def __init__(self, screen, spawn_pos=(0, 0)):
        super().__init__(screen, spawn_pos)

        self.gun = BulletGun(screen, self)

    def update(self):
        super().update()

        self.gun.update()
    
    def collision_check(self, objects):
        self.gun.collision_check(objects)
        