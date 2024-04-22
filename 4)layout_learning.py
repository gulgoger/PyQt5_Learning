import sys
from PyQt5 import QtWidgets, QtGui

object = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setGeometry(200,200,600,400)

save = QtWidgets.QPushButton()
save.setText("Save")

exit = QtWidgets.QPushButton()
exit.setText("Exit")

#horizontal layout
# hb = QtWidgets.QHBoxLayout()

# hb.addWidget(save)
# hb.addStretch()
# hb.addWidget(exit)

# window.setLayout(hb)

#vertical layout

vb = QtWidgets.QVBoxLayout()
vb.addWidget(save)
vb.addWidget(exit)

vb.addStretch()

window.setLayout(vb)

window.show()

sys.exit(object.exec())