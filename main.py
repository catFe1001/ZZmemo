import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from ZZmemo import ZZmemo

if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = ZZmemo()
    win.show()
    sys.exit(app.exec_())
