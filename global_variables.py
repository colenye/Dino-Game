import pygame
pygame.init()

resolution = (1280, 720)
display = pygame.display.set_mode(resolution)
FLOOR = (0, resolution[1] * 0.6, resolution[0], 200)
PLAYERHEIGHT = 100
PLAYERWIDTH = 50
ENEMYWIDTH = 50
ENEMYHEIGHT = 50
enemyspeed = 5
GRAVITY = 0.3
JUMPSTRENGTH = 10
FALLSTRENGTH = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
BULSPEED = 25
ding = False