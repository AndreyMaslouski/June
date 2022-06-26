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
        self.num_1.resize(20,50)
        self.num_1.move(5,100)
        # self.num_1.clicked.connect()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())

