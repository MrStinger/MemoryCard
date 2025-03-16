#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,300)

radio_group = QGroupBox('Варианты ответов:')
answer_group  = QGroupBox('Результат Теста:')

lbl_question = QLabel('Вопрос')
rbtn1 = QRadioButton('Ответ 1')
rbtn2 = QRadioButton('Ответ 2')
rbtn3 = QRadioButton('Ответ 3')
rbtn4 = QRadioButton('Ответ 4')
btn_ok = QPushButton('Ответить')
lbl_answer = QLabel('Результат')
lbl_result = QLabel('Верно/Неверно')
lbl_correct = QLabel('Правильный ответ')
lbl_stat = QLabel('Статистика')



ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn1)
ButtonGroup.addButton(rbtn2)
ButtonGroup.addButton(rbtn3)
ButtonGroup.addButton(rbtn4)

answ = [rbtn1, rbtn2, rbtn3, rbtn4]

row1 = QHBoxLayout()
row1.addWidget(rbtn1)
row1.addWidget(rbtn2)
row2 = QHBoxLayout()
row2.addWidget(rbtn3)
row2.addWidget(rbtn4)
col = QVBoxLayout()
col.addLayout(row1)
col.addLayout(row2)

radio_group.setLayout(col)

col1 = QVBoxLayout()
col1.addWidget(lbl_result, alignment=Qt.AlignLeft)
col1.addWidget(lbl_correct, alignment=Qt.AlignCenter)
answer_group.setLayout(col1)
answer_group.hide()
main_layout = QVBoxLayout()
main_layout.setSpacing(15)
main_layout.addWidget(lbl_question, alignment=Qt.AlignCenter, stretch=1)
main_layout.addWidget(radio_group, stretch=2)
main_layout.addWidget(answer_group, stretch=2)
main_layout.addWidget(btn_ok)
main_layout.addWidget(lbl_stat, stretch=2)

main_win.setLayout(main_layout)

main_win.score=0
main_win.total=0

class Question():
    def __init__(self, q, r, w1, w2, w3):
        self.question = q
        self.r_answer = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

question_list = []
Q = Question('Сколько серий в 1 сезоне сериала Кухня?', '20', '15', '30', '100')
question_list.append(Q)
Q = Question('Как называется компания, которая разработала GTA 5?', 'Rockstar', 'Nintendo', 'Supersell', 'Sega')
question_list.append(Q)
Q = Question('В какой игре ужасов игрокам нужно выжить с аниматрониками?', 'FNAF', 'Granny', 'Hello, neigbor', 'Brawl Stars')
question_list.append(Q)
Q = Question('Как звали рыбку шефа в сериале Кухня?', 'Аркадий', 'Михаил', 'Владимир', 'Огузок')
question_list.append(Q)




def ShowResult():
    radio_group.hide()
    answer_group.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    num = randint(0, len(question_list)-1)
    ask(question_list[num])
    answer_group.hide()
    radio_group.show()
    btn_ok.setText('Ответить')
    ButtonGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    ButtonGroup.setExclusive(True)
def start_test():
    if btn_ok.text() == 'Ответить':
        ShowResult()
    else:
        show_question()

def ask(q):
    shuffle(answ)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.r_answer)
    answ[0].setText(q.r_answer)
    answ[1].setText(q.wrong1)
    answ[2].setText(q.wrong2)
    answ[3].setText(q.wrong3)
    main_win.total+=1

def check_answer():
    if btn_ok.text() == 'Ответить':
        if answ[0].isChecked():
            lbl_result.setText('Верно!')
            main_win.score+=1
        else:
            lbl_result.setText('Неверно!')
        ShowResult()
        lbl_stat.setText('статистика:\nВсего вопросов: '+str(main_win.total)+'\nПравильных ответов: '+str(main_win.score)+'\nРейтинг: '+str(main_win.score/main_win.total*100))
    else:
        show_question()
    

num = randint(0, len(question_list)-1)
ask(question_list[num])


btn_ok.clicked.connect(check_answer)




main_win.show()
app.exec_()
