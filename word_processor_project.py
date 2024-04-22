import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Word_processor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.text_space = QtWidgets.QTextEdit()
        self.open = QtWidgets.QPushButton("Open")
        self.save = QtWidgets.QPushButton("Save")
        self.clear = QtWidgets.QPushButton("Clear")
        self.exit = QtWidgets.QPushButton("Exit")

        hbox = QtWidgets.QHBoxLayout()

        hbox.addWidget(self.open)
        hbox.addWidget(self.save)
        hbox.addWidget(self.clear)
        hbox.addWidget(self.exit)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.text_space)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle("Word Processor Program")

        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)
        self.clear.clicked.connect(self.delete_text)
        self.exit.clicked.connect(self.log_out)

        self.show()

    def open_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",os.getenv("Desktop"))

        with open(file[0],"r") as file:
            self.text_space.setText(file.read())
        
    def save_file(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self,"Save File", os.getenv("Desktop"))

        with open(file[0],"w") as file:
            file.write(self.text_space.toPlainText())

    def delete_text(self):
        self.text_space.clear()

    def log_out(self):
        quit() 

object  = QtWidgets.QApplication(sys.argv)

wordProcessor = Word_processor()
sys.exit(object.exec_())


















