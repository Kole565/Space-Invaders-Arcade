class Collisionable:

    def __init__(self, screen):
        self.rect = self.surface.get_rect()
    
    def collision_check(self, collisionables):
        copy = collisionables[:]
        if self in copy:
            copy.remove(self)

        for object in copy:
            if self.rect.colliderect(object.rect):
                print("{1} collide with {0}".format(self, object))
