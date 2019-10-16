import pygame
if __name__ != '__main__':
    import modules.variables as v
else:
    import variables as v

class Object:
    def __init__(self, name, sprite, x, y, drag = False):
        self.name = name
        self.sprite = sprite

        sprite_size = sprite.get_rect().size
        self.rect = pygame.Rect(x, y, sprite_size[0], sprite_size[1])
        self.drag = drag
        
    def draw(self):
        v.simWindow.blit(self.sprite, (self.rect.x, self.rect.y))

    def is_collided_with_mouse(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def move(self, pos):
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

class Magnet(Object):
    def __init__(self, name, sprite, x, y):
        Object.__init__(self, name, sprite, x, y)
        magnetic_field = []