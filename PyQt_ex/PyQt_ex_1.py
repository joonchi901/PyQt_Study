import sys

from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt_test')
        self.setGeometry(300, 300, 480, 250)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyApp()
    sys.exit(app.exec_())