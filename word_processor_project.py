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
        





















