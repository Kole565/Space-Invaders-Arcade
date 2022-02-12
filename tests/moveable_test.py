import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

import pygame
from binary.interfaces.moveable import Moveable, MoveableByInput


class TestMoveable(unittest.TestCase):

    def setUp(self):
        self.moveable = Moveable()

    def test_create(self):
        self.assertTrue(self.moveable)
    
    def test_init_coords(self):
        self.assertEqual(self.moveable.coords, (0, 0))

    def test_init_direction(self):
        self.assertEqual(self.moveable.direction, (0, 0))
    
    def test_transform_position(self):
        self.moveable.transform_position(100, 100)

        self.assertEqual(self.moveable.coords, (100, 100))
    
    def test_move_relative(self):
        self.moveable.move_relative(5, 15)

        self.assertEqual(self.moveable.coords, (5, 15))
    
    def test_move_by_direction(self):
        self.moveable.direction = (1, 1)
        self.moveable.move_by_direction()

        self.assertEqual(self.moveable.coords, (1, 1))
    
    def test_move_by_direction_with_speed(self):
        self.moveable.direction = (1, 1)
        self.moveable.horizontal_speed = 100
        self.moveable.vertical_speed = 100

        self.moveable.move_by_direction()

        self.assertEqual(self.moveable.coords, (100, 100))
        

class TestMoveableByInput(TestMoveable):

    def setUp(self):
        pygame.init()
        self.moveable = MoveableByInput()
    
    def test_move(self):
        self.moveable.move()
        