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
    def __init__(self, name, sprite, x, y, B = 5, field_visible = False):
        Object.__init__(self, name, sprite, x, y)
        self.B = B
        self.field_visible = field_visible
        
    def draw_magnetic_field(self):
        ellipse_width = 330
        ellipse_height = 60
        rect = pygame.Rect(0, 0, ellipse_width, ellipse_height)
        rect.midbottom = self.rect.center
        x = rect.x
        y = rect.y

        j = 0
        for _ in range(0, self.B):
            pygame.draw.ellipse(
                v.simWindow, 
                v.magnetic_field_color,
                pygame.Rect(x, y-j, ellipse_width, ellipse_height+j), 3)
            j += 10

        j = 0
        for _ in range(0, self.B):
            pygame.draw.ellipse(
                v.simWindow, 
                v.magnetic_field_color, 
                pygame.Rect(x, y+ellipse_height, ellipse_width, ellipse_height+j), 3)
            j += 10

    def show_magnetic_field(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            if self.field_visible:
                self.field_visible = False
            elif not self.field_visible:
                self.field_visible = True
        

