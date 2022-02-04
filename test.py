# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *

class T(object):
    def __init__(self,parent=None):
        flo = QFormLayout()
        le1 = QLineEdit(self)
        
        flo.addRow('a',le1)
        le1.setPlaceholderText('hi')
        
        main_frame = QWidget()
        main_frame.setLayout(flo)
        self.setCentralWidget(main_frame)
        
        print('a')
        le1.returnPressed.connect(lambda:self.printt(le1.text()))

class testt(T):
    def __init__(self):
        super(testt,self).__init__()
        # flo = QFormLayout()
        # le1 = QLineEdit(self)
        
        # flo.addRow('a',le1)
        # le1.setPlaceholderText('hi')
        
        # main_frame = QWidget()
        # main_frame.setLayout(flo)
        # self.setCentralWidget(main_frame)
        
        # print('a')
        # le1.returnPressed.connect(lambda:self.printt(le1.text()))
        
        

    def printt(self,t):
        # t=self.le1.text()
        print(t)
    def a(self):
        pass
                
class test(QMainWindow,testt):
    def __init__(self):
        super(test,self).__init__()

app = QApplication(sys.argv)
# win = QMainWindow()
ui = test()
# ui.setupUi(win)
# win.show()
ui.show()
sys.exit(app.exec_())
