from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)

app = QApplication([])

btn_tg = QPushButton('К игре') 

lb_title = QLabel('Настройки темы и сложности')
lb_themediscr = QLabel('Описание темы:')
lb_difdiscr = QLabel('Описание сложности:')

ThemeGroupBox = QGroupBox("Тема:") 
DifGroupBox = QGroupBox("Уровень сложности:") 
 
rbtn_1 = QRadioButton('Классика')
rbtn_2 = QRadioButton('Аркада')
rbtn_3 = QRadioButton('Легко')
rbtn_4 = QRadioButton('Тяжело')

RadioGroup1 = QButtonGroup() 
RadioGroup1.addButton(rbtn_1)
RadioGroup1.addButton(rbtn_2)
RadioGroup2 = QButtonGroup() 
RadioGroup2.addButton(rbtn_3)
RadioGroup2.addButton(rbtn_4)

layout_thm = QHBoxLayout()
layout_dif = QHBoxLayout()
layout_thm.addWidget(rbtn_1)
layout_thm.addWidget(rbtn_2)
layout_dif.addWidget(rbtn_3)
layout_dif.addWidget(rbtn_4)

ThemeGroupBox.setLayout(layout_thm)
DifGroupBox.setLayout(layout_dif)

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()
layout_line5 = QHBoxLayout()
layout_line6 = QHBoxLayout()

layout_line1.addWidget(lb_title, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(ThemeGroupBox)
layout_line3.addWidget(DifGroupBox)
layout_line4.addWidget(lb_themediscr)
layout_line5.addWidget(lb_difdiscr)
layout_line6.addStretch(1)
layout_line6.addWidget(btn_tg, stretch=2)
layout_line6.addStretch(1)

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

theme = None
dif = None
meny = True

def classtheme(lb):
        lb.setText('Описание темы: "Классическая тема. Черный фон, белые мяч, ракетки, границы и сообщение о проигрыше. Звуки из настольного пинг-понга."')

def arctheme(lb):
        lb.setText('Описание темы: "Аркадная тема. Черный фон с зеленоватым оттенком, лаймовые мяч, ракетки, границы и сообщение о проигрыше. Звуки пинг-понга заменены на аркадные."')

def easdif(lb):
        lb.setText('Описание сложности: "Легкий уровень сложности. Мяч большой и медленный. Ракетки медленные, но легко управляются."')

def hardif(lb):
        lb.setText('Описание сложности: "Тяжелый уровень сложности. Мяч маленький, а скорость увеличивается с каждым 3 касанием ракетки. Ракетки быстрые, но трудно управляются."')

def check_options():
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
    

win = QWidget()       
win.resize(950, 200) 
win.setWindowTitle('Настройки "Ping-Pong"')
win.setLayout(layout_ult)

btn_tg.clicked.connect(check_options) 
rbtn_1.clicked.connect(lambda: classtheme(lb_themediscr))
rbtn_2.clicked.connect(lambda: arctheme(lb_themediscr))
rbtn_3.clicked.connect(lambda: easdif(lb_difdiscr))
rbtn_4.clicked.connect(lambda: hardif(lb_difdiscr))

win.show()
app.exec()