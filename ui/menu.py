import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QSplitter, QLabel, QLineEdit, QHBoxLayout, \
    QPushButton, QComboBox


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.cd = QPushButton("Начать сбор данных", self.frame)
        self.cd.clicked.connect(self.start_work)
        font = QFont()
        font.setPointSize(15)
        self.cd.setFont(font)
        self.cd.resize(420, 40)
        self.cd.move(30, 40)

        self.ad = QPushButton("Выход", self.frame)
        self.ad.clicked.connect(self.close)
        font = QFont()
        font.setPointSize(15)
        self.ad.setFont(font)
        self.ad.resize(400, 40)
        self.ad.move(40, 265)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.frame)

        self.setLayout(hbox)
        self.close()

    def start_work(self):
        from ui import worker
        global ex
        self.close()
        ex = worker.MainWindow()
        ex.setGeometry(1000, 1000, 670, 600)
        ex.setWindowTitle('TradesCollector')
        ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.setGeometry(1000, 1000, 1000, 600)
    ex.setFixedSize(500, 350)
    ex.setWindowTitle('TradesCollector')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    ex.show()
    sys.exit(app.exec_())
