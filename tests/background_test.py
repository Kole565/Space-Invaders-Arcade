import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from binary.environment.background import Background
from pygame import display


class TestBackground(unittest.TestCase):

    def setUp(self):
        screen = display.set_mode((100, 100))
        self.back = Background(screen)

    def test_image_load(self):
        self.assertTrue(self.back.surface)
    
    def test_image_safe_load(self):
        screen = display.set_mode((100, 100))
        try:
            back = Background(screen, "./resource/image/static/miss.error")
        except:
            self.fail()
        else:
            pass
    
    def test_with_texture_path(self):
        screen = display.set_mode((100, 100))
        back = Background(screen, "./resource/image/static/test_back.png")
    
    def test_update(self):
        self.back.update()
        