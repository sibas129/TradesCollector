import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui import menu
from ui.menu import Menu
from main.AdxParser import AdxParser
from main.DfmParser import DfmParser


class MainData(QWidget):
    def __init__(self):
        super().__init__()

        self.leftFrame = QFrame()
        self.leftFrame.setFrameShape(QFrame.StyledPanel)

        self.rightFrame = QFrame()
        self.rightFrame.setFrameShape(QFrame.StyledPanel)

        splitter2 = QSplitter(Qt.Horizontal)

        splitter2.addWidget(self.leftFrame)
        splitter2.addWidget(self.rightFrame)
        splitter2.setSizes([22, 22])

        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)

        self.setLayout(hbox)
        self.crt()

    def crt(self):
        parser = AdxParser()
        parser.get_main_adx_data()
        parser_data = parser.print_main_data()
        str1 = str(parser_data[0]) + " / " + str(parser_data[1])

        parser = DfmParser()
        parser.get_main_dfm_data()
        parser_data = parser.print_main_data()
        str2 = str(parser_data[0]) + " / " + str(parser_data[1]) + " %"

        self.company_name = QLineEdit("ADX", self.leftFrame)
        self.company_name.setReadOnly(True)
        self.company_name.setGeometry(20, 10, 90, 60)
        self.company_name.setFrame(False)
        font = QFont()
        font.setPointSize(22)
        self.company_name.setFont(font)

        self.company_name2 = QLineEdit(str1, self.leftFrame)
        self.company_name2.setReadOnly(True)
        self.company_name2.setGeometry(20, 70, 250, 60)
        self.company_name2.setFrame(False)
        font = QFont()
        font.setPointSize(15)
        self.company_name2.setFont(font)

        # self.add_btn = QPushButton("Провести анализ", self.rightFrame)
        # self.add_btn.setGeometry(QtCore.QRect(10, 160, 200, 40))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.add_btn.setFont(font)
        # self.add_btn.clicked.connect(self.predict)

        self.lineEdit = QLineEdit("DFM", self.rightFrame)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 90, 60))
        self.company_name2.setFrame(False)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit.setFont(font)

        self.lineEdit2 = QLineEdit(str2, self.rightFrame)
        self.lineEdit2.setReadOnly(True)
        self.lineEdit2.setGeometry(QtCore.QRect(20, 70, 250, 60))
        self.company_name2.setFrame(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit2.setFont(font)

    # def predict(self):


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.area = MainData()
        self.setCentralWidget(self.area)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setGeometry(300, 500, 650, 500)
    ex.setWindowTitle('TradesCollector')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    ex.show()
    sys.exit(app.exec_())



