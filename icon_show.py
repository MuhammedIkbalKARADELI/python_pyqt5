from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QLabel
from PyQt5.QtGui import QIcon, QImage, QPixmap
import requests

img_path = "icon.png"

app = QApplication([])
win = QMainWindow()

win.setWindowTitle("First Applications")
win.setGeometry(600,200,500,500)

image = QImage()
image.load(img_path)


image_label = QLabel()
image_label.setPixmap(QPixmap(image))
image_label.move(50,60)
image_label.show()

app.exec_()
