import modules.variables as v
import modules.functions as f
import pygame

magnet = f.Object('magnet', v.sp_magnet, 375, 375)

while True:
    v.simWindow.fill(v.background)
    f.draw_object(magnet)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and f.obj_clicked(magnet, event.pos):
            v.drag = True
        elif event.type == pygame.MOUSEMOTION and v.drag:
            f.move_obj(magnet, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            v.drag = False
        elif event.type == pygame.QUIT:
            exit()
    
    pygame.display.update()
    v.clock.tick(60)