from pygame import *

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
   def __init__(self, sprt_image, sprt_x = 0, sprt_y = 0, sprt_speed = 0):
       self.image = transform.scale(image.load(sprt_image), (49, 72))
   def rupdate(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 55:
           self.rect.y += self.speed
   def lupdate(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 55:
           self.rect.y += self.speed

back = (0, 70, 0)
win_width = 700
win_height = 600
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

lrackt
rrackt
ball

font.init()
font = SysFont('Arial', 40)
lost = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lost = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))