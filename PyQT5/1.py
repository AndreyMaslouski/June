from PyQt5.QtWidgets import QWidget, QApplication
import sys

class Calculator (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setGeometry(300,300,225,370)
        self.setWindowTitle("Калькулятор")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())

