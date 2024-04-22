import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Window(QtWidgets.QWidget):
    # def __init__(self):
    #     super().__init__()
    #     self.init_ui()

    def init_ui(self):
        self.text = QtWidgets.QLineEdit()
        self.delete = QtWidgets.QPushButton("Delete")
        self.save = QtWidgets.QPushButton("Save")
        self.label = QtWidgets.QLabel()

        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.text)
        vb.addWidget(self.delete)
        vb.addWidget(self.save)
        vb.addStretch()
        vb.addWidget(self.label)

        self.setLayout(vb)
        self.show()

        self.delete.clicked.connect(self.clear)
        self.save.clicked.connect(self.record)
    def clear(self):
        self.text.clear()
    def record(self):
        self.label.setText(self.text.text()+ " saved")

object = QtWidgets.QApplication(sys.argv)
window = Window()
window.init_ui()
window.setGeometry(200,200,400,300)

sys.exit(object.exec())