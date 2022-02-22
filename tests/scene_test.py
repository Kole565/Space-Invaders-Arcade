import os
import sys
import time

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

import unittest

from binary.environment.background import Background
from binary.template.scene import Scene
from pygame import display


class TestScene(unittest.TestCase):
    
    """Provide tests for scene"""

    def setUp(self):
        screen = display.set_mode((100, 100))        
        back = Background(screen)
        ship = TestObject(screen)
        alien = TestObject(screen)
        some_gui = TestObject(screen)
        
        self.scene = Scene(screen, [back], [ship, alien], [some_gui])

    def test_create(self):
        self.assertTrue(self.scene)
    
    def test_containment(self):
        self.assertTrue(self.scene.environment)
        self.assertTrue(self.scene.objects)
        self.assertTrue(self.scene.gui)
    
    def test_update(self):
        self.scene.update()
    
    def test_update_environment(self):
        self.scene.update_environment()
    
    def test_update_objects(self):
        self.scene.update_objects()
    
    def test_update_gui(self):
        self.scene.update_gui()
    
    def test_update_screen(self):
        self.scene.update_screen()
    
    def test_update_list(self):
        self.scene.update_list([TestObject()])
    
    def test_exit_check(self):
        self.scene.exit_check()
    
    def test_exit(self):
        try:
            self.scene.exit()
        except SystemExit:
            pass
        else:
            self.fail()


class TestObject:

    def __init__(self, screen=None):
        self.screen = screen
    
    def update(self):
        pass

    def collision_check(self, objects):
        pass
    