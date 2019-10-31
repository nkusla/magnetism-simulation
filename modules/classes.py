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
        self.inside_coil = False
        
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
    
    def check_inside_coil(self, coil_rect):
        case_1 = coil_rect.collidepoint(self.rect.topleft) and coil_rect.collidepoint(self.rect.bottomleft)
        case_2 = coil_rect.collidepoint(self.rect.topright) and coil_rect.collidepoint(self.rect.bottomright)
        if case_1 or case_2:
            self.inside_coil = True

        if not coil_rect.colliderect(self.rect):
            self.inside_coil = False
        
    def relative_move(self, coil_rect, pos):
        self.check_inside_coil(coil_rect)

        if not self.inside_coil:
            case_1 = (pos[1] - self.rect.height/2) >= coil_rect.bottom
            case_2 = (pos[1] + self.rect.height/2) <= coil_rect.top
            case_3 = self.rect.left > coil_rect.right
            case_4 = self.rect.right < coil_rect.left
            if (case_1 or case_2) or (case_3 or case_4):
                self.move(pos)
            else:
                pom_x = self.rect.centerx
                pom_y = self.rect.centery
                self.move(pos)
                if coil_rect.colliderect(self.rect):
                    self.move((pom_x, pom_y))
                    self.drag = False
        else:
            case_1 = (pos[1] + self.rect.height/2) <= coil_rect.bottom - 3
            case_2 = (pos[1] - self.rect.height/2) >= coil_rect.top + 3
            if case_1 and case_2:
                self.move(pos)
            else:
                self.drag = False

    def change_magnet_features(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if self.B > v.induction_min:
                    self.B -= 1 
            elif event.key == pygame.K_w:
                if self.B < v.induction_max:
                    self.B += 1


class Coil(Object):
    def __init__(self, name, x, y, num_coils = 10):
        super().__init__(name, x, y, size = [v.coil_width, v.coil_height])
        self.coil_color = v.coil_color
        self.num_coils = num_coils
        self.coils_list = []
        self.save_coils_rect()
        self.rectunion = None
        self.get_rectunion()

    def save_coils_rect(self):
        self.coils_list = []
        for _ in range(self.num_coils):
            coil_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            self.coils_list.append(coil_rect)
            self.rect.x += v.coil_spacing
        
        self.rect.x -= self.num_coils * v.coil_spacing
    
    def get_rectunion(self):
        rectunion_width = self.coils_list[-1].topright[0] - self.rect.x
        rectunion = pygame.Rect(self.rect.x, self.rect.y, rectunion_width, self.rect.height)
        self.rectunion = rectunion

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

    def draw_lightbulb(self):
        start_pos = self.rectunion.midleft
        end_pos = [self.rectunion.left, self.rectunion.y - v.coil_line_lenght]
        pygame.draw.line(v.simWindow, v.coil_color, start_pos, end_pos, v.coil_thickness-2)

        start_pos = self.rectunion.midright
        end_pos[0] = self.rectunion.right
        pygame.draw.line(v.simWindow, v.coil_color, start_pos, end_pos, v.coil_thickness-2)

        start_pos = [self.rectunion.left, self.rectunion.y - v.coil_line_lenght]
        pygame.draw.line(v.simWindow, v.coil_color, start_pos, end_pos, v.coil_thickness-2)

        circle_center = [self.rectunion.centerx, self.rectunion.y - v.coil_line_lenght]
        pygame.draw.circle(v.simWindow, v.lightbulb_color, circle_center, v.lightbulb_radius)

        pygame.draw.circle(v.simWindow, (79, 88, 89), circle_center, v.lightbulb_radius, 4)

    def change_coil_features(self, event):        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.rect.height >= v.coil_min_height:
                    self.rect.height -= 5
            elif event.key == pygame.K_DOWN:
                if self.rect.height <= v.coil_max_height:
                    self.rect.height += 5
            elif event.key == pygame.K_LEFT:
                if self.num_coils > v.coil_min_num:
                    self.num_coils -= 1
            elif event.key == pygame.K_RIGHT:
                if self.num_coils < v.coil_max_num:
                    self.num_coils += 1

        self.save_coils_rect()
        self.get_rectunion()
    