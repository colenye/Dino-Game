from __future__ import annotations
import pygame as p
from global_variables import *

class Background:
    def __init__(self) -> None:
        self.backgroundImg = p.transform.scale(p.image.load("Sprites/background.jpg"), resolution)
        self.rect = self.backgroundImg.get_rect()
    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = 0
        display.blit(self.backgroundImg, (self.rect.x, self.rect.y))
        display.blit(self.backgroundImg, (self.rect.x + resolution[0], self.rect.y))