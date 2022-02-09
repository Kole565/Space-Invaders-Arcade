from pygame import image
from pygame import transform

from .alien import Alien


class SmallAlien(Alien):

    texture = "./resource/image/dynamic/alliens/small_alien.png"
    size = 25

    def __init__(self, spawn_pos, screen=None):
        Alien.__init__(self, spawn_pos)

        self.screen = screen
        self.init_texture()
    
    def init_texture(self):
        pre_texture = image.load(self.texture)
        x, y = pre_texture.get_size()
        x, y = 2, 1
        size = (self.size * x / y, self.size * y / x)
        
        self.texture = transform.scale(pre_texture, size)
    
    def update(self):
        self.render()
        # self.test_move()
    
    def render(self):
        self.screen.blit(self.texture, self.coords)
        print("Log: SmallAlien render")        
    
    # def test_move(self):
    #     self.move_relative(1, 0)
