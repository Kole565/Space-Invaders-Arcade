class Collisionable:

    def __init__(self, screen):
        print("__init__ from {:s}".format(self.__class__.__name__))
        self.rect = self.surface.get_rect()
    
    def collision_check(self, list):
        # print(list)
        pass
        # for collisionable in list:
        #     for other in list:
        #         if collisionable.rect.colliderect(other):
        #             print("{:} collide with {:}".format(collisionable, other))
