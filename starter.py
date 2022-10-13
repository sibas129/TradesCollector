import sys
from main.AdxParser import AdxParser
from main.DfmParser import DfmParser
from PyQt5.QtWidgets import *
from ui.menu import Menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.setGeometry(300, 500, 500, 350)
    ex.setWindowTitle('TradesCollector')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    ex.show()
    sys.exit(app.exec_())
    # parser = AdxParser()
    # parser.collect_all_adx_data()
