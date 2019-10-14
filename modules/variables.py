import pygame as pg

drag = False

# Window variables
wind_width = 1000
wind_height = 800

simWindow = pg.display.set_mode((wind_width, wind_height))
pg.display.set_caption('Simulation')

# Color variables
background = (102, 102, 102)

# Sprites
sp_magnet = pg.image.load('resources/magnet.png')

# Clock variables
clock = pg.time.Clock()
