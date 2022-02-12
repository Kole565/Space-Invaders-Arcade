import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from binary.objects.small_alien import SmallAlien
from pygame import display


class TestSmallAlien(unittest.TestCase):

    def setUp(self):
        screen = display.set_mode((100, 100))
        self.alien = SmallAlien((0, 0), screen)
    
    def test_borders(self):
        left = 0
        right = display.get_surface().get_size()[0]

        self.assertEqual(self.alien.left_border, left)
        self.assertEqual(self.alien.right_border, right)
    
    def test_direction_and_aim(self):
        self.assertEqual(self.alien.direction, [1, 0])
        self.assertLess(100000, self.alien.vertical_aim)

    def test_create(self):
        self.assertTrue(self.alien)
    
    def test_update(self):
        self.alien.update()
        