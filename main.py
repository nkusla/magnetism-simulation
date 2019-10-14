import modules.variables as v
import modules.functions as f
import pygame as pg

magnet = f.Object('magnet', v.sp_magnet, v.sp_magnet.get_rect().size, 375, 375)

while True:
    v.simWindow.fill(v.background)
    f.draw_object(magnet)

    for event in pg.event.get():
        if (event.type == pg.MOUSEBUTTONDOWN and f.obj_clicked(magnet, event.pos)) or v.drag:
            v.drag = True
            if event.type == pg.MOUSEMOTION:
                f.move_obj(magnet, event.pos)
            if event.type == pg.MOUSEBUTTONUP:
                v.drag = False
    
    pg.display.update()
    v.clock.tick(60)