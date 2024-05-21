import pygame as p
from sys import exit
from dino import *
from floor import Floor
from enemy import Enemy
from text import Text
from global_variables import *
import global_variables as gv
p.init()

clock = p.time.Clock()

player = Dino()
floor = Floor()
enemy = Enemy()
rocket = Rocket()
text = Text("PublicPixel", BLACK, resolution[0] * 0.43, resolution[1] * 0.1)

# music/sound
ding = p.mixer.music.load('Audio/ding.mp3')
p.mixer.music.set_volume(25)
# pause
paused = False
class Run():
    def __init__(self) -> None:
        self.score = 0
        self.saved = False
    def loop(self):
        while paused is False:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    exit()
            display.fill(GREY)
            floor.update()
            player.update()
            enemy.update()
            rocket.update()
            text.draw_text(self.score)
            
            if gv.ding is True:
                p.mixer.music.play(0, 0.8, 200)
                gv.ding = False
            # collision
            if floor.floor.colliderect(player.player.x, player.player.y + player.dy, player.player.width, player.player.height) or \
                floor.floor2.colliderect(player.player.x, player.player.y + player.dy, player.player.width, player.player.height):
                if player.dy >= 0:
                    player.dy = floor.floor.top - player.player.top
                    player.VELY = 0
                    player.onGround = True
            
            if enemy.enemy.colliderect(player.player.x, player.player.y, player.player.width, player.player.height):
                self.dead()
            self.score += 1
            
            p.display.update()
            clock.tick(60)
    def dead(self):
        while True:
            greatest = 0
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    exit()
            with open ('save.txt', 'a') as file:
                if self.saved is False:
                    file.write(str(self.score // 10) + '\n')
                    self.saved = True
            with open('save.txt', 'r') as file:
                for line in file:
                    if int(line) > greatest:
                        greatest = int(line)
            input = p.key.get_pressed()
            if input[p.K_y]:
                self.score = 0
                enemy.enemy.left = resolution[0]
                gv.enemyspeed = 5
                self.saved = False
                self.loop()
            if input[p.K_n]:
                p.quit()
                exit()
            display.fill(GREY)
            display.blit(player.playerImg, player.player)
            display.blit(enemy.enemyImg, enemy.enemy)
            display.blit(floor.floorImg, (floor.floor.x, floor.floor.y - 35))
            display.blit(floor.floorImg, (floor.floor2.x, floor.floor.y - 35))
            text.draw_text(self.score)
            text.draw_normal("Try again? Y/N", resolution[0] * 0.5, resolution[1] * 0.3)
            text.draw_normal("High score: " + str(greatest), resolution[0] * 0.5, resolution[1] * 0.5)
            p.display.update()
            clock.tick(30)
j = Run()
j.loop()