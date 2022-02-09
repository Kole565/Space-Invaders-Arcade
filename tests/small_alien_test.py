import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from binary.objects.small_alien import SmallAlien

from pygame import display


class TestSmallAlien(unittest.TestCase):

    spawn_pos = (50, 50)

    def setUp(self):
        screen = display.set_mode((400, 400))
        self.alien = SmallAlien(self.spawn_pos, screen)

    def test_create(self):
        self.assertTrue(self.alien)
    
    def test_update(self):
        self.alien.update()
    
    def test_render(self):
        self.alien.render()
        