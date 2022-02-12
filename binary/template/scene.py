import sys

import pygame


class Scene:

    """Container for updateable objects on screen"""
    
    def __init__(self, screen=None, environment=[], objects=[], gui=[]):
        self.screen = screen
        
        self.environment = environment
        self.objects = objects
        self.gui = gui

    def update(self):
        events = pygame.event.get()
        self.exit_check(events)
        
        self.update_environment()
        self.update_objects()
        self.update_gui()

        self.update_screen()
    
    def exit_check(self, events):
        """Exit game by input"""
        for event in events:
            if (event.type == pygame.QUIT or
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.exit()
    
    def exit(self):
        pygame.quit()
        sys.exit()
    
    def update_environment(self):
        self.update_list(self.environment)
    
    def update_objects(self):
        self.update_list(self.objects)
    
    def update_gui(self):
        self.update_list(self.gui)

    def update_screen(self):
        pygame.display.update()
    
    def update_list(self, list):
        for updateable in list:
            updateable.update()
            