from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QButtonGroup, QRadioButton)
from random import randint

app = QApplication([])
Group = QButtonGroup()
DifGroup = QButtonGroup()

gamePBUTN = QPushButton('К игре') 
classRBUTN = QRadioButton('Классика')
arcadeRBUTN = QRadioButton('Аркада')

racktim = 'arcracket.png'
ballim = 'arcball.png'
back = 'arcback.jpg'
wbls = 'arcwallball.ogg'
rbls = 'arcracketball.ogg'

txtcolor = (0, 255, 0)
win_width = 700
win_height = 600

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
background = transform.scale(image.load(back), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
wallballsnd = mixer.Sound(wbls)
racketballsnd = mixer.Sound(rbls)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (txtcolor))
lose2 = font.render('PLAYER 2 LOSE!', True, (txtcolor))

class GameSprite(sprite.Sprite):
   def __init__(self, sprt_image, sprt_x, sprt_y, sprt_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(sprt_image), (wight, height))
       self.speed = sprt_speed
       self.rect = self.image.get_rect()
       self.rect.x = sprt_x
       self.rect.y = sprt_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def rupdate(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 30:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 180:
           self.rect.y += self.speed
   def lupdate(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 30:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 180:
           self.rect.y += self.speed

class Ball(sprite.Sprite):
    def __init__(self, sprt_image, sprt_x, sprt_y, sprt_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(sprt_image), (wight, height))
        self.yspeed = sprt_speed
        self.xspeed = sprt_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprt_x
        self.rect.y = sprt_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def bubdate(self, lck, rck):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if sprite.collide_rect(lck, self) or sprite.collide_rect(rck, self):
            racketballsnd.play()
            self.xspeed *= -1
        if ball.rect.y > win_height-45 or ball.rect.y < 15:
            wallballsnd.play()
            self.yspeed *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (100, 200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (400, 200))
            game_over = True

lrackt = Player(racktim, 30, 200, 4, 30, 150)
rrackt = Player(racktim, 620, 200, 4, 30, 150)
ball = Ball(ballim, 200, 200, 4, 30, 30)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        lrackt.lupdate()
        rrackt.rupdate()
        ball.bubdate(lrackt, rrackt)

        lrackt.reset()
        rrackt.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)