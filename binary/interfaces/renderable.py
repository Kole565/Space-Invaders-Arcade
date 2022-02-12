from pygame import image, transform


class Renderable:

    texture_default_path = "./resource/image/static/missing_texture.png"

    def __init__(self, screen):
        self.screen = screen

        self.init_image_surface()

    def init_image_surface(self):
        surface = self.try_get_image_if_none_return_default()
        
        self.surface = transform.scale(surface, self.size)
    
    def try_get_image_if_none_return_default(self):
        try:
            surface = image.load(self.texture_path)
        except (FileNotFoundError, AttributeError):
            surface = image.load(self.texture_default_path)
        
        return surface

    def render(self):
        self.screen.blit(self.surface, self.coords)
        