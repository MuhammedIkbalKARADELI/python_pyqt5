## Window - items 

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()


    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Adınız: ")
    lbl_name.move(50, 30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız: ")
    lbl_surname.move(50, 70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)

    def cilicked(self):
        print("Butona Tıklandı Adınız: " + txt_name.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(150, 110)
    btn_save.clicked.connect(cilicked)


    win.setWindowTitle("First Applications")
    win.setGeometry(600,200,500,500)
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("my")


    win.show()
    sys.exit(app.exec_()) # Çarpı tuşuna bastığında kapanacaktır

window()