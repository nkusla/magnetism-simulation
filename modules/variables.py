import pygame

# Window variables
wind_width = 1000
wind_height = 800

simWindow = pygame.display.set_mode((wind_width, wind_height))
pygame.display.set_caption('Simulation')

# Color variables
background = (102, 102, 102)

# Sprites
sp_magnet = pygame.image.load('resources/magnet.png')
sp_coil = pygame.image.load('resources/coil.png')

# Clock variables
clock = pygame.time.Clock()
