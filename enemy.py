import pygame as p
from global_variables import *
import global_variables as gv
import os
import random
p.init()

class Enemy():
    def __init__(self) -> None:
        self.cacti = []
        self.bird = []
        self.enemyImg = p.image.load('Sprites/Cactus/Cactus_Large_Doube.png')
        self.enemy = self.enemyImg.get_rect()
        self.enemy.y = resolution[1] * 0.7
        self.enemy.x = resolution[0] * 2
        self.randenemy = 0
        self.counter = 0
        self.index = 0
        for file in os.listdir('Sprites/Cactus'):
            self.cacti.append(p.image.load('Sprites/Cactus/' + file))
        for file in os.listdir("Sprites/Bird"):
            self.bird.append(p.image.load("Sprites/Bird/" + file))
    
    def moveEnemy(self):
        self.randenemy = random.randint(0, 1)
        if self.randenemy == 0:
            self.enemyImg = self.cacti[random.randint(0, len(self.cacti) - 1)]
        else:
            self.enemyImg = self.bird[0]
        self.enemy = self.enemyImg.get_rect()
        self.enemy.left = resolution[0] * 2
        if self.randenemy == 0:
            self.enemy.y = resolution[1] * 0.7
        else:
            self.enemy.y = resolution[1] * 0.55
        gv.ding = True
    def update(self):
        # animation
        self.counter += 1
        if self.randenemy == 1 and self.counter % 10 == 0:
            self.enemyImg = self.bird[self.index]
            if self.index == 0:
                self.index += 1
            else:
                self.index -=1
        self.enemy.x -= gv.enemyspeed
        gv.enemyspeed += 0.01
        if self.enemy.right < 0:
            self.moveEnemy()
        display.blit(self.enemyImg, self.enemy)