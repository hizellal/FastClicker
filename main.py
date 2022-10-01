from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

#Додаток
app = QApplication([])
#Вікно
window = QWidget()

window.setWindowTitle("Назва вікна")
#І так зрозуміло
window.resize(400, 200)
#Переміщення вікна
window.move(500, 200)

#Створення віджетів

lb_text1 = QLabel("Дізнайтеся переможця")
lb_text2 = QLabel("?")
btn_clicktocheck = QPushButton("Натисни")

#Розташування віджетів

v_line = QVBoxLayout()
v_line.addWidget(lb_text1, alignment = Qt.AlignCenter)
v_line.addWidget(lb_text2, alignment = Qt.AlignCenter)
v_line.addWidget(btn_clicktocheck, alignment = Qt.AlignCenter)

window.setLayout(v_line)

def random_win():
    rand_win = randint(1, 100)
    lb_text1.setText("Переможець:")
    lb_text2.setText(f'{randint(1, 100)}')

btn_clicktocheck.clicked.connect(random_win)






#Щоб показувалось
window.show()
#Щоб не закривалось
app.exec_()