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
    def __init__(self, name, sprite, x, y, B = 3):
        Object.__init__(self, name, sprite, x, y)
        self.B = B
        
    def draw_magnetic_field(self):
        ellipse_width = 60
        ellipse_height = 330
        rect = pygame.Rect(0, 0, ellipse_height, ellipse_width)
        rect.midbottom = self.rect.center
        x = rect.x
        y = rect.y

        j = 0
        for i in range(0, self.B):
            pygame.draw.ellipse(
                v.simWindow, 
                v.magnetic_field_color,
                pygame.Rect(x, y-j, ellipse_height, ellipse_width+j), 3)
            j += 10

        j = 0
        for i in range(0, self.B):
            pygame.draw.ellipse(
                v.simWindow, 
                v.magnetic_field_color, 
                pygame.Rect(x, y+ellipse_width, ellipse_height, ellipse_width+j), 3)
            j += 10

