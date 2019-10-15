import pygame
if __name__ != '__main__':
    import modules.variables as v
else:
    import variables as v

class Object:
    def __init__(self, name, sprite, x, y):
        self.name = name
        self.sprite = sprite

        sprite_size = sprite.get_rect().size
        self.rect = pygame.Rect(x, y, sprite_size[0], sprite_size[1])
        
def draw_object(obj):
    v.simWindow.blit(obj.sprite, (obj.rect.x, obj.rect.y))

def obj_clicked(obj, mouse_pos):
    if obj.rect.collidepoint(mouse_pos):
        return True
    else:
        return False

def move_obj(obj, pos):
    obj.rect.centerx =+ pos[0]
    obj.rect.centery =+ pos[1]
    return obj