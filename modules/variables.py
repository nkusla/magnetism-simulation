import pygame

# Window variables
wind_width = 1200
wind_height = 800

simWindow = pygame.display.set_mode((wind_width, wind_height))
pygame.display.set_caption('Simulation')

# Color variables
background = (102, 102, 102)
magnetic_field_color = (97, 189, 194)
coil_color = (184, 115, 51)

# Other variables
field_width = 330
field_height = 60
field_lines_thickness = 2

coil_width = 50
coil_height = 120
coil_min_height = 95
coil_max_height = 200
coil_spacing = 16
coil_thickness = 5

# Sprites
sp_magnet = pygame.image.load('resources/magnet.png')
sp_coil = pygame.image.load('resources/coil.png')

# Clock variable
clock = pygame.time.Clock()
