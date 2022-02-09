import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from binary.objects.alien import Alien


class TestAlien(unittest.TestCase):

    spawn_pos = (50, 50)

    def setUp(self):
        self.alien = Alien(self.spawn_pos)

    def test_create(self):
        self.assertTrue(self.alien)
    
    def test_init_coords(self):
        self.assertEqual(self.alien.coords, self.spawn_pos)
    
    def test_update_abstract(self):
        self.alien.update()
    
    def test_move(self):
        self.alien.move(100, 100)

        self.assertEqual(self.alien.coords, (100, 100))
    
    def test_move_relative(self):
        self.alien.move(10, 10)
        self.alien.move_relative(5, 15)

        self.assertEqual(self.alien.coords, (15, 25))
        