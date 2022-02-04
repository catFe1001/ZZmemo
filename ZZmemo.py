# -*- coding: utf-8 -*-

import sys
from traceback import print_tb
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from UI.mainUI import Ui_ZZmemo



class ZZmemo(QMainWindow):
    def __init__(self,parent=None):
        super(ZZmemo,self).__init__(parent)
        self.ui = Ui_ZZmemo()
        self.ui.setupUi(self)
        
    def eventSelect(self):
        t = self.ui.input.text()

    
if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = ZZmemo()
    win.show()
    
    sys.exit(app.exec_())
