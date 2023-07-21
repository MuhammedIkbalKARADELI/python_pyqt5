## Window - items 

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


import sys

class Mywindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setWindowTitle("First Applications")
        self.setGeometry(600,200,500,500)
        self.setWindowIcon(QIcon("icon.png"))
        self.setToolTip("my")

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50, 30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50, 70)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_name.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150, 110)
        self.btn_save.clicked.connect(self.cilicked)
    
    def cilicked(self):
        self.lbl_resut.setText('ad: '+ self.txt_name.text()+ ' soyad: '+ self.txt_surname.text()) 


        


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.show()
    sys.exit(app.exec_()) # Çarpı tuşuna bastığında kapanacaktır

window()