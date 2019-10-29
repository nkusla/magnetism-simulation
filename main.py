import modules.variables as v
import modules.functions as f
import pygame

magnet = f.Magnet('magnet', 375, 375, v.sp_magnet)
coil = f.Coil('coil', 200, 200, 2)

while True:
    v.simWindow.fill(v.background)
    coil.draw()
    magnet.draw_magnetic_field()
    magnet.draw()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and magnet.is_collided_with_mouse(event.pos):
            magnet.drag = True
        elif event.type == pygame.MOUSEMOTION and magnet.drag:
            magnet.move(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            magnet.drag = False
        elif event.type == pygame.QUIT:
            exit()

        magnet.show_magnetic_field(event)
        
    pygame.display.update()
    v.clock.tick(60)