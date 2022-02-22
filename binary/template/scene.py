import sys

import pygame


class Scene:

    """Contain, update objects on screen"""

    collision_tick_speed = 200 # TODO: Rewrite to time using
    
    def __init__(self, screen, environment=[], objects=[], gui=[]):
        self.screen = screen
        
        self.environment = environment
        self.objects = objects
        self.gui = gui

        self.events = []

        self.collision_tick = 0

    def update(self):
        self.exit_check()
        
        self.update_environment()
        self.update_objects()
        self.update_gui()

        self.update_screen()
    
    def exit_check(self):
        """Exit game by input"""
        events = pygame.event.get()
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
        self.collision_check(self.objects)
    
    def update_gui(self):
        self.update_list(self.gui)

    def update_screen(self):
        pygame.display.update()
    
    def update_list(self, list):
        for updateable in list:
            updateable.update()
    
    def collision_check(self, objects):
        if self.is_can_check_collision():
            for collisionable in objects:
                collisionable.collision_check(objects)
    
    def is_can_check_collision(self):
        return True
            