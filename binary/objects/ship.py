from binary.interfaces.moveable import MoveableByInput
from binary.interfaces.renderable import Renderable
from binary.objects.gun import BulletGun


class Ship(MoveableByInput, Renderable):

    texture_path = "./resource/image/dynamic/ship/ship.png"
    size = (50, 50)

    vertical_speed = 2
    horizontal_speed = 2

    def __init__(self, spawn_pos=(0, 0), screen=None):
        MoveableByInput.__init__(self, spawn_pos)
        Renderable.__init__(self, screen)

        self.gun = BulletGun(screen, self)

    def update(self):
        self.move()
        self.render()

        self.gun.update()
        