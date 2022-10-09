# This is a sample Python script.
import pandas
import bs4
import sys
from main.adxParser import adxPareser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.worker import MainWindow



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    parser = adxPareser()
    # Use a breakpoint in the code line below to debug your script.
    print(parser.get_main_adx_data())  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setGeometry(300, 500, 650, 500)
    ex.setWindowTitle('TradesCollector')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    ex.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
