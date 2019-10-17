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

    def draw_magnetic_field(self):
        rect = pygame.Rect(400, 420, 330, 60)
        rect.midbottom = self.rect.center
        x = rect.x
        y = rect.y
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y, 330, 60), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 10, 330, 70), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 20, 330, 80), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 30, 330, 90), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 40, 330, 100), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 50, 330, 110), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 60, 330, 120), 3)
        # pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 70, 330, 130), 3)
        # pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 80, 330, 140), 3)
        # pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y - 90, 330, 150), 3)

        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 60), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 70), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 80), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 90), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 100), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 110), 3)
        pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 120), 3)
        # pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 130), 3)
        # pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 140), 3)
        # pygame.draw.ellipse(v.simWindow, v.magnetic_field_color, pygame.Rect(x, y + 60, 330, 150), 3)
