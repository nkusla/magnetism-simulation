import pygame as pg
if __name__ != '__main__':
    import modules.variables as v
else:
    import variables as v

class Object:
    def __init__(self, name, sprite, resolution, x, y):
        self.name = name
        self.sprite = sprite
        self.resolution = resolution
        self.x = x
        self.y = y
        
def draw_object(obj):
    v.simWindow.blit(obj.sprite, (obj.x, obj.y))

def obj_clicked(obj, mouse_pos):
    if mouse_pos[0] >= obj.x and mouse_pos[0] <= obj.resolution[0] + obj.x:
        if mouse_pos[1] >= obj.y and mouse_pos[1] <= obj.resolution[1] + obj.y:
            return True
        else:
            return False
    else:
        return False

def move_obj(obj, pos):
    obj.x =+ pos[0]
    obj.y =+ pos[1]
    return obj