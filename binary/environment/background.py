import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from binary.interfaces.renderable import Renderable


class Background(Renderable):

    """Represent background image"""

    texture_path = "./resource/image/static/test_back.png"

    def __init__(self, screen, texture_path=None):
        self.screen = screen
        if texture_path:
            self.texture_path = texture_path

        self.coords = (0, 0)
        self.size = (screen.get_size())

        Renderable.__init__(self, screen)
    
    def update(self):
        self.render()
        