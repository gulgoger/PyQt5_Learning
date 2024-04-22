import sys
from PyQt5 import QtWidgets, QtGui

#frame adding
object = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setGeometry(200,200,600,400)

label = QtWidgets.QLabel(window)
label.setPixmap(QtGui.QPixmap("folder.png"))

label.move(150,50)

#button adding
button = QtWidgets.QPushButton(window)
button.setText("Okay")
button.move(70,300)


window.show()

sys.exit(object.exec())