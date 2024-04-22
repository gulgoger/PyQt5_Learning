import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.checkbox = QtWidgets.QCheckBox("I have read the membership agreement")
        self.label = QtWidgets.QLabel()
        self.signup = QtWidgets.QPushButton("Sign up")

        vb = QtWidgets.QVBoxLayout()
        vb.addStretch()
        vb.addWidget(self.checkbox)
        vb.addWidget(self.label)
        vb.addWidget(self.signup)

        self.setLayout(vb)

        self.signup.clicked.connect(lambda : self.click(self.checkbox.isChecked()))
        self.show()
        
    def click(self,checkbox):
        if checkbox:
            self.label.setText("Membership was successful")
        else:
            self.label.setText("Approving the contract!")

object = QtWidgets.QApplication(sys.argv)
window = Window()
window.setGeometry(300,300,400,300)
window.setWindowTitle("Checkbox")
sys.exit(object.exec())