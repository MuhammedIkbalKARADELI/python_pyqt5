from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        # set the title
        self.setWindowTitle("Ambriel Health")
 
        # setting  the geometry of window
        self.setGeometry(500, 500, 700, 700)
 
        # creating label
        self.label = QLabel(self)
         
        # loading image
        self.pixmap = QPixmap('icon.png')
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
 
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        
        print(self.pixmap.width())
        # show all the widgets
        self.show()
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())