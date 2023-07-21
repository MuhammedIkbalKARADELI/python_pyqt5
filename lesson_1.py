from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Applications")
    win.setGeometry(600,200,500,500)
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("my")


    win.show()
    sys.exit(app.exec_()) # Çarpı tuşuna bastığında kapanacaktır

window()