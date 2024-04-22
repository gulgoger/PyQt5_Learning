import sys
from PyQt5 import QtWidgets

object = QtWidgets.QApplication(sys.argv)   # argumanlarin kullanimi
window = QtWidgets.QWidget()
window.setGeometry(200,200,400,300)
window.show()




sys.exit(object.exec()) # acilan pencerenin hemen kaybolmamasi icin