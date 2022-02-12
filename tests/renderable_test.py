import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from pygame import display
from binary.interfaces.renderable import Renderable


class TestRenderable(unittest.TestCase):

    def setUp(self):
        screen = display.set_mode((100, 100))
        self.renderable = TestObject(screen)

    def test_create(self):
        self.assertTrue(self.renderable)
    
    def test_render(self):
        self.renderable.render()


class TestObject(Renderable):

    size = (10, 10)
    coords = (0, 0)

    def __init__(self, screen):
        Renderable.__init__(self, screen)
