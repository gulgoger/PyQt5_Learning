import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.button = QtWidgets.QPushButton("Bring the image")
        self.image = QtWidgets.QLabel("Image not loaded")

        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.image)
        vb.addWidget(self.button)
        vb.addStretch()

        hb = QtWidgets.QHBoxLayout()
        hb.addStretch()
        hb.addLayout(vb)
        hb.addStretch()

        self.setLayout(hb)
        self.show()

        self.button.clicked.connect(self.click)

    def click(self):
        self.image.setPixmap(QtGui.QPixmap("folder.png"))

object = QtWidgets.QApplication(sys.argv)

window = Window()
window.setGeometry(200,200,400,300)
sys.exit(object.exec())
