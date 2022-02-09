import pygame


class Scene:

    """Container for environment, objects and gui on screen"""
    
    def __init__(self, screen=None, environment=[], objects=[], gui=[]):
        self.screen = screen
        
        self.environment = environment
        self.objects = objects
        self.gui = gui

    def update(self):
        self.update_environment()
        self.update_objects()
        self.update_gui()

        self.update_screen()
        print("Log: update")
    
    def update_environment(self):
        self.update_list(self.environment)
        print("Log: update_environment")
    
    def update_objects(self):
        self.update_list(self.objects)
        print("Log: update_objects")
    
    def update_gui(self):
        self.update_list(self.gui)
        print("Log: update_gui")

    def update_screen(self):
        pygame.display.update()
        print("Log: update_screen")
    
    def update_list(self, list):
        for updateable in list:
            updateable.update()    
