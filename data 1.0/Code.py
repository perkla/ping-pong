#модули
from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
#МЕНЮ НАСТРОЕК
#приложение
app = QApplication([])
#кнопка для перехода к игре
btn_tg = QPushButton('К игре') 
#надпись сверху и описание тем и уровней сложности
lb_title = QLabel('Настройки темы и сложности')
lb_themediscr = QLabel('Описание темы:')
lb_difdiscr = QLabel('Описание сложности:') 
#4 кнопки
rbtn_1 = QRadioButton('Классика')
rbtn_2 = QRadioButton('Аркада')
rbtn_3 = QRadioButton('Легко')
rbtn_4 = QRadioButton('Тяжело')
#2 группы кнопок (программно)
RadioGroup1 = QButtonGroup() 
RadioGroup1.addButton(rbtn_1)
RadioGroup1.addButton(rbtn_2)
RadioGroup2 = QButtonGroup() 
RadioGroup2.addButton(rbtn_3)
RadioGroup2.addButton(rbtn_4)
#нанизывание кнопок
layout_thm = QHBoxLayout()
layout_dif = QHBoxLayout()
layout_thm.addWidget(rbtn_1)
layout_thm.addWidget(rbtn_2)
layout_dif.addWidget(rbtn_3)
layout_dif.addWidget(rbtn_4)
#2 группы кнопок (визуально)
ThemeGroupBox = QGroupBox("Тема:") 
DifGroupBox = QGroupBox("Уровень сложности:")
ThemeGroupBox.setLayout(layout_thm)
DifGroupBox.setLayout(layout_dif)
#создание облика программы (ч.1)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()
layout_line5 = QHBoxLayout()
layout_line6 = QHBoxLayout()
#создание облика программы (ч.2)
layout_line1.addWidget(lb_title)
layout_line2.addWidget(ThemeGroupBox)
layout_line3.addWidget(DifGroupBox)
layout_line4.addWidget(lb_themediscr)
layout_line5.addWidget(lb_difdiscr)
layout_line6.addStretch(1)
layout_line6.addWidget(btn_tg, stretch=2)
layout_line6.addStretch(1)
#создание облика программы (ч.3)
layout_ult = QVBoxLayout()
layout_ult.addLayout(layout_line1, stretch=2)
layout_ult.addLayout(layout_line2, stretch=4)
layout_ult.addLayout(layout_line3, stretch=4)
layout_ult.addStretch(1)
layout_ult.addLayout(layout_line4)
layout_ult.addStretch(1)
layout_ult.addLayout(layout_line5)
layout_ult.addStretch(3)
layout_ult.addLayout(layout_line6, stretch=1)
layout_ult.addStretch(1)
layout_ult.setSpacing(5)
#переменные для игры
theme = None
dif = None
#функции для кнопок
def classtheme(lb):
        lb.setText('Описание темы: "Классическая тема. Черный фон, белые мяч, ракетки, границы и сообщение о проигрыше. Звуки из настольного пинг-понга."')
def arctheme(lb):
        lb.setText('Описание темы: "Аркадная тема. Черный фон с зеленоватым оттенком, лаймовые мяч, ракетки, границы и сообщение о проигрыше. Звуки пинг-понга заменены на аркадные."')
def easdif(lb):
        lb.setText('Описание сложности: "Легкий уровень сложности. Мяч большой и медленный. Ракетки медленные, но легко управляются."')
def hardif(lb):
        lb.setText('Описание сложности: "Тяжелый уровень сложности. Мяч маленький, а скорость увеличивается с каждым 3 касанием ракетки. Ракетки быстрые, но трудно управляются."')
def check_options():
        global theme
        global dif
        if rbtn_1.isChecked() and rbtn_3.isChecked():
                theme = 1
                dif = 1
                app.exit()
        elif rbtn_1.isChecked() and rbtn_4.isChecked():
                theme = 1
                dif = 2
                app.exit()
        elif rbtn_2.isChecked() and rbtn_3.isChecked():
                theme = 2
                dif = 1
                app.exit()
        elif rbtn_2.isChecked() and rbtn_4.isChecked():
                theme = 2
                dif = 2
                app.exit()
#окно настроек
win = QWidget()       
win.resize(950, 200) 
win.setWindowTitle('Настройки "Ping-Pong"')
win.setLayout(layout_ult)
#привязка кнопок к функциям
btn_tg.clicked.connect(check_options) 
rbtn_1.clicked.connect(lambda: classtheme(lb_themediscr))
rbtn_2.clicked.connect(lambda: arctheme(lb_themediscr))
rbtn_3.clicked.connect(lambda: easdif(lb_difdiscr))
rbtn_4.clicked.connect(lambda: hardif(lb_difdiscr))
#окончание меню
win.show()
app.exec()
#ИГРА
#переменные, выбранные ранее
if theme == 1:
    racktim = 'classracket.png'
    ballim = 'classball.png'
    back = 'classback.jpg'
    wbls = 'classwallball.ogg'
    rbls = 'classracketball.ogg'
    txtcolor = (255, 255, 255)
elif theme == 2:
    racktim = 'arcracket.png'
    ballim = 'arcball.png'
    back = 'arcback.jpg'
    wbls = 'arcwallball.ogg'
    rbls = 'arcracketball.ogg'
    txtcolor = (0, 255, 0)
if dif == 1:
    dcpl = 0
    ballsize = 50
    ballwall = 65
    rackspeed = 4
elif dif == 2:
    dcpl = 0.25
    ballsize = 30
    ballwall = 45
    rackspeed = 20
#переменные без выбора и флаги
win_width = 700
win_height = 600
difcof = 1
dcpl = 0.25
dcplreg = 0
game = True
finish = False
clock = time.Clock()
FPS = 60
#окно игры
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load(back), (win_width, win_height))
#звуки
mixer.init()
wallballsnd = mixer.Sound(wbls)
racketballsnd = mixer.Sound(rbls)
#надписи
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (txtcolor))
lose2 = font.render('PLAYER 2 LOSE!', True, (txtcolor))
#классы
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
        global finish
        global difcof
        global dcplreg
        dcplreg += 1
        self.rect.x += self.xspeed * difcof
        self.rect.y += self.yspeed * difcof
        if sprite.collide_rect(lck, self) or sprite.collide_rect(rck, self):
            racketballsnd.play()
            self.xspeed *= -1
            if dcplreg % 3 == 0:
                difcof += dcpl
        if self.rect.y > win_height - ballwall or self.rect.y < 15:
            wallballsnd.play()
            self.yspeed *= -1
        if self.rect.x < 0:
            finish = True
            window.blit(lose1, (100, 200))
        if self.rect.x > win_width:
            finish = True
            window.blit(lose2, (400, 200))
#создание объектов
lrackt = Player(racktim, 30, 200, rackspeed, 30, 150)
rrackt = Player(racktim, 620, 200, rackspeed, 30, 150)
ball = Ball(ballim, 200, 200, 4, ballsize, ballsize)
#игровой цикл
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