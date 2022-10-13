import sys
from main.AdxParser import AdxParser
from main.DfmParser import DfmParser
from PyQt5.QtWidgets import *
from ui.main import Menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.setGeometry(300, 500, 500, 350)
    ex.setWindowTitle('TradesCollector')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    ex.show()
    sys.exit(app.exec_())
    # parser = DfmParser()
    # parser.get_main_dfm_data()
    # parser.print_main_data()
