import sys
from PyQt5 import QtWidgets

object = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Add Text")
window.setGeometry(200,200,400,300)

label = QtWidgets.QLabel(window)
label.setText("Levent Ertunalılar")
#label.move(150,100)

window.show()

sys.exit(object.exec())