from global_variables import *
import pygame as p
import global_variables as gv


class Floor():
    def __init__(self) -> None:
        self.floorImg = p.image.load('Sprites/Ground.png')
        self.floorImg = self.floorImg.subsurface((0, 50, 2400, 46))
        self.floor = self.floorImg.get_rect()
        self.floor2 = self.floorImg.get_rect()
        self.floor2.x += 2400
        self.floor.y = resolution[1] * 0.8 + 30
        self.floor2.y = resolution[1] * 0.8 + 30
    def update(self):
        self.floor.x -= gv.enemyspeed
        self.floor2.x -= gv.enemyspeed
        if self.floor.right <= 0:
            self.floor.left = 2400
        if self.floor2.right <= 0:
            self.floor2.left = 2400
        display.blit(self.floorImg, (self.floor.x, self.floor.y - 35))
        display.blit(self.floorImg, (self.floor2.x, self.floor.y - 35))