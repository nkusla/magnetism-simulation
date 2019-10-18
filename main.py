import modules.variables as v
import modules.functions as f
import pygame

magnet = f.Magnet('magnet', v.sp_magnet, 375, 375)
#coil = f.Object('coil', v.sp_coil, 200, 200)

while True:
    v.simWindow.fill(v.background)
    #coil.draw()
    magnet.B = 10
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
    
    pygame.display.update()
    v.clock.tick(60)