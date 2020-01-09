import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from design import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        qp.setBrush(QColor(red, green, blue))
        radius = randint(10, 200)
        qp.drawEllipse(210 - radius // 2, 160 - radius // 2, radius, radius)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())