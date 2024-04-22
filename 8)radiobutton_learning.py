import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.question = QtWidgets.QLabel("Which sport do you like most?")
        self.soccer = QtWidgets.QRadioButton("Soccer")
        self.basketball = QtWidgets.QRadioButton("Basketball")
        self.volleyball = QtWidgets.QRadioButton("Volleyball")
        self.swim = QtWidgets.QRadioButton("Swim")
        self.label = QtWidgets.QLabel()
        self.button = QtWidgets.QPushButton("Save")

        vb = QtWidgets.QVBoxLayout()
        vb.addWidget(self.question)
        vb.addWidget(self.soccer)
        vb.addWidget(self.basketball)
        vb.addWidget(self.volleyball)
        vb.addWidget(self.swim)
        vb.addStretch()
        vb.addWidget(self.label)
        vb.addWidget(self.button)

        self.button.clicked.connect(lambda: self.click(self.soccer.isChecked(),self.basketball.isChecked(),self.volleyball.isChecked(),self.swim.isChecked(),self.label))

        self.setLayout(vb)
        self.show()

    def click(self,soccer,basketball,volleybal,swim,label):
        if soccer:
            self.label.setText("Soccer saved")
        if basketball:
            self.label.setText("Basketball saved")
        if volleybal:
            self.label.setText("Volleyball saved")
        if swim:
            self.label.setText("Swim saved")


object = QtWidgets.QApplication(sys.argv)
window = Window()
window.setGeometry(300,300,400,300)
window.setWindowTitle("Radiobutton")
sys.exit(object.exec())