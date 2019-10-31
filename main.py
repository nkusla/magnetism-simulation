import modules.variables as v
import modules.classes as c
import pygame

magnet = c.Magnet('magnet', 450, 500, v.sp_magnet)
coil = c.Coil('coil', 300, 280, 20)

while True:
    v.simWindow.fill(v.background)
    coil.draw_lightbulb()
    coil.draw_first_half()
    magnet.draw_magnetic_field()
    magnet.draw()
    coil.draw_second_half()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and magnet.is_collided_with_mouse(event.pos):
            magnet.drag = True
        elif event.type == pygame.MOUSEMOTION and magnet.drag:
            magnet.relative_move(coil.rectunion, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            magnet.drag = False
        elif event.type == pygame.QUIT:
            exit()

        magnet.show_magnetic_field(event)
        magnet.change_magnet_features(event)
        coil.change_coil_features(event)
        
    v.write_author_name(v.simWindow)
    pygame.display.update()
    v.clock.tick(60)