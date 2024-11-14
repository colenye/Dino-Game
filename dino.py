from __future__ import annotations
import pygame as p
from global_variables import *

class Gun:
    """
    abstract class do not instantiate directly
    """
    def __init__(self) -> None:
        super().__init__()
    def shoot(self):
        pass
    def update(self):
        pass

class HugeRocket(Gun):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = p.transform.scale(p.image.load('Sprites/HugeRocket.png'), (100, 100))
class Rocket(Gun):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = p.transform.scale(p.image.load('Sprites/rocketlauncher.png'), (100, 100))

class Bullet:
    def __init__(self, pos: p.rect) -> None:
        self.bulsprite = p.transform.scale(p.image.load('Sprites/bullet.png'), (50, 50))
        self.bulpos = self.bulsprite.get_rect()
        self.bulpos.y = pos + 20
        self.bulpos.x += 100

class RocketBullet:
    def __init__(self, pos: p.rect) -> None:
        self.bulsprite = p.transform.scale(p.image.load('Sprites/BulletBill.png'), (75, 75))
        self.bulpos = self.bulsprite.get_rect()
        self.bulpos.y = pos + 20
        self.bulpos.x += 100

class Dino():
    def __init__(self) -> None:
        self.playerRun = []
        self.playerIdle = p.image.load('Sprites/Dino_Idle.png')
        self.playerImg = self.playerIdle
        for num in range(1, 3):
            self.playerRun.append(p.image.load(f'Sprites/dinorun{num}.png'))
        self.player = self.playerIdle.get_rect()
        self.player.x += 30
        self.player.y += 300
        self.dy = 0
        self.dx = 0
        self.VELY = 0
        self.onGround = False
        self.halved = False
        self.counter = 0
        self.index = 0
        self.gun = Rocket()
        self.gunType = "Rocket"
        self.bullets = []
    def update(self):
        self.dy = 0
        self.dx = 0
        self.counter += 1
        if self.counter % 10 == 0:
            self.playerImg = self.playerRun[self.index]
            if self.index == 0:
                self.index += 1
            else:
                self.index = 0
        # gravity
        if self.VELY < 10:
            self.VELY += GRAVITY
        # movement
        input = p.key.get_pressed()
        mouse = p.mouse.get_pressed()
        if input[p.K_UP] and self.onGround is True:
            self.VELY = -JUMPSTRENGTH
            self.onGround = False
        if input[p.K_DOWN] and self.onGround is True and self.halved is False:
            self.player = p.Rect(self.player.x, self.player.y + PLAYERHEIGHT / 2, PLAYERWIDTH, PLAYERHEIGHT)
            self.halved = True
        if not input[p.K_DOWN] and self.halved is True:
            self.player = p.Rect(self.player.x, self.player.y - PLAYERHEIGHT / 2, PLAYERWIDTH, PLAYERHEIGHT)
            self.halved = False
        if input[p.K_DOWN] and self.onGround is False:
            self.VELY += FALLSTRENGTH
        if input[p.K_2]:
            self.bullets = []
            self.gunType = "HugeRocket"
        if input[p.K_1]:
            self.bullets = []
            self.gunType = "Rocket"
        if mouse[0] and self.gunType == "Rocket":
            self.gun = Rocket()
            newbul = Bullet(self.player.y)
            self.bullets.append((newbul.bulsprite, newbul.bulpos))
        elif mouse[0] and self.gunType == "HugeRocket":
            self.gun = HugeRocket()
            newbul = RocketBullet(self.player.y)
            self.bullets.append((newbul.bulsprite, newbul.bulpos))
        self.dy += self.VELY
        self.player.x += self.dx
        self.player.y += self.dy
        
        # drawing
        display.blit(self.playerImg, self.player)
        display.blit(self.gun.sprite, (self.player.x, self.player.y))
        for bul in self.bullets:
            display.blit(bul[0], bul[1])
            bul[1].x += BULSPEED
        self.gun.update()