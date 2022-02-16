import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from binary.objects.ship import Ship
from pygame import display


class TestShip(unittest.TestCase):

    def setUp(self):
        screen = display.set_mode((100, 100))
        self.ship = Ship(screen)

    def test_create(self):
        self.assertTrue(self.ship)
    
    def test_update(self):
        self.ship.update()
        