from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys


class Calculator (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setGeometry(300,300,225,370)
        self.setWindowTitle("Калькулятор")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(225,95)
        self.move(0,0)

        self.num_1 = QPushButton('1',self)
        self.num_1.resize(50,50)
        self.num_1.move(5,100)
        # self.num_1.clicked.connect()

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 100)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 100)

        self.div = QPushButton('/', self)
        self.div.resize(50,50)
        self.div.move(170,100)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 155)
        # self.num_1.clicked.connect()

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 155)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 155)

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 155)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 210)
        # self.num_1.clicked.connect()

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 210)


        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 210)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(5, 265)

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(60, 265)

        self.step = QPushButton('^', self)
        self.step.resize(50, 50)
        self.step.move(115, 265)

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(170, 265)

        self.ravn = QPushButton('=', self)
        self.ravn.resize(150, 50)
        self.ravn.move(5, 320)

        self.c = QPushButton('C', self)
        self.c.resize(50, 50)
        self.c.move(170, 320)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())

