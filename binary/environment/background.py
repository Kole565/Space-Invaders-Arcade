import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from pygame import image
import pygame


class Background():

    """Represent background image"""

    def __init__(self, path, screen=None):
        self.surface = image.load(path)
        self.screen_surface = screen

        self.coords = (0, 0)
    
    def update(self):
        self.render()
    
    def render(self):
        self.screen_surface.blit(self.surface, self.coords)
        print("Log: Background render")
        