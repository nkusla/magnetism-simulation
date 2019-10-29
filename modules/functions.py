import pygame
from math import pi
if __name__ != '__main__':
    import modules.variables as v
else:
    import variables as v

class Object:
    def __init__(self, name, x, y, sprite = None, size = None, drag = False):
        self.name = name
        if sprite != None:
            self.sprite = sprite
            sprite_size = sprite.get_rect().size
            self.rect = pygame.Rect(x, y, sprite_size[0], sprite_size[1])
        elif sprite == None and size != None:
            self.rect = pygame.Rect(x, y, size[0], size[1])
        else:
            self.x = x
            self.y = y

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
    def __init__(self, name, x, y, sprite, B = 5, field_visible = False):
        super().__init__(name, x, y, sprite = sprite)
        self.B = B
        self.field_visible = field_visible
        
    def draw_magnetic_field(self):
        if self.field_visible:
            ellipse_width = v.field_width
            ellipse_height = v.field_height
            rect = pygame.Rect(0, 0, ellipse_width, ellipse_height)
            rect.midbottom = self.rect.center
            x = rect.x
            y = rect.y

            j = 0
            for _ in range(0, self.B):
                pygame.draw.ellipse(
                    v.simWindow, 
                    v.magnetic_field_color,
                    pygame.Rect(x, y-j, ellipse_width, ellipse_height+j), v.field_lines_thickness)
                j += 10

            j = 0
            for _ in range(0, self.B):
                pygame.draw.ellipse(
                    v.simWindow, 
                    v.magnetic_field_color, 
                    pygame.Rect(x, y+ellipse_height, ellipse_width, ellipse_height+j), v.field_lines_thickness)
                j += 10

    def show_magnetic_field(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            if self.field_visible:
                self.field_visible = False
            elif not self.field_visible:
                self.field_visible = True
        
class Coil(Object):
    def __init__(self, name, x, y, num_coils = 10):
        super().__init__(name, x, y, size = [v.coil_width, v.coil_height])
        self.coil_color = v.coil_color
        self.num_coils = num_coils
        self.coils_list = []
        self.save_coils_rect()

    def save_coils_rect(self):
        for _ in range(self.num_coils):
            coil_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            self.coils_list.append(coil_rect)
            self.rect.x += v.coil_spacing
        
        self.rect.x -= self.num_coils * v.coil_spacing

    def draw_first_half(self):
        for i in range(self.num_coils):
            pygame.draw.arc(v.simWindow, v.coil_color, 
                self.coils_list[i], 
                pi/2, 3/2*pi,
                v.coil_thickness)

    def draw_second_half(self):
        for i in range(self.num_coils):
            pygame.draw.arc(v.simWindow, v.coil_color, 
                self.coils_list[i], 
                3/2*pi, pi/2,
                v.coil_thickness)
