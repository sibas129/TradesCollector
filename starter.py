import pandas
import bs4
import sys
from main.adxParser import adxPareser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.worker import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setGeometry(300, 500, 650, 500)
    ex.setWindowTitle('TradesCollector')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    ex.show()
    sys.exit(app.exec_())
    # parser = adxPareser()
    # parser.print_main_data()
