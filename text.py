import pygame as p
from global_variables import *

class Text():
    def __init__(self, font, text_col, x, y) -> None:
        self.text = ""
        if font == 'Arial':
            self.font = p.font.SysFont("Arial", 30)
        if font == 'PublicPixel':
            self.font = p.font.Font('PublicPixel.ttf', 30)
        self.text_col = text_col
        self.x = x
        self.y = y
    def draw_text(self, score):
        self.text = "Score " + str(score // 10)
        img = self.font.render(self.text, True, self.text_col)
        display.blit(img, (self.x - 50, self.y))
    def draw_normal(self, msg: str, x: float, y: float) -> None:
        self.text = msg
        img = self.font.render(self.text, True, self.text_col)
        imgRect = img.get_rect(center = (x, y))
        display.blit(img, imgRect)